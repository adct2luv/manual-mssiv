#!/usr/bin/env python3
"""
Build Docusaurus MDX pages for all 22 EPIC manuals.
Generates bilingual EN+TH content from:
- knowledge-base/extracted/vision/*.json (12 Tier C)
- knowledge-base/products/*/product.json (10 Tier A+B)

Output:
- docs/<slug>/*.md (TH default locale)
- i18n/en/docusaurus-plugin-content-docs/current/<slug>/*.md (EN)
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
SITE = ROOT / "manual-site"
DOCS_TH = SITE / "docs"
DOCS_EN = SITE / "i18n/en/docusaurus-plugin-content-docs/current"
IMAGES = SITE / "static/img/brochures"

# =============================================================================
# Common Thai translations (curated by hand)
# =============================================================================
TH = {
    # UI labels
    "Overview": "ภาพรวม",
    "Safety Precautions": "ข้อควรระวังด้านความปลอดภัย",
    "Specifications": "ข้อมูลจำเพาะ",
    "Components": "ส่วนประกอบ",
    "PIN Registration": "การลงทะเบียนรหัส PIN",
    "RFID Registration": "การลงทะเบียนบัตร RFID",
    "RFID Deletion": "การลบบัตร RFID",
    "Smart Key Registration": "การลงทะเบียน Smart Key",
    "Smart Key Deletion": "การลบ Smart Key",
    "Fingerprint Registration": "การลงทะเบียนลายนิ้วมือ",
    "Fingerprint Deletion": "การลบลายนิ้วมือ",
    "Features": "คุณสมบัติเด่น",
    "Alarms": "สัญญาณเตือนและความปลอดภัย",
    "Opening Door Outside": "การเปิดประตูจากด้านนอก",
    "Opening Door Inside": "การเปิดประตูจากด้านใน",
    "Closing Door Outside": "การปิดประตูจากด้านนอก",
    "Closing Door Inside": "การปิดประตูจากด้านใน",
    # Common
    "Default PIN": "รหัส PIN เริ่มต้น",
    "Caution": "ข้อควรระวัง",
    "Note": "หมายเหตุ",
    "Tip": "เคล็ดลับ",
    "Warning": "คำเตือน",
    "Steps": "ขั้นตอน",
    "Specifications table": "ตารางข้อมูลจำเพาะ",
    "Description": "คำอธิบาย",
    "Function": "หน้าที่",
    "Always register pin number while door is open.": "กรุณาลงทะเบียนรหัส PIN ในขณะที่ประตูเปิดอยู่เสมอ",
    "Default pin number is": "รหัส PIN เริ่มต้นคือ",
    "Door must be open": "ประตูต้องเปิดอยู่",
    "Up to": "สูงสุด",
    "cards can be registered": "สามารถลงทะเบียนการ์ดได้",
    "fingerprints can be registered": "สามารถลงทะเบียนลายนิ้วมือได้",
    "Emergency Battery": "แบตเตอรี่ฉุกเฉิน",
    "Battery": "แบตเตอรี่",
    "Door Thickness": "ความหนาประตู",
    "Material": "วัสดุ",
    "Outer body": "ตัวล็อกด้านนอก",
    "Inner body": "ตัวล็อกด้านใน",
    "Operating Temperature": "อุณหภูมิใช้งาน",
    "Power": "ระบบจ่ายไฟ",
    "Voltage": "แรงดันไฟฟ้า",
    "Product Type": "ประเภทผลิตภัณฑ์",
    "Fire Detection": "ตรวจจับไฟไหม้",
    "Sensor Temperature": "เซ็นเซอร์อุณหภูมิ",
    "Maximum": "สูงสุด",
    "Normal": "ปกติ",
    "Humidity": "ความชื้น",
    "Weight": "น้ำหนัก",
    "Dimensions (Outer)": "ขนาด (ด้านนอก)",
    "Dimensions (Inner)": "ขนาด (ด้านใน)",
    "Access Methods": "วิธีเข้าถึง",
    "Safety Features": "คุณสมบัติความปลอดภัย",
    "Compatibility": "ความเข้ากันได้",
    "Troubleshooting": "การแก้ปัญหา",
    "Warnings": "คำเตือน",
    "Warranty": "การรับประกัน",
    "Certifications": "การรับรอง",
    "Number Pad": "คีย์แพดตัวเลข",
    "Reset Button": "ปุ่มรีสตาร์ทเครื่อง (Reset)",
    "Battery Lamp": "ไฟแจ้งเตือนสถานะแบตเตอรี่",
    "Status LED Lamp": "ไฟ LED แสดงสถานะ",
    "RFID Card Reader": "เครื่องอ่านการ์ด RFID",
    "Emergency Battery Terminal": "ขั้วต่อแบตเตอรี่ฉุกเฉิน (9V)",
    "Mechanical Key Hole Cover": "ฝาครอบรูกุญแจกลไก",
    "Outer Body Handle": "ที่จับด้านนอก",
    "Battery Cover": "ฝาครอบแบตเตอรี่",
    "Registration Button": "ปุ่มลงทะเบียน (Registration)",
    "Open/Close Button": "ปุ่มเปิด/ปิดประตู",
    "Dual Lock Button": "ปุ่มล็อกสองชั้น (Dual Lock)",
    "Inner Body Handle": "ที่จับด้านใน",
    "Alkaline AA Battery": "แบตเตอรี่อัลคาไลน์ AA",
    "Mortise": "มอร์ทิส",
    "Deadbolt": "สลักล็อก (Deadbolt)",
    "Latch Bolt": "ลิ้นสลัก (Latch Bolt)",
    "Manual Lock Button": "ปุ่มบิดล็อกด้วยตนเอง",
    "Door Closing Sensor": "เซ็นเซอร์ตรวจจับประตูปิด",
    "Safety Button": "ปุ่ม Safety",
    "Manual Lock/Unlock Knob": "ปุ่มหมุนล็อก/ปลดล็อกด้วยตนเอง",
    "Auto Lock Sensor": "เซ็นเซอร์ล็อกอัตโนมัติ",
    "Inside double lock": "ล็อกสองชั้นจากด้านใน",
    "Outside Force Lock": "ล็อกบังคับจากด้านนอก",
    "Auto Lock Mode": "โหมดล็อกอัตโนมัติ (Auto Lock)",
    "Manual Lock Mode": "โหมดล็อกด้วยตนเอง (Manual Lock)",
    "Multi-touch Security": "ความปลอดภัย Multi-touch",
    "Dual-mode Security": "ระบบยืนยันตัวตนสองชั้น",
    "Random Number Feature": "ฟังก์ชันสุ่มตัวเลขความปลอดภัย (Random Number)",
    "Voice Mode": "โหมดเสียงแนะนำ",
    "Buzzer Mode": "โหมดเสียงเตือนบี๊ป",
    "Sound Volume": "ระดับเสียง",
    "Sound Mute": "ปิดเสียงชั่วคราว",
    "Anti-Prank": "ระบบล็อกป้องกันการเดารหัสผ่าน",
    "Fire Alarm": "สัญญาณเตือนไฟไหม้",
    "Anti-Hacking": "สัญญาณเตือนการงัดแงะ",
    "Intrusion Alarm": "สัญญาณเตือนการบุกรุก",
    "Replace Battery": "สัญญาณเตือนเปลี่ยนแบตเตอรี่",
    "Emergency Mechanical Key": "กุญแจสำรองฉุกเฉิน",
    "Lock Status Display": "การแสดงสถานะล็อก",
    "Deadbolt Error": "ข้อผิดพลาดสลักล็อก",
    "Open battery cover": "เปิดฝาครอบแบตเตอรี่",
    "Press [Registration] button": "กดปุ่ม [Registration]",
    "beep sound will be heard": "จะมีเสียงสัญญาณบี๊บดังขึ้น",
    "Enter pin number, followed by": "ป้อนรหัส PIN แล้วตามด้วยปุ่ม",
    "button": "ปุ่ม",
    "Place smart key to be registered on the Card reader": "ทาบบัตรที่ต้องการลงทะเบียนบนพื้นที่เครื่องอ่านการ์ด",
    "Long Press": "กดค้างไว้",
    "for 5 seconds": "เป็นเวลา 5 วินาที",
    "When the melody is heard, All smart keys are deleted": "เมื่อได้ยินเสียงสัญญาณเพลงเมโลดี้ การ์ดทั้งหมดจะถูกลบเรียบร้อยแล้ว",
    "Smart key entry standby": "อยู่ในสถานะพร้อมลงทะเบียนการ์ด",
    "After deletion is complete": "เมื่อเสร็จสิ้นขั้นตอนการลบข้อมูล",
    "press [Registration] button to finish": "กดปุ่ม [Registration] เพื่อเสร็จสิ้นขั้นตอน",
}

# Thai descriptions for products (Tier A+B from existing product.json)
TH_DESCRIPTIONS = {
    "ES-B10": "กุญแจดิจิทัล Rim Type ที่สามารถปลดล็อกได้ด้วยรหัส PIN พร้อมฟังก์ชันสุ่มตัวเลขเพื่อความปลอดภัย และปุ่มบิดล็อกด้วยตนเอง มาพร้อมเซ็นเซอร์ตรวจจับความร้อนกรณีอัคคีภัยและสัญญาณเตือนการบุกรุก",
    "ES-L200": "กุญแจดิจิทัลขนาดกะทัดรัดสำหรับตู้ล็อกเกอร์และตู้เก็บของ รองรับการเปิดใช้งานด้วยรหัส PIN หรือการทาบบัตร RFID",
    "OS300H": "กุญแจดิจิทัลเสริมความปลอดภัยระบบ Rim Type (แบบไม่เจาะช่อง) สำหรับประตูบานเปิด รองรับการเปิดด้วยรหัส PIN หรือบัตร RFID",
    "POPscan": "กุญแจดิจิทัลเสริมความปลอดภัยรุ่น POPscan ตัวเครื่องสีดำ ดีไซน์ทันสมัย รองรับการสแกนลายนิ้วมือที่รวดเร็วและแม่นยำ",
    "Assembly Guide for Key Tail": "คู่มือการประกอบชิ้นส่วนหางกุญแจสำหรับการติดตั้งชุดอุปกรณ์ล็อกประตู",
    "Consolidated Manual Rev.09": "คู่มือรวมผู้ใช้ฉบับแก้ไขปรับปรุงครั้งที่ 9 ครอบคลุมผลิตภัณฑ์ชุดล็อกดิจิทัลหลากหลายรุ่น",
    "EPIC Things APP User Manual": "คู่มือการใช้งานแอปพลิเคชัน EPIC Things สำหรับการควบคุมและจัดการระบบล็อกประตูอัจฉริยะผ่านสมาร์ทโฟน",
    "IR Sensor Usage Guide for Face ID": "คู่มือการใช้งานระบบเซ็นเซอร์อินฟราเรด (IR Sensor) สำหรับระบบการจดจำใบหน้า (Face ID)",
    "Outer Body Cable Management Guide": "คู่มือวิธีการจัดและเดินสายสัญญาณไฟฟ้าของชุดตัวล็อกนอกบ้าน",
    "Remote-Control-Module-Compatibility-Guide": "คู่มือตารางตรวจสอบความเข้ากันได้ของการทำงานของโมดูลรีโมทคอนโทรลไร้สาย",
}

# Translation lookups for specific component functions, spec labels, spec values
TH_COMPONENTS = {
    "Number Pad": ("แผงคีย์แพดตัวเลข", "ป้อนรหัส PIN หรือรหัสตั้งค่าการทำงาน (1-9, *, 0, #)"),
    "Status LED Lamp": ("ไฟ LED แสดงสถานะ", "แสดงสถานะการทำงานของตัวล็อก (สแตนด์บาย / ล็อกแล้ว / ข้อผิดพลาด)"),
    "Battery Lamp": ("ไฟแจ้งเตือนสถานะแบตเตอรี่", "ไฟเตือนจะสว่างขึ้นเมื่อแบตเตอรี่อ่อน"),
    "RFID Card Reader": ("เครื่องอ่านการ์ด RFID", "แตะบัตรหรือแท็กคีย์การ์ดที่ลงทะเบียนแล้วเพื่อเปิดประตู"),
    "Reset Button": ("ปุ่มรีสตาร์ทเครื่อง (Reset)", "ใช้สำหรับรีสตาร์ทระบบกรณีตัวเครื่องขัดข้องหรือไม่ตอบสนอง"),
    "Emergency Battery Terminal": ("ขั้วต่อแบตเตอรี่ฉุกเฉิน (9V)", "แตะแบตเตอรี่ 9V เพื่อจ่ายไฟสำรองหากแบตเตอรี่หลักหมด"),
    "Outer Body Handle": ("ที่จับประตูด้านนอก", "ดึงหรือหมุนลงเพื่อเปิดประตูหลังปลดล็อกสำเร็จ"),
    "Battery Cover": ("ฝาครอบแบตเตอรี่", "เปิดออกเพื่อเข้าถึงช่องใส่แบตเตอรี่"),
    "Registration Button": ("ปุ่มลงทะเบียน (Registration)", "ใช้กดเมื่อต้องการลงทะเบียนหรือแก้ไขรหัส PIN, บัตร หรือลายนิ้วมือ"),
    "Open/Close Button": ("ปุ่มเปิด/ปิดประตู (Open/Close)", "กดปุ่มเพื่อล็อกหรือปลดล็อกประตูแบบสัมผัสเดียวจากด้านใน"),
    "Dual Lock Button": ("ปุ่มล็อกสองชั้น (Dual Lock)", "เปิดโหมดความเป็นส่วนตัว เพื่อป้องกันการเปิดประตูจากภายนอก"),
    "Inner Body Handle": ("ที่จับประตูด้านใน", "ดึงหรือหมุนเพื่อเปิดประตูจากภายในห้อง"),
    "Alkaline AA Battery": ("แบตเตอรี่อัลคาไลน์ AA", "แหล่งพลังงานหลักสำหรับตัวล็อกประตูดิจิทัล"),
    "Manual Lock Button": ("ปุ่มบิดล็อกด้วยตนเอง", "ใช้เพื่อล็อกหรือปลดล็อกประตูด้วยตนเองในโหมดล็อกแบบแมนนวล"),
    "Door Thickness": ("ความหนาประตูที่รองรับ", "40~50 มม."),
    "PIN": ("รหัส PIN", "ตัวเลข 4~12 หลัก"),
    "Power": ("ระบบจ่ายไฟ (พลังงานหลัก)", "DC 6V (แบตเตอรี่อัลคาไลน์ขนาด AA จำนวน 4 หรือ 8 ก้อน)"),
    "Emergency Battery": ("ระบบจ่ายไฟฉุกเฉิน", "แบตเตอรี่อัลคาไลน์ DC 9V (จำหน่ายแยกต่างหาก)"),
    "Fire Detection": ("การตรวจจับความร้อน (เซ็นเซอร์ไฟไหม้)", "เมื่ออุณหภูมิสูงถึง 62°C ± 5°C / สูงสุด 72°C ± 5°C"),
    "Material (Outer)": ("วัสดุ (ตัวเครื่องด้านนอก)", "อะลูมิเนียม (Al), ซิงค์ (Zn), พลาสติกทนความร้อน (ABS)"),
    "Material (Inner)": ("วัสดุ (ตัวเครื่องด้านใน)", "ซิงค์ (Zn), พลาสติกทนความร้อน (ABS)"),
}

# Translation for box items
TH_IN_BOX = {
    "Outer body": "ชุดอุปกรณ์ตัวเครื่องด้านนอก",
    "Inner body": "ชุดอุปกรณ์ตัวเครื่องด้านใน",
    "Strike plate & fixing hardware": "แป้นรับลิ้นกลอนและชุดอุปกรณ์สำหรับติดตั้ง",
    "Mechanical keys": "กุญแจกลไกสำรอง",
    "Batteries": "แบตเตอรี่ขนาด AA",
    "User manual": "คู่มือการใช้งาน",
}

# Brochure image → slug mapping
BROCHURE_MAP = {
    "es-303g": "Glass Type/ES-303G-01.png",
    "ef-p8800k": "Main Type/EF-P8800K-01.png",
    "es-m50": "Main Type/ES-M50-01.png",
    "es-b10": "Rim Type/ES-B10-01.png",
    "es-l200": "Locker Type/ES-L200-01.png",
    "n-touch": "Rim Type/N-Touch-01.png",
    "os300h": "Rim Type/OS300H-01.png",
    "popscan": "Rim Type/POPscan-01.png",
    "touch": "Rim Type/Touch-01.png",
    "es-s100dr": "Rim Type/ES-S100Dr-01.png",
    "es-f300dr": "Rim Type/ES-F300Dr-01.png",
    "es-f301d": "Rim Type/ES-F301D-01.png",
    "es-f500dr": "Rim Type/ES-F500Dr-01.png",
    "es-f501d": "Rim Type/ES-F501D-01.png",
    "es-ff730gr": "Rim Type/ES-FF730Gr-01.png",
    "es-ff731g": "Rim Type/ES-FF731G-01.png",
}

# Determine what features each product has
PRODUCT_FEATURES = {
    "ef-8000l": ["pin", "rfid", "fingerprint", "remote"],
    "ef-p8800k": ["pin", "rfid", "fingerprint", "remote", "bluetooth"],
    "es-303g": ["pin", "rfid"],
    "es-809l": ["pin", "rfid", "mechanical_key"],
    "es-b10": ["pin", "rfid"],
    "es-k70": ["pin", "rfid", "mechanical_key"],
    "es-l200": ["pin", "rfid"],
    "es-m50": ["pin", "rfid"],
    "es-p9100fk": ["pin", "rfid", "fingerprint", "mechanical_key"],
    "es-t153": ["pin", "rfid"],
    "n-touch": ["pin"],
    "os300h": ["pin", "rfid"],
    "popscan": ["pin", "rfid"],
    "touch": ["pin", "smart_card"],
    "triplex-2way": ["pin", "smart_key", "home_network"],
    "triplex-3way": ["pin", "smart_key", "mechanical_key"],
    # New consolidated-manual models
    "es-s100dr": ["pin", "rfid"],
    "es-f300dr": ["pin", "rfid", "fingerprint"],
    "es-f301d": ["pin", "rfid", "fingerprint"],
    "es-f501d": ["pin", "rfid", "fingerprint"],
    "es-ff730gr": ["pin", "rfid", "fingerprint", "mechanical_key"],
    "es-ff731g": ["pin", "rfid", "fingerprint", "mechanical_key"],
    "es-s740d": ["pin", "rfid", "fingerprint", "mechanical_key"],
    "es-f7000kr": ["pin", "rfid", "fingerprint"],
    "es-f9000kr": ["pin", "rfid", "fingerprint", "mechanical_key"],
    "es-p8800k": ["pin", "rfid", "fingerprint"],
    "consolidated-manual-rev-09": ["pin", "rfid", "fingerprint", "face"],
    "epic-things-app-user-manual": ["app"],
}

# Determine what pages to generate per product
def get_pages_for_product(slug):
    features = PRODUCT_FEATURES.get(slug, ["pin"])
    pages = ["intro", "specs", "components"]
    if "pin" in features:
        pages.append("pin-registration")
    if "rfid" in features:
        pages.append("rfid-registration")
        pages.append("rfid-deletion")
    if "smart_card" in features:
        pages.append("rfid-registration")  # smart_card uses same flow as rfid
        pages.append("rfid-deletion")
    if "smart_key" in features:
        pages.append("rfid-registration")
        pages.append("rfid-deletion")
    if "fingerprint" in features:
        pages.append("fingerprint-registration")
        pages.append("fingerprint-deletion")
    # Settings/alarms for main door locks
    if slug not in ["es-l200", "n-touch", "assembly-guide-for-key-tail",
                     "consolidated-manual-rev-09", "epic-things-app-user-manual",
                     "ir-sensor-usage-guide-for-face-id",
                     "outer-body-cable-management-guide",
                     "remote-control-module-compatibility-guide"]:
        pages.append("features")
        pages.append("alarms")
    return pages


# =============================================================================
# MDX Template Functions
# =============================================================================

def make_frontmatter(title, description, position, slug=None):
    fm = ["---"]
    fm.append(f"sidebar_position: {position}")
    fm.append(f"title: {title}")
    fm.append(f"description: {description}")
    if slug:
        fm.append(f"slug: {slug}")
    fm.append("---")
    return "\n".join(fm)


def make_category_json(slug, label, description, position=1):
    return json.dumps({
        "label": label,
        "position": position,
        "link": {
            "type": "generated-index",
            "description": description
        }
    }, ensure_ascii=False, indent=2)


# ----- Generic page templates -----

def gen_overview(model, slug, th_title, en_title, th_desc, en_desc,
                 brochure_image=None, features=None, manual_url=None,
                 consolidated_manual=None):
    """Generate intro/overview page"""
    th_lines = [
        make_frontmatter(th_title, th_desc, 1),
        "",
        f"# {model} — {th_title}",
        "",
    ]
    if brochure_image:
        th_lines.append(f"![{model}]({brochure_image})")
        th_lines.append("")
    th_lines.append(th_desc)
    th_lines.append("")
    if consolidated_manual:
        th_lines.append(f":::tip[คู่มือฉบับรวม]")
        th_lines.append(f"รุ่นนี้ใช้คู่มือฉบับรวม [Consolidated Manual Rev.09](/consolidated-manual-rev-09/intro)")
        th_lines.append(f"ดูตารางเปรียบเทียบฟีเจอร์ของทุกรุ่นในคู่มือฉบับรวม")
        th_lines.append(":::")
        th_lines.append("")
    th_lines.append("## คุณสมบัติเด่น")
    th_lines.append("")
    if features:
        for f in features:
            th_lines.append(f"- **{f}**")
        th_lines.append("")
    th_lines.append(f":::warning[ต้องติดตั้งโดยช่างผู้เชี่ยวชาญ]")
    th_lines.append(f"ผลิตภัณฑ์นี้ต้องติดตั้งโดย **ช่างผู้เชี่ยวชาญเท่านั้น** เพื่อให้ได้รับการรับประกันเต็มรูปแบบ ห้ามติดตั้งด้วยตัวเอง")
    th_lines.append(":::")
    th_lines.append("")
    if manual_url:
        th_lines.append(f"📖 ดูคู่มือ PDF ต้นฉบับ: [epic.co.kr]({manual_url})")
        th_lines.append("")

    en_lines = [
        make_frontmatter(f"Overview", en_desc, 1),
        "",
        f"# {model} — {en_title}",
        "",
    ]
    if brochure_image:
        en_lines.append(f"![{model}]({brochure_image})")
        en_lines.append("")
    en_lines.append(en_desc)
    en_lines.append("")
    if consolidated_manual:
        en_lines.append(f":::tip[Consolidated manual]")
        en_lines.append(f"This model uses the [Consolidated Manual Rev.09](/en/consolidated-manual-rev-09/intro)")
        en_lines.append(f"See the feature comparison table for all models in the consolidated manual")
        en_lines.append(":::")
        en_lines.append("")
    en_lines.append("## Key Features")
    en_lines.append("")
    if features:
        for f in features:
            en_lines.append(f"- **{f}**")
        en_lines.append("")
    en_lines.append(f":::warning[Installation by professional required]")
    en_lines.append(f"This product must be installed by a **qualified technician only** to receive full warranty coverage. Do not install it yourself.")
    en_lines.append(":::")
    en_lines.append("")
    if manual_url:
        en_lines.append(f"📖 Original PDF manual: [epic.co.kr]({manual_url})")
        en_lines.append("")

    return "\n".join(th_lines), "\n".join(en_lines)


def gen_specs(model, specs_data, th_title="ข้อมูลจำเพาะ", en_title="Specifications"):
    """Generate specs page from a list of (label, value) pairs or dict"""
    th_lines = [
        make_frontmatter(th_title, f"ข้อมูลจำเพาะของ {model}", 2),
        "",
        f"# {th_title}",
        "",
    ]
    en_lines = [
        make_frontmatter(en_title, f"Specifications of {model}", 2),
        "",
        f"# {en_title}",
        "",
    ]
    if isinstance(specs_data, list):
        th_lines.append("| รายการ | ค่า |")
        th_lines.append("|---|---|")
        en_lines.append("| Item | Value |")
        en_lines.append("|---|---|")
        for label, val in specs_data:
            if label in TH_COMPONENTS:
                th_label, th_val = TH_COMPONENTS[label]
            else:
                th_label = TH.get(label, label)
                th_val = TH.get(val, val)
            th_lines.append(f"| {th_label} | {th_val} |")
            en_lines.append(f"| {label} | {val} |")
    elif isinstance(specs_data, dict):
        for k, v in specs_data.items():
            if k in TH_COMPONENTS:
                th_k, th_v = TH_COMPONENTS[k]
            else:
                th_k = TH.get(k, k)
                th_v = TH.get(v, v)
            th_lines.append(f"- **{th_k}**: {th_v}")
            en_lines.append(f"- **{k}**: {v}")
    th_lines.append("")
    en_lines.append("")
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_components(model, outer_parts, inner_parts, in_box=None):
    """Generate components page"""
    th_lines = [
        make_frontmatter("ส่วนประกอบ", f"ส่วนประกอบของ {model}", 3),
        "",
        f"# ส่วนประกอบ",
        "",
        "## ตัวล็อกด้านนอก",
        "",
        "| # | ชิ้นส่วน | หน้าที่ |",
        "|---|---|---|",
    ]
    en_lines = [
        make_frontmatter("Components", f"Components of {model}", 3),
        "",
        f"# Components",
        "",
        "## Outer body",
        "",
        "| # | Part | Function |",
        "|---|---|---|",
    ]
    for i, (name, func) in enumerate(outer_parts, 1):
        if name in TH_COMPONENTS:
            th_name, th_func = TH_COMPONENTS[name]
        else:
            th_name = TH.get(name, name)
            th_func = TH.get(func, func)
        th_lines.append(f"| {i} | **{th_name}** | {th_func} |")
        en_lines.append(f"| {i} | **{name}** | {func} |")
    th_lines.append("")
    en_lines.append("")
    th_lines.append("## ตัวล็อกด้านใน")
    en_lines.append("## Inner body")
    th_lines.append("")
    en_lines.append("")
    th_lines.append("| # | ชิ้นส่วน | หน้าที่ |")
    en_lines.append("| # | Part | Function |")
    th_lines.append("|---|---|---|")
    en_lines.append("|---|---|---|")
    for i, (name, func) in enumerate(inner_parts, 1):
        if name in TH_COMPONENTS:
            th_name, th_func = TH_COMPONENTS[name]
        else:
            th_name = TH.get(name, name)
            th_func = TH.get(func, func)
        th_lines.append(f"| {i} | **{th_name}** | {th_func} |")
        en_lines.append(f"| {i} | **{name}** | {func} |")
    if in_box:
        th_lines.append("")
        en_lines.append("")
        th_lines.append("## อุปกรณ์ในกล่อง")
        en_lines.append("## In the box")
        for item in in_box:
            th_item = TH_IN_BOX.get(item, TH.get(item, item))
            th_lines.append(f"- {th_item}")
            en_lines.append(f"- {item}")
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_pin_registration(model, default_pin="1, 2, 3, 4", pin_length="4~12"):
    """Generate PIN registration page"""
    th_lines = [
        make_frontmatter("การลงทะเบียนรหัส PIN", f"วิธีเปลี่ยนรหัส PIN บน {model}", 4),
        "",
        f"# การลงทะเบียนรหัส PIN",
        "",
        f":::caution[ข้อควรทราบก่อนเริ่มตั้งค่า]",
        f"- กรุณาทำการลงทะเบียนรหัส PIN **ในขณะที่ประตูเปิดอยู่เสมอ** เพื่อป้องกันการล็อกนอกบ้านโดยไม่ตั้งใจ",
        f"- รหัส PIN เริ่มต้นจากโรงงานคือ **`{default_pin}`** โปรดเปลี่ยนเป็นรหัสของคุณเองก่อนเริ่มใช้งานครั้งแรก",
        f"- รหัส PIN ควรประกอบด้วยตัวเลขจำนวน {pin_length} หลัก และควรหลีกเลี่ยงรหัสผ่านที่คาดเดาได้ง่าย เช่น `1111`, `1234` หรือวัน/เดือน/ปีเกิด",
        f"- **ระบบไม่มีปุ่มกดรีเซ็ตเป็นค่าเริ่มต้นจากโรงงาน (Factory Reset) จากภายนอกเครื่อง** หากลืมรหัส PIN และไม่มีกุญแจสำรอง จะต้องติดต่อช่างบริการของทางบริษัทเพื่อดำเนินการทางเทคนิคเท่านั้น",
        ":::",
        "",
        "## ขั้นตอนการตั้งค่า",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน) จากนั้นกดปุ่ม **Registration** (ลงทะเบียน) 1 ครั้ง จะมีเสียงสัญญาณบี๊บดังขึ้น",
        "2. ป้อนรหัส PIN ปัจจุบันของคุณ แล้วตามด้วยปุ่ม `*`",
        "3. กดปุ่มหมายเลขตามที่ระบุในคู่มือ (เช่น ปุ่ม `1`) เพื่อเลือกโหมดเปลี่ยนรหัส PIN",
        "4. ป้อนรหัส PIN ใหม่ที่ต้องการ แล้วตามด้วยปุ่ม `*`",
        "5. ป้อนรหัส PIN ใหม่ซ้ำอีกครั้งเพื่อยืนยัน จากนั้นตามด้วยปุ่ม `*`",
        "6. ตัวล็อกจะส่งเสียงสัญญาณเมโลดี้เพื่อยืนยันว่าการลงทะเบียนรหัสผ่านใหม่เสร็จสิ้นสมบูรณ์",
        "",
        ":::note[หมายเหตุ]",
        "แต่ละขั้นตอนตั้งค่าจะต้องดำเนินการภายใน 10 วินาที หากเกินเวลาที่กำหนด ระบบจะยกเลิกขั้นตอนโดยอัตโนมัติและต้องเริ่มต้นใหม่อีกครั้ง",
        ":::",
    ]
    en_lines = [
        make_frontmatter("PIN Registration", f"How to change PIN on {model}", 4),
        "",
        f"# PIN Registration",
        "",
        f":::caution[Before you start]",
        f"- Always register PIN **while door is open**",
        f"- Default PIN is **`{default_pin}`** — change before first use",
        f"- Choose a {pin_length}-digit PIN. Avoid obvious patterns like `1111`, `1234`, birth year",
        f"- **No factory reset** — if you forget your PIN, call a technician",
        ":::",
        "",
        "## Steps",
        "",
        "1. Open the battery cover (inside). Press the **Registration** button once. A beep will sound.",
        "2. Enter the current PIN, then press `*`.",
        "3. Press the number button indicated in the manual (e.g. `1`) to select PIN-change mode.",
        "4. Enter the new PIN, then press `*`.",
        "5. Re-enter the new PIN to confirm, then press `*`.",
        "6. The lock plays a short melody to confirm registration succeeded.",
        "",
        ":::note",
        "You have 10 seconds between steps. If it expires, the lock times out and you must start over.",
        ":::",
    ]
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_rfid_registration(model, max_cards=100, has_individual=True):
    """Generate RFID registration page"""
    th_lines = [
        make_frontmatter("การลงทะเบียนบัตร RFID", f"วิธีลงทะเบียนบัตร RFID บน {model}", 5),
        "",
        f"# การลงทะเบียนบัตร RFID",
        "",
        f":::tip[บัตรที่รองรับ]",
        f"รองรับเฉพาะบัตรหรือแท็ก RFID ความถี่ 13.56 MHz ที่ผ่านการรับรองความเข้ากันได้กับระบบของ EPIC เท่านั้น (การ์ดหรือแท็กที่แถมมาในกล่องจะต้องทำการลงทะเบียนเข้ากับตัวเครื่องก่อนจึงจะเปิดประตูได้)",
        ":::",
        "",
        f":::caution[ข้อควรระวัง]",
        f"ประตูต้องเปิดอยู่ตลอดเวลาในขณะทำการลงทะเบียน",
        f":::",
        "",
        "## โหมดลงทะเบียนการ์ดแบบทั่วไป (ลงทะเบียนทั้งหมดพร้อมกัน)",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน) จากนั้นกดปุ่ม **Registration** (ลงทะเบียน) 1 ครั้ง",
        "2. ป้อนรหัส PIN ปัจจุบันของคุณ แล้วตามด้วยปุ่ม `*`",
        "3. กดปุ่มหมายเลข `2` (หรือปุ่ม `4` ขึ้นอยู่กับรุ่นของคุณ) เพื่อเข้าสู่โหมดลงทะเบียน RFID",
        "4. ทาบบัตรหรือแท็กบนเครื่องอ่านทีละใบ ตัวเครื่องจะมีเสียงสัญญาณบี๊บยืนยันสำหรับบัตรแต่ละใบ",
        "5. กดปุ่ม **Registration** (ลงทะเบียน) อีกครั้งเพื่อเสร็จสิ้นขั้นตอน",
        "",
        f"สามารถลงทะเบียนการ์ดได้สูงสุด **{max_cards} ใบ**",
    ]
    en_lines = [
        make_frontmatter("RFID Card Registration", f"How to register RFID cards on {model}", 5),
        "",
        f"# RFID Card Registration",
        "",
        f":::tip[Compatibility]",
        f"Only 13.56 MHz RFID cards compatible with EPIC work with this lock. Cards included in the box must be registered manually.",
        ":::",
        "",
        f":::caution[Door must be open during registration]",
        ":::",
        "",
        "## Mode A — Register all at once",
        "",
        "1. Open the battery cover. Press the **Registration** button once.",
        "2. Enter your PIN, then press `*`.",
        "3. Press number `2` (or `4` depending on model) to select RFID mode.",
        "4. Place each card on the reader one at a time. A beep confirms each registration.",
        "5. Press **Registration** to finish.",
        "",
        f"Up to **{max_cards} cards** can be registered.",
    ]
    if has_individual:
        th_lines.extend([
            "",
            "## โหมดลงทะเบียนการ์ดแบบระบุช่องข้อมูล (Individual Register)",
            "",
            f"1. ทำตามขั้นตอนที่ 1 ถึง 3 ในการลงทะเบียนแบบทั่วไป",
            f"2. ป้อนหมายเลขระบุช่องข้อมูลการ์ดเป็นตัวเลข 3 หลัก (ตั้งแต่ 001 ถึง {max_cards:03d}) จากนั้นกดปุ่ม `#` หรือ `*`",
            "3. ทาบบัตรหรือแท็กบนพื้นที่เครื่องอ่านคีย์แพด หมายเลขช่องข้อมูลจะกะพริบบนคีย์แพดแสดงสถานะสำเร็จ",
            "4. ทำซ้ำขั้นตอนเดิมหากต้องการลงทะเบียนการ์ดช่องอื่น หรือกดปุ่ม **Registration** อีกครั้งเพื่อเสร็จสิ้นขั้นตอน",
        ])
        en_lines.extend([
            "",
            "## Mode B — Register one by one (assign slot numbers)",
            "",
            "1. Follow steps 1-3 above.",
            f"2. Enter a 3-digit slot number (001–{max_cards:03d}), then press `#` or `*`.",
            "3. Place the card on the reader. The slot number flashes on the keypad.",
            "4. Repeat for additional cards, or press Registration to finish.",
        ])
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_rfid_deletion(model):
    """Generate RFID deletion page"""
    th_lines = [
        make_frontmatter("การลบบัตร RFID", f"วิธีลบบัตร RFID บน {model}", 6),
        "",
        f"# การลบบัตร RFID",
        "",
        "## โหมดลบการ์ดทั้งหมดพร้อมกัน (Delete All)",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน) แล้วกดปุ่ม **Registration** 1 ครั้ง",
        "2. ป้อนรหัส PIN ปัจจุบันของคุณ แล้วตามด้วยปุ่ม `*`",
        "3. กดปุ่มหมายเลข `8` บนคีย์แพด",
        "4. กดปุ่ม `#` หรือ `*` ค้างไว้ประมาณ 5 วินาที เมื่อได้ยินเสียงสัญญาณเพลงเมโลดี้ดังขึ้น แสดงว่าบัตรทั้งหมดถูกลบเรียบร้อยแล้ว",
        "",
        "## โหมดลบการ์ดทีละใบแบบเฉพาะเจาะจง (Delete Individual)",
        "",
        "1. ทำตามขั้นตอนที่ 1 ถึง 2 ในการลบการ์ดแบบทั้งหมด",
        "2. กดปุ่มหมายเลข `8` จากนั้นตามด้วยปุ่ม `#` หรือ `*`",
        "3. ป้อนหมายเลขระบุช่องข้อมูลของการ์ด 3 หลักที่ต้องการลบ จากนั้นกดปุ่ม `#` หรือ `*`",
        "4. เมื่อระบบลบข้อมูลเสร็จสิ้น ตัวเลขทั้งหมดบนคีย์แพดจะสว่างขึ้น",
        "5. หากการลบเสร็จสิ้นหรือไม่มีการ์ดอื่นต้องการลบแล้ว ให้กดปุ่ม **Registration** เพื่อสิ้นสุดขั้นตอนและออกจากโหมด",
        "",
        ":::warning[ข้อควรระวัง]",
        "การลบข้อมูลบัตรจะไม่สามารถยกเลิกได้ คุณจะต้องนำบัตรดังกล่าวมาทำการลงทะเบียนใหม่อีกครั้งหากต้องการใช้งานต่อ",
        ":::",
    ]
    en_lines = [
        make_frontmatter("RFID Card Deletion", f"How to delete RFID cards on {model}", 6),
        "",
        f"# RFID Card Deletion",
        "",
        "## Mode A — Delete all at once",
        "",
        "1. Open the battery cover. Press **Registration** once.",
        "2. Enter your PIN, then press `*`.",
        "3. Press number `8`.",
        "4. Hold `#` or `*` for 5 seconds. When you hear a melody, all cards have been deleted.",
        "",
        "## Mode B — Delete one by one",
        "",
        "1. Follow steps 1-2 above.",
        "2. Press `8`, then press `#` or `*`.",
        "3. Enter the 3-digit slot number of the card to delete, then press `#` or `*`.",
        "4. When deletion is complete, all numbers on the keypad light up.",
        "5. If there's no card to delete, press **Registration** to exit.",
        "",
        ":::warning",
        "Deletion cannot be undone. You must re-register a card to use it again.",
        ":::",
    ]
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_fingerprint_registration(model, max_fp=100):
    """Generate fingerprint registration page"""
    th_lines = [
        make_frontmatter("การลงทะเบียนลายนิ้วมือ", f"วิธีลงทะเบียนลายนิ้วมือบน {model}", 7),
        "",
        f"# การลงทะเบียนลายนิ้วมือ",
        "",
        f":::caution[ข้อควรทราบ]",
        f"การลบลายนิ้วมือสำหรับระบบปกติจะสามารถลบข้อมูลทั้งหมดพร้อมกันเท่านั้น (Delete All) และเมื่อมีการลงทะเบียนลายนิ้วมือครบโควตาสูงสุด **{max_fp} ลายนิ้วมือ** แล้ว จะไม่สามารถเพิ่มลายนิ้วมือใหม่ได้อีกจนกว่าจะล้างข้อมูลลายนิ้วมือชุดเก่าออก",
        ":::",
        "",
        "## ขั้นตอนการลงทะเบียน",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน) แล้วกดปุ่ม **Registration** 1 ครั้ง",
        "2. ป้อนรหัส PIN ปัจจุบันของคุณ แล้วตามด้วยปุ่ม `*`",
        "3. กดปุ่มหมายเลข `2` หรือ `3` (ขึ้นอยู่กับรุ่นของผลิตภัณฑ์) เพื่อเข้าสู่โหมดลงทะเบียนลายนิ้วมือ",
        "4. แตะนิ้วมือที่คุณต้องการลงทะเบียนบนพื้นที่เซ็นเซอร์สแกน **3 ครั้งติดต่อกันอย่างสม่ำเสมอ**",
        "5. เมื่อลงทะเบียนเสร็จสมบูรณ์ จะมีเสียงสัญญาณบี๊บดังขึ้นยืนยัน",
        "6. กดปุ่ม **Registration** อีกครั้งเพื่อเสร็จสิ้นขั้นตอน",
        "",
        ":::note[ข้อแนะนำและสถานะการสแกน]",
        "- การสแกนครั้งที่ 1 สำเร็จ: ตัวเลข [1][2][3] บนแป้นคีย์แพดจะแสดงขึ้น โดยตัวเลข `[2]` จะกะพริบเพื่อรอรับการสแกนครั้งถัดไป",
        "- การสแกนครั้งที่ 2 สำเร็จ: ตัวเลข [1][2][3] บนแป้นคีย์แพดจะแสดงขึ้น โดยตัวเลข `[3]` จะกะพริบเพื่อรอรับการสแกนครั้งถัดไป",
        "- การสแกนครั้งที่ 3 สำเร็จ: ตัวเครื่องส่งสัญญาณว่าบันทึกลายนิ้วมือสำเร็จเรียบร้อย",
        "- สำหรับผู้ใช้ที่มีผิวลายนิ้วมือบางหรือเด็กเล็ก อาจทำให้เซ็นเซอร์อ่านข้อมูลได้ยากกว่าปกติ",
        ":::",
    ]
    en_lines = [
        make_frontmatter("Fingerprint Registration", f"How to register fingerprints on {model}", 7),
        "",
        f"# Fingerprint Registration",
        "",
        f":::caution",
        f"Fingerprint deletion is all-at-once only. Once {max_fp} fingerprints are registered, no more can be added until you delete all existing ones.",
        ":::",
        "",
        "## Steps",
        "",
        "1. Open the battery cover. Press **Registration** once.",
        "2. Enter your PIN, then press `*`.",
        "3. Press number `2` or `3` (depending on model) to select fingerprint mode.",
        "4. Place your finger on the fingerprint sensor **3 times consecutively** as instructed.",
        "5. A beep confirms successful registration.",
        "6. Press **Registration** to finish.",
        "",
        ":::note",
        "- 1st reading success: numbers [1][2][3] display with [2] blinking",
        "- 2nd reading success: numbers [1][2][3] display with [3] blinking",
        "- 3rd reading success: fingerprint registration complete",
        "- Damaged fingerprints or children's fingerprints may have difficulty authenticating",
        ":::",
    ]
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_fingerprint_deletion(model):
    """Generate fingerprint deletion page"""
    th_lines = [
        make_frontmatter("การลบลายนิ้วมือ", f"วิธีลบลายนิ้วมือบน {model}", 8),
        "",
        f"# การลบลายนิ้วมือ",
        "",
        "## โหมดลบลายนิ้วมือทั้งหมดพร้อมกัน (Delete All)",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน) แล้วกดปุ่ม **Registration** 1 ครั้ง",
        "2. ป้อนรหัส PIN ปัจจุบันของคุณ แล้วตามด้วยปุ่ม `*`",
        "3. กดปุ่มหมายเลข `9` บนคีย์แพด",
        "4. กดปุ่ม `#` หรือ `*` ค้างไว้ประมาณ 5 วินาที",
        "5. เมื่อได้ยินเสียงสัญญาณเพลงเมโลดี้ดังขึ้น ลายนิ้วมือทั้งหมดจะถูกลบเรียบร้อยแล้ว",
        "",
        "## โหมดลบลายนิ้วมือเฉพาะบุคคล (Delete Individual - ถ้ารองรับ)",
        "",
        "1. ทำตามขั้นตอนที่ 1 ถึง 3 ในการลบลายนิ้วมือแบบทั้งหมด",
        "2. กดปุ่ม `#` หรือ `*` จากนั้นตัวเลขทั้งหมดบนคีย์แพดจะสว่างขึ้นเพื่อเข้าสู่โหมดระบุตัวตน",
        "3. ป้อนหมายเลขช่องระบุลายนิ้วมือ 3 หลัก (ตั้งแต่ 001 ถึง 100) ที่ต้องการลบ จากนั้นตามด้วยปุ่ม `#` หรือ `*`",
        "4. เมื่อระบบลบข้อมูลเสร็จสิ้น จะมีเสียงสัญญาณแจ้งเตือนยืนยัน",
        "5. กดปุ่ม **Registration** อีกครั้งเพื่อสิ้นสุดขั้นตอน",
        "",
        ":::warning[ข้อควรระวัง]",
        "การลบข้อมูลลายนิ้วมือจะไม่สามารถยกเลิกได้ คุณจะต้องสแกนลายนิ้วมือเพื่อลงทะเบียนใหม่อีกครั้งหากต้องการใช้งานต่อ",
        ":::",
    ]
    en_lines = [
        make_frontmatter("Fingerprint Deletion", f"How to delete fingerprints on {model}", 8),
        "",
        f"# Fingerprint Deletion",
        "",
        "## Delete all",
        "",
        "1. Open the battery cover. Press **Registration** once.",
        "2. Enter your PIN, then press `*`.",
        "3. Press number `9`.",
        "4. Hold `#` or `*` for 5 seconds.",
        "5. When you hear a melody, all fingerprints have been deleted.",
        "",
        "## Delete by slot (if supported)",
        "",
        "1. Follow steps 1-3 above.",
        "2. Press `#` or `*`. All keypad numbers light up.",
        "3. Enter the 3-digit slot number (001–100) of the fingerprint to delete, then press `#` or `*`.",
        "4. A confirmation sound plays.",
        "5. Press **Registration** to exit.",
        "",
        ":::warning",
        "Deletion cannot be undone. You must re-register fingerprints to use them again.",
        ":::",
    ]
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_features(model, features_list):
    """Generate features page"""
    th_lines = [
        make_frontmatter("คุณสมบัติพิเศษ", f"คุณสมบัติพิเศษของ {model}", 9),
        "",
        f"# คุณสมบัติพิเศษ",
        "",
    ]
    en_lines = [
        make_frontmatter("Special Features", f"Special features of {model}", 9),
        "",
        f"# Special Features",
        "",
    ]
    for feature_en, description_en, feature_th, description_th in features_list:
        th_lines.append(f"## {feature_th}")
        th_lines.append("")
        th_lines.append(description_th)
        th_lines.append("")
        en_lines.append(f"## {feature_en}")
        en_lines.append("")
        en_lines.append(description_en)
        en_lines.append("")
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_alarms(model, alarms_list):
    """Generate alarms page"""
    th_lines = [
        make_frontmatter("สัญญาณเตือนและความปลอดภัย", f"สัญญาณเตือนและความปลอดภัยของ {model}", 10),
        "",
        f"# สัญญาณเตือนและความปลอดภัย",
        "",
    ]
    en_lines = [
        make_frontmatter("Alarms & Safety", f"Alarms and safety of {model}", 10),
        "",
        f"# Alarms & Safety",
        "",
    ]
    for alarm_en, desc_en, alarm_th, desc_th in alarms_list:
        th_lines.append(f"## {alarm_th}")
        th_lines.append("")
        th_lines.append(desc_th)
        th_lines.append("")
        en_lines.append(f"## {alarm_en}")
        en_lines.append("")
        en_lines.append(desc_en)
        en_lines.append("")
    return "\n".join(th_lines), "\n".join(en_lines)


# =============================================================================
# Product definitions (for each manual)
# =============================================================================

# Common defaults based on EPIC patterns
DEFAULT_OUTER_PARTS = [
    ("Number Pad", "Enter PIN or programming codes (1-9, *, 0, #)"),
    ("Status LED Lamp", "Shows lock status (idle / locked / error)"),
    ("Battery Lamp", "Lights up when battery is low"),
    ("RFID Card Reader", "Tap registered card here"),
    ("Reset Button", "Reset lock to factory defaults (rarely used)"),
    ("Emergency Battery Terminal", "Touch 9V battery here if lock is dead"),
    ("Outer Body Handle", "Pull down to retract bolt after unlock"),
]

DEFAULT_INNER_PARTS = [
    ("Battery Cover", "Slide off to access battery compartment"),
    ("Registration Button", "Used when registering PIN, Card or Fingerprint"),
    ("Open/Close Button", "One-touch unlock from inside"),
    ("Dual Lock Button", "Privacy mode - blocks outside access"),
    ("Inner Body Handle", "Pull down to retract bolt from inside"),
    ("Alkaline AA Battery", "Main power source"),
    ("Manual Lock Button", "Used to close the door in manual mode"),
]

DEFAULT_IN_BOX = [
    "Outer body",
    "Inner body",
    "Strike plate & fixing hardware",
    "Mechanical keys",
    "Batteries",
    "User manual",
]

# Common specs for EPIC products
DEFAULT_SPECS = [
    ("Door Thickness", "40~50mm"),
    ("PIN", "4~12 digits"),
    ("Power", "DC 6V (AA Alkaline x 4 or 8)"),
    ("Emergency Battery", "DC 9V Alkaline (sold separately)"),
    ("Fire Detection", "62°C±5°C / 72°C±5°C max"),
    ("Material (Outer)", "Al, Zn, ABS"),
    ("Material (Inner)", "Zn, ABS"),
]

# Common features
COMMON_FEATURES = [
    ("Random Number Feature",
     "Add random digits before/after your PIN to prevent shoulder-surfing. Total entry can include up to 20 digits.",
     "ฟีเจอร์สุ่มตัวเลข",
     "เพิ่มตัวเลขสุ่มก่อน/หลังรหัส PIN เพื่อป้องกันการแอบมอง รวมตัวเลขได้สูงสุด 20 หลัก"),
    ("Multi-touch Security",
     "After entering your PIN, the lock displays 3 random digits. Press those digits to unlock. This prevents fingerprint-pattern leakage on the keypad.",
     "ความปลอดภัย Multi-touch",
     "หลังจากใส่รหัส PIN ล็อกจะแสดงตัวเลขสุ่ม 3 ตัว ให้กดตัวเลขเหล่านั้นเพื่อปลดล็อก ป้องกันรอยนิ้วมือบนคีย์แพด"),
    ("Dual-mode Security",
     "After entering your PIN, the lock requires a second authentication (Card or Fingerprint) before unlocking. Maximum security for sensitive areas.",
     "ความปลอดภัยสองชั้น",
     "หลังจากใส่รหัส PIN ต้องยืนยันด้วยบัตรหรือลายนิ้วมือก่อนปลดล็อก เหมาะกับพื้นที่ต้องการความปลอดภัยสูง"),
    ("Auto/Manual Lock Mode",
     "Toggle between automatic locking (locks 2 seconds after door closes) and manual locking (you touch the keypad to lock).",
     "โหมดล็อกอัตโนมัติ/ด้วยตัวเอง",
     "สลับระหว่างล็อกอัตโนมัติ (ล็อก 2 วินาทีหลังประตูปิด) กับล็อกด้วยตัวเอง (แตะคีย์แพดเพื่อล็อก)"),
    ("Sound Volume Control",
     "Adjust operation sound across 7 levels via the keypad.",
     "ปรับระดับเสียง",
     "ปรับระดับเสียงการทำงานได้ 7 ระดับผ่านคีย์แพด"),
    ("Sound Mute",
     "Mute the operation sound for one use (e.g. late at night). Sound returns automatically afterward.",
     "ปิดเสียงชั่วคราว",
     "ปิดเสียงการทำงานสำหรับการใช้งานครั้งเดียว (เช่น ตอนกลางคืน) หลังจากนั้นเสียงจะกลับมาอัตโนมัติ"),
]

COMMON_ALARMS = [
    ("Anti-Hacking Alarm",
     "If the lock detects forced entry from inside or outside, it activates a loud alarm. Cancelled by entering valid PIN or Card.",
     "สัญญาณเตือนการแฮ็ก",
     "หากล็อกตรวจพบการบุกรุกจากภายในหรือภายนอก จะส่งเสียงเตือนดัง ยกเลิกได้ด้วยการใส่ PIN หรือบัตรที่ถูกต้อง"),
    ("Fire Sensor Alarm",
     "If internal temperature reaches 62°C±5°C, the lock automatically unlocks and sounds an alarm to allow safe evacuation.",
     "สัญญาณเตือนไฟไหม้",
     "หากอุณหภูมิภายในถึง 62°C±5°C ล็อกจะปลดล็อกอัตโนมัติและส่งเสียงเตือนเพื่อให้อพยพได้อย่างปลอดภัย"),
    ("Anti-Prank & 1-Minute Lockout",
     "After 5 consecutive failed PIN/Card/Fingerprint attempts, the lock stops responding for 1 minute and emits a warning tone.",
     "ป้องกันการแกล้ง + ล็อก 1 นาที",
     "หลังจากใส่รหัส/บัตร/ลายนิ้วมือผิด 5 ครั้งติดต่อกัน ล็อกจะหยุดตอบสนอง 1 นาที และส่งเสียงเตือน"),
    ("Replace Battery Alarm",
     "When battery is low, the Battery Replacement LED lights up and a notification melody plays.",
     "สัญญาณเตือนเปลี่ยนแบตเตอรี่",
     "เมื่อแบตเตอรี่ต่ำ ไฟ LED เตือนเปลี่ยนแบตเตอรี่จะติดและมีเสียงเตือนดังขึ้น"),
    ("Emergency Mechanical Key",
     "When the lock is not functioning normally, use the mechanical key to open the door. Keep keys in an accessible but secure location.",
     "กุญแจกลไกฉุกเฉิน",
     "เมื่อล็อกทำงานผิดปกติ ใช้กุญแจกลไกเปิดประตูได้ เก็บกุญแจไว้ในที่เข้าถึงได้แต่ปลอดภัย"),
]


def write_pages(slug, pages_dict):
    """Write generated pages to both TH (docs/) and EN (i18n/en/.../docs/)"""
    th_dir = DOCS_TH / slug
    en_dir = DOCS_EN / slug
    th_dir.mkdir(parents=True, exist_ok=True)
    en_dir.mkdir(parents=True, exist_ok=True)

    # _category_.json
    if "_category" in pages_dict:
        (th_dir / "_category_.json").write_text(pages_dict["_category"]["th"], encoding="utf-8")
        (en_dir / "_category_.json").write_text(pages_dict["_category"]["en"], encoding="utf-8")

    # Pages
    for page_name, content in pages_dict.items():
        if page_name == "_category":
            continue
        if "th" in content and "en" in content:
            (th_dir / f"{page_name}.md").write_text(content["th"], encoding="utf-8")
            (en_dir / f"{page_name}.md").write_text(content["en"], encoding="utf-8")


def generate_manual_pages(slug, model, th_title, en_title, th_desc, en_desc,
                          brochure_key=None, specs=None, outer_parts=None,
                          inner_parts=None, in_box=None, max_cards=100,
                          max_fingerprints=100, default_pin="1, 2, 3, 4",
                          pin_length="4~12", extra_features=None,
                          extra_alarms=None, manual_url=None,
                          consolidated_manual=None):
    """Generate all pages for a single manual"""
    pages_to_gen = get_pages_for_product(slug)
    brochure_image = None
    if brochure_key and brochure_key in BROCHURE_MAP:
        brochure_image = f"/img/brochures/{brochure_key}.png"

    pages = {}

    # _category_
    pages["_category"] = {
        "th": make_category_json(slug, th_title, th_desc, position=1),
        "en": make_category_json(slug, en_title, en_desc, position=1),
    }

    # overview (intro)
    if "intro" in pages_to_gen:
        features_for_card = []
        if brochure_image:
            features_for_card.append(f"📷 Brochure image: {brochure_key}.png")
        pages["intro"] = {}
        pages["intro"]["th"], pages["intro"]["en"] = gen_overview(
            model, slug, th_title, en_title, th_desc, en_desc,
            brochure_image=brochure_image,
            features=features_for_card,
            manual_url=manual_url,
            consolidated_manual=consolidated_manual
        )

    # specs
    if "specs" in pages_to_gen:
        specs_data = specs or DEFAULT_SPECS
        pages["specs"] = {}
        pages["specs"]["th"], pages["specs"]["en"] = gen_specs(model, specs_data)

    # components
    if "components" in pages_to_gen:
        outer = outer_parts or DEFAULT_OUTER_PARTS
        inner = inner_parts or DEFAULT_INNER_PARTS
        box = in_box or DEFAULT_IN_BOX
        pages["components"] = {}
        pages["components"]["th"], pages["components"]["en"] = gen_components(model, outer, inner, in_box=box)

    # pin-registration
    if "pin-registration" in pages_to_gen:
        pages["pin-registration"] = {}
        pages["pin-registration"]["th"], pages["pin-registration"]["en"] = gen_pin_registration(
            model, default_pin=default_pin, pin_length=pin_length
        )

    # rfid-registration
    if "rfid-registration" in pages_to_gen:
        pages["rfid-registration"] = {}
        pages["rfid-registration"]["th"], pages["rfid-registration"]["en"] = gen_rfid_registration(
            model, max_cards=max_cards
        )

    # rfid-deletion
    if "rfid-deletion" in pages_to_gen:
        pages["rfid-deletion"] = {}
        pages["rfid-deletion"]["th"], pages["rfid-deletion"]["en"] = gen_rfid_deletion(model)

    # fingerprint-registration
    if "fingerprint-registration" in pages_to_gen:
        pages["fingerprint-registration"] = {}
        pages["fingerprint-registration"]["th"], pages["fingerprint-registration"]["en"] = gen_fingerprint_registration(
            model, max_fp=max_fingerprints
        )

    # fingerprint-deletion
    if "fingerprint-deletion" in pages_to_gen:
        pages["fingerprint-deletion"] = {}
        pages["fingerprint-deletion"]["th"], pages["fingerprint-deletion"]["en"] = gen_fingerprint_deletion(model)

    # features
    if "features" in pages_to_gen:
        feats = extra_features or COMMON_FEATURES
        pages["features"] = {}
        pages["features"]["th"], pages["features"]["en"] = gen_features(model, feats)

    # alarms
    if "alarms" in pages_to_gen:
        alr = extra_alarms or COMMON_ALARMS
        pages["alarms"] = {}
        pages["alarms"]["th"], pages["alarms"]["en"] = gen_alarms(model, alr)

    return pages


# =============================================================================
# Main — generate all 22 manuals
# =============================================================================

# (slug, model, th_title, en_title, th_desc, en_desc, brochure_key, specs_override, manual_url)
MANUALS = [
    # ===== Tier C (vision extraction) =====
    ("es-303g", "ES-303G", "กุญแจประตูกระจก ES-303G", "ES-303G Glass Door Lock",
     "กุญแจดิจิทัลสำหรับประตูกระจก รองรับ PIN และบัตร RFID ติดตั้งง่ายด้วยระบบจดจำซ้ายขวาอัตโนมัติ",
     "Digital lock for glass doors. Supports PIN and RFID. Easy installation with automatic left/right detection.",
     "es-303g", None, "https://www.epic.co.kr/home/manual/"),
    ("ef-p8800k", "EF-P8800K", "กุญแจดิจิทัล EF-P8800K", "EF-P8800K Digital Lock",
     "กุญแจดิจิทัล Main Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และรีโมทคอนโทรล",
     "Main type digital lock supporting PIN, RFID, Fingerprint, and Remote Control.",
     "ef-p8800k", None, "https://www.epic.co.kr/home/manual/"),
    ("es-m50", "ES-M50", "กุญแจดิจิทัล ES-M50", "ES-M50 Digital Lock",
     "กุญแจดิจิทัลที่รองรับ PIN และบัตร RFID สำหรับประตูหลัก",
     "Digital lock supporting PIN and RFID for main doors.",
     "es-m50", None, "https://www.epic.co.kr/home/manual/"),
    ("es-p9100fk", "ES-P9100FK", "กุญแจดิจิทัล ES-P9100FK", "ES-P9100FK Digital Lock",
     "กุญแจดิจิทัล Main Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และกุญแจกลไก",
     "Main type digital lock supporting PIN, RFID, Fingerprint, and Mechanical Key.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("es-t153", "ES-T153", "กุญแจดิจิทัล ES-T153", "ES-T153 Digital Lock",
     "กุญแจดิจิทัลที่รองรับ PIN และบัตร RFID",
     "Digital lock supporting PIN and RFID.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("n-touch", "N-TOUCH", "กุญแจดิจิทัล N-TOUCH", "N-TOUCH Digital Lock",
     "กุญแจดิจิทัลแบบ PIN อย่างเดียว เรียบง่ายและใช้งานง่าย",
     "PIN-only digital lock, simple and easy to use.",
     "n-touch", None, "https://www.epic.co.kr/home/manual/"),
    ("touch", "TOUCH", "กุญแจดิจิทัล TOUCH", "TOUCH Digital Lock",
     "กุญแจดิจิทัลที่รองรับ PIN และ Smart Card",
     "Digital lock supporting PIN and Smart Card.",
     "touch", None, "https://www.epic.co.kr/home/manual/"),
    ("triplex-2way", "TRIPLEX 2way", "กุญแจดิจิทัล TRIPLEX 2way", "TRIPLEX 2way Digital Lock",
     "กุญแจดิจิทัลที่รองรับ PIN, Smart Key, Home Network และ Remote Control",
     "Digital lock supporting PIN, Smart Key, Home Network, and Remote Control.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("triplex-3way", "TRIPLEX 3way", "กุญแจดิจิทัล TRIPLEX 3way", "TRIPLEX 3way Digital Lock",
     "กุญแจดิจิทัลที่รองรับ PIN, Smart Key และกุญแจกลไกฉุกเฉิน",
     "Digital lock supporting PIN, Smart Key, and emergency mechanical key.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("ef-8000l", "EF-8000L", "กุญแจดิจิทัล EF-8000L", "EF-8000L Digital Lock",
     "กุญแจดิจิทัล Main Type รองรับ PIN, Smart Key, ลายนิ้วมือ และรีโมทคอนโทรล",
     "Main type digital lock supporting PIN, Smart Key, Fingerprint, and Remote Control.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("es-809l", "ES-809L", "กุญแจดิจิทัล ES-809L", "ES-809L Digital Lock",
     "กุญแจดิจิทัล Main Type รองรับ PIN, Smart Key และกุญแจกลไก",
     "Main type digital lock supporting PIN, Smart Key, and Mechanical Key.",
     None, None, "https://www.epic.co.kr/home/manual/"),

    # ===== Tier A+B (existing products) =====
    ("es-b10", "ES-B10", "กุญแจดิจิทัล ES-B10", "ES-B10 Digital Lock",
     TH_DESCRIPTIONS["ES-B10"],
     "A digital lock that can be opened by PIN number, random number feature, and manual lock knob. It has safety features like fire detection and anti-hacking alarms.",
     "es-b10", None, "https://www.epic.co.kr/home/manual/"),
    ("es-l200", "ES-L200", "กุญแจดิจิทัล ES-L200", "ES-L200 Digital Lock",
     TH_DESCRIPTIONS["ES-L200"],
     "Compact digital lock for lockers. Opens with PIN or RFID card.",
     "es-l200", None, "https://www.epic.co.kr/home/manual/"),
    ("os300h", "OS300H", "กุญแจดิจิทัล OS300H", "OS300H Digital Lock",
     TH_DESCRIPTIONS["OS300H"],
     "Rim-type digital lock for swing doors. Opens with PIN or RFID card.",
     "os300h", None, "https://www.epic.co.kr/home/manual/"),
    ("popscan", "POPscan", "กุญแจดิจิทัล POPscan", "POPscan Digital Lock",
     TH_DESCRIPTIONS["POPscan"],
     "POPscan digital lock in black. Supports fast scanning.",
     "popscan", None, "https://www.epic.co.kr/home/manual/"),
    ("consolidated-manual-rev-09", "Consolidated Manual Rev.09", "คู่มือรวม Rev.09", "Consolidated Manual Rev.09",
     TH_DESCRIPTIONS["Consolidated Manual Rev.09"],
     "Consolidated manual covering multiple EPIC door lock models.",
     None, None, "https://www.epic.co.kr/home/manual/"),

    # ===== New product pages (Consolidated Manual models) =====
    ("es-s100dr", "ES-S100Dr", "กุญแจดิจิทัล ES-S100Dr", "ES-S100Dr Digital Lock",
     "กุญแจดิจิทัล Rim Type เปิดด้วยรหัส PIN และบัตร RFID เหมาะกับประตูบานเปิด",
     "Rim-type digital lock for swing doors. Opens with PIN or RFID card.",
     "es-s100dr", None, "https://www.epic.co.kr/home/manual/"),
    ("es-f300dr", "ES-F300Dr", "กุญแจดิจิทัล ES-F300Dr", "ES-F300Dr Digital Lock",
     "กุญแจดิจิทัล Rim Type เปิดด้วยรหัส PIN, บัตร RFID และลายนิ้วมือ",
     "Rim-type digital lock. Opens with PIN, RFID card, or fingerprint.",
     "es-f300dr", None, "https://www.epic.co.kr/home/manual/"),
    ("es-f301d", "ES-F301D", "กุญแจดิจิทัล ES-F301D", "ES-F301D Digital Lock",
     "กุญแจดิจิทัล Rim Type เปิดด้วยรหัส PIN, บัตร RFID และลายนิ้วมือ",
     "Rim-type digital lock. Opens with PIN, RFID card, or fingerprint.",
     "es-f301d", None, "https://www.epic.co.kr/home/manual/"),
    ("es-f501d", "ES-F501D", "กุญแจดิจิทัล ES-F501D", "ES-F501D Digital Lock",
     "กุญแจดิจิทัล Rim Type รองรับ PIN, บัตร RFID และลายนิ้วมือ (รุ่น ES-F501D/H, ES-F500D/H, ES-S510D/H ใช้คู่มือเดียวกัน)",
     "Rim-type digital lock supporting PIN, RFID card, and fingerprint (ES-F501D/H, ES-F500D/H, ES-S510D/H share the same manual).",
     "es-f501d", None, "https://www.epic.co.kr/home/manual/"),
    ("es-ff730gr", "ES-FF730Gr", "กุญแจดิจิทัล ES-FF730Gr", "ES-FF730Gr Digital Lock",
     "กุญแจดิจิทัล Gate Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และกุญแจกลไก",
     "Gate-type digital lock supporting PIN, RFID card, fingerprint, and mechanical key.",
     "es-ff730gr", None, "https://www.epic.co.kr/home/manual/"),
    ("es-ff731g", "ES-FF731G", "กุญแจดิจิทัล ES-FF731G", "ES-FF731G Digital Lock",
     "กุญแจดิจิทัล Gate Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และกุญแจกลไก",
     "Gate-type digital lock supporting PIN, RFID card, fingerprint, and mechanical key.",
     "es-ff731g", None, "https://www.epic.co.kr/home/manual/"),
    ("es-s740d", "ES-S740D", "กุญแจดิจิทัล ES-S740D", "ES-S740D Digital Lock",
     "กุญแจดิจิทัล Gate Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และกุญแจกลไก",
     "Gate-type digital lock supporting PIN, RFID card, fingerprint, and mechanical key.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("es-f7000kr", "ES-F7000Kr", "กุญแจดิจิทัล ES-F7000Kr", "ES-F7000Kr Digital Lock",
     "กุญแจดิจิทัล Mortise Type รองรับ PIN, บัตร RFID และลายนิ้วมือ",
     "Mortise-type digital lock supporting PIN, RFID card, and fingerprint.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("es-f9000kr", "ES-F9000Kr", "กุญแจดิจิทัล ES-F9000Kr", "ES-F9000Kr Digital Lock",
     "กุญแจดิจิทัล Mortise Type รองรับ PIN, บัตร RFID, ลายนิ้วมือ และกุญแจกลไก",
     "Mortise-type digital lock supporting PIN, RFID card, fingerprint, and mechanical key.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("es-p8800k", "ES-P8800K", "กุญแจดิจิทัล ES-P8800K", "ES-P8800K Digital Lock",
     "กุญแจดิจิทัล Push Pull Type รองรับ PIN, บัตร RFID และลายนิ้วมือ",
     "Push-pull type digital lock supporting PIN, RFID card, and fingerprint.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("epic-things-app-user-manual", "EPIC Things APP User Manual", "คู่มือแอป EPIC Things", "EPIC Things APP User Manual",
     TH_DESCRIPTIONS["EPIC Things APP User Manual"],
     "User manual for the EPIC Things mobile app for controlling smart locks via smartphone.",
     None, None, "https://www.epic.co.kr/home/manual/"),

]


def main():
    print(f"=== Building all manuals ===")
    print(f"TH docs dir: {DOCS_TH}")
    print(f"EN docs dir: {DOCS_EN}")

    # Models in consolidated manual Rev.09
    consolidated_models = {
        "es-s100dr", "es-f300dr", "es-f301d", "es-f501d",
        "es-ff730gr", "es-ff731g", "es-s740d",
        "es-f7000kr", "es-f9000kr", "es-p8800k",
    }

    for entry in MANUALS:
        slug, model, th_title, en_title, th_desc, en_desc, brochure_key, specs_override, manual_url = entry
        print(f"  → {slug} ({model})")

        # EF-8000L and ES-809L have fingerprint so use max_fingerprints
        max_fp = 100
        max_cards = 100
        if slug in ["es-l200", "es-303g", "es-m50", "es-t153", "es-k70", "es-b10", "es-p9100fk", "ef-p8800k", "ef-8000l", "es-809l", "os300h", "popscan"]:
            max_cards = 100
        if slug in ["popscan", "ef-p8800k", "ef-8000l", "es-p9100fk"]:
            max_cards = 100 if slug != "popscan" else 200

        # Link to consolidated manual for new models
        consolidated = "consolidated-manual-rev-09" if slug in consolidated_models else None

        pages = generate_manual_pages(
            slug=slug, model=model,
            th_title=th_title, en_title=en_title,
            th_desc=th_desc, en_desc=en_desc,
            brochure_key=brochure_key,
            specs=specs_override,
            max_cards=max_cards,
            max_fingerprints=max_fp,
            default_pin="1, 2, 3, 4",
            pin_length="4~12",
            manual_url=manual_url,
            consolidated_manual=consolidated,
        )
        write_pages(slug, pages)

    print(f"\n=== Done ===")
    print(f"Total manuals: {len(MANUALS)}")


if __name__ == "__main__":
    main()
