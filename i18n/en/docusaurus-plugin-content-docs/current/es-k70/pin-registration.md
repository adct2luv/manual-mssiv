---
sidebar_position: 5
title: PIN Registration
description: How to change the PIN on the ES-K70.
---

# PIN Number Registration

This procedure **changes an existing PIN** to a new one. The first time you set up the lock, the existing PIN is the default `1234`.

:::caution[Before you start]
- Always register the PIN **while the door is open**. You don't want to be locked out if something goes wrong.
- The default PIN is **`1`, `2`, `3`, `4`**. Change it before first use.
- A new PIN overwrites **all previously registered PINs**. The ES-K70 only supports one PIN at a time.
- Choose a 4 – 12 digit PIN. **Avoid** `0000`, `1234`, repeated digits, your birth year, or any obvious pattern.
- **There is no factory reset path.** If you forget your PIN with no valid RFID card or mechanical key, you will need to call a technician to disassemble the lock.
:::

## Step-by-step

> The illustrations in the printed manual show the number pad (1 – 9, *, 0, #) and the inner-body **Registration** button under the battery cover.

### ① Open the battery cover

Open the **inner-body battery cover** so you can reach the **Registration** button.

![Open battery cover](https://placehold.co/480x320/f5f5f5/888?text=Step+1:+Open+battery+cover)

### ② Press the Registration button once

Press the **Registration** button once. A short **beep** confirms the lock has entered registration mode.

![Press Registration button — beep](https://placehold.co/480x320/f5f5f5/888?text=Step+2:+Press+Registration)

You now have **10 seconds** to complete the next step. If you wait longer, the lock times out and you'll need to start over.

### ③ Enter the current PIN, then `*`

On the outer-body keypad, enter the **current PIN**, then press **`*`** to confirm.

| If this is the first time | Use the default PIN `1 2 3 4` |
|---|---|

### ④ Enter the new PIN, then `*`

Enter your **new PIN** (4 – 12 digits), then press **`*`** to confirm.

### ⑤ Enter the new PIN again, then `*`

Enter the **same new PIN** once more, then press **`*`** to confirm.

A **melody plays** — this confirms the new PIN is registered.

## Common pitfalls

| Symptom | Likely cause |
|---|---|
| Three short beeps instead of a melody | The two new-PIN entries didn't match — start over |
| Beep on step ②, then nothing on step ③ | The 10-second timeout elapsed — press Registration again |
| Status LED flashes red | The PIN contains invalid characters — digits only, 4 – 12 long |

## Quick-reference card

```
╔══════════════════════════════════════════════╗
║  CHANGE PIN — door must be open             ║
╠══════════════════════════════════════════════╣
║  1. Open battery cover (inner body)          ║
║  2. Press [Registration]      → beep         ║
║  3. Current PIN + [✱]                       ║
║  4. New PIN (4–12 digits) + [✱]              ║
║  5. New PIN again + [✱]      → melody       ║
║  Timeout: 10 s between steps                ║
╚══════════════════════════════════════════════╝
```

## Next step

Once your PIN works, register at least one RFID card as a backup. See **[RFID Card Registration](./rfid-registration)**.
