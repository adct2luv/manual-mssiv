# Dynamic Docusaurus Manual Builder Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the manual generator script to dynamically parse specifications, components, features, alarms, and operations for all 22 models from their JSON source files, ensuring zero generic fallbacks and complete accuracy.

**Architecture:** Load data from `extracted/vision/*.json` (for Tier C) and `products/*/product.json` (for Tier A+B). Implement dynamic page detectors for specs, components, operations, settings/features, and alarms, converting raw JSON structures to clean translated markdown.

**Tech Stack:** Python, Docusaurus, JSON

---

### Task 1: Clean Translation Dictionary and Helper Functions

**Files:**
- Modify: `scripts/build_manuals.py`

- [ ] **Step 1: Write a comprehensive component/action translation dictionary and mapping**
- [ ] **Step 2: Add translation functions for steps, notes, and titles**
- [ ] **Step 3: Implement dynamic specs parser that reads door thickness and power specs directly from JSON**

### Task 2: Implement Component and Operation Generator

**Files:**
- Modify: `scripts/build_manuals.py`

- [ ] **Step 1: Write a function to load and clean component lists (outer body, inner body, in-box) from JSON**
- [ ] **Step 2: Add door operations page generator (`door-operations.md`) that maps opening and closing steps from inside/outside**

### Task 3: Implement Dynamic Feature and Alarm Generator

**Files:**
- Modify: `scripts/build_manuals.py`

- [ ] **Step 1: Implement features page generator (`features.md`) to format Guest PIN, Force Lock, Volume, Mute, RFID detection, Dual Mode, and Network Module settings dynamically**
- [ ] **Step 2: Implement alarms page generator (`alarms.md`) to format high temperature, intrusion, anti-prank, deadbolt jam, replace battery, and emergency battery alarms dynamically**

### Task 4: Integrate All Models (Including ES-K70) and Run Build

**Files:**
- Modify: `scripts/build_manuals.py`
- Modify: `sidebars.ts`

- [ ] **Step 1: Add ES-K70 to the MANUALS list in `build_manuals.py` and `sidebars.ts` if missing**
- [ ] **Step 2: Update `main()` in `build_manuals.py` to loop over all models and call the dynamic parser instead of hardcoded fallbacks**
- [ ] **Step 3: Run the build script to generate all 32 manuals**
- [ ] **Step 4: Clean and compile Docusaurus to verify there are no errors**

### Task 5: Double-Check and Verification Loop

**Files:**
- Modify: `progress.md`

- [ ] **Step 1: Verify generated pages for ES-303G (specs, components, operations, features, alarms) and check against the JSON content**
- [ ] **Step 2: Verify at least three other models (e.g. ES-K70, ES-B10, TOUCH) for handles, keys, and door thickness accuracy**
- [ ] **Step 3: Confirm everything compiles cleanly and document verification findings**


