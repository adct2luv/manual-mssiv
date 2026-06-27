---
sidebar_position: 5
title: Door Lock Management
description: Connect, manage, and delete locks via the app
---

# Door Lock Management

The **Door Lock** menu from the main screen is used to connect and manage all EPIC locks.

## 🔌 Connect a lock (Add Lock)

You must be logged in as **Super Admin** first.

### Connect via Bluetooth (BLE)

:::tip Easiest method
Bluetooth is the best way to start with initial setup.
:::

**Steps:**
1. Enable **Bluetooth** on your smartphone
2. In the app, tap **+ Add** in the Door Lock menu
3. Select **Bluetooth** mode
4. On the lock, press the **Registration (R)** button
5. Enter **Super Admin PIN** and press `[#]`
6. The app will search for nearby locks (named EPIC xxx BLE)
7. Select the lock you want
8. Tap **Add** → confirmation sound

### Connect via Wi-Fi Bridge (remote)

:::note Add Wi-Fi Bridge first
You need to set up the Wi-Fi Bridge in the Wifi Bridge menu first.
:::

**Steps:**
1. Tap **+ Add** → select **Wi-Fi**
2. Select a **Wi-Fi Bridge** that's already registered
3. On the lock, press the **Registration (R)** button
4. Enter **Super Admin PIN** + `[#]`
5. The app will connect through the Bridge

### Important notes

:::warning
- **Super Admin PIN must be set** before connecting
- **One lock** = **One Super Admin** (only one)
- If someone else connects first, you must **remove the lock** from their account first
- **Guest Key works only in Wi-Fi mode** (not Bluetooth)
:::

## 📋 Lock List

The Door Lock page shows:

- **Lock name** (set by Super Admin)
- **Model** (e.g., ES-K70, EF-P8800K)
- **Serial Number** (EBR...)
- **Status** (Online/Offline)
- **Connection mode** (Bluetooth/Wi-Fi)
- **Battery level**

Locks you added will appear in the list. Tap to:
- Open/close door
- View status
- Configure (Key, Member)
- View history

## ✏️ Edit lock info

**Steps:**
1. Select a lock from the list
2. Tap **Edit** (or pencil icon)
3. Edit:
   - **Name** (e.g., "Front door", "Office")
4. Tap **Save**

## 🗑 Remove Lock

**Steps:**
1. Select a lock from the list
2. Tap **Delete** (or trash icon)
3. Confirm deletion

:::caution
- Removing a lock from the app **does NOT reset the lock**
- The lock remains — only the app connection is severed
- **All registered keys remain** on the lock
- You can reconnect later
:::

## 🔄 Switch connection mode

**Bluetooth ↔ Wi-Fi:**

:::info
Locks can switch between Bluetooth and Wi-Fi
- Bluetooth works within range (≤ 10 meters)
- Wi-Fi works anywhere (requires Wi-Fi Bridge)
- **Wi-Fi mode supports Guest Key** and remote control
:::

**Steps:**
1. Open **Door Lock** menu, select a lock
2. Tap **Connection Mode**
3. Select **Bluetooth** or **Wi-Fi**

## 📋 Usage examples

### First-time setup
1. Enable Bluetooth on your smartphone
2. Login as Super Admin
3. Connect the lock via Bluetooth
4. Set the lock name (e.g., "Front door")
5. Add members (General Admin / User)
6. Add keys (PIN, Card, Fingerprint)
7. Configure Wi-Fi Bridge (if needed)

### Remote control
1. Switch to **Wi-Fi** mode
2. Open/close door from anywhere
3. Create Guest Keys
4. View entry/exit history
