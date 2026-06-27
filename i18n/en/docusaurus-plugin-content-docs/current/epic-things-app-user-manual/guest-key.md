---
sidebar_position: 8
title: Guest Key
description: One-time access keys for visitors
---

# Guest Key

Guest Key is a special feature that lets visitors (e.g., guests, repair technicians) open the door **once** without needing to register a Card/Fingerprint.

## 🎯 Requirements

:::warning Must use Wi-Fi mode
**Guest Key only works in Wi-Fi mode** — cannot use Bluetooth
- Must have a **Wi-Fi Bridge** registered
- Lock must be in **Wi-Fi mode** (not Bluetooth)
:::

## 📋 Guest Key types

| Type | Description | Used for |
|---|---|---|
| **One-time** | Valid for 1 use then expires | Visitors, repair technicians |
| **Time-limited** | Valid for multiple uses within specified time | Short-term renters, cleaners |

## ➕ Create Guest Key

**Steps:**
1. Go to **Guest Key** menu from the main screen
2. Tap **+ Add** or the **+** icon
3. Select type:
   - **One-time** — valid for 1 use
   - **Time-limited** — set expiration time
4. Fill in:
   - **Name** (e.g., "Repairman", "Sunday Guest")
   - **Valid Period** (for Time-limited)
   - **Allowed Locks** (select lock)
5. Tap **Generate** or **Create**
6. **Share Guest Key** via email, SMS, QR code, or copy link

## 🎫 How to use Guest Key

### For Guest Key recipient
1. Open the **Guest Key** (received via email/QR/link)
2. Open the EPIC Things app (or Guest Web App)
3. Tap **"Open Door"** button in the Guest Key
4. Lock will open **1 time**

### Limitations
- **Guest Key is valid once** then auto-expires (for One-time)
- **Guest Key does not require account registration** — just have link/code
- **Guest Key requires Wi-Fi mode** — cannot use Bluetooth
- **Guest recipient does not need app** (can use Web App)

## 📊 Manage Guest Key

### View Guest Key list

The Guest Key page shows:
- **Name** (Guest Key name)
- **Type** (One-time / Time-limited)
- **Status** (Active/Used/Expired)
- **Used by** (who used it)
- **Valid until** (expiration date)

### Cancel Guest Key

**Steps:**
1. Select the Guest Key you want
2. Tap **Cancel** or **Revoke**
3. Confirm cancellation

:::caution
- **Used Guest Keys** cannot be reused
- **Cancelled Guest Keys** cannot be used again
- Must create a new Guest Key if needed
:::

### View usage history

Each Guest Key has a **usage log**:
- **Who used it** (if has account)
- **When** (date-time)
- **Which lock** (which lock opened)
- **Success or not**

## 📋 Usage examples

### Visitors
1. Super Admin creates **One-time Guest Key** "House guest"
2. Sets **Valid Period** 24 hours
3. **Sends link** to guest via email
4. Guest opens link → taps "Open Door" button
5. Door opens **1 time** then Guest Key expires

### Repair technician
1. Super Admin creates **Time-limited Guest Key** "Repair"
2. Sets **Valid Period** 3 hours (09:00-12:00)
3. **Sends QR code** to technician
4. Technician scans QR → gets multiple access for 3 hours
5. After 12:00 → Guest Key expires

### Short-term renter
1. Super Admin creates **Time-limited Guest Key** "1-month renter"
2. Sets **Valid Period** 30 days
3. Renter can open door multiple times in 30 days
4. After 30 days → Guest Key expires

## 💡 Tips

- **Create Guest Key before guest arrives** — don't wait until they're at the door
- **Use memorable names** — "Plumber 5/5", "Guest tonight"
- **Use One-time** for people you don't know well
- **Use Time-limited** for trusted people (technicians, renters)
- **Share via email/QR** more convenient than copying link
- **Check expired Guest Keys** regularly
- **Cancel immediately** if plans change last-minute
