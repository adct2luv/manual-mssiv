# Dynamic Docusaurus Manual Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `scripts/build_manuals.py` to dynamically parse specs, components, features, alarms, and operations for all models from their JSON files, ensuring zero generic fallbacks and complete bilingual (TH/EN) accuracy.

**Architecture:** Load data from `extracted/vision/*.json` (for Tier C) and `products/*/product.json` (for Tier A+B). Determine product characteristics (e.g. handle, key, RFID count) dynamically, extract feature/alarm panels, and apply an expanded localization dictionary.

**Tech Stack:** Python, Docusaurus (Markdown/JSON)

---

### Task 1: Setup and JSON Directory Paths Loading
**Files:**
- Modify: `scripts/build_manuals.py:1148-1196` (add ES-K70 and setup file loading)
- Modify: `scripts/build_manuals.py:214-245` (update feature flags)

- [ ] **Step 1: Add ES-K70 to MANUALS list in `build_manuals.py`**
  Add `("es-k70", "ES-K70", "กุญแจดิจิทัล ES-K70", "ES-K70 Digital Lock", "กุญแจดิจิทัลแบบ Rim Type รองรับ PIN และบัตร RFID พร้อมกุญแจกลไกสำรอง", "Rim-type digital lock supporting PIN, RFID, and backup mechanical key.", "es-k70", None, "https://www.epic.co.kr/home/manual/")` under Tier C section.
- [ ] **Step 2: Add logic in the loop to load the source JSON**
  Check path `knowledge-base/extracted/vision/Manual_<MODEL>.json` for Tier C and `knowledge-base/products/<DIR>/product.json` for Tier A/B.
  Code snippet to add:
  ```python
  def load_source_json(slug):
      # Try vision path
      model_up = slug.upper().replace("-", "_")
      if slug == "triplex-2way": model_up = "TRIPLEX 2way"
      elif slug == "triplex-3way": model_up = "TRIPLEX 3way"
      
      vision_path = SITE.parent / "knowledge-base" / "extracted" / "vision" / f"Manual_{model_up}.json"
      if vision_path.exists():
          with open(vision_path, "r", encoding="utf-8") as f:
              return json.load(f), "vision"
              
      # Try products path
      dir_map = {
          "es-b10": "ES-B10", "es-l200": "ES-L200", "os300h": "OS300H", "popscan": "POPscan",
          "consolidated-manual-rev-09": "Consolidated-Manual-Rev.09",
          "epic-things-app-user-manual": "EPIC-Things-APP-User-Manual"
      }
      p_dir = dir_map.get(slug)
      if p_dir:
          p_path = SITE.parent / "knowledge-base" / "products" / p_dir / "product.json"
          if p_path.exists():
              with open(p_path, "r", encoding="utf-8") as f:
                  return json.load(f), "product"
                  
      # Fallback to Consolidated Manual for consolidated models
      consolidated_models = {
          "es-s100dr", "es-f300dr", "es-f301d", "es-f501d",
          "es-ff730gr", "es-ff731g", "es-s740d",
          "es-f7000kr", "es-f9000kr", "es-p8800k"
      }
      if slug in consolidated_models:
          p_path = SITE.parent / "knowledge-base" / "products" / "Consolidated-Manual-Rev.09" / "product.json"
          if p_path.exists():
              with open(p_path, "r", encoding="utf-8") as f:
                  return json.load(f), "consolidated"
      return None, None
  ```
- [ ] **Step 3: Commit changes**
  Run: `git add scripts/build_manuals.py && git commit -m "feat: add JSON loaders and ES-K70"`

---

### Task 2: Implement Dynamic Specifications & Component Extractor
**Files:**
- Modify: `scripts/build_manuals.py` (add spec and component extraction helpers)

- [ ] **Step 1: Write `parse_specs_from_json(slug, data, source_type)`**
  Extract specs:
  - If "vision": search for dimensions/specs panel table. Handle 3-column rows. For `ES-303G`, map thickness to `12mm tempered glass only` / `กระจกนิรภัยเทมเปอร์หนา 12 มม. เท่านั้น`.
  - If "product" or "consolidated": read `th["specs"]` and `en["specs"]` from the JSON.
  - Return formatted list of `(label_en, value_en)` and `(label_th, value_th)`.
- [ ] **Step 2: Write `parse_components_from_json(slug, data, source_type)`**
  Identify handles and mechanical keys:
  - Non-handle models: `es-303g`, `es-b10`, `os300h`, `popscan`, `touch`, `n-touch`, locker locks, and rim locks. Remove any outer/inner body handles.
  - Non-key models: If `mechanical_key` is not in `PRODUCT_FEATURES[slug]`, remove mechanical keys from components and in-box items.
  - RFID Card count: Extract from `in_box` lists (e.g. `RFID Card (Sticker) 2EA` for `ES-303G`).
- [ ] **Step 3: Integrate with `generate_manual_pages`**
  Modify specs and components generation block to call the new helpers.
- [ ] **Step 4: Commit changes**
  Run: `git add scripts/build_manuals.py && git commit -m "feat: implement dynamic spec and component parser"`

---

### Task 3: Implement Dynamic Feature & Alarm Panel Extractor
**Files:**
- Modify: `scripts/build_manuals.py`

- [ ] **Step 1: Write `parse_features_from_json(slug, data, source_type)`**
  Collect setting/operational panels: `guest_pin`, `force_lock_outside`, `force_lock_inside`, `sound_volume`, `sound_mute`, `auto_manual_lock`, `rfid_auto_manual`, `normal_safe_open`, `multi_touch`, `dual_mode`, `melody`, `home_network`.
  Format steps, descriptions, cautions, and notes into markdown. Translate to Thai.
- [ ] **Step 2: Write `parse_alarms_from_json(slug, data, source_type)`**
  Collect alarm panels: `anti_hacking` (invasion), `fire_sensor`, `anti_prank` (1-minute lock), `deadbolt_jammed`, `replace_battery`, `emergency_battery`.
  Format to markdown with translation.
- [ ] **Step 3: Integrate features and alarms generation in `generate_manual_pages`**
  Call the helpers and fallback to static common lists if JSON has no panels.
- [ ] **Step 4: Commit changes**
  Run: `git add scripts/build_manuals.py && git commit -m "feat: implement dynamic feature and alarm extraction"`

---

### Task 4: Implement Door Operations Page Generator
**Files:**
- Modify: `scripts/build_manuals.py`

- [ ] **Step 1: Write `gen_door_operations(slug, data, source_type)`**
  Parse door operations from panels: `open_outside`, `close_outside`, `open_inside`, `close_inside`.
  Write bilingual files to `docs/<slug>/door-operations.md` and `i18n/en/.../<slug>/door-operations.md`.
- [ ] **Step 2: Commit changes**
  Run: `git add scripts/build_manuals.py && git commit -m "feat: implement door operations page generator"`

---

### Task 5: Expand Translation Dictionary and Build Site
**Files:**
- Modify: `scripts/build_manuals.py` (expand translation dictionary)

- [ ] **Step 1: Update `TRANSLATIONS_DICT` and `translate_text`**
  Add all missing terms (e.g. "Outside Force Lock", "MELODY SETTINGS", "RFID Card Auto / Manual Detection Setting", etc.) to map to natural Thai.
- [ ] **Step 2: Run build script to generate all manuals**
  Run: `python3 scripts/build_manuals.py`
- [ ] **Step 3: Verify ES-303G outputs**
  Check `docs/es-303g/specs.md`, `components.md`, `features.md`, `alarms.md` to confirm correct values, counts, and translations.
- [ ] **Step 4: Run Docusaurus build**
  Run: `npm run clear && npm run build`
- [ ] **Step 5: Commit all generated pages**
  Run: `git add docs/ i18n/ && git commit -m "docs: regenerate all manuals dynamically with bilingual accuracy"`
