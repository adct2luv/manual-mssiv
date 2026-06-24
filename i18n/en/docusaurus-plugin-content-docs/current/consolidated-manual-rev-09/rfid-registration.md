---
sidebar_position: 5
title: Smart Card Registration
description: How to register Smart Cards (RFID) and configure Auto Recognition
---

# Smart Card Registration

## 1. Card Registration (LED [2])

**Up to 200 cards** per lock

**Steps:**
1. Press **R** and enter main PIN + `[#]`
2. LEDs [1] [2] [3] [4] [5] light up → press number **[2]**
3. Place the Smart Card on the reader → beep sounds
4. Press **R** → melody plays to confirm

:::tip
- Smart Cards must be **13.56 MHz** (FeliCa/Mifare)
- Up to **200 cards** can be registered
- Registered cards are managed in the system
:::

## 2. Smart Card Auto/Manual Recognition (LED [1] / [4])

Set the Smart Card reading mode.

**Steps:**
1. Touch the keypad to turn on LEDs
2. Enter main PIN, then press `[#]`
3. Press **[1]** for **Auto** or **[4]** for **Manual**
4. Press **R** → melody plays to confirm

| Mode | Behavior |
|---|---|
| **Auto (LED [1])** | Place card on reader → door opens immediately |
| **Manual (LED [4])** | Must touch keypad first, then place card |

:::caution
- In **Manual** mode, if you don't touch the keypad first, the card won't be read
- When Auto is set and FeliCa Auto-Detection is OFF, LED [2] will blink
- LED [2] blinking + error tone = error
:::

## 3. Door Open Alarm ON/OFF (LED [7])

Set the alarm when door is left open.

**Steps:**
1. Touch keypad → enter PIN + `[#]`
2. Press **[7]** to toggle ON/OFF
3. Press **R** to confirm

**Behavior:**
- **Enabled:** When Door Open Alarm Mode is ON and Deadbolt Auto Lock is active, if the Latch/Magnet sensor is disconnected → **beep 3 times every 7 seconds**

## ⚠️ Cautions

- Registering more than 200 cards is rejected — delete old cards first
- Card registration does NOT delete the main PIN
- To delete all cards, use **LED [2] in Deletion mode** (press for 5 seconds)
- If an error occurs, LED [2] will blink
- Cards used with **FeliCa Auto-Detection** will be read automatically when in range
- **Smart Card + PIN** = Dual Authentication
