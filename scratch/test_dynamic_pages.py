import os
import json
import re
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

# Translation dictionary
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
}

TRANSLATIONS_DICT = {
    "open the battery cover": "เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน)",
    "open the [battery cover]": "เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน)",
    "open battery cover": "เปิดฝาครอบแบตเตอรี่",
    "open battery compartment cover": "เปิดฝาครอบแบตเตอรี่ (ตัวเครื่องด้านใน)",
    "press [registration] button once": "กดปุ่มลงทะเบียน [Registration] 1 ครั้ง",
    "press registration button once": "กดปุ่มลงทะเบียน [Registration] 1 ครั้ง",
    "beep sound will be heard": "จะมีเสียงสัญญาณบี๊บดังขึ้น",
    "beep": "บี๊บ",
    "enter current pin number followed by [✱] button": "ป้อนรหัส PIN ปัจจุบัน แล้วตามด้วยปุ่ม [✱]",
    "enter pin number, followed by [✱] button": "ป้อนรหัส PIN แล้วตามด้วยปุ่ม [✱]",
    "press number 1 button": "กดปุ่มหมายเลข [1]",
    "press [1] button": "กดปุ่มหมายเลข [1]",
    "enter new pin number to be registered 4~12 digits": "ป้อนรหัส PIN ใหม่ที่ต้องการลงทะเบียน (4~12 หลัก)",
    "press [✱] button": "กดปุ่ม [✱]",
    "press the [✱] button": "กดปุ่ม [✱]",
    "a melody will be heard, and the registration is complete": "จะมีเสียงสัญญาณเพลงเมโลดี้ดังขึ้นเพื่อยืนยันว่าการลงทะเบียนเสร็จสิ้น",
    "press [registration] button after cards has been registered": "กดปุ่มลงทะเบียน [Registration] หลังจากลงทะเบียนการ์ดเสร็จสิ้น",
    "and the registration is complete": "และการลงทะเบียนเสร็จสมบูรณ์",
    "melody will be heard and the door will open": "จะมีเสียงสัญญาณเพลงเมโลดี้ดังขึ้นและประตูจะเปิดออก",
    "place rfid card to be registered on the card reader": "ทาบบัตร RFID ที่ต้องการลงทะเบียนบนพื้นที่เครื่องอ่านการ์ด",
    "place registered rfid card on the reader": "ทาบบัตร RFID ที่ลงทะเบียนแล้วบนพื้นที่เครื่องอ่านการ์ด",
    "place smart keys to be registered on the card reader": "ทาบสมาร์ทคีย์ที่ต้องการลงทะเบียนบนพื้นที่เครื่องอ่านการ์ด",
    "during automatic detection mode": "เมื่ออยู่ในโหมดตรวจจับอัตโนมัติ (Automatic Detection)",
    "during manual detection mode": "เมื่ออยู่ในโหมดตรวจจับแบบปกติ (Manual Detection)",
    "place registered smart key on sensor": "ทาบบัตรหรือแท็ก RFID ที่ลงทะเบียนแล้วบนพื้นที่เซ็นเซอร์",
    "touch the number pad": "แตะแป้นคีย์แพดตัวเลขเพื่อปลุกหน้าจอ",
    "enter [pin number] and press [✱] button": "ป้อนรหัส PIN แล้วตามด้วยปุ่ม [✱]",
    "after the melody is heard, the door will open": "เมื่อได้ยินเสียงเพลงเมโลดี้ ประตูจะปลดล็อกและเปิดออก",
    "the door will lock automatically": "ประตูจะล็อกโดยอัตโนมัติ",
    "after 2 seconds of closing the door": "หลังจากประตูปิดสนิท 2 วินาที",
    "while the door is locked": "ในขณะที่ประตูเปิดอยู่หรือปิดล็อกอยู่",
    "press [open/close] button": "กดปุ่มเปิด/ปิดประตู [Open/Close]",
    "and the door will open": "และประตูจะปลดล็อกเปิดออก",
    "while door is locked": "ในขณะที่ประตูปิดล็อกอยู่",
    "press [safety] button": "กดปุ่ม [Safety]",
    "then press [open/close] button": "จากนั้นกดปุ่มเปิด/ปิดประตู [Open/Close]",
    "turn the [manual lock knob] to [open] direction": "บิดหมุน [ปุ่มล็อกแบบแมนนวล] ไปที่ทิศทางเปิด [Open]",
    "after closing the door": "หลังจากประตูปิดสนิท",
    "turn the [manual lock knob] to [close] direction": "บิดหมุน [ปุ่มล็อกแบบแมนนวล] ไปที่ทิศทางปิด [Close]",
    "and the door will lock": "และประตูจะปิดล็อก",
    "while the door is closed": "ในขณะที่ประตูปิดสนิท",
    "press [open/close] button for 3 seconds": "กดปุ่มเปิด/ปิดประตู [Open/Close] ค้างไว้เป็นเวลา 3 วินาที",
    "when the confirmation tone is heard, the setting is complete": "เมื่อได้ยินเสียงยืนยัน การตั้งค่าจะเสร็จสมบูรณ์",
    "press [3] to increase sound": "กดปุ่มหมายเลข [3] เพื่อเพิ่มระดับเสียง",
    "press [6] to decrease the sound": "กดปุ่มหมายเลข [6] เพื่อลดระดับเสียง",
    "sound can be adjusted up to 7 levels": "ปรับระดับเสียงการทำงานได้สูงสุด 7 ระดับ",
}

def translate_text(text):
    if not text:
        return ""
    if isinstance(text, list):
        return [translate_text(item) for item in text]
    
    orig = text
    text_lower = text.lower().strip()
    
    # Check exact match
    if text_lower in TRANSLATIONS_DICT:
        return TRANSLATIONS_DICT[text_lower]
        
    # Replace substrings case-insensitively
    translated = text
    for en, th in sorted(TRANSLATIONS_DICT.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        translated = pattern.sub(th, translated)
        
    return translated

def main():
    # Load ES-303G
    data = json.load(open(extracted_dir / "Manual_ES-303G.json"))
    
    # Let us list the panels in Manual_ES-303G
    panels = {}
    for page in data["pages"]:
        for p in page["panels"]:
            panels[p["panel"]] = p
            
    print("ES-303G loaded panels:", list(panels.keys()))
    
    # 1. Door Operations Page
    print("\n==================== DOOR OPERATIONS (EN) ====================")
    ops_en = []
    ops_th = []
    
    # Open outside
    if "open_outside" in panels:
        p = panels["open_outside"]
        ops_en.append(f"## {p.get('title', 'Opening Door Outside')}")
        ops_th.append(f"## การเปิดประตูจากด้านนอก ({p.get('title', 'Opening Door Outside')})")
        if "methods" in p:
            for m in p["methods"]:
                ops_en.append(f"### {m['name']}")
                ops_th.append(f"### {translate_text(m['name'])}")
                if "steps" in m:
                    for idx, step in enumerate(m["steps"], 1):
                        ops_en.append(f"{idx}. {step}")
                        ops_th.append(f"{idx}. {translate_text(step)}")
                if "procedure" in m:
                    ops_en.append(m["procedure"])
                    ops_th.append(translate_text(m["procedure"]))
                if "note" in m:
                    ops_en.append(f":::note\n{m['note']}\n:::")
                    ops_th.append(f":::note\n{translate_text(m['note'])}\n:::")
                if "caution" in m:
                    ops_en.append(f":::caution\n{m['caution']}\n:::")
                    ops_th.append(f":::caution\n{translate_text(m['caution'])}\n:::")
                ops_en.append("")
                ops_th.append("")
                
    # Print a small slice of ops translation
    print("\n".join(ops_en[:15]))
    print("\n==================== DOOR OPERATIONS (TH) ====================")
    print("\n".join(ops_th[:15]))

if __name__ == "__main__":
    main()
