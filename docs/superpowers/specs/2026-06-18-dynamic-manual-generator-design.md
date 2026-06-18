# Design Spec: Dynamic Docusaurus Manual Generator

## 1. Goal
Rewrite the manual generator script (`scripts/build_manuals.py`) to dynamically load and parse product specifications, components, features, operations, and alarms from their corresponding JSON source files. This eliminates incorrect hardcoded default fallbacks and ensures 100% accurate representation of all 32 manuals (including glass-type locks like ES-303G with 12mm thickness, no handles, no mechanical keys, and 2 RFID cards in the box).

---

## 2. Source Data Mapping
* **Tier C Models (12 models)**:
  - Source path: `../knowledge-base/extracted/vision/Manual_<MODEL>.json`
  - Models: `es-303g` (ES-303G), `ef-p8800k` (EF-P8800K), `es-m50` (ES-M50), `es-p9100fk` (ES-P9100FK), `es-t153` (ES-T153), `n-touch` (N-TOUCH), `touch` (TOUCH), `triplex-2way` (TRIPLEX 2way), `triplex-3way` (TRIPLEX 3way), `ef-8000l` (EF-8000L), `es-809l` (ES-809L), `es-k70` (ES-K70).
* **Tier A+B Models (4 models)**:
  - Source path: `../knowledge-base/products/<MODEL_DIR>/product.json`
  - Models: `es-b10` (ES-B10), `es-l200` (ES-L200), `os300h` (OS300H), `popscan` (POPscan).
* **Consolidated Manual Rev.09 Models (10 models)**:
  - Source path: `../knowledge-base/products/Consolidated-Manual-Rev.09/product.json`
  - Models: `es-s100dr`, `es-f300dr`, `es-f301d`, `es-f501d`, `es-ff730gr`, `es-ff731g`, `es-s740d`, `es-f7000kr`, `es-f9000kr`, `es-p8800k`.
  - Behavior: Load from Consolidated Manual JSON.
* **App Manual**:
  - Source path: `../knowledge-base/products/EPIC-Things-APP-User-Manual/product.json`.

---

## 3. Detailed Design & Dynamic Parsers

### A. Specification Parser (`parse_specs_from_json`)
* Locate the specs panel: Look for panel/title names containing "dimension", "spec", "specs", or "specification".
* Parse the specs table:
  - Handle 3-column rows (e.g. `["Installation", "tempered glass door", "Glass door thickness 12mm"]`):
    - Map `row[0]` as category, `row[1]` as subcategory/description, `row[2]` as actual value.
    - If `row[0]` is blank but contains items in other columns, merge or associate with the previous category.
  - Handle 2-column rows: Map `row[0]` as label and `row[1]` as value.
  - Clean values: e.g. extract "12mm tempered glass only" for `ES-303G` door thickness.
* Fallback to product JSON fields for Tier A/B.

### B. Component Parser (`parse_components_from_json`)
* Parse lists: `outer_body`, `inner_body`, and `in_box` from the components panel.
* Extract name and function if present in dictionary format (e.g. `{"name": "Touch-Type Number Pad", "function": "..."}`).
* Match components against a translation dictionary:
  - Ensure models without handles (like `ES-303G`, rim locks) do not list outer/inner handles.
  - Ensure models without keys do not list mechanical keys.
  - Write specific count for in-box items (e.g. `RFID Card (Sticker) 2EA` for `ES-303G`).

### C. Feature & Alarm Panel Extractors
Instead of sharing `COMMON_FEATURES` and `COMMON_ALARMS`, parse them directly:
* **Features**:
  - Panels: `guest_pin`, `force_lock_outside`, `force_lock_inside`, `sound_volume`, `sound_mute`, `auto_manual_lock`, `rfid_auto_manual`, `normal_safe_open` (Safety Button/Kanpang Foss Lok), `multi_touch`, `dual_mode`, `melody`, `home_network`.
  - Extract the panel descriptions, caution notices, steps, and options/modes.
* **Alarms**:
  - Panels: `anti_hacking` (invasion), `fire_sensor`, `anti_prank` (1-minute lock), `deadbolt_jammed`, `replace_battery`, `emergency_battery`.
  - Extract the description, alarm triggers, cancellation methods, and cautions.

### D. Operation & Registration Generators
* Use the steps, notes, and cautions extracted from panels like `pin_registration`, `rfid_registration_normal`, `rfid_registration_individual`, `rfid_deletion_all`, `rfid_deletion_individual`, `open_outside`, `close_outside`, `open_inside`, `close_inside`.
* Map them to markdown ordered lists with collapsible warning/caution boxes using Docusaurus MDX admonitions (e.g., `:::caution[ข้อควรระวัง]`).

---

## 4. Bilingual Translation Strategy (`translate_text`)
Maintain and expand a master dictionary (`TRANSLATIONS_DICT`) of terms, instructions, and warnings:
1. Translate exact match terms first (case-insensitive).
2. Substitute substrings for compound sentences.
3. Ensure no English fragments remain in Thai versions for settings, step instructions, and cautions.

---

## 5. Verification Checklist
- [ ] Run the generator script: `python3 scripts/build_manuals.py`.
- [ ] Inspect generated `docs/es-303g/specs.md` and check:
  - Door thickness = `กระจกนิรภัยเทมเปอร์หนา 12 มม. เท่านั้น` / `12mm tempered glass only`.
  - Product Type = `ไม่มีกุญแจกลไก` / `Non-key`.
- [ ] Inspect generated `docs/es-303g/components.md` and check:
  - Outer body parts contain NO outer body handle.
  - Inner body parts contain NO inner body handle.
  - In-box items contain `RFID Card (Sticker) 2EA` (RFID Card 2 ใบ) and NO mechanical keys.
- [ ] Inspect generated `docs/es-303g/features.md` and check presence of Guest PIN, Volume, Auto/Manual, RFID Detection, Dual Mode, Melody.
- [ ] Inspect generated `docs/es-303g/alarms.md` and check battery warnings and fire sensor.
- [ ] Verify other models (e.g. `es-k70` with mechanical keys, `es-b10` with rim lock properties) have their distinct specs and components.
- [ ] Run Docusaurus build `npm run clear && npm run build` to ensure zero compilation errors.
