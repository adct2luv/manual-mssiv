---
sidebar_position: 2
title: การตั้งค่าเริ่มต้น (Setup)
description: Super Admin PIN, สมัคร, Login, ลืมรหัสผ่าน, Guest Login
---

# การตั้งค่าเริ่มต้น (Setup)

## 0. ตั้ง Super Admin PIN (ต้องทำก่อน)

:::tip ทำก่อนใช้งานแอป
ก่อนเปิด EPIC Things App ต้องตั้ง **Super Admin PIN** ที่ตัวล็อกก่อน
:::

**Super Admin คืออะไร:**
- ระดับผู้ใช้สูงสุดของ EPIC Door Lock
- มีสิทธิ์ควบคุมทุกฟังก์ชัน
- เชื่อมต่อแอปกับล็อกได้ (ป้องกันผู้อื่นเชื่อมต่อโดยไม่ได้รับอนุญาต)

**ขั้นตอนการตั้ง Super Admin PIN:**
1. กดปุ่ม **[R]** ที่ตัวล็อกด้านใน
2. ใส่ **User PIN** (PIN หลัก) แล้วกด `[#]`
3. **กดค้างปุ่ม [OPEN/CLOSE] 3 วินาที** จน LED บนตัวล็อกด้านนอกติด
4. ใส่ **Super Admin PIN 6-12 หลัก** แล้วกด `[#]`
5. ใส่ Super Admin PIN **อีกครั้ง** เพื่อยืนยัน
6. กดปุ่ม **[R]** เพื่อเสร็จสิ้น

:::note
ถ้า Super Admin PIN ลงทะเบียนแล้ว LED จะไม่ติดในขั้นตอนที่ 3
:::

---

## 1. Sign Up (สมัครบัญชี)

:::tip Quick Login
ถ้าต้องการ login ด้วย Apple หรือ Google account โดยตรง ข้าม Sign Up ไป Quick Login ได้เลย
:::

**ขั้นตอน:**
1. เปิด EPIC Things App
2. กด **Sign Up**
3. กรอก **Email** และ **Password** (≥ 8 ตัวอักษร)
4. กดเลือก **"Agree to the terms"** (4 ข้อ)
5. กด **Next**
6. กรอก **Verification Code** ที่ส่งไปยัง email
7. กด **Submit** (หรือ Skip ถ้ามี account อยู่แล้ว)

**ข้อกำหนด:**
- Password ≥ 8 ตัวอักษร
- ต้องยอมรับ **Terms, Collection, Personal Info, All Terms**
- Verification Code ต้องกรอกก่อน Submit

:::caution
- **ถ้าไม่ได้รับ Verification Code** → กด **REQUEST AGAIN** หรือตรวจ spam folder
- **ถ้าออกจากหน้า Sign Up** ก่อนใส่ Code → ต้อง REQUEST AGAIN ใหม่
- **Tap SKIP** ได้ถ้ามี verification code อยู่แล้ว
:::

---

## 2. Login / Quick Login

### Login ปกติ (ด้วย EPIC Account)

**ขั้นตอน:**
1. กรอก **Email** + **Password**
2. (Optional) ติ๊ก **ID Saving** เพื่อจำ email
3. กด **Sign In**

:::caution
- ถ้า Email หรือ Password ผิด จะมี pop-up แจ้งเตือน
- **ถ้ายังไม่มีบัญชี** ให้ไปที่ Sign Up ก่อน
- **Login status คงอยู่แม้ออกจากแอป** — ต้อง Logout เองถ้าต้องการออก
:::

### Quick Login (Apple / Google)

**ขั้นตอน:**
1. เลือก icon **Apple** หรือ **Google**
2. Login ด้วย account ที่ login อยู่บนเครื่อง

:::info
Quick Login ช่วยให้ login ได้โดยไม่ต้องสมัคร EPIC account
แต่บัญชี Apple/Google และ EPIC จะถือว่าแยกกัน
:::

---

## 3. Forgot Password (ลืมรหัสผ่าน)

**ขั้นตอน:**
1. กด **Forgot Password** ที่หน้า Login
2. กรอก **Email** ที่ใช้สมัคร
3. กด **Continue**
4. ตรวจ email → กดลิงก์ **"Reset Password"**
5. ตั้ง **Password ใหม่** (≥ 8 ตัวอักษร)
6. **Login ใหม่** ด้วย password ใหม่

---

## 4. Guest Login (โหมดผู้เยี่ยนชม)

ใช้แอปโดยไม่ต้อง Login — เหมาะสำหรับ **ทดลองใช้** หรือ **ผู้ใช้ชั่วคราว**

**ขั้นตอน:**
1. กด **Guest Login** ที่หน้า Login
2. ใช้งานแอปได้ทันที (ฟีเจอร์จำกัด)

:::warning ข้อจำกัดของ Guest Login
- **ไม่สามารถบันทึกการตั้งค่า** ระหว่าง session
- **ไม่สามารถเพิ่ม/ลบ** ล็อกหรือสมาชิกจริง
- **ข้อมูลจะหายไป** เมื่อออกจาก Guest mode
- ต้อง Login ด้วย EPIC account จริงเพื่อใช้งานเต็มรูปแบบ
:::

:::tip เมื่อไหร่ควรใช้ Guest Login?
- ทดลองดูหน้าตาแอปก่อนตัดสินใจ
- ให้เพื่อน/ครอบครัวทดลองใช้ชั่วคราว
- ดูตัวอย่างก่อนสมัคร
- **ไม่เหมาะ** สำหรับการใช้งานจริงจัง
:::
