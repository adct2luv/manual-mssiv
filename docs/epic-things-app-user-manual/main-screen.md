---
sidebar_position: 3
title: หน้าจอหลัก (Main Screen)
description: หน้าจอหลักของ EPIC Things App และฟีเจอร์ต่างๆ
---

# หน้าจอหลัก (Main Screen)

หน้าจอหลักของ EPIC Things App ประกอบด้วย 6 ส่วนหลัก:

## 1. 🔓 Open/Close (เปิด/ปิดประตู)

**ใช้เปุ่มนี้เปิดหรือปิดประตู** เมื่อประตูเปิด ไอคอนแม่กุญแจตรงกลางจะเปลี่ยนเป็น **สถานะเปิด** (🔓)

## 2. 📊 Door Lock Status (สถานะล็อก)

**ตรวจสอบสถานะปัจจุบันของล็อก** — แสดงสถานะล็อก ในบางสถานการณ์ ไอคอนจะเป็นสีแดง

**สถานะที่แสดง:**
- 🔓 **Door is open** (ประตูเปิด)
- ⚠️ **Low Battery Alarm** (แบตเตอรี่ต่ำ)
- ⚠️ **Trick Alarm** (การงัดแงะ)
- ⚠️ **Spring Alarm** (สปริงผิดปกติ)
- ⚠️ **High-temperature Alarm** (อุณหภูมิสูง)

## 3. 🔐 Door Lock List (รายการล็อก)

แสดง **รายการล็อกที่ใช้งานอยู่** — เลือกเพื่อดูล็อกที่ใช้งานได้

- ล็อกที่ใช้งานอยู่จะมี **ขอบสีแดง**
- ล็อกที่ลงทะเบียนกับบัญชีของคุณจะมี **ไอคอน "me"** กำกับ

## 4. 📡 Connection Mode (โหมดการเชื่อมต่อ)

แสดง **โหมดการเชื่อมต่อปัจจุบัน** — เลือกเพื่อดูโหมดที่ใช้งานได้

**โหมดที่รองรับ:**
- 🔵 **Bluetooth (BLE)** — ค่าเริ่มต้น, ใช้ได้ในระยะใกล้
- 🔴 **Wi-Fi** — ต้องมี Wi-Fi Bridge, ใช้ได้ระยะไกล

:::info
- โหมด Bluetooth ตั้งเป็น **ค่าเริ่มต้น**
- โหมด Wi-Fi ต้องใช้ **Wi-Fi Bridge** เพื่อเปิดใช้งาน
- **Wi-Fi รองรับ Guest Key และการควบคุมระยะไกล**
:::

## 5. 👤 Profile (โปรไฟล์)

**ตั้งค่าโปรไฟล์** — ดูรายละเอียดเพิ่มเติมได้ที่ [App Settings](/epic-things-app-user-manual/app-settings)

## 6. 📋 Menu (เมนู)

**เมนูหลัก** ประกอบด้วย:
- **Member** — จัดการสมาชิก ([Member →](/epic-things-app-user-manual/member))
- **Door Lock** — เชื่อมต่อ/จัดการล็อก ([Door Lock →](/epic-things-app-user-manual/door-lock))
- **Wifi Bridge** — ตั้งค่า Wi-Fi Bridge ([Wifi Bridge →](/epic-things-app-user-manual/wifi-bridge))
- **Key** — จัดการกุญแจ ([Key →](/epic-things-app-user-manual/key-management))
- **Guest Key** — กุญแจแขก ([Guest Key →](/epic-things-app-user-manual/guest-key))
- **History** — ประวัติ ([History →](/epic-things-app-user-manual/history))
- **App Settings** — ตั้งค่าแอป ([App Settings →](/epic-things-app-user-manual/app-settings))

## 🎯 การใช้งานขั้นพื้นฐาน

### เปิดประตูจากแอป
1. แตะ **Open/Close** (ไอคอนกุญแจตรงกลาง)
2. ล็อกจะเปิด (ต้องอยู่ในระยะ Bluetooth หรือ Wi-Fi)
3. ไอคอนเปลี่ยนเป็น **สถานะเปิด**

### ตรวจสอบสถานะล็อก
1. ดูที่ **สถานะบน Door Lock Status**
2. ถ้ามี **สีแดง** = มีปัญหา (เช่น แบตเตอรี่ต่ำ, งัดแงะ, อุณหภูมิสูง)

### สลับโหมด Bluetooth / Wi-Fi
1. กดที่ **Connection Mode**
2. เลือก Bluetooth หรือ Wi-Fi
3. Wi-Fi ต้องมี **Wi-Fi Bridge** ที่ลงทะเบียนไว้ก่อน

:::tip เริ่มต้นใช้งาน
1. ตั้ง **Super Admin PIN** ที่ตัวล็อก ([Setup](/epic-things-app-user-manual/setup))
2. **Login** ในแอป
3. **เพิ่ม Door Lock** ([Door Lock →](/epic-things-app-user-manual/door-lock))
4. เริ่มใช้งาน!
:::
