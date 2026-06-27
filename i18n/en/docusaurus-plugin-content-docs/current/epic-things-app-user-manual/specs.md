---
sidebar_position: 11
title: Specifications
description: EPIC Things App specifications
---

# Specifications

## 📱 App Requirements

| Item | Value |
|---|---|
| **App Version** | 1.0.45 (depends on version) |
| **Platform** | iOS 12.0+ / Android 7.0+ |
| **App Size** | ~50 MB |
| **Languages** | English, Thai (depends on version) |
| **Distribution** | Apple App Store, Google Play Store |
| **License** | Free (with EPIC door lock) |

## 🔌 Connectivity

| Mode | Range | Speed | Use case |
|---|---|---|---|
| **Bluetooth (BLE)** | ≤ 10 meters | Fast | Near lock |
| **Wi-Fi** | Unlimited (network) | Depends on Wi-Fi | Remote |
| **Wi-Fi Bridge** | Depends on Wi-Fi | Fast | Connect to Wi-Fi |

## 📋 User Levels

| Level | Permissions |
|---|---|
| **Super Admin** | Everything |
| **General Admin** | Manage members, view history, add/remove keys |
| **User** | Use keys to open door |
| **Guest** | Open door 1 time (Guest Key) |

## 🔑 Authentication Methods

| Type | Limit | Register via app |
|---|---|---|
| **PIN** | 1 PIN per lock (4-12 digits) | ❌ At lock |
| **Smart Card** | 200 cards | ✅ |
| **Fingerprint** | 100 prints | ✅ |
| **Remote Control** | Per model | ✅ |
| **Face ID** | 30 faces | ✅ |

## 🔐 Security Features

- **Two-Factor Authentication (2FA)** — can be enabled
- **Biometric Login** — iOS Face ID, Android Fingerprint
- **Auto Logout** — after idle time
- **Session Management** — view and logout devices
- **Encrypted Communication** — between app and lock (BLE/Wi-Fi)

## 📊 History

| Item | Details |
|---|---|
| **Types** | Entry, Failed, Alarm, Guest, Settings |
| **Retention** | 90 days (depends on version) |
| **Export** | CSV, PDF |
| **Filter** | By lock, time, user |

## 🎫 Guest Key

| Type | Details |
|---|---|
| **One-time** | Valid for 1 use |
| **Time-limited** | Valid for multiple uses within specified time |
| **Required mode** | Wi-Fi mode only |
| **Share** | Email, SMS, QR code, link |

## 🔋 Lock Requirements

- **EPIC Door Lock** with BLE support
- **Wi-Fi Bridge** (optional, sold separately)
- **Super Admin PIN** must be set first
- **App version 1.0.45+**

## 📞 Support

- **In-app**: Help → Contact Support
- **Email**: support@epic.co.kr
- **Website**: [epic.co.kr](https://www.epic.co.kr)
- **Phone**: See website
