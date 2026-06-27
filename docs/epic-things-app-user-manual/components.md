---
sidebar_position: 12
title: ส่วนประกอบ (Components)
description: ส่วนประกอบและโครงสร้างของ EPIC Things App
---

# ส่วนประกอบ (Components)

## 📱 หน้าจอหลัก (Main Screen)

| # | ส่วน | คำอธิบาย |
|---|---|---|
| 1 | **Open/Close Button** | ปุ่มเปิด/ปิดประตู — ไอคอนแม่กุญแจตรงกลาง |
| 2 | **Door Lock Status** | แสดงสถานะล็อก (เปิด/ปิด/แบตเตอรี่/สัญญาณเตือน) |
| 3 | **Door Lock List** | รายการล็อกที่ใช้งาน — เลือกเพื่อจัดการ |
| 4 | **Connection Mode** | โหมดการเชื่อมต่อ (Bluetooth / Wi-Fi) |
| 5 | **Profile Icon** | เข้าถึงโปรไฟล์และการตั้งค่า |
| 6 | **Menu Grid** | เมนูหลัก: Member, Door Lock, Wifi Bridge, Key, Guest Key, History, App Settings |

## 🎛️ เมนูหลัก (Main Menu)

| เมนู | ไอคอน | คำอธิบาย |
|---|---|---|
| **Member** | 👥 | จัดการสมาชิก (เพิ่ม/ลบ/แก้ไข) |
| **Door Lock** | 🔐 | เชื่อมต่อ/จัดการล็อก |
| **Wifi Bridge** | 📡 | ตั้งค่า Wi-Fi Bridge |
| **Key** | 🗝️ | จัดการกุญแจ (PIN, Card, FP, Remote, Face) |
| **Guest Key** | 🎫 | กุญแจสำหรับแขก |
| **History** | 📋 | ประวัติการใช้งาน |
| **App Settings** | ⚙️ | ตั้งค่าแอป |

## 📱 เมนูล็อก (Lock Menu)

| เมนู | คำอธิบาย |
|---|---|
| **Lock Status** | สถานะปัจจุบัน (Online/Offline, Battery, Connection) |
| **Open/Close** | เปิด/ปิดประตู |
| **Lock Info** | ชื่อ, รุ่น, Serial Number, Firmware |
| **Edit Name** | เปลี่ยนชื่อล็อก |
| **Delete Lock** | ลบล็อกออกจากแอป (ไม่ลบที่ตัวล็อก) |
| **Connection Mode** | เปลี่ยน Bluetooth/Wi-Fi |

## 🔑 เมนู Key (Key Menu)

| เมนู | คำอธิบาย |
|---|---|
| **PIN** | จัดการรหัสผ่าน (ดู/เปลี่ยน) |
| **Card** | Smart Card ที่ลงทะเบียน |
| **Fingerprint** | ลายนิ้วมือที่ลงทะเบียน |
| **Remote** | รีโมทคอนโทรล |
| **Face** | Face ID |

แต่ละ tab มี:
- **+ Add** — เพิ่มกุญแจใหม่
- **Item list** — รายการกุญแจที่ลงทะเบียน
- **Edit/Delete** — แก้ไข/ลบ

## 🔧 ส่วนประกอบ Settings

| ส่วน | คำอธิบาย |
|---|---|
| **Profile** | ชื่อ, Email, Phone, รูปภาพ |
| **Change Password** | เปลี่ยนรหัสผ่าน |
| **Language** | ภาษา UI |
| **Notifications** | การแจ้งเตือน (Push, Email, Sound) |
| **Security** | 2FA, Active Sessions |
| **Clear Cache** | ลบแคช |
| **About** | เวอร์ชัน, License |
| **Logout** | ออกจากระบบ |
| **Delete Account** | ลบบัญชี |

## 📡 Wi-Fi Bridge Management

| ส่วน | คำอธิบาย |
|---|---|
| **+ Add Bridge** | เพิ่ม Bridge ใหม่ |
| **Bridge List** | รายการ Bridge ที่ลงทะเบียน |
| **Register Wi-Fi** | ลงทะเบียน Wi-Fi network |
| **SSID List** | รายการ Wi-Fi ที่มองเห็น |
| **Delete** | ลบ Bridge |

## 🎫 Guest Key Management

| ส่วน | คำอธิบาย |
|---|---|
| **+ Add Guest Key** | สร้าง Guest Key ใหม่ |
| **Type Selector** | One-time / Time-limited |
| **Name Field** | ตั้งชื่อ Guest Key |
| **Valid Period** | ตั้งเวลาหมดอายุ |
| **Lock Selector** | เลือกล็อกที่ Guest Key ใช้ได้ |
| **Share** | แชร์ผ่าน Email/QR/Link |
| **Guest Key List** | รายการ Guest Key |
| **Status** | Active/Used/Expired |

## 👥 Member Management

| ส่วน | คำอธิบาย |
|---|---|
| **+ Add Member** | เพิ่มสมาชิกใหม่ |
| **Permission Selector** | General Admin / User |
| **Email Field** | email ของสมาชิก |
| **Name Field** | ชื่อสมาชิก |
| **Member List** | รายการสมาชิกทั้งหมด |
| **Permission Level** | แสดงระดับของแต่ละคน |
| **Edit/Delete** | แก้ไข/ลบ |

## 📊 History (ประวัติ)

| ส่วน | คำอธิบาย |
|---|---|
| **Lock Selector** | เลือกล็อก |
| **Time Range** | Today/Week/Month/Custom |
| **Event List** | รายการเหตุการณ์ |
| **Event Type Filter** | Entry/Failed/Alarm/Settings |
| **Export** | CSV/PDF |
| **Detail View** | ดูรายละเอียดแต่ละเหตุการณ์ |
| **Filter** | ตามผู้ใช้, ตามล็อก, ตามเวลา |
