---
sidebar_position: 3
title: Key & Member Management
description: How to manage PIN, Card, Fingerprint, Remote Control and members via the app
---

# Key & Member Management

## 🔑 Key Management

After connecting a lock, you can manage different types of keys via the app:

### PIN

1. Select a lock from the Home page
2. Go to **Key Management** → **PIN**
3. Tap **+ Add PIN**
4. Enter a 4-12 digit PIN
5. Set a user name (e.g. "Dad", "Mom", "Kid")
6. Optionally set an expiry date
7. Tap **Save**

### Card (RFID)

1. Go to **Key Management** → **Card**
2. Tap **+ Add Card**
3. Enter a user name
4. Tap the card on the lock's reader
5. The app will confirm the card has been added
6. Tap **Save**

### Fingerprint

1. Go to **Key Management** → **Fingerprint**
2. Tap **+ Add Fingerprint**
3. Enter a user name
4. On the lock, place your finger on the sensor 3 times as instructed
5. The app will show the registration result
6. Tap **Save**

### Remote Control

1. Go to **Key Management** → **Remote**
2. Tap **+ Add Remote**
3. Press the pairing button on the remote
4. Name the remote
5. Tap **Save**

### Face ID (supported models only)

1. Go to **Key Management** → **Face**
2. Tap **+ Add Face**
3. Authenticate with Super Admin PIN
4. On the lock, look into the camera sensor
5. Wait for the system to recognize your face
6. Tap **Save**

## 👥 Member Management

### Add a member

1. Go to **Members** → **+ Add Member**
2. Enter details:
   - Full name
   - Email
   - Phone (optional)
   - Type: **Admin** / **Member** / **Guest**
3. Assign which locks the member can access
4. Tap **Invite** or **Send** — the system will send an email invitation

### Member types

| Type | Permissions |
|---|---|
| **Admin** | Manage all locks + add/remove members + view history |
| **Member** | Use keys + view their own history |
| **Guest** | Temporary key access (with expiry) |

### Remove a member

1. Go to **Members**
2. Select the member to remove
3. Tap **Delete Member** or **Remove**
4. Confirm the deletion

:::warning
Removing a member **immediately revokes their access** to locks, but does NOT delete their keys (PIN/Card/Fingerprint).
:::

## 📜 History Management

1. Go to **History**
2. Select the lock you want to view
3. Select a time range (Today / This week / This month / Custom)
4. View entries:
   - Date & time
   - User name (if available)
   - Method (PIN, Card, Fingerprint, App)
   - Status (Success / Failed)
5. You can **Export CSV** or **Share** via other apps
