---
sidebar_position: 11
title: ข้อมูลจำเพาะ (Specs)
description: ข้อมูลจำเพาะของ EPIC Things App
---

# ข้อมูลจำเพาะ (Specs)

## 📱 App Requirements

| รายการ | ค่า |
|---|---|
| **App Version** | 1.0.45 (ขึ้นกับเวอร์ชัน) |
| **Platform** | iOS 12.0+ / Android 7.0+ |
| **App Size** | ~50 MB |
| **Languages** | English, ไทย (ขึ้นกับเวอร์ชัน) |
| **Distribution** | Apple App Store, Google Play Store |
| **License** | Free (with EPIC door lock) |

## 🔌 การเชื่อมต่อ

| โหมด | ระยะ | ความเร็ว | ใช้งาน |
|---|---|---|---|
| **Bluetooth (BLE)** | ≤ 10 เมตร | เร็ว | ใกล้ล็อก |
| **Wi-Fi** | ไม่จำกัด (ตามเน็ต) | ขึ้นกับ Wi-Fi | ระยะไกล |
| **Wi-Fi Bridge** | ขึ้นกับ Wi-Fi | เร็ว | เชื่อมต่อ Wi-Fi |

## 📋 User Levels

| ระดับ | สิทธิ์ |
|---|---|
| **Super Admin** | ทุกอย่าง |
| **General Admin** | จัดการสมาชิก, ดูประวัติ, เพิ่ม/ลบกุญแจ |
| **User** | ใช้กุญแจเปิดประตู |
| **Guest** | เปิดประตู 1 ครั้ง (Guest Key) |

## 🔑 Authentication Methods

| ประเภท | จำกัด | ลงทะเบียนผ่านแอป |
|---|---|---|
| **PIN** | 1 PIN ต่อล็อก (4-12 หลัก) | ❌ ที่ตัวล็อก |
| **Smart Card** | 200 ใบ | ✅ |
| **Fingerprint** | 100 ลาย | ✅ |
| **Remote Control** | แล้วแต่รุ่น | ✅ |
| **Face ID** | 30 ใบ | ✅ |

## 🔐 Security Features

- **Two-Factor Authentication** (2FA) — เปิดใช้งานได้
- **Biometric Login** — iOS Face ID, Android Fingerprint
- **Auto Logout** — เมื่อไม่ใช้งานตามเวลาที่ตั้ง
- **Session Management** — ดูและ logout อุปกรณ์ที่ login
- **Encrypted Communication** — ระหว่าง app กับ lock (BLE/Wi-Fi)

## 📊 History (ประวัติ)

| รายการ | รายละเอียด |
|---|---|
| **ประเภท** | Entry, Failed, Alarm, Guest, Settings |
| **เก็บนาน** | 90 วัน (ขึ้นกับเวอร์ชัน) |
| **Export** | CSV, PDF |
| **Filter** | ตามล็อก, ตามช่วงเวลา, ตามผู้ใช้ |

## 🎫 Guest Key

| ประเภท | รายละเอียด |
|---|---|
| **One-time** | ใช้ได้ 1 ครั้ง |
| **Time-limited** | ใช้ได้หลายครั้งในช่วงเวลาที่กำหนด |
| **ต้องใช้โหมด** | Wi-Fi mode เท่านั้น |
| **แชร์ได้** | Email, SMS, QR code, link |

## 🔋 ข้อกำหนดล็อกที่รองรับ

- **EPIC Door Lock** ที่รองรับ BLE
- **Wi-Fi Bridge** (อุปกรณ์เสริม ซื้อแยก)
- **Super Admin PIN** ต้องตั้งก่อน
- **EMF 1.0.45+** (เวอร์ชันแอป)

## 📞 Support

- **In-app**: Help → Contact Support
- **Email**: support@epic.co.kr
- **Website**: [epic.co.kr](https://www.epic.co.kr)
- **Phone**: ดูในเว็บ
