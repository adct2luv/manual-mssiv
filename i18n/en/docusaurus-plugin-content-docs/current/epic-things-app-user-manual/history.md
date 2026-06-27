---
sidebar_position: 9
title: History
description: Entry/exit history and usage logs
---

# History

The **History** menu shows all usage history of locks you manage.

## 📋 Data types in history

| Type | Description | Example |
|---|---|---|
| **Entry** | Successful door open | "Dad opened door at 09:30 via PIN" |
| **Failed attempt** | Failed authentication | "Unknown tried PIN at 22:15 (failed)" |
| **Guest entry** | Guest Key used to open door | "Guest opened door at 14:00" |
| **Tamper/Alarm** | Abnormal events | "Trick alarm triggered at 03:00" |
| **Settings change** | Configuration changes | "Super Admin changed PIN at 10:00" |

## 🔍 View history

**Steps:**
1. Go to **History** from the main screen
2. Select **Lock** you want (if multiple locks)
3. Select **Time range**:
   - **Today**
   - **This week**
   - **This month**
   - **Custom**
4. View event list

## 📊 Information in each entry

Each history entry shows:

- **Date & Time**
- **User name** (if available) or "Unknown"
- **Authentication method** (PIN, Card, Fingerprint, App, Guest Key)
- **Lock** (which lock) — if multiple locks
- **Status** (Success / Failed / Alarm)
- **Notes** (e.g., "Trick alarm", "Low battery")

## 📤 Export history

**Steps:**
1. On History page → select lock + time range
2. Tap **Export** or **Share**
3. Select format:
   - **CSV** — open in Excel/Sheets
   - **PDF** — save as PDF
   - **Share** — send via email/messenger

## 🔍 Filter data

Filter history by:

- **Event type**: Entry / Failed / Alarm / Settings
- **User**: specific person, Guest, Unknown
- **Authentication method**: PIN, Card, Fingerprint, App, Guest Key
- **Time range**: day/week/month/custom
- **Lock**: specific lock or all

## 💡 Tips for using History

### Use for security checks

- **Check Failed attempts** — frequent failed PIN/Card attempts may indicate attempted break-in
- **Check Unknown entries** — frequent "Unknown" entries may mean unregistered users
- **Check Alarm events** — Trick alarm, High temp, Low battery
- **Check Guest entries** — track Guest Key usage

### Use for administration

- **View usage statistics** — which locks are used most
- **Check employee entry/exit** — use with Wi-Fi Bridge + Member
- **Check Guest visits** — who visited when
- **Audit trail** — for retrospective investigation

## ⚠️ Cautions

- **History may be deleted** if you delete the lock from the app (depends on settings)
- **History is stored by server time** (not local time)
- **Time accuracy** depends on Wi-Fi Bridge configuration
- **Failed attempts data** is kept for 90 days (may vary by version)
- **Guest entries** show fewer details than Member entries
