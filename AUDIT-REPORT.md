# รายงานการตรวจสอบ (Audit) เอกสาร Docusaurus เทียบกับคู่มือต้นฉบับ

> ผู้ตรวจ: Claude (auditor) · วันที่: 2026-06-20
> ต้นฉบับ: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/Manual/*.pdf`
> เป้าหมาย: `manual-site/docs/` (ไทย) และ `manual-site/i18n/en/.../docs/` (อังกฤษ)

---

## 1. สรุปผู้บริหาร (Executive Summary)

ข้อผิดพลาด **ไม่ได้กระจายสม่ำเสมอทุกรุ่น** แต่ **กระจุกตัวตามแหล่งข้อมูลต้นทาง** ของแต่ละรุ่น
เอกสารทั้งหมดถูก generate ด้วย `scripts/build_manuals.py` ซึ่งดึงข้อมูลจาก 3 แหล่ง คุณภาพต่างกันมาก:

| ระดับ | แหล่งข้อมูล | จำนวนรุ่น | คุณภาพ |
|---|---|---|---|
| **A (ดี)** | `extracted/vision/*.json` (สกัดจาก PDF ทีละหน้า) | 10 รุ่น | **เชื่อถือได้สูง** — ตรงกับ PDF |
| **B (ผสม)** | `products/*/product.json` (รุ่นเดี่ยว) | ~4 รุ่น | specs จริงบางส่วน + features/alarms ปลอม |
| **C (แย่)** | `Consolidated-Manual-Rev.09` (คู่มือรวม 1 ไฟล์ → แตกเป็นหลายรุ่น) | 9 รุ่น | **เนื้อหาส่วนใหญ่ถูกสร้างขึ้นเอง (generic) ไม่ตรงรุ่น** |

**ผลตรวจ PDF fidelity:** สุ่มอ่าน PDF `Manual_ES-303G.pdf` หน้า 1 เทียบกับ vision JSON → **ตรงกันเป๊ะ** ทั้ง cover, ส่วนประกอบ, ขั้นตอน PIN/RFID/เปิด-ปิดประตู
สรุปได้ว่า **รุ่นกลุ่ม A เชื่อถือได้** ปัญหาจริงอยู่ที่กลุ่ม B และ C

---

## 2. รุ่นแบ่งตามแหล่งข้อมูล

**กลุ่ม A — vision (เชื่อถือได้):**
`ES-303G`, `EF-8000L`, `EF-P8800K`, `ES-809L`, `ES-K70`, `ES-M50`, `ES-P9100FK`, `ES-T153`, `N-TOUCH`, `TOUCH`

**กลุ่ม B — product.json รุ่นเดี่ยว (ผสม):**
`ES-B10`, `ES-L200`, `OS300H`, `POPscan`

**กลุ่ม C — แตกจากคู่มือรวม Consolidated (เนื้อหาปลอม/generic):**
`ES-F300DR`, `ES-F301D`, `ES-F501D`, `ES-F7000KR`, `ES-F9000KR`, `ES-FF730GR`, `ES-FF731G`, `ES-S100DR`, `ES-S740D`

---

## 3. ปัญหาที่พบ (เรียงตามความรุนแรง)

### 🔴 ร้ายแรง #1 — เนื้อหา "คุณสมบัติพิเศษ" และ "สัญญาณเตือน" เป็นข้อความสำเร็จรูป (generic) ไม่ใช่ของจริงในรุ่นนั้น

ทุกรุ่นในกลุ่ม **B และ C** มีหน้า `features.md` และ `alarms.md` ครบ — **แต่เนื้อหาเป็นข้อความ generic ที่ก๊อปจากคลังกลาง** (`COMMON_FEATURES` / `COMMON_ALARMS` ใน `build_manuals.py` บรรทัด 2829–2877) ไม่ได้สกัดจากคู่มือจริงของรุ่นนั้นเลย

- **หลักฐาน:** `docs/es-f501d/features.md`, `docs/es-b10/features.md`, `docs/os300h/features.md` มีหัวข้อชุดเดียวกันเป๊ะ (ฟีเจอร์สุ่มตัวเลข / Multi-touch / ความปลอดภัยสองชั้น / โหมดล็อก / ปรับเสียง / ปิดเสียง) — ต่างกันแค่ "ตัด/ไม่ตัด" หัวข้อตาม subset เท่านั้น
- **เทียบกับกลุ่ม A:** `docs/es-303g/features.md` มี Guest PIN, Force Lock ใน/นอก, Multi-touch, Dual-mode, ตั้งเสียงเมโลดี้, โมดูลเครือข่าย ฯลฯ — รายละเอียดจริงครบจาก vision JSON
- **ผลกระทบ:** ผู้อ่านรุ่น ES-F501D / ES-B10 จะเห็นวิธีใช้งานที่ "ฟังดูถูก" แต่ **อาจไม่ตรงกับปุ่ม/ขั้นตอนจริงของรุ่นนั้น**

### 🔴 ร้ายแรง #2 — ค่าอุณหภูมิตรวจจับความร้อนผิด (hardcode 62°C±5°C ทั้งไซต์)

`specs.md` และ `alarms.md` แสดง **"การตรวจจับความร้อน 62°C ± 5°C"** ในเกือบทุกรุ่น (45 ไฟล์)

- **Ground truth (จาก text ต้นฉบับ Consolidated):** `"Detect high temperature (If the temperature sensor is at 60°C ± 10°C for 5 seconds)"`
- **source `product.json`** ระบุ `"Fire Detection Temperature: 60°C ± 10℃"` และ `"...activated at 60°C ± 10℃ for 5 seconds, opens after 10 seconds"`
- **แต่ docs ทุกรุ่นกลุ่ม C/B แสดง 62°C ± 5°C** → เป็นค่า default ที่ถูก hardcode มาจากรุ่น ES-303G แล้วยัดให้ทุกรุ่น **ผิดสำหรับตระกูล F/FF/S/B10/OS300H/POPscan**
- ไฟล์ที่ได้รับผลกระทบ: `es-f300dr, es-f301d, es-f501d, es-f7000kr, es-f9000kr, es-ff730gr, es-ff731g, es-s100dr, es-s740d, es-b10, os300h, popscan` (× specs + alarms)

### 🔴 ร้ายแรง #3 — แถว specs ที่ถูกกุขึ้นมา (วัสดุ / ประเภทผลิตภัณฑ์)

`docs/es-f501d/specs.md` (และรุ่น C/B อื่น) แสดง:
- `วัสดุ (ตัวเครื่องด้านนอก) | อะลูมิเนียม (Al), ซิงค์ (Zn), ABS`
- `วัสดุ (ตัวเครื่องด้านใน) | ซิงค์ (Zn), ABS`
- `ประเภทผลิตภัณฑ์ | ไม่มีกุญแจกลไก`

แต่ใน `products/Consolidated-Manual-Rev.09/product.json` ฟิลด์เหล่านี้ **เป็น null ทั้งหมด** (`dimensions_outer: null`, ไม่มี material, ไม่มี product_type)
→ แถวเหล่านี้ **ถูกคัดลอกค่า default จาก ES-303G มาแปะ** ไม่ใช่ข้อมูลจริงของรุ่น

### 🟠 ปานกลาง #4 — ส่วนประกอบ (components) ของกลุ่ม B/C เป็น template ทั่วไป

`docs/es-f501d/components.md` ใช้คำอธิบายชิ้นส่วนแบบ generic และรายการ "อุปกรณ์ในกล่อง" แบบ template (`ชุดอุปกรณ์ตัวเครื่องด้านนอก/ด้านใน…`) — `product.json` ของ Consolidated มี `components: NONE` จึงเป็นการเดา ไม่ใช่ของจริง

### 🟠 ปานกลาง #5 — ขั้นตอนเปิด/ปิดประตู (door-operations) ของกลุ่ม C เป็น fallback generic

มี logic fallback ใน `build_manuals.py` (บรรทัด ~2006–2139): ถ้า parse ขั้นตอนจริงไม่ได้ จะใส่ขั้นตอน generic แทน รุ่นกลุ่ม C เข้าเงื่อนไขนี้ → ขั้นตอนที่แสดงอาจไม่ตรงปุ่มจริงของรุ่น

### 🟡 เล็กน้อย #6 — รายการชิ้นส่วนตกหล่นในกลุ่ม A

- `ES-303G`: source JSON outer_body มี 6 ชิ้น (`Touch-Type Number Pad`, `Number Pad`, ...) แต่ docs แสดง 5 — **"Touch-Type Number Pad" หายไป** (logic dedup รวม/ตัดทิ้ง) ทั้งที่ PDF แยกเป็นคนละชิ้น

### 🟡 เล็กน้อย #7 — หัวข้อ "คุณสมบัติเด่น" ใน intro เป็น placeholder

`intro.md` เกือบทุกรุ่นแสดงแค่ `- 📷 Brochure image: <slug>.png` ใต้หัวข้อ "คุณสมบัติเด่น" แทนที่จะเป็นฟีเจอร์เด่นจริง

### 🟡 เล็กน้อย #8 — คำแปลไทยพังใน source product.json (ยังไม่หลุดเข้า docs แต่ควรรู้)

`products/Consolidated-Manual-Rev.09/product.json` → `description_th` มีข้อความปนภาษามั่ว เช่น
`"การรับรองบัตรสmarth card อัตโนมัติ"` (Thai+English ปนกัน)
ปัจจุบัน intro ใช้ dict ที่เขียนมือใน build script จึง **ยังไม่หลุดเข้า docs** — แต่ถ้ามีการแก้ให้ดึง `description_th` มาใช้ จะพังทันที

---

## 4. ข้อมูลที่ "ขาดหาย" (มีในต้นฉบับ แต่ไม่อยู่ใน docs)

จาก `Consolidated-Manual-Rev.09/product.json` มีข้อมูลจริงที่ **ไม่ถูกนำมาแสดง**:

- **อุณหภูมิใช้งาน** `operating_temp: -20°C to 60°C` — ไม่มีในตาราง specs
- **ความชื้น** `humidity: 0-80% RH` — ไม่มี
- **คำเตือนติดตั้ง** `"Do not install outdoor and direct weather affect place."` — ไม่มี
- **การแก้ปัญหา (troubleshooting)** `"Lock doesn't respond → Check battery level"` — ไม่มีหน้า troubleshooting เลย
- **ความหนาประตูต่อรุ่น** — text ต้นฉบับมีตารางแยกรุ่น (40~50mm, 30~50mm, 35~50mm) แต่ถูกยุบรวม
- **รายละเอียดสัญญาณเตือนความร้อน** `"opens after 10 seconds"` — ไม่ถูกนำมาแสดง

---

## 5. ข้อเสนอแนะการแก้ไข (priority)

1. **แก้ #2 ก่อน (เร็ว/ผลกระทบสูง):** เปลี่ยน hardcode `62°C ± 5°C` ให้อ่านค่าจริงต่อรุ่น — กลุ่ม C/B ต้องเป็น `60°C ± 10°C`
2. **แก้ #3:** เอาแถว วัสดุ / ประเภทผลิตภัณฑ์ ที่ไม่มีข้อมูลจริงออก (อย่าเดา) และเติม operating_temp / humidity / warnings ที่มีจริง
3. **แก้ #1, #4, #5 (ต้องลงแรง):** รุ่นกลุ่ม C (9 รุ่น) ควรสกัดข้อมูลจริงจาก `Consolidated-Manual-Rev.09.pdf` ด้วย vision (แบบเดียวกับกลุ่ม A) แทนการใช้ generic fallback — หรือไม่งั้นควรแจ้งชัดในหน้าเพจว่า "ใช้คู่มือฉบับรวม โปรดดูคู่มือ PDF"
4. **แก้ #6:** ปรับ logic dedup ใน components ไม่ให้ตัดชิ้นส่วนที่ต่างกันจริง
5. **แก้ #8:** อย่าดึง `description_th` จาก product.json ที่แปลพัง

---

---

## 6. การแก้ไขที่ลงมือแล้ว (อัปเดต 2026-06-20)

### ✅ ข้อ 1 — แก้ specs (เสร็จ, build ผ่านทั้ง th/en)
แก้ใน `scripts/build_manuals.py`:
- เพิ่ม `extract_fire_temp()` ดึงอุณหภูมิตรวจจับความร้อน **ค่าจริง** จาก source (vision panel / safety_features) แทน hardcode 62°C
  - กลุ่ม C (es-f*, es-s*, es-ff*, es-p8800k) + consolidated: 62 → **60°C ± 10°C** ✓
  - es-303g: เลือก **62°C** (Normal Environment) ไม่หยิบ 72°C (Testing Room) ✓
- ตัดแถว **วัสดุ / ประเภทผลิตภัณฑ์ ที่กุขึ้น** ออก สำหรับ source product/consolidated ที่ไม่มีข้อมูลจริง
- เพิ่มแถว **อุณหภูมิใช้งาน / ความชื้น** เมื่อ source มีข้อมูล (เช่น -20°C to 60°C, 0-80% RH)
- กลุ่ม A (vision) ที่ถูกต้องอยู่แล้วไม่ถูกแตะ

### 🟡 ข้อ 2 — ตรวจกลุ่ม A เชิงลึก (พบปัญหาใหม่ + แก้บางส่วน)

**2a. รุ่น vision ที่ JSON บาง/ว่าง → เนื้อหาเป็น fallback (ไม่ใช่ของจริง):**

| รุ่น | panels | สถานะ |
|---|---|---|
| **es-809l** | สกัดได้แค่หน้า 4-7 (ที่เหลือ inferred จาก EF-8000L) | specs/components/features/alarms ส่วนใหญ่ **generic** |
| **ef-8000l** | 6 panel เศษ (เฉพาะ deletion/closing) | specs/components/alarms/pin-reg/rfid-reg **generic** |
| **es-t153** | 6 panel (ไม่มี door-ops/features/alarms) | features/alarms/door-ops **generic ล้วน** |
| es-k70/es-m50/es-p9100fk | ครบพอควร | alarms บางส่วน fallback |

**2b. หัวข้ออังกฤษ/คีย์ดิบหลุดในหน้าไทย → แก้แล้ว:**
- คีย์ดิบ `## outside_force_lock`, `## emergency_key`, `## deadbolt_error`, `## forced_lock`, `## mechanical_key` ฯลฯ (triplex, touch, es-p9100fk, es-k70, es-m50) → แก้ให้ใช้ชื่อ canonical ไทย ✓
- หัวข้ออังกฤษ `Guest PIN Registration`, `Anti-Hacking Alarm`, `Dual-mode Security Setting` ฯลฯ → แก้ ✓
- method door-ops `Opening by Smart Key`, `Auto`, `Manual` ฯลฯ → เติมคำแปลใน RAW_MAP ✓

**2c. การแปลเป็นแบบ "dictionary lookup ระดับประโยค" → แก้แล้วเป็นส่วนใหญ่:**
`translate_text()` แปลได้เฉพาะประโยคที่อยู่ใน `RAW_MAP` ประโยคที่ไม่มีจะคงเป็นอังกฤษ
- **เก็บตก ~38 ประโยคปฏิบัติการที่ตกค้าง** (guest PIN, ปรับเสียง/ปิดเสียง, RFID auto/manual, สัญญาณเตือน ฯลฯ) แปลและเติม `RAW_MAP` โดยใช้คำศัพท์ชุดเดียวกับ es-303g ✓
- ครอบคลุมหลายรุ่นพร้อมกัน (ประโยคซ้ำข้ามรุ่น): ef-8000l, es-809l, touch, es-m50, es-k70, es-p9100fk, triplex
- **ลด English/mixed leak จาก ~58 จุด → เหลือ 11 จุด** (build ผ่านทั้ง th/en)

**เหลือ 11 จุดใน 2 รุ่นข้อมูลบาง (เชิงโครงสร้าง ไม่ใช่ dict gap):**
- `es-l200` (8): door-ops มาจาก source/generator ที่มี**ประโยคปนไทย-อังกฤษมาแต่แรก** เช่น `"แตะแป้นคีย์แพดตัวเลขเพื่อปลุกหน้าจอ to wake up the screen."`
- `n-touch` (3): features ใช้ generator คนละ path ที่ bypass การแปล (หัวข้อ `## Multi-Touch Feature` ก็ยังเป็นอังกฤษ)
→ ต้องแก้ generator/ทำความสะอาด source data ของ 2 รุ่นนี้แยกต่างหาก

### ✅ ข้อ 3 — สกัดเนื้อหาจริงจาก Consolidated PDF (เสร็จ — เจ้าของงานเลือกแนวทางนี้)

อ่าน `Consolidated-Manual-Rev.09.pdf` (2 หน้า เนื้อหาแน่น) ด้วย vision แล้วสกัดเนื้อหาจริงของตระกูล:
- สร้าง `CONSOLIDATED_FEATURES` (12 ฟีเจอร์จริง) + `CONSOLIDATED_ALARMS` (5-6 สัญญาณเตือนจริง) ใน `build_manuals.py` พร้อมคำแปลไทย + ขั้นตอนกดปุ่มจริง
  - features: Smart Card Auto/Manual, Deadbolt Auto/Manual Lock, Sound Setting, Voice/Buzzer, Door Open Alarm, Internal/External Forced Lock, **Dual Authentication**, Alarm Notification, **IR Sensor**, **FeliCa**, **Etiquette Mode**, Random Number, Auto Re-locking
  - alarms: **High Temperature (60°C±10°C, เปิดหลัง 10 วินาที, 80dB 2 นาที)**, 1-Minute Lock, Low Battery, Deadbolt Error, Intrusion, (+ Emergency Key สำหรับรุ่น mortise)
- wire ให้ source `consolidated` ใช้ชุดนี้แทน generic → **ทั้ง 9 รุ่นได้เนื้อหาจริงพร้อมกัน** ทั้ง TH+EN
- กรองตามรุ่น: IR Sensor/FeliCa แสดงเฉพาะรุ่นมี face; Emergency Key เฉพาะรุ่นมีกุญแจกลไก
- แก้ข้อมูล `es-f7000kr` ให้มี mechanical_key (คู่มือแสดงว่ามีรูกุญแจกลไก)
- specs ต่อรุ่นยังแม่น (จาก item 1: door thickness, fire 60°C±10°C, power)
- build ผ่านทั้ง th/en

**งานต่อเนื่องที่ยังเหลือ (ยังไม่ทำ — เนื้อหายัง fabricated/templated):**
- 🔴 **หน้า registration เป็น template hardcode ทุกรุ่น** (`gen_pin_registration` บรรทัด 2640) — ไม่ได้ดึง step จริงต่อรุ่น เช่น es-303g คู่มือจริงมี **4 ขั้นตอน** แต่หน้าที่ generate มี **6 ขั้นตอน เพิ่ม "ป้อน PIN ใหม่ซ้ำเพื่อยืนยัน" ที่ไม่มีในคู่มือ** → ขั้นตอนอาจไม่ตรงเครื่องจริง (กระทบ pin/rfid/fingerprint-registration ทุกรุ่น)
- หน้า `door-operations` ของตระกูล F ยังเป็น generic (ไม่ขัดกับ features ใหม่ แต่ยังไม่ใช่ของจริง) — Registration/Deletion Mode จริงมีในคู่มือที่อ่านแล้ว สกัดเพิ่มได้
- ลบ `docs/superpowers/` (ไฟล์ภายใน) ออกจาก site
- แก้ generator/source ของ es-l200 + n-touch (11 จุดที่ปนไทย-อังกฤษเชิงโครงสร้าง)

### หมายเหตุการตรวจสอบความแม่นยำ (item 3)
เลขปุ่มใน `CONSOLIDATED_FEATURES/ALARMS` ตรวจสอบ cross-check กับ text extraction อิสระแล้ว ตรงทุกตัวที่เทียบได้ (Smart Card [1]/[4], Deadbolt [2]/[5], Sound [3]/[6], Voice [8], Door Alarm [7], Internal [9], External [0], Dual [#]×2→[2]/[5], Etiquette [#]) — แก้ IR Sensor note (LED 8 ไม่ใช่ LED 3) ตามต้นฉบับแล้ว

### 🟡 อื่นๆ ที่พบ
- โฟลเดอร์ `docs/superpowers/` (ไฟล์ plan/spec ภายใน) ถูก publish เป็นหน้าเอกสารผู้ใช้ — ควรเอาออกจาก docs
- es-l200 door-ops ยังมี `### Normal Opening` 1 จุด (path product-type ไม่เรียก translate)

---

## ภาคผนวก: วิธีตรวจสอบ
- โครงสร้างหน้า/รุ่น: สำรวจ `docs/*/` ครบทุกโฟลเดอร์
- เทียบเนื้อหา: vision JSON / product.json ↔ docs ที่ generate (ไทย+อังกฤษ)
- ยืนยัน fallback: เทียบ md5 + อ่าน `COMMON_FEATURES`/`COMMON_ALARMS` ใน `build_manuals.py`
- Ground truth: อ่าน PDF `Manual_ES-303G.pdf` หน้า 1 + grep `extracted/text/Consolidated-Manual-Rev.09.txt`
