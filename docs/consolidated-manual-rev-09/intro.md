---
sidebar_position: 1
title: คู่มือรวม Rev.09
description: คู่มือรวมฉบับแก้ไขครั้งที่ 9 ครอบคลุม 10 รุ่น (ES-S100Dr, ES-F300Dr, ES-F301D, ES-F501D/H, ES-FF730Gr, ES-FF731G, ES-S740D, ES-F7000Kr, ES-F9000Kr, ES-P8800K)
---

# คู่มือรวม Rev.09 — Consolidated Manual

คู่มือฉบับนี้ครอบคลุม **10 รุ่น** ของ EPIC Door Lock แต่ละรุ่นมีหน้าเฉพาะในเว็บไซต์นี้เช่นกัน — คลิกชื่อรุ่นเพื่อดูรายละเอียด

## 📋 รุ่นที่ครอบคลุม

| # | รุ่น | ประเภท |
|---|---|---|
| 1 | [ES-S100Dr](/es-s100dr/intro) | RIM |
| 2 | [ES-F300Dr](/es-f300dr/intro) | RIM |
| 3 | [ES-F301D](/es-f301d/intro) | RIM |
| 4 | [ES-F501D/H](/es-f501d/intro) | RIM (รวม ES-F500D/H, ES-F501D/H, ES-S510D/H) |
| 5 | [ES-FF730Gr](/es-ff730gr/intro) | GATE |
| 6 | [ES-FF731G](/es-ff731g/intro) | GATE |
| 7 | [ES-S740D](/es-s740d/intro) | GATE |
| 8 | [ES-F7000Kr](/es-f7000kr/intro) | MORTISE |
| 9 | [ES-F9000Kr](/es-f9000kr/intro) | MORTISE |
| 10 | [ES-P8800K](/es-p8800k/intro) | PUSH PULL |

## 📊 ตารางเปรียบเทียบฟีเจอร์

| ประเภท | รุ่น | PIN | บัตร | ลายนิ้วมือ | กุญแจกลไก |
|---|---|:---:|:---:|:---:|:---:|
| **RIM** | ES-S100Dr | ✅ | ✅ | — | — |
| **RIM** | ES-F300Dr | ✅ | ✅ | ✅ | — |
| **RIM** | ES-F301D | ✅ | ✅ | ✅ | — |
| **RIM** | ES-F500D/H, ES-F501D/H, ES-S510D/H | ✅ | ✅ | ✅ | — |
| **GATE** | ES-FF730Gr | ✅ | ✅ | ✅ | ✅ |
| **GATE** | ES-FF731G | ✅ | ✅ | ✅ | ✅ |
| **GATE** | ES-S740D | ✅ | ✅ | ✅ | ✅ |
| **MORTISE** | ES-F7000Kr | ✅ | ✅ | ✅ | — |
| **MORTISE** | ES-F9000Kr | ✅ | ✅ | ✅ | ✅ |
| **PUSH PULL** | ES-P8800K | ✅ | ✅ | ✅ | — |

## 🎯 โหมดการลงทะเบียน (Registration Mode — User)

กดปุ่ม R (Registration) บนตัวล็อกด้านใน LED ที่คีย์แพดจะแสดงตัวเลข 1-6 และ R เพื่อเลือกโหมด:

| LED | โหมด | วิธีใช้ |
|---|---|---|
| **LED [1]** | PIN Number | ใส่ PIN เริ่มต้น `1234` + `[#]` แล้วใส่ PIN ใหม่ → `[R]` |
| **LED [2]** | Card (one-by-one) | ใส่ PIN + `[#]` แล้วแตะบัตร → `[R]` |
| **LED [3]** | Fingerprint (one-by-one) | ใส่ PIN + `[#]` แล้วแตะนิ้ว 4 ครั้ง → `[R]` |
| **LED [4]** | Guest PIN Number | ใส่ PIN + `[#]` แล้วใส่ Guest PIN → `[R]` |
| **LED [5]** | Remote Control (one-by-one) | ใส่ PIN + `[#]` แล้วกดปุ่ม OPEN ที่รีโมท → `[R]` |
| **LED [6]** | Face ID (one-by-one) | ใส่ PIN + `[#]` แล้วมองตรงเข้ากล้อง → `[R]` |
| **R Button** | Super Admin PIN | กด `OPEN/CLOSE` + กด R 10 วินาที → ใส่ Super Admin PIN ใหม่ |

## 🗑 โหมดการลบ (Deletion Mode — User)

กด `OPEN/CLOSE` 3 วินาที แล้วใส่ PIN + `[#]` แล้วเลือก LED:

| LED | โหมด | วิธีใช้ |
|---|---|---|
| **LED [2]** | Card | ทั้งหมด: `LED [#]` 5 วินาที / ทีละใบ: ใส่หมายเลข + `LED [#]` |
| **LED [3]** | Fingerprint | ทั้งหมด: `LED [#]` 5 วินาที / ทีละใบ: ใส่หมายเลข + `LED [#]` |
| **LED [5]** | Remote Control | ทั้งหมด: `LED [#]` 5 วินาที / ทีละใบ: ใส่หมายเลข + `LED [#]` |
| **LED [6]** | Face ID | ทั้งหมด: `LED [#]` 5 วินาที / ทีละใบ: ใส่หมายเลข + `LED [#]` |
| **R Button** | User Registered & Settings Reset | กด `OPEN/CLOSE` + กด R 10 วินาที → ลบทั้งหมด |

## 📋 หมายเหตุสำคัญ

- **มี PIN ได้แค่ 1 ชุด**
- **รหัส PIN เริ่มต้น:** `[1, 2, 3, 4]`
- **การลงทะเบียน Guest PIN ใหม่จะลบ Guest PIN เก่า**
- **รองรับบัตรได้สูงสุด 200 ใบ**
- **รองรับลายนิ้วมือได้สูงสุด 100 ลายนิ้วมือ**
- **รองรับใบหน้าได้สูงสุด 30 ใบ**
- **การยืนยันตัวตนเพิ่มเติม (Card, Fingerprint, Remote, Face) ไม่ลบการยืนยันหลัก (PIN)**
- ถ้าไม่ได้ลงทะเบียน PIN หลัก → Dual Authentication ใช้งานไม่ได้
- ถ้าเกิดข้อผิดพลาดระหว่างลงทะเบียน LED [2] จะกระพริบ
- ถ้าโมดูล Remote Control ไม่ได้เชื่อมต่อ LED [5] จะไม่ติด → ไม่สามารถลงทะเบียน/ลบรีโมทได้

:::warning ข้อควรระวัง
- ติดตั้งโดยช่างผู้เชี่ยวชาญเท่านั้น
- ห้ามติดตั้งกลางแจ้งหรือที่โดนฝน/แดดโดยตรง
:::

📖 ดูคู่มือ PDF ต้นฉบับ: [epic.co.kr](https://www.epic.co.kr/home/manual/)
