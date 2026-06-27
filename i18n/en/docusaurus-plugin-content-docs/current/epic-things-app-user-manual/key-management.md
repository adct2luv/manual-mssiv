---
sidebar_position: 7
title: Key Management
description: Manage PIN, Card, Fingerprint, Remote Control, and Face ID
---

# Key Management

The **Key** menu manages authentication methods registered to the lock.

:::tip Register quickly through the app
You can quickly register authentication methods through the app.
**But PIN cannot be registered through the app** — it must be done at the lock.
:::

## 📋 Supported key types

| Type | Description | Register via app | Limit |
|---|---|---|---|
| **PIN** | 4-12 digit code | ❌ Must be done at lock | 1 PIN per lock |
| **Card** | Smart Card / RFID 13.56 MHz | ✅ | Up to 200 cards |
| **Fingerprint** | Fingerprint | ✅ | Up to 100 prints |
| **Remote** | Remote control | ✅ | Per model |
| **Face ID** | Face recognition | ✅ | Up to 30 faces |

## 1. PIN Management

### View current PIN

**Steps:**
1. Go to the lock → tap **Key** → **PIN** tab
2. Select **User PIN #1** to see the current PIN
3. Tap **Change PIN** to change

:::info
- The PIN registered in the app is the **User PIN** (not Super Admin PIN)
- PIN must be **≥ 4 digits**
- Only **1 User PIN** can be set per lock
:::

### Change PIN via the app

**Steps:**
1. **PIN** tab → tap **Change PIN**
2. Enter **new PIN** (≥ 4 digits)
3. Tap **Confirm** → done

:::warning
You need to change the PIN at the lock first (if the original PIN is 1234), then change it in the app.
- If never changed → must go to the lock first
:::

## 2. Card Management (Smart Card)

### View Card list

**PIN** tab next → **Card** tab

Shows:
- **Card #1, #2, ...** (card number)
- Status (registered/empty)
- User name (if any)

### Add new Card

**Steps:**
1. **Card** tab → tap **+ Add**
2. **Tap Smart Card** on the lock's reader
3. App recognizes card and adds to system
4. Tap **Save** or **Close**

:::tip
- Smart Cards must be **13.56 MHz** (Mifare / FeliCa)
- Supports up to **200 cards**
- Cards included in the lock box can be used immediately
:::

### Delete Card

**Steps:**
1. Select the card to delete
2. Tap **Delete** (trash icon)
3. Confirm deletion

## 3. Fingerprint Management

### Add fingerprint

**Steps:**
1. **Fingerprint** tab → tap **+ Add**
2. **Place finger on sensor 4 times** (at the lock)
3. Each time there's a beep + LED showing progress
4. When done → app shows success + saves

:::info
- Must place finger **4 times** in the same position
- Supports up to **100 fingerprints**
- One fingerprint per user
:::

### Delete fingerprint

**Steps:**
1. Select the fingerprint to delete
2. Tap **Delete**
3. Confirm

## 4. Remote Control Management

**Steps:**
1. **Remote** tab → tap **+ Add**
2. **Press pairing button on remote** (until LED blinks)
3. App pairs with the remote
4. Name the remote (e.g., "Living Room Remote")
5. Tap **Save**

### Delete Remote

**Steps:**
1. Select the remote → tap **Delete**
2. Confirm

## 5. Face ID Management (supported models)

**Steps:**
1. **Face** tab → tap **+ Add**
2. **Look directly into camera** (on the lock) at **1 meter** distance
3. Wait for system to recognize (green LED = success)
4. Name it (e.g., "Dad", "Mom")
5. Tap **Save**

### Delete Face ID

**Steps:**
1. Select Face → tap **Delete**
2. Confirm

## 🔄 Change User Name

**Steps:**
1. Select the key (PIN, Card, Fingerprint, Remote, Face) you want
2. Tap **Change User** or pencil icon
3. Enter new name (e.g., "Dad", "Daughter")
4. Tap **Confirm** → name will appear in history

## 📊 View key statistics

- **Total count** — total registered keys
- **Available** — remaining registrations
- **By type** — counts by type (PIN/Card/FP/Remote/Face)

## ⚠️ Cautions

- **PIN cannot be registered through the app** — must be done at the lock
- **Deleted keys cannot be recovered** — must re-register
- **1 Card per user** (if multiple users, need multiple cards)
- **Damaged/wet fingerprints** may fail to scan → use PIN instead
- **5 consecutive failed authentications** = Anti-Prank + 1-minute lockout
- **Deleting a key does NOT delete the User** in Member — must delete Member separately
