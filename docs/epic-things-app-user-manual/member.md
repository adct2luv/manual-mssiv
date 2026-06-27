---
sidebar_position: 4
title: การจัดการสมาชิก (Member Management)
description: เพิ่ม ลบ แก้ไข จัดการสมาชิก และกำหนดสิทธิ์
---

# การจัดการสมาชิก (Member Management)

เมนู **Member** อยู่ในหน้าจอหลัก ใช้จัดการสมาชิกทั้งหมดของล็อก

## 📋 ประเภทสมาชิก

EPIC Door Lock มี **3 ระดับผู้ใช้** ตามลำดับสิทธิ์:

| ระดับ | คำอธิบาย | สิทธิ์ |
|---|---|---|
| **Super Admin** | ระดับสูงสุด | ทุกอย่าง รวมถึงเชื่อมต่อแอป, ตั้ง Super Admin PIN |
| **General Admin** | ผู้ดูแลทั่วไป | จัดการสมาชิก, ดูประวัติ, เพิ่ม/ลบกุญแจ |
| **User** | ผู้ใช้ทั่วไป | ใช้กุญแจ (PIN, Card, Fingerprint ฯลฯ) เปิดประตู |

:::info
- **Super Admin** ต้องตั้งที่ตัวล็อก (ไม่สามารถสร้างจากแอป)
- **General Admin** และ **User** ถูกสร้างจากแอป (ต้อง login Super Admin ก่อน)
:::

## ➕ เพิ่มสมาชิกใหม่

**ขั้นตอน:**
1. เข้าเมนู **Member** จากหน้าจอหลัก
2. กด **"+ Add"** หรือไอคอน "+"
3. เลือกประเภทสมาชิก: **General Admin** หรือ **User**
4. กรอกข้อมูล:
   - **Name** (ชื่อ-นามสกุล)
   - **Email** (ใช้ login)
   - **Phone** (ไม่บังคับ)
   - **Permission level** (General Admin / User)
5. กด **Save** หรือ **Send**
6. ระบบจะส่ง **คำเชิญทาง email** ให้สมาชิกใหม่

:::note
- **Email ต้องไม่ซ้ำ** กับสมาชิกอื่นในระบบ
- **General Admin** จัดการสมาชิกที่ตนเองสร้างได้
- **User** ใช้ได้แค่เปิดประตู
:::

## ✏️ แก้ไขสมาชิก

**ขั้นตอน:**
1. ในเมนู **Member** เลือกสมาชิกที่ต้องการ
2. กด **Edit** หรือไอคอนดินสอ
3. แก้ไขข้อมูล:
   - Name, Email, Phone
   - Permission level (General Admin / User)
4. กด **Save**

:::warning
- เปลี่ยน Permission level เป็น General Admin จะให้สิทธิ์เพิ่ม — **ระวังการเพิ่มสิทธิ์ให้คนอื่น**
- การแก้ไข Email อาจต้องให้สมาชิก verify email ใหม่
:::

## 🗑 ลบสมาชิก

**ขั้นตอน:**
1. ในเมนู **Member** เลือกสมาชิก
2. กด **Delete** หรือไอคอนถังขยะ
3. ยืนยันการลบ

:::caution
- **การลบสมาชิกไม่ลบกุญแจ (PIN, Card, Fingerprint)** ที่ลงทะเบียนไว้
- ต้องลบกุญแจแยกต่างหากในเมนู **Key**
- สมาชิกที่ถูกลบจะไม่สามารถ login เข้าแอปได้อีก
:::

## 🔄 เปลี่ยน Permission Level

| จาก → ไป | ต้องทำอย่างไร |
|---|---|
| User → General Admin | แก้ไข permission ใน Member list |
| General Admin → User | แก้ไข permission |
| General Admin → Super Admin | **ไม่สามารถทำได้** — Super Admin ตั้งที่ตัวล็อกเท่านั้น |

## 📊 ดูรายการสมาชิก

หน้า Member แสดง:
- **ชื่อ-นามสกุล**
- **Email**
- **Permission level** (Super Admin / General Admin / User)
- **สถานะ** (ใช้งาน/รอ verify)
- **ล็อกที่เข้าถึงได้**

## 💡 Best Practices

- ใช้ **Email จริง** ของสมาชิก — ใช้สำหรับ login และกู้คืนรหัสผ่าน
- **Permission level** ควรตรงกับหน้าที่จริง (อย่าให้ User เป็น General Admin โดยไม่จำเป็น)
- **ลบสมาชิกที่ไม่ได้ใช้งาน** เพื่อความปลอดภัย
- **ตรวจสอบรายการสมาชิก** เป็นประจำ
- **Permission level ของ Super Admin** ควรมีแค่ 1-2 คน
