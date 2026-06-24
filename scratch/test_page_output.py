import json
import re
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

# Translation dict for text
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
    
    if text_lower in TRANSLATIONS_DICT:
        return TRANSLATIONS_DICT[text_lower]
        
    translated = text
    for en, th in sorted(TRANSLATIONS_DICT.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        translated = pattern.sub(th, translated)
        
    return translated

def format_panel_markdown(p, lang="en"):
    lines = []
    title = p.get("title", p.get("panel", "Feature")).replace("_", " ").title()
    title_th = translate_text(title)
    
    display_title = title if lang == "en" else title_th
    lines.append(f"### {display_title}")
    lines.append("")
    
    if "description" in p:
        desc = p["description"]
        lines.append(desc if lang == "en" else translate_text(desc))
        lines.append("")
        
    if "steps" in p and isinstance(p["steps"], list):
        lines.append("#### Steps" if lang == "en" else "#### ขั้นตอนการตั้งค่า")
        for idx, step in enumerate(p["steps"], 1):
            lines.append(f"{idx}. {step if lang == "en" else translate_text(step)}")
        lines.append("")
        
    if "setting_steps" in p and isinstance(p["setting_steps"], list):
        lines.append("#### Setting Steps" if lang == "en" else "#### ขั้นตอนการตั้งค่า")
        for idx, step in enumerate(p["setting_steps"], 1):
            lines.append(f"{idx}. {step if lang == "en" else translate_text(step)}")
        lines.append("")
        
    if "cancellation" in p:
        cancel = p["cancellation"]
        lines.append(f":::tip[Cancellation]" if lang == "en" else f":::tip[วิธียกเลิก]")
        lines.append(cancel if lang == "en" else translate_text(cancel))
        lines.append(":::")
        lines.append("")
        
    if "cautions" in p and isinstance(p["cautions"], list):
        lines.append(f":::caution[Caution]" if lang == "en" else f":::caution[ข้อควรระวัง]")
        for c in p["cautions"]:
            lines.append(f"- {c if lang == "en" else translate_text(c)}")
        lines.append(":::")
        lines.append("")
        
    if "notes" in p and isinstance(p["notes"], list):
        lines.append(f":::note[Note]" if lang == "en" else f":::note[หมายเหตุ]")
        for n in p["notes"]:
            lines.append(f"- {n if lang == "en" else translate_text(n)}")
        lines.append(":::")
        lines.append("")
        
    return "\n".join(lines)

def main():
    data = json.load(open(extracted_dir / "Manual_ES-303G.json"))
    
    # Get all panels
    panels = []
    for page in data.get("pages", []):
        p_panels = page.get("panels", [])
        if not p_panels:
            p_panels = [page]
        for p in p_panels:
            panels.append(p)
            
    # Extract features
    features = []
    for p in panels:
        p_name = p.get("panel", "").lower()
        if any(k in p_name for k in ["guest_pin", "force_lock", "volume", "mute", "auto_manual", "detection", "safe_open", "multi_touch", "dual_mode", "melody", "home_network"]):
            features.append(p)
            
    print(f"Found {len(features)} features for ES-303G.")
    for f in features:
        print("\n----------------------------------------")
        print(f"Formatting panel: {f['panel']}")
        print(format_panel_markdown(f, "th")[:200] + "...")

if __name__ == "__main__":
    main()
