---
sidebar_position: 6
title: RFID Card Registration
description: How to register up to 100 RFID cards on the ES-K70.
---

# RFID Card Registration

The ES-K70 supports up to **100 RFID cards**. There are two modes:

- **All-at-once** — register multiple cards without assigning specific slot numbers. Fastest when you only need a few cards.
- **One-by-one** — assign each card to a specific 3-digit slot number (001 – 100). Useful when you want to delete a single lost card later.

:::tip Compatibility
Only EPIC-compatible 13.56 MHz RFID cards work with this lock. Cards included in the original box are pre-registered as a courtesy in some regions, but the manual states that **in-box cards are not registered by default** — register them yourself.
:::

:::caution Always register with the door open. If something goes wrong, you don't want to be locked out.
:::

---

## Mode A — All-at-once registration

Best for: registering a handful of cards without caring about slot numbers.

### ① Open the battery cover

Open the **inner-body battery cover** to reach the **Registration** button.

### ② Press the Registration button

Press the **Registration** button once. A short **beep** confirms registration mode is active.

### ③ Enter the current PIN, then `*`

Enter your **current PIN**, then press **`*`**.

### ④ Press `2`

Press the number **`2`** button to select all-at-once mode.

### ⑤ Place each card on the reader

One at a time, place each card on the **RFID card reader** on the outer body. After each card, you should hear a beep. The number pad will briefly display the assigned slot (e.g. `001`, `002`, …).

### ⑥ Press Registration to finish

Press the **Registration** button again. The lock beeps to confirm registration is complete.

#### Note

- Up to **100 cards** total can be registered across both modes.
- Repeat step ⑤ before the 10-second timeout to add more cards. After 10 s without activity, registration cancels.
- After the 100th card is registered, no further cards can be added until you delete one or more.

---

## Mode B — One-by-one registration

Best for: large deployments or when you need to be able to delete a specific lost card.

### ① Open the battery cover

Open the **inner-body battery cover**.

### ② Press the Registration button

Press the **Registration** button once. A **beep** confirms registration mode is active.

### ③ Enter the current PIN, then `*`

Enter the **current PIN**, then press **`*`**.

### ④ Press `2`

Press **`2`** to select registration mode.

### ⑤ Enter the 3-digit slot, then `#`

Enter the **3-digit slot number** (`001` – `100`) you want this card to occupy, then press **`#`**.

> The slot number **must always be 3 digits**. `1` is invalid; use `001`.

### ⑥ Place the card on the reader

Hold the card on the **RFID card reader**. A beep confirms, and the slot number flashes on the number pad.

### ⑦ When the pad returns to standby

The number pad returns to its normal display when the lock is back in standby mode.

### ⑧ Register more cards (optional)

- **To register additional cards:** while all 9 segments of the pad are lit, enter the next slot number + `#`, then place the next card. Repeat as needed.
- **When there are no more cards:** press the **Registration** button to finish.

---

## Quick-reference card

```
╔═══════════════════════════════════════════════════════╗
║  REGISTER RFID — door open                            ║
╠═══════════════════════════════════════════════════════╣
║  ALL-AT-ONCE                                          ║
║    1. Open cover                                      ║
║    2. [Registration]            → beep                ║
║    3. PIN + [✱]                                       ║
║    4. [2]                                              ║
║    5. Tap card on reader            (repeat per card) ║
║    6. [Registration]            → finish              ║
║                                                       ║
║  ONE-BY-ONE                                           ║
║    1. Open cover                                      ║
║    2. [Registration]            → beep                ║
║    3. PIN + [✱]                                       ║
║    4. [2]                                              ║
║    5. Slot (001–100) + [#]                            ║
║    6. Tap card on reader                               ║
║    7. (Optional) Slot + [#] + tap next card           ║
║    8. [Registration]            → finish              ║
║                                                       ║
║  Capacity: 100 cards · Timeout: 10 s between steps    ║
╚═══════════════════════════════════════════════════════╝
```

## Need to remove a card?

If a card is lost or stolen, see **[RFID Card Deletion](./rfid-deletion)**.
