---
sidebar_position: 4
title: Member Management
description: Add, remove, edit members and set permissions
---

# Member Management

The **Member** menu is on the main screen, used to manage all members of the lock.

## 📋 Member types

EPIC Door Lock has **3 user levels** by permission order:

| Level | Description | Permissions |
|---|---|---|
| **Super Admin** | Highest level | Everything, including linking the app, setting Super Admin PIN |
| **General Admin** | General administrator | Manage members, view history, add/remove keys |
| **User** | Regular user | Use keys (PIN, Card, Fingerprint etc.) to open the door |

:::info
- **Super Admin** must be set at the lock (cannot be created from the app)
- **General Admin** and **User** are created from the app (must login as Super Admin first)
:::

## ➕ Add new member

**Steps:**
1. Go to **Member** from the main screen
2. Tap **+ Add** or the **+** icon
3. Select member type: **General Admin** or **User**
4. Enter details:
   - **Name**
   - **Email** (used to login)
   - **Phone** (optional)
   - **Permission level** (General Admin / User)
5. Tap **Save** or **Send**
6. The system will send an **invitation email** to the new member

:::note
- **Email must be unique** among members
- **General Admin** can manage members they created
- **User** can only open the door
:::

## ✏️ Edit member

**Steps:**
1. In the **Member** menu, select a member
2. Tap **Edit** or pencil icon
3. Edit details:
   - Name, Email, Phone
   - Permission level (General Admin / User)
4. Tap **Save**

:::warning
- Changing permission to General Admin gives more access — **be careful granting permissions to others**
- Editing Email may require the member to verify email again
:::

## 🗑 Remove member

**Steps:**
1. In the **Member** menu, select a member
2. Tap **Delete** or trash icon
3. Confirm deletion

:::caution
- **Deleting a member does NOT delete their keys (PIN, Card, Fingerprint)** registered to the lock
- Keys must be deleted separately in the **Key** menu
- Deleted members can no longer log in to the app
:::

## 🔄 Change Permission Level

| From → To | How |
|---|---|
| User → General Admin | Edit permission in Member list |
| General Admin → User | Edit permission |
| General Admin → Super Admin | **Not possible** — Super Admin can only be set at the lock |

## 📊 View member list

The Member page shows:
- **Name**
- **Email**
- **Permission level** (Super Admin / General Admin / User)
- **Status** (active/pending verification)
- **Accessible locks**

## 💡 Best practices

- Use **real email addresses** for members — used for login and password recovery
- **Permission level** should match actual role (don't make users General Admin unnecessarily)
- **Remove inactive members** for security
- **Review member list** regularly
- **Super Admin permission** should be limited to 1-2 trusted people
