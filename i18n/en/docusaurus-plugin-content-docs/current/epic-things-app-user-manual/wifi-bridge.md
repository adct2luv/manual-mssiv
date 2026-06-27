---
sidebar_position: 6
title: Wi-Fi Bridge
description: Wi-Fi Bridge setup for remote lock control
---

# Wi-Fi Bridge

The **Wifi Bridge** menu registers and manages Wi-Fi Bridges used to connect locks via Wi-Fi.

:::tip Wi-Fi mode requires Wi-Fi Bridge
To use **Wi-Fi mode** (including **Guest Key** and remote control), you must connect a Wi-Fi Bridge first.
:::

## 🔌 Add new Wi-Fi Bridge (Add)

### Preparation
1. Plug the **Wi-Fi Bridge** into a power outlet near the lock
2. Wait for the LED on the Bridge to light up (usually ~30 seconds)

### Add Bridge in the app
**Steps:**
1. Go to **Wifi Bridge** from the main screen
2. Tap **+ Add** or the **+** icon
3. The app will start scanning for nearby Bridges (via Bluetooth)
4. Select the **Bridge** you want (identified by **Serial Number** e.g., EBR000001, EBR000342)
5. Tap **Connect** → Bridge will be added to the system

:::note
- Bridge must be within Bluetooth range (≤ 10 meters) to be added
- If Bridge not found → check that it's plugged in and LED is on
- If still not found → press reset button on Bridge
:::

## 📡 Register Bridge with Wi-Fi

**After adding Bridge to the app, register Wi-Fi:**

**Steps:**
1. In Wifi Bridge menu, select a Bridge that was added
2. Tap **Register Wi-Fi**
3. Select a **Wi-Fi Network** from the list (e.g., EPICSYSTEMS4G, ehwhaglofotech, etc.)
4. **Enter Wi-Fi Password** (tap eye icon to show)
5. Tap **Submit**

### Limitations

:::caution
- Supports only **2.4 GHz Wi-Fi** (not 5 GHz)
- Verify SSID before selecting — if not visible, may be 5 GHz
- If your Wi-Fi isn't in the list, scan again
:::

### Troubleshooting Wi-Fi Registration

| Issue | Solution |
|---|---|
| Wi-Fi not in list | Check if 2.4 GHz, scan again |
| Can't enter password | Tap eye icon to show, try again |
| Bridge won't register | Check Bridge is plugged in, LED is on |
| **Already registered WiFi Bridges will not be detected** | This Bridge is already registered, use a different Bridge |
| **Manually enter the SSID if it is not publicly visible** | Manually enter the SSID (if hidden) |

## 📋 Wi-Fi Bridge List

The Wifi Bridge page shows:

- **Bridge name** (Serial Number e.g., EBR000001)
- **Status** (Online/Offline)
- **Connected Wi-Fi Network**
- **MAC Address** (for reference)
- **Number of connected locks**

## 🗑 Delete Wi-Fi Bridge

**Steps:**
1. Select a Bridge from the list
2. Tap **Delete** (trash icon)
3. Confirm deletion

:::caution
- **Deleting Bridge doesn't delete data on the lock**
- Locks connected to this Bridge will need to **reconnect**
- After deletion, can't use the same Bridge — must **add a new one**
:::

## ⚠️ Cautions

- **Each Bridge can only register Wi-Fi once** — to change Wi-Fi, must delete and re-add
- **Wi-Fi Bridge must be plugged in constantly** — no backup battery
- **LED on Bridge** shows status: green=normal, red=problem
- **Hidden SSID** must be entered manually
- **Wi-Fi signal strength** affects connectivity

## 💡 Best Practices

- Place Bridge where **Wi-Fi signal is strong**
- Name Bridge by location (e.g., "Bridge-Floor1", "Bridge-LivingRoom")
- **Update SSID/Password** when main Wi-Fi changes
- Have a backup Bridge if possible (for important systems)
