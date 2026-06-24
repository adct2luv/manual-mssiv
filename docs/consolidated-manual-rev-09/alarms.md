---
sidebar_position: 10
title: สัญญาณเตือนและความปลอดภัย (Alarms & Safety)
description: สัญญาณเตือนทั้งหมดของคู่มือรวม - High Temp, Intrusion, Deadbolt Error, Self-Diagnosis
---

# สัญญาณเตือนและความปลอดภัย (Alarms & Safety)

## 🔥 High Temperature Alarm Function

:::warning อันตราย
ตรวจจับอุณหภูมิสูง **60°C ± 10°C** เป็นเวลา 5 วินาที → **เสียงเตือน 80dB นาน 2 นาที + ปลดล็อกประตูอัตโนมัติ**
:::

**เงื่อนไขการทำงาน:**
- เซ็นเซอร์ตรวจจับอุณหภูมิ ≥ 60°C
- หลังจาก 5 วินาที → เสียงเตือน 80dB เริ่ม
- หลังจาก 10 วินาที → deadbolt เปิดอัตโนมัติ
- เสียงเตือนดังต่อเนื่อง **2 นาที**

**ข้อยกเว้น:** ถ้า **Door Lock power off** → High Temperature Alarm Function จะถูกปิด

:::tip
- ใช้ได้กับทุกรุ่น
- เมื่อทำงาน LED [8] ติด
- หลังอุณหภูมิลด → ระบบกลับสู่ปกติ
- ไม่สามารถปิดได้
:::

## 🚨 Intrusion Alarm Function

:::warning
**ถ้า Deadbolt sensor ไม่ตอบสนอง** ในขณะที่ deadbolt sensor on **เกิน 7 วินาที** → **เสียงเตือน 80dB**
:::

**วิธียกเลิก:**
- ผ่านการยืนยันตัวตน (PIN, Card, Fingerprint, Remote Control)

**ข้อยกเว้น:**
- ถ้า Door Lock power off → Intrusion Alarm ถูกปิด
- ระหว่าง Intrusion Alarm → LED [5] ติด

## ⚙️ Deadbolt Operation Error Warning Function

:::warning
**ถ้า Deadbolt เปิดหรือปิด แต่ทำงานผิดปกติ** → เปิด Deadbolt Operation Error Warning Function
:::

**พฤติกรรม:**
- LED [4] ติด
- ระหว่าง Deadbolt Operation Error → **เสียงเตือนดังขึ้น**
- **ลองใหม่ 3 ครั้ง** เพื่อให้กลอนทำงานปกติ
- ถ้ายังไม่สำเร็จ → เสียงเตือนยังคงดัง

**คุณสมบัติ:**
- ไม่สามารถปิดได้
- ป้องกันกลอนเสียหาย

## 📊 Self-Diagnosis (LED Indicators)

ไฟ LED บนคีย์แพดแสดงสถานะของล็อก

| LED | ความหมาย |
|---|---|
| **LED [1]** | FeliCa Auto-Detection ON ไม่สามารถตั้งค่าได้ |
| **LED [2]** | Registration Error / Deletion Error (Dual Authentication ON ไม่ตั้งได้, Setting Error) |
| **LED [3]** | จำนวน Card, Fingerprint, Remote Control, Face ID ครบแล้ว (FULL) / ไม่มี Fingerprint หรือ Face ID |
| **LED [4]** | Deadbolt Operation Error |
| **LED [5]** | Intrusion Alarm |
| **LED [6]** | Authentication Error (PIN, Card, Fingerprint, Face ที่ไม่ได้ลงทะเบียน) |
| **LED [7]** | หมายเลขช่องที่ลงทะเบียนแล้ว (Card, Fingerprint, Face) |
| **LED [8]** | Internal / External Forced Lock Setting |
| **LED [9]** | Fingerprint / Face recognition device ทำงานผิดปกติ |
| **LED [0]** | Fingerprint module error (Deadbolt Lock LED ติด) |

## 🔒 Locking from Outside

:::info
**เมื่อ Deadbolt Auto Lock เปิด** (ตรวจจับโดย deadbolt sensor):
- ล็อกอัตโนมัติทันที
- เสียง + การแจ้งเตือน (ถ้าเปิด)
:::

**ขั้นตอน:**
1. เปิดประตู → ตรวจจับ deadbolt sensor
2. หาก Deadbolt Auto Lock เปิดอยู่ → ล็อกทันที (ภายใน 2 วินาที)
3. หากเปิดใช้งาน Door Open Alarm → เสียงเตือน

**เงื่อนไข:**
- เมื่อแตะคีย์แพด (Manual mode) → ล็อกทันที
- เมื่อ Deadbolt Auto Lock เปิด → ล็อกอัตโนมัติ

## 🚪 Locking from Inside

| ประเภท | วิธีล็อก |
|---|---|
| **Sub Type** (ประตูบานเลื่อน) | กดปุ่ม OPEN/CLOSE + หมุนปุ่ม |
| **Main Type** | กดปุ่ม OPEN/CLOSE |
| **เมื่อ Deadbolt Auto Lock เปิด** | แตะคีย์แพด 2 วินาที → ล็อกอัตโนมัติ |
| **เมื่อ Deadbolt Auto Lock ปิด** | แตะคีย์แพด 2 วินาที → ล็อกด้วยตนเอง |

## 📋 Other alarms

### Anti-Hacking Alarm (LED [5])
- เมื่อตรวจพบการงัดแงะ
- เสียงเตือนดัง
- ยกเลิกด้วย PIN/Card/Fingerprint ที่ลงทะเบียน

### Fire Alarm
- เหมือน High Temperature Alarm (LED [8])
- อุณหภูมิ ≥ 60°C
- ปลดล็อกอัตโนมัติ
- เสียงเตือน 2 นาที

### Deadbolt Jammed Alarm
- เมื่อกลอนติดขณะเปิด/ปิด → เสียง beep-beep-beep 3 ครั้ง
- ลอง 3 ครั้ง
- ถ้ายังไม่สำเร็จ → เสียงเตือน

### Replace Battery Alarm
- ไฟ LED ติด + เสียง "beep-ree-reep"
- เปลี่ยนแบตเตอรี่ทั้งหมดทันที
