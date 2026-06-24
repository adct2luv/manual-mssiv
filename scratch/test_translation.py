import re

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
}

def translate_step(step):
    orig = step
    step_lower = step.lower().strip()
    
    # Try exact match first
    if step_lower in TRANSLATIONS_DICT:
        return TRANSLATIONS_DICT[step_lower]
        
    # Replace parts
    translated = step
    for en, th in sorted(TRANSLATIONS_DICT.items(), key=lambda x: len(x[0]), reverse=True):
        # use regex to replace case-insensitively
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        translated = pattern.sub(th, translated)
        
    return translated

def main():
    steps = [
        "Open the [Battery Cover]. Press [Registration] button once — beep.",
        "Enter current pin number followed by [✱] button.",
        "Press number 1 button.",
        "Enter new pin number to be registered 4~12 digits. Press [✱] button."
    ]
    print("Original Steps:")
    for s in steps:
        print("-", s)
    print("\nTranslated Steps:")
    for s in steps:
        print("-", translate_step(s))

if __name__ == "__main__":
    main()
