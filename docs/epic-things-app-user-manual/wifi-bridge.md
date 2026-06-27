---
sidebar_position: 6
title: Wi-Fi Bridge
description: การตั้งค่า Wi-Fi Bridge สำหรับควบคุมล็อกจากระยะไกล
---

# Wi-Fi Bridge

เมนู **Wifi Bridge** ใช้ลงทะเบียนและจัดการ Wi-Fi Bridge ที่ใช้เชื่อมต่อล็อกผ่าน Wi-Fi

:::tip ใช้ Wi-Fi mode ต้องมี Wi-Fi Bridge
ถ้าจะใช้ **Wi-Fi mode** (รวมถึง **Guest Key** และควบคุมระยะไกล) ต้องเชื่อมต่อ Wi-Fi Bridge ก่อน
:::

## 🔌 เพิ่ม Wi-Fi Bridge ใหม่ (Add)

### ขั้นตอนเตรียมการ
1. เสียบ **Wi-Fi Bridge** เข้ากับปลั๊กไฟใกล้กับล็อก
2. รอให้ไฟ LED บน Bridge ติด (ปกติ ~30 วินาที)

### เพิ่ม Bridge ในแอป
**ขั้นตอน:**
1. เข้าเมนู **Wifi Bridge** จากหน้าจอหลัก
2. กด **+ Add** หรือไอคอน "+"
3. แอปจะเริ่มสแกนหา Bridge ในระยะใกล้ (ผ่าน Bluetooth)
4. เลือก **Bridge** ที่ต้องการ (ระบุด้วย **Serial Number** เช่น EBR000001, EBR000342)
5. กด **Connect** → Bridge จะถูกเพิ่มเข้าระบบ

:::note
- Bridge ต้องอยู่ในระยะ Bluetooth ของสมาร์ทโฟน (≤ 10 เมตร) เพื่อเพิ่ม
- ถ้าไม่เจอ Bridge → ตรวจสอบว่าเสียบปลั๊กไฟและไฟ LED ติด
- ถ้ายังไม่เจอ → กดปุ่ม reset ที่ Bridge
:::

## 📡 ลงทะเบียน Bridge กับ Wi-Fi

**หลังเพิ่ม Bridge ในแอป ต้องลงทะเบียน Wi-Fi:**

**ขั้นตอน:**
1. ในเมนู Wifi Bridge เลือก Bridge ที่เพิ่มไว้
2. กด **Register Wi-Fi**
3. เลือก **Wi-Fi Network** จากรายการ (เช่น EPICSYSTEMS4G, ehwhaglofotech, etc.)
4. **กรอก Wi-Fi Password** (กดไอคอนตาเพื่อดู)
5. กด **Submit**

### ข้อจำกัด

:::caution
- รองรับเฉพาะ **Wi-Fi 2.4 GHz** เท่านั้น (ไม่รองรับ 5 GHz)
- ตรวจ SSID ก่อนเลือก — ถ้าไม่เห็น SSID อาจเป็น 5 GHz
- ถ้า Wi-Fi ที่เลือกไม่อยู่ในรายการ ให้สแกนใหม่
:::

### การแก้ปัญหา Wi-Fi Registration

| ปัญหา | วิธีแก้ |
|---|---|
| Wi-Fi ไม่ปรากฏในรายการ | ตรวจว่าเป็น 2.4 GHz, สแกนใหม่ |
| กรอก Password ไม่ได้ | กดไอคอนตาเพื่อดู, ลองใหม่ |
| Bridge ไม่ register ได้ | ตรวจ Bridge เสียบปลั๊กไฟ, ไฟ LED ติด |
| **Already registered WiFi Bridges will not be detected** | Bridge นี้ลงทะเบียนแล้ว ใช้ Bridge อื่น |
| **Manually enter the SSID if it is not publicly visible** | กรอก SSID เอง (ถ้าซ่อน) |

## 📋 รายการ Wi-Fi Bridge

หน้า Wifi Bridge แสดง:

- **ชื่อ Bridge** (Serial Number เช่น EBR000001)
- **สถานะ** (Online/Offline)
- **Wi-Fi Network** ที่เชื่อมต่อ
- **MAC Address** (สำหรับอ้างอิง)
- **จำนวนล็อกที่เชื่อมต่อ**

## 🗑 ลบ Wi-Fi Bridge

**ขั้นตอน:**
1. เลือก Bridge จากรายการ
2. กด **Delete** (ไอคอนถังขยะ)
3. ยืนยันการลบ

:::caution
- **การลบ Bridge ไม่ลบข้อมูลบนล็อก**
- ล็อกที่เชื่อมต่อ Bridge นี้จะ **ต้องเชื่อมต่อใหม่**
- ลบแล้วใช้ Bridge เดิมไม่ได้ ต้อง **เพิ่ม Bridge ใหม่**
:::

## ⚠️ ข้อควรระวัง

- **Bridge แต่ละเครื่องลงทะเบียน Wi-Fi ได้ครั้งเดียว** — เปลี่ยน Wi-Fi ต้องลบ Bridge แล้วเพิ่มใหม่
- **Wi-Fi Bridge ต้องเสียบปลั๊กไฟตลอด** — ไม่มีแบตเตอรี่สำรอง
- **ไฟ LED บน Bridge** แสดงสถานะ: เขียว=ปกติ, แดง=มีปัญหา
- **SSID ที่ซ่อน (hidden)** ต้องกรอกเอง
- **ความแรงสัญญาณ Wi-Fi** มีผลต่อการเชื่อมต่อ

## 💡 Best Practices

- วาง Bridge ในตำแหน่งที่มี **สัญญาณ Wi-Fi แรง**
- ตั้งชื่อ Bridge ตามตำแหน่ง (เช่น "Bridge-ชั้น1", "Bridge-ห้องนั่งเล่น")
- **อัปเดต SSID/Password** เมื่อ Wi-Fi หลักเปลี่ยน
- มี Bridge สำรองถ้าเป็นไปได้ (ระบบที่สำคัญ)
