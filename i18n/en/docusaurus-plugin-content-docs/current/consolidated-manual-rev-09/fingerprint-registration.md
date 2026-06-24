---
sidebar_position: 7
title: Fingerprint Registration
description: How to register fingerprints (LED [3]) — for models with Fingerprint Reader
---

# Fingerprint Registration

:::info Available on models with Fingerprint Reader
ES-F300Dr, ES-F301D, ES-F500D/H, ES-F501D/H, ES-S510D/H, ES-FF730Gr, ES-FF731G, ES-S740D, ES-F7000Kr, ES-F9000Kr, ES-P8800K
:::

**Up to 100 fingerprints** per lock

## 🖐 Register fingerprint (LED [3])

**Steps:**
1. Press **R** and enter main PIN + `[#]`
2. LEDs [1] [2] [3] [4] [5] light up → press number **[3]** (Fingerprint)
3. **Place finger on the sensor 4 times** (~1 second each) — beep sounds each time
4. On successful 4th scan → melody plays → fingerprint registered
5. Press **R** to finish

## 📊 LED scan status

| LED | Meaning |
|---|---|
| LED [1] [2] [3] blinking [2] | 1st scan successful |
| LED [1] [2] [3] blinking [3] | 2nd scan successful |
| LED [1] [2] [3] blinking (no number) | 3rd scan successful |
| LED [0] lit | Error or finger not aligned |

## 💡 Fingerprint scanning tips

- **Place finger fully on the sensor** — not just the tip
- **Finger must be clean** — not wet, no lotion, no cuts
- **Press gently** — no need to press hard
- Children's or elderly fingerprints may scan poorly — use other authentication methods

## ⚠️ Cautions

:::warning
- **One fingerprint per user** — don't register the same finger twice
- If **4 scans fail** → LED [0] lights → must start over
- **All fingerprints are deleted** if deleted via LED [3] in Deletion mode
- **Fingerprint registration does NOT delete the main PIN**
- **5 consecutive failed scans** = Anti-Prank + 1-minute lockout
- Must register a **valid fingerprint** before using Dual Authentication
- Damaged/wet/cut fingerprints may fail to scan → use PIN instead
:::
