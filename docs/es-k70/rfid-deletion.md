---
sidebar_position: 7
title: RFID Card Deletion
description: Delete one card or all cards on the ES-K70.
---

# RFID Card Deletion

There are two deletion modes:

- **All-at-once** — wipe every registered card in one operation. Use this if a card is lost and you can't identify which slot it occupied.
- **One-by-one** — delete a specific slot. Use this when you know exactly which card number to remove.

:::warning
Deleting cards **cannot be undone**. The deleted cards must be re-registered to work again.
:::

---

## Mode A — Delete all cards at once

### ① Open the battery cover

Open the **inner-body battery cover**.

### ② Press the Registration button

Press the **Registration** button once. A **beep** confirms deletion mode is active.

### ③ Enter the current PIN, then `*`

Enter your **current PIN**, then press **`*`**.

### ④ Press `8`

Press the number **`8`** button to select delete-all mode.

### ⑤ Hold `8` for 5 seconds

**Long-press** the **`8`** button for **5 seconds**. When the lock's melody plays, all registered RFID cards have been deleted.

---

## Mode B — Delete one card by slot

### ① Open the battery cover

Open the **inner-body battery cover**.

### ② Press the Registration button

Press the **Registration** button once. A **beep** confirms deletion mode is active.

### ③ Enter the current PIN, then `*`

Enter the **current PIN**, then press **`*`**.

### ④ Press `8`, then `#`

Press **`8`** to select delete mode, then press **`#`** to confirm one-by-one deletion.

### ⑤ Enter the slot number, then `#`

Enter the **3-digit slot number** (`001` – `100`) of the card you want to remove, then press **`#`**.

When the deletion is complete, all 9 segments of the number pad light up. The lock returns to normal operation.

If the slot you entered had no card registered, the lock simply beeps and stays in standby — nothing is deleted.

### ⑥ Press Registration to finish

If there are no more cards to delete, press the **Registration** button to confirm.

---

## Quick-reference card

```
╔═══════════════════════════════════════════════════════╗
║  DELETE RFID — door open                              ║
╠═══════════════════════════════════════════════════════╣
║  ALL                                                  ║
║    1. Open cover                                      ║
║    2. [Registration]            → beep                ║
║    3. PIN + [✱]                                       ║
║    4. [8]                                              ║
║    5. Hold [8] for 5 s           → melody             ║
║                                                       ║
║  ONE-BY-ONE                                           ║
║    1. Open cover                                      ║
║    2. [Registration]            → beep                ║
║    3. PIN + [✱]                                       ║
║    4. [8] + [#]                                        ║
║    5. Slot (001–100) + [#]                            ║
║    6. [Registration]            → finish              ║
║                                                       ║
║  Empty slot + [#] = no-op (lock stays in standby)     ║
╚═══════════════════════════════════════════════════════╝
```

## Lost your PIN too?

If you've forgotten **both** the PIN and all valid cards, contact an EPIC technician. Without a valid credential or the mechanical key, the lock cannot be reset electronically — the inner body must be powered and the Registration button pressed directly.
