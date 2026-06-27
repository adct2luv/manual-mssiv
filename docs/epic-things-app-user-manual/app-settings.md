---
sidebar_position: 10
title: ตั้งค่าแอป (App Settings)
description: ตั้งค่าโปรไฟล์, ภาษา, การแจ้งเตือน และอื่นๆ
---

# ตั้งค่าแอป (App Settings)

เข้าเมนู **App Settings** จากหน้าจอหลัก เพื่อตั้งค่าต่างๆ ของแอปและโปรไฟล์

## 👤 โปรไฟล์ (Profile)

### ข้อมูลส่วนตัว

- **Name** (ชื่อ-นามสกุล)
- **Email** (ใช้ login, กู้คืนรหัสผ่าน)
- **Phone** (ไม่บังคับ)
- **Profile Picture** (รูปภาพ)
- **Account Created Date**
- **Last Login**

### แก้ไขโปรไฟล์

**ขั้นตอน:**
1. เข้า **App Settings** → **Profile**
2. กด **Edit** (ไอคอนดินสอ)
3. แก้ไข Name, Phone, Profile Picture
4. กด **Save**

:::info Email ไม่สามารถเปลี่ยนได้
- Email ใช้เป็น **identifier หลัก** ของบัญชี
- ถ้าต้องการเปลี่ยน Email ต้อง **สร้างบัญชีใหม่** และโอนย้ายข้อมูล
:::

### ลบบัญชี (Delete Account)

:::danger การลบบัญชีไม่สามารถยกเลิกได้
- ลบบัญชี → **ข้อมูลทั้งหมดหาย** (ล็อก, สมาชิก, ประวัติ, Guest Key)
- **ล็อกยังคงอยู่ที่ตัวล็อก** แต่ต้องเชื่อมต่อใหม่ด้วยบัญชีอื่น
- **ต้อง Login Super Admin** ใหม่ก่อนถึงจะเชื่อมต่อกลับได้
:::

**ขั้นตอน:**
1. **App Settings** → **Profile**
2. กด **Delete Account**
3. ยืนยัน

## 🔐 เปลี่ยนรหัสผ่าน (Change Password)

**ขั้นตอน:**
1. **App Settings** → **Change Password**
2. ใส่ **Password ปัจจุบัน**
3. ใส่ **Password ใหม่** (≥ 8 ตัวอักษร)
4. ใส่ Password ใหม่ **อีกครั้ง** เพื่อยืนยัน
5. กด **Submit**

## 🌐 ภาษา (Language)

**ขั้นตอน:**
1. **App Settings** → **Language**
2. เลือก **ภาษา** ที่ต้องการ (English, ไทย, อื่นๆ)
3. แอปจะรีโหลดเป็นภาษาที่เลือก

:::note
ภาษาในแอปเป็นภาษา UI เท่านั้น ไม่กระทบเนื้อหาในคู่มือที่แสดงในเว็บเบราว์เซอร์
:::

## 🔔 การแจ้งเตือน (Notifications)

### เปิด/ปิด การแจ้งเตือน

**ขั้นตอน:**
1. **App Settings** → **Notifications**
2. สลับ toggle แต่ละประเภท:
   - **Push Notifications** — แจ้งเตือนผ่านแอป
   - **Email Notifications** — ส่ง email
   - **Sound** — เปิดเสียงแจ้งเตือน
3. กด **Save**

### ประเภทการแจ้งเตือน

| ประเภท | คำอธิบาย |
|---|---|
| **Entry** | แจ้งเตือนเมื่อมีคนเปิดประตู |
| **Failed Attempt** | แจ้งเตือนเมื่อมีคนยืนยันตัวตนล้มเหลว |
| **Alarm** | แจ้งเตือนเมื่อเกิดเหตุการณ์ผิดปกติ (Trick, High temp, Low battery) |
| **Guest Key Used** | แจ้งเตือนเมื่อ Guest Key ถูกใช้ |
| **Settings Changed** | แจ้งเตือนเมื่อมีการเปลี่ยนแปลงการตั้งค่า |

## 🔧 การตั้งค่าอื่นๆ

### ลบข้อมูลแคช (Clear Cache)

**ขั้นตอน:**
1. **App Settings** → **Clear Cache**
2. ยืนยัน
3. แอปจะรีโหลด

### เกี่ยวกับแอป (About)

**ข้อมูล:**
- **App Version** (เช่น 1.0.45)
- **Build Number**
- **Last Updated**
- **License / Open Source Notices**

### ออกจากระบบ (Logout)

**ขั้นตอน:**
1. **App Settings** → **Logout**
2. ยืนยัน

:::warning
- หลัง Logout ต้อง Login ใหม่เพื่อใช้งาน
- **Guest Key** ที่สร้างไว้ยังใช้ได้ (ไม่ต้อง login)
- **Guest Key ที่ค้างใน Guest mode** อาจหาย
:::

## 🔐 ความปลอดภัย (Security)

### Two-Factor Authentication (2FA)

:::info ต้องตั้ง Email ก่อน
ต้องมี Email ที่ verify แล้วจึงจะเปิด 2FA ได้
:::

**ขั้นตอน:**
1. **App Settings** → **Security**
2. สลับ **Two-Factor Authentication** เปิด
3. ใส่ **Password** เพื่อยืนยัน
4. ทุกครั้งที่ login จะต้องใส่ **Verification Code** จาก email

### Active Sessions

ดู **อุปกรณ์ที่ login อยู่**:
- **Device name**
- **Last activity**
- **Location** (ถ้ามี)
- **Logout** อุปกรณ์นี้ได้ทันที

## 📋 เมนูอื่นๆ

### ภาษา (Language)
- **App Language** — ภาษา UI
- **Input Method** — keyboard language

### ข้อมูลแอป
- **Version** — เวอร์ชัน
- **License** — สัญญาอนุญาต
- **Privacy Policy** — นโยบายความเป็นส่วนตัว
- **Terms of Service** — ข้อกำหนดการใช้งาน

### Help & Support
- **User Guide** — ลิงก์ไปคู่มือ
- **FAQ** — คำถามที่พบบ่อย
- **Contact Support** — ติดต่อทีม support
- **Report a Problem** — รายงานปัญหา
- **Rate the App** — ให้คะแนน

## 💡 Best Practices

- **เปิด 2FA** เสมอสำหรับ Super Admin
- **Logout** เมื่อใช้เสร็จบนอุปกรณ์ที่ใช้ร่วม
- **อัปเดตแอป** เมื่อมีเวอร์ชันใหม่
- **ตรวจสอบ Active Sessions** เป็นประจำ
- **ลบ Guest Keys** ที่ไม่ใช้แล้ว
- **ตรวจสอบ Email** ให้ถูกต้อง (ใช้สำหรับกู้คืนรหัสผ่าน)
