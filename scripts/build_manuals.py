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
    "Features": "คุณสมบัติ",
    "Alarms": "สัญญาณเตือน",
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
    "Always register pin number while door is open.": "ลงทะเบียนรหัส PIN ขณะประตูเปิดเสมอ",
    "Default pin number is": "รหัส PIN เริ่มต้นคือ",
    "Door must be open": "ประตูต้องเปิด",
    "Up to": "สูงสุด",
    "cards can be registered": "บัตรที่ลงทะเบียนได้",
    "fingerprints can be registered": "ลายนิ้วมือที่ลงทะเบียนได้",
    "Emergency Battery": "ไฟฉุกเฉิน",
    "Battery": "แบตเตอรี่",
    "Door Thickness": "ความหนาประตู",
    "Material": "วัสดุ",
    "Outer body": "ตัวล็อกด้านนอก",
    "Inner body": "ตัวล็อกด้านใน",
    "Operating Temperature": "อุณหภูมิใช้งาน",
    "Power": "พลังงาน",
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
    "Reset Button": "ปุ่มรีเซ็ต",
    "Battery Lamp": "ไฟแบตเตอรี่",
    "Status LED Lamp": "ไฟ LED แสดงสถานะ",
    "RFID Card Reader": "เครื่องอ่านบัตร RFID",
    "Emergency Battery Terminal": "ขั้วแบตเตอรี่ฉุกเฉิน",
    "Mechanical Key Hole Cover": "ฝาครอบรูกุญแจกลไก",
    "Outer Body Handle": "ที่จับด้านนอก",
    "Battery Cover": "ฝาครอบแบตเตอรี่",
    "Registration Button": "ปุ่มลงทะเบียน",
    "Open/Close Button": "ปุ่มเปิด/ปิด",
    "Dual Lock Button": "ปุ่ม Dual Lock",
    "Inner Body Handle": "ที่จับด้านใน",
    "Alkaline AA Battery": "แบตเตอรี่อัลคาไลน์ AA",
    "Mortise": "มอร์ทิส",
    "Deadbolt": "กลอนตาย",
    "Latch Bolt": "สลัก",
    "Manual Lock Button": "ปุ่มล็อกด้วยตัวเอง",
    "Door Closing Sensor": "เซ็นเซอร์ตรวจจับประตูปิด",
    "Safety Button": "ปุ่ม Safety",
    "Manual Lock/Unlock Knob": "ปุ่มหมุนล็อก/ปลดล็อกด้วยตัวเอง",
    "Auto Lock Sensor": "เซ็นเซอร์ล็อกอัตโนมัติ",
    "Inside double lock": "ล็อกสองชั้นด้านใน",
    "Outside Force Lock": "ล็อกบังคับจากด้านนอก",
    "Auto Lock Mode": "โหมดล็อกอัตโนมัติ",
    "Manual Lock Mode": "โหมดล็อกด้วยตัวเอง",
    "Multi-touch Security": "ความปลอดภัย Multi-touch",
    "Dual-mode Security": "ความปลอดภัยสองชั้น",
    "Random Number Feature": "ฟีเจอร์สุ่มตัวเลข",
    "Voice Mode": "โหมดเสียง",
    "Buzzer Mode": "โหมดเสียงบี๊ป",
    "Sound Volume": "ระดับเสียง",
    "Sound Mute": "ปิดเสียง",
    "Anti-Prank": "ป้องกันการแกล้ง",
    "Fire Alarm": "สัญญาณเตือนไฟไหม้",
    "Anti-Hacking": "ป้องกันการแฮ็ก",
    "Intrusion Alarm": "สัญญาณเตือนการบุกรุก",
    "Replace Battery": "เปลี่ยนแบตเตอรี่",
    "Emergency Mechanical Key": "กุญแจกลไกฉุกเฉิน",
    "Lock Status Display": "การแสดงสถานะล็อก",
    "Deadbolt Error": "ข้อผิดพลาดกลอนตาย",
    "Open battery cover": "เปิดฝาครอบแบตเตอรี่",
    "Press [Registration] button": "กดปุ่ม [Registration]",
    "beep sound will be heard": "จะได้ยินเสียงบี๊บ",
    "Enter pin number, followed by": "ใส่รหัส PIN แล้วกด",
    "button": "ปุ่ม",
    "Place smart key to be registered on the Card reader": "วางบัตรที่ต้องการลงทะเบียนบนเครื่องอ่าน",
    "Long Press": "กดค้างไว้",
    "for 5 seconds": "5 วินาที",
    "When the melody is heard, All smart keys are deleted": "เมื่อได้ยินเพลง บัตรทั้งหมดถูกลบแล้ว",
    "Smart key entry standby": "สถานะรอรับบัตร",
    "After deletion is complete": "เมื่อลบเสร็จ",
    "press [Registration] button to finish": "กดปุ่ม [Registration] เพื่อเสร็จสิ้น",
}

# Thai descriptions for products (Tier A+B from existing product.json)
TH_DESCRIPTIONS = {
    "ES-B10": "กุญแจดิจิทัลที่เปิดได้ด้วยรหัส PIN ฟีเจอร์สุ่มตัวเลข และปุ่มล็อกด้วยตัวเอง มีระบบตรวจจับไฟไหม้และสัญญาณเตือนการโจมตี",
    "ES-L200": "กุญแจดิจิทัลขนาดเล็กสำหรับตู้ล็อกเกอร์ เปิดด้วยรหัส PIN หรือบัตร RFID",
    "OS300H": "กุญแจดิจิทัลระบบ Rim Type สำหรับประตูบานเปิด เปิดด้วยรหัส PIN หรือบัตร RFID",
    "POPscan": "กุญแจดิจิทัลรุ่น POPscan สีดำ รองรับการสแกนที่รวดเร็ว",
    "Assembly Guide for Key Tail": "คู่มือการประกอบชิ้นส่วนหางกุญแจสำหรับการติดตั้ง",
    "Consolidated Manual Rev.09": "คู่มือรวมฉบับแก้ไขครั้งที่ 9 ครอบคลุมหลายรุ่น",
    "EPIC Things APP User Manual": "คู่มือการใช้งานแอป EPIC Things สำหรับควบคุมกุญแจอัจฉริยะผ่านสมาร์ทโฟน",
    "IR Sensor Usage Guide for Face ID": "คู่มือการใช้งานเซ็นเซอร์ IR สำหรับฟีเจอร์ Face ID",
    "Outer Body Cable Management Guide": "คู่มือการจัดการสายเคเบิลของตัวล็อกด้านนอก",
    "Remote-Control-Module-Compatibility-Guide": "ตารางความเข้ากันได้ของโมดูลรีโมทคอนโทรล",
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
    "assembly-guide-for-key-tail": [],
    "consolidated-manual-rev-09": ["pin", "rfid", "fingerprint", "face"],
    "epic-things-app-user-manual": ["app"],
    "ir-sensor-usage-guide-for-face-id": [],
    "outer-body-cable-management-guide": [],
    "remote-control-module-compatibility-guide": [],
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
                 brochure_image=None, features=None, manual_url=None):
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
    th_lines.append("## คุณสมบัติเด่น")
    th_lines.append("")
    if features:
        for f in features:
            th_lines.append(f"- **{f}**")
        th_lines.append("")
    th_lines.append(f":::warning ต้องติดตั้งโดยช่างผู้เชี่ยวชาญ")
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
    en_lines.append("## Key Features")
    en_lines.append("")
    if features:
        for f in features:
            en_lines.append(f"- **{f}**")
        en_lines.append("")
    en_lines.append(f":::warning Installation by professional required")
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
            th_lines.append(f"| {label} | {val} |")
            en_lines.append(f"| {label} | {val} |")
    elif isinstance(specs_data, dict):
        for k, v in specs_data.items():
            th_lines.append(f"- **{k}**: {v}")
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
        th_lines.append(f"| {i} | **{name}** | {func} |")
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
        th_lines.append(f"| {i} | **{name}** | {func} |")
        en_lines.append(f"| {i} | **{name}** | {func} |")
    if in_box:
        th_lines.append("")
        en_lines.append("")
        th_lines.append("## อุปกรณ์ในกล่อง")
        en_lines.append("## In the box")
        for item in in_box:
            th_lines.append(f"- {item}")
            en_lines.append(f"- {item}")
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_pin_registration(model, default_pin="1, 2, 3, 4", pin_length="4~12"):
    """Generate PIN registration page"""
    th_lines = [
        make_frontmatter("การลงทะเบียนรหัส PIN", f"วิธีเปลี่ยนรหัส PIN บน {model}", 4),
        "",
        f"# การลงทะเบียนรหัส PIN",
        "",
        f":::caution ก่อนเริ่ม",
        f"- ลงทะเบียนรหัส PIN **ขณะประตูเปิดเสมอ**",
        f"- รหัส PIN เริ่มต้นคือ **`{default_pin}`** เปลี่ยนก่อนใช้งานครั้งแรก",
        f"- เลือก PIN {pin_length} หลัก หลีกเลี่ยงรหัสที่เดาง่าย เช่น `1111`, `1234`, ปีเกิด",
        f"- **ไม่มีวิธีรีเซ็ตจากโรงงาน** ถ้าลืมรหัส PIN ต้องเรียกช่าง",
        ":::",
        "",
        "## ขั้นตอน",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ (ด้านใน) กดปุ่ม **Registration** หนึ่งครั้ง จะได้ยินเสียงบี๊บ",
        "2. ใส่รหัส PIN ปัจจุบัน แล้วกด `*`",
        "3. กดปุ่มหมายเลขตามที่ระบุในคู่มือ (เช่น `1`) เพื่อเลือกโหมดเปลี่ยน PIN",
        "4. ใส่รหัส PIN ใหม่ แล้วกด `*`",
        "5. ใส่รหัส PIN ใหม่อีกครั้งเพื่อยืนยัน แล้วกด `*`",
        "6. ล็อกจะเล่นเพลงสั้นเพื่อยืนยันว่าลงทะเบียนสำเร็จ",
        "",
        ":::note",
        "คุณมีเวลา 10 วินาทีระหว่างขั้นตอน ถ้านานเกินไปล็อกจะหมดเวลาและต้องเริ่มใหม่",
        ":::",
    ]
    en_lines = [
        make_frontmatter("PIN Registration", f"How to change PIN on {model}", 4),
        "",
        f"# PIN Registration",
        "",
        f":::caution Before you start",
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
        f":::tip ความเข้ากันได้",
        f"ใช้ได้เฉพาะบัตร RFID 13.56 MHz ที่เข้ากันได้กับ EPIC บัตรในกล่องต้องลงทะเบียนเอง",
        ":::",
        "",
        f":::caution ประตูต้องเปิดขณะลงทะเบียน",
        ":::",
        "",
        "## โหมด A — ลงทะเบียนทั้งหมดพร้อมกัน",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ กดปุ่ม **Registration** หนึ่งครั้ง",
        "2. ใส่รหัส PIN แล้วกด `*`",
        "3. กดปุ่มหมายเลข `2` (หรือ `4` แล้วแต่รุ่น) เพื่อเลือกโหมด RFID",
        "4. วางบัตรบนเครื่องอ่านทีละใบ จะได้ยินเสียงบี๊บทุกครั้ง",
        "5. กดปุ่ม **Registration** เพื่อเสร็จสิ้น",
        "",
        f"ลงทะเบียนได้สูงสุด **{max_cards} ใบ**",
    ]
    en_lines = [
        make_frontmatter("RFID Card Registration", f"How to register RFID cards on {model}", 5),
        "",
        f"# RFID Card Registration",
        "",
        f":::tip Compatibility",
        f"Only 13.56 MHz RFID cards compatible with EPIC work with this lock. Cards included in the box must be registered manually.",
        ":::",
        "",
        f":::caution Door must be open during registration",
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
            "## โหมด B — ลงทะเบียนทีละใบ (ระบุหมายเลขช่อง)",
            "",
            f"1. ทำตามขั้นตอน 1-3 ข้างต้น",
            f"2. ใส่หมายเลขช่อง 3 หลัก (001–{max_cards:03d}) แล้วกด `#` หรือ `*`",
            "3. วางบัตรบนเครื่องอ่าน หมายเลขช่องจะกะพริบบนคีย์แพด",
            "4. ทำซ้ำสำหรับบัตรใบอื่น หรือกด Registration เพื่อจบ",
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
        "## โหมด A — ลบทั้งหมดพร้อมกัน",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ กดปุ่ม **Registration** หนึ่งครั้ง",
        "2. ใส่รหัส PIN แล้วกด `*`",
        "3. กดปุ่มหมายเลข `8`",
        "4. กดปุ่ม `#` หรือ `*` ค้างไว้ 5 วินาที เมื่อได้ยินเพลง บัตรทั้งหมดถูกลบแล้ว",
        "",
        "## โหมด B — ลบทีละใบ",
        "",
        "1. ทำตามขั้นตอน 1-2 ข้างต้น",
        "2. กดปุ่ม `8` แล้วกด `#` หรือ `*`",
        "3. ใส่หมายเลขช่อง 3 หลักของบัตรที่ต้องการลบ แล้วกด `#` หรือ `*`",
        "4. เมื่อลบเสร็จ ตัวเลขทุกตัวบนคีย์แพดจะติด",
        "5. ถ้าไม่มีบัตรที่ต้องการลบ กดปุ่ม **Registration** เพื่อออก",
        "",
        ":::warning",
        "การลบบัตรไม่สามารถยกเลิกได้ ต้องลงทะเบียนใหม่หากต้องการใช้บัตรอีกครั้ง",
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
        f":::caution",
        f"การลบลายนิ้วมือสามารถทำได้ทีละครั้งเท่านั้น (ลบทั้งหมด) เมื่อลงทะเบียนครบ {max_fp} ลายนิ้วมือ จะไม่สามารถเพิ่มได้อีก จนกว่าจะลบของเก่าออก",
        ":::",
        "",
        "## ขั้นตอน",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ กดปุ่ม **Registration** หนึ่งครั้ง",
        "2. ใส่รหัส PIN แล้วกด `*`",
        "3. กดปุ่มหมายเลข `2` หรือ `3` (ตามรุ่น) เพื่อเลือกโหมดลายนิ้วมือ",
        "4. วางนิ้วบนเซ็นเซอร์ลายนิ้วมือ **3 ครั้งติดต่อกัน** ตามคำแนะนำ",
        "5. เมื่อสำเร็จ จะมีเสียงบี๊บยืนยัน",
        "6. กดปุ่ม **Registration** เพื่อเสร็จสิ้น",
        "",
        ":::note",
        "- การอ่านครั้งแรกสำเร็จ: ตัวเลข [1][2][3] แสดงพร้อมกระพริบหมายเลข [2]",
        "- การอ่านครั้งที่สองสำเร็จ: ตัวเลข [1][2][3] แสดงพร้อมกระพริบหมายเลข [3]",
        "- การอ่านครั้งที่สามสำเร็จ: ลายนิ้วมือลงทะเบียนเสร็จสมบูรณ์",
        "- ลายนิ้วมือที่เสียหายหรือลายนิ้วมือเด็กอาจมีปัญหาในการยืนยันตัวตน",
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
        "## ลบทั้งหมด",
        "",
        "1. เปิดฝาครอบแบตเตอรี่ กดปุ่ม **Registration** หนึ่งครั้ง",
        "2. ใส่รหัส PIN แล้วกด `*`",
        "3. กดปุ่มหมายเลข `9`",
        "4. กดปุ่ม `#` หรือ `*` ค้างไว้ 5 วินาที",
        "5. เมื่อได้ยินเพลง ลายนิ้วมือทั้งหมดถูกลบแล้ว",
        "",
        "## ลบทีละช่อง (ถ้ารองรับ)",
        "",
        "1. ทำตามขั้นตอน 1-3 ข้างต้น",
        "2. กดปุ่ม `#` หรือ `*` ตัวเลขทุกตัวบนคีย์แพดจะติด",
        "3. ใส่หมายเลขช่อง 3 หลัก (001–100) ของลายนิ้วมือที่ต้องการลบ แล้วกด `#` หรือ `*`",
        "4. เมื่อลบเสร็จ จะมีเสียงยืนยัน",
        "5. กดปุ่ม **Registration** เพื่อออก",
        "",
        ":::warning",
        "การลบลายนิ้วมือไม่สามารถยกเลิกได้ ต้องลงทะเบียนใหม่",
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
                          extra_alarms=None, manual_url=None):
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
            manual_url=manual_url
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
    ("assembly-guide-for-key-tail", "Assembly Guide for Key Tail", "คู่มือประกอบหางกุญแจ", "Key Tail Assembly Guide",
     TH_DESCRIPTIONS["Assembly Guide for Key Tail"],
     "Step-by-step guide for assembling the key tail component during installation.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("consolidated-manual-rev-09", "Consolidated Manual Rev.09", "คู่มือรวม Rev.09", "Consolidated Manual Rev.09",
     TH_DESCRIPTIONS["Consolidated Manual Rev.09"],
     "Consolidated manual covering multiple EPIC door lock models.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("epic-things-app-user-manual", "EPIC Things APP User Manual", "คู่มือแอป EPIC Things", "EPIC Things APP User Manual",
     TH_DESCRIPTIONS["EPIC Things APP User Manual"],
     "User manual for the EPIC Things mobile app for controlling smart locks via smartphone.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("ir-sensor-usage-guide-for-face-id", "IR Sensor Usage Guide for Face ID", "คู่มือใช้งาน IR Sensor สำหรับ Face ID", "IR Sensor Usage Guide for Face ID",
     TH_DESCRIPTIONS["IR Sensor Usage Guide for Face ID"],
     "Guide for using the IR sensor for Face ID functionality.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("outer-body-cable-management-guide", "Outer Body Cable Management Guide", "คู่มือจัดการสายเคเบิลตัวล็อกด้านนอก", "Outer Body Cable Management Guide",
     TH_DESCRIPTIONS["Outer Body Cable Management Guide"],
     "Guide for cable management on the outer body of EPIC locks.",
     None, None, "https://www.epic.co.kr/home/manual/"),
    ("remote-control-module-compatibility-guide", "Remote Control Module Compatibility Guide", "ตารางความเข้ากันได้ของโมดูลรีโมท", "Remote Control Module Compatibility",
     TH_DESCRIPTIONS["Remote-Control-Module-Compatibility-Guide"],
     "Compatibility table for remote control modules across EPIC models.",
     None, None, "https://www.epic.co.kr/home/manual/"),
]


def main():
    print(f"=== Building all manuals ===")
    print(f"TH docs dir: {DOCS_TH}")
    print(f"EN docs dir: {DOCS_EN}")

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
        )
        write_pages(slug, pages)

    print(f"\n=== Done ===")
    print(f"Total manuals: {len(MANUALS)}")


if __name__ == "__main__":
    main()
