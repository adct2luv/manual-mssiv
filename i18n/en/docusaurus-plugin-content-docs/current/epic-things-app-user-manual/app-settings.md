---
sidebar_position: 10
title: App Settings
description: Profile, language, notifications, and other settings
---

# App Settings

Go to **App Settings** from the main screen to configure various app and profile settings.

## 👤 Profile

### Personal information

- **Name**
- **Email** (used for login, password recovery)
- **Phone** (optional)
- **Profile Picture**
- **Account Created Date**
- **Last Login**

### Edit profile

**Steps:**
1. Go to **App Settings** → **Profile**
2. Tap **Edit** (pencil icon)
3. Edit Name, Phone, Profile Picture
4. Tap **Save**

:::info Email cannot be changed
- Email is the **primary identifier** of the account
- To change Email, must **create new account** and transfer data
:::

### Delete account

:::danger Account deletion cannot be undone
- Delete account → **All data lost** (locks, members, history, Guest Keys)
- **Locks remain on the device** but need to reconnect with another account
- **Must login as Super Admin** again to reconnect
:::

**Steps:**
1. **App Settings** → **Profile**
2. Tap **Delete Account**
3. Confirm

## 🔐 Change Password

**Steps:**
1. **App Settings** → **Change Password**
2. Enter **Current Password**
3. Enter **New Password** (≥ 8 characters)
4. Enter New Password **again** to confirm
5. Tap **Submit**

## 🌐 Language

**Steps:**
1. **App Settings** → **Language**
2. Select the **language** you want (English, Thai, others)
3. App will reload in the selected language

:::note
The language in the app is for UI only — does not affect content displayed in the web browser.
:::

## 🔔 Notifications

### Enable/Disable notifications

**Steps:**
1. **App Settings** → **Notifications**
2. Toggle each type:
   - **Push Notifications** — notify through app
   - **Email Notifications** — send email
   - **Sound** — turn on notification sound
3. Tap **Save**

### Notification types

| Type | Description |
|---|---|
| **Entry** | Notify when someone opens the door |
| **Failed Attempt** | Notify when someone fails authentication |
| **Alarm** | Notify on abnormal events (Trick, High temp, Low battery) |
| **Guest Key Used** | Notify when Guest Key is used |
| **Settings Changed** | Notify when settings are changed |

## 🔧 Other settings

### Clear Cache

**Steps:**
1. **App Settings** → **Clear Cache**
2. Confirm
3. App will reload

### About

**Info:**
- **App Version** (e.g., 1.0.45)
- **Build Number**
- **Last Updated**
- **License / Open Source Notices**

### Logout

**Steps:**
1. **App Settings** → **Logout**
2. Confirm

:::warning
- After Logout, must Login again to use
- **Guest Keys** you created still work (no need to login)
- **Guest Key remaining in Guest mode** may be lost
:::

## 🔐 Security

### Two-Factor Authentication (2FA)

:::info Email must be set first
Must have verified Email to enable 2FA
:::

**Steps:**
1. **App Settings** → **Security**
2. Toggle **Two-Factor Authentication** on
3. Enter **Password** to confirm
4. Every login will require a **Verification Code** from email

### Active Sessions

View **logged-in devices**:
- **Device name**
- **Last activity**
- **Location** (if available)
- **Logout** this device immediately

## 📋 Other menus

### Language
- **App Language** — UI language
- **Input Method** — keyboard language

### App Info
- **Version** — version
- **License** — license
- **Privacy Policy** — privacy policy
- **Terms of Service** — terms of service

### Help & Support
- **User Guide** — link to manual
- **FAQ** — frequently asked questions
- **Contact Support** — contact support team
- **Report a Problem** — report issue
- **Rate the App** — rate

## 💡 Best Practices

- **Enable 2FA** always for Super Admin
- **Logout** when done on shared devices
- **Update the app** when new version available
- **Check Active Sessions** regularly
- **Delete unused Guest Keys**
- **Verify Email** correctly (used for password recovery)
