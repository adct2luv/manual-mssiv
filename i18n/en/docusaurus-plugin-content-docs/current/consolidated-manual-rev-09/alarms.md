---
sidebar_position: 10
title: Alarms & Safety
description: All alarms in the consolidated manual - High Temp, Intrusion, Deadbolt Error, Self-Diagnosis
---

# Alarms & Safety

## 🔥 High Temperature Alarm Function

:::warning
Detects high temperature **60°C ± 10°C** for 5 seconds → **80dB alarm for 2 minutes + automatic door unlock**
:::

**Operating conditions:**
- Sensor detects temperature ≥ 60°C
- After 5 seconds → 80dB alarm starts
- After 10 seconds → deadbolt opens automatically
- Alarm continues for **2 minutes**

**Exception:** If **Door Lock power is off** → High Temperature Alarm Function is disabled

:::tip
- Works on all models
- When active, LED [8] lights
- After temperature drops → system returns to normal
- Cannot be disabled
:::

## 🚨 Intrusion Alarm Function

:::warning
**If the Deadbolt sensor doesn't respond** while deadbolt sensor is on for **more than 7 seconds** → **80dB alarm**
:::

**How to cancel:**
- Through authentication (PIN, Card, Fingerprint, Remote Control)

**Exception:**
- If Door Lock power is off → Intrusion Alarm is disabled
- During Intrusion Alarm → LED [5] lights

## ⚙️ Deadbolt Operation Error Warning Function

:::warning
**If Deadbolt opens or closes but operates abnormally** → Deadbolt Operation Error Warning Function activates
:::

**Behavior:**
- LED [4] lights
- During Deadbolt Operation Error → **alarm sounds**
- **Retries 3 times** for normal operation
- If still fails → alarm continues

**Features:**
- Cannot be disabled
- Prevents deadbolt damage

## 📊 Self-Diagnosis (LED Indicators)

Keypad LEDs show lock status.

| LED | Meaning |
|---|---|
| **LED [1]** | FeliCa Auto-Detection ON cannot be set |
| **LED [2]** | Registration Error / Deletion Error (Dual Authentication ON cannot be set, Setting Error) |
| **LED [3]** | Card, Fingerprint, Remote Control, Face ID count is FULL / No Fingerprint or Face ID registered |
| **LED [4]** | Deadbolt Operation Error |
| **LED [5]** | Intrusion Alarm |
| **LED [6]** | Authentication Error (unregistered PIN, Card, Fingerprint, Face) |
| **LED [7]** | Slot number already registered (Card, Fingerprint, Face) |
| **LED [8]** | Internal / External Forced Lock Setting |
| **LED [9]** | Fingerprint / Face recognition device malfunction |
| **LED [0]** | Fingerprint module error (Deadbolt Lock LED lights) |

## 🔒 Locking from Outside

:::info
**When Deadbolt Auto Lock is enabled** (detected by deadbolt sensor):
- Auto-locks immediately
- Sound + notification (if enabled)
:::

**Steps:**
1. Open door → deadbolt sensor detects
2. If Deadbolt Auto Lock is on → locks immediately (within 2 seconds)
3. If Door Open Alarm is enabled → alarm sounds

**Conditions:**
- Touch keypad (Manual mode) → locks immediately
- When Deadbolt Auto Lock is on → auto-locks

## 🚪 Locking from Inside

| Type | How to lock |
|---|---|
| **Sub Type** (sliding door) | Press OPEN/CLOSE + turn knob |
| **Main Type** | Press OPEN/CLOSE |
| **When Deadbolt Auto Lock is on** | Touch keypad 2 sec → auto-lock |
| **When Deadbolt Auto Lock is off** | Touch keypad 2 sec → manual lock |

## 📋 Other alarms

### Anti-Hacking Alarm (LED [5])
- Detects forced entry
- Alarm sounds
- Cancel with registered PIN/Card/Fingerprint

### Fire Alarm
- Same as High Temperature Alarm (LED [8])
- Temperature ≥ 60°C
- Auto-unlock
- 2-minute alarm

### Deadbolt Jammed Alarm
- Deadbolt stuck while opening/closing → beep-beep-beep ×3
- Retries 3 times
- If still fails → alarm continues

### Replace Battery Alarm
- LED lights + "beep-ree-reep" sound
- Replace all batteries immediately
