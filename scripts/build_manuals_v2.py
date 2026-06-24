#!/usr/bin/env python3
"""
Build Docusaurus MDX pages for all 22 EPIC manuals — v2 with vision JSON content.
Uses actual PDF content (vision extraction) when available, falls back to templates.
Generates bilingual EN+TH content.
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
SITE = ROOT / "manual-site"
DOCS_TH = SITE / "docs"
DOCS_EN = SITE / "i18n/en/docusaurus-plugin-content-docs/current"
VISION_DIR = KB / "extracted/vision"
PRODUCTS_DIR = KB / "products"

# =============================================================================
# Thai translations
# =============================================================================
TH = {
    "Overview": "ภาพรวม",
    "Safety Precautions": "ข้อควรระวังด้านความปลอดภัย",
    "Specifications": "ข้อมูลจำเพาะ",
    "Components": "ส่วนประกอบ",
    "PIN Registration": "การลงทะเบียนรหัส PIN",
    "RFID Registration": "การลงทะเบียนบัตร RFID",
    "RFID Deletion": "การลบบัตร RFID",
    "Smart Key Registration": "การลงทะเบียน Smart Key",
    "Smart Key Deletion": "การลบ Smart Key",
    "Fingerprint Registration": "การลงทะเบียนลายนิ้วมือ",
    "Fingerprint Deletion": "การลบลายนิ้วมือ",
    "Features": "คุณสมบัติ",
    "Alarms": "สัญญาณเตือน",
}

# =============================================================================
# Helpers
# =============================================================================
def fm(title, desc, position=1, slug=None):
    parts = ["---", f"sidebar_position: {position}", f"title: {title}", f"description: {desc}"]
    if slug:
        parts.append(f"slug: {slug}")
    parts.append("---")
    return "\n".join(parts)


def category_json(slug, label, description):
    return json.dumps({
        "label": label,
        "position": 1,
        "link": {
            "type": "generated-index",
            "description": description
        }
    }, ensure_ascii=False, indent=2)


def table_th_en(rows, th_left=True):
    """Generate a markdown table with TH | EN columns or vice versa."""
    if th_left:
        return ["| TH | EN |", "|---|---|"] + [f"| {r[0]} | {r[1]} |" for r in rows]
    else:
        return ["| EN | TH |", "|---|---|"] + [f"| {r[0]} | {r[1]} |" for r in rows]


# =============================================================================
# Vision-JSON-driven page generators
# =============================================================================
def gen_intro_from_vision(model, slug, vision):
    """Generate intro.md from vision JSON page 1 (cover) + features list."""
    th_lines = [fm(f"ภาพรวม {model}", f"ภาพรวมและคุณสมบัติของ {model}", 1), "", f"# {model}"]

    # Page 1 (cover) - usually has default pin, model info
    page1 = vision.get("pages", [{}])[0] if vision.get("pages") else {}
    if page1.get("panel") == "Table of Contents":
        page1 = vision["pages"][1] if len(vision["pages"]) > 1 else {}

    # Handle 2-page brochure structure: panels nested inside page
    if not page1.get("panel") and page1.get("panels"):
        # Find cover panel in page 1's panels
        for p in page1["panels"]:
            if "cover" in p.get("panel", "").lower():
                page1 = p
                break

    en_lines = [fm("Overview", f"Overview and features of {model}", 1), "", f"# {model}"]

    # Try to find a "cover" panel
    cover_panel = None
    for p in vision.get("pages", []):
        # Check if p is a panel directly
        if p.get("panel") and "cover" in p["panel"].lower():
            cover_panel = p
            break
        # Check panels nested inside
        panels = p.get("panels", [])
        for panel in panels:
            if "cover" in panel.get("panel", "").lower() or "title" in panel.get("panel", "").lower():
                cover_panel = panel
                break
        if cover_panel:
            break

    if cover_panel:
        for lang, lines in [("th", th_lines), ("en", en_lines)]:
            lines.append("")
            title_key = "title" if lang == "en" else "title"
            if title_key in cover_panel:
                lines.append(f"**{cover_panel[title_key]}**")
            if "default_pin" in cover_panel:
                lines.append("")
                if lang == "th":
                    lines.append(f"**รหัส PIN เริ่มต้น:** `{cover_panel['default_pin']}`")
                    if cover_panel.get("default_pin_warning"):
                        lines.append(f"\n> {cover_panel['default_pin_warning']}")
                else:
                    lines.append(f"**Default PIN:** `{cover_panel['default_pin']}`")
                    if cover_panel.get("default_pin_warning"):
                        lines.append(f"\n> {cover_panel['default_pin_warning']}")

    # Features list - extract from anywhere
    features = []
    for p in vision.get("pages", []):
        # Check page-level features_list
        if p.get("panel") == "Features":
            for f_item in p.get("features_list", []):
                features.append((f_item.get("feature", ""), f_item.get("details", "")))
            break
        # Check nested panels
        for panel in p.get("panels", []):
            if "feature" in panel.get("panel", "").lower():
                f_list = panel.get("features_list", []) or panel.get("features", [])
                for f_item in f_list:
                    if isinstance(f_item, dict):
                        features.append((f_item.get("feature", f_item.get("title", "")), f_item.get("details", f_item.get("description", ""))))
                    else:
                        features.append((str(f_item), ""))
                if features:
                    break
        if features:
            break

    if features:
        th_lines.extend([
            "",
            "## คุณสมบัติเด่น",
            "",
        ])
        en_lines.extend([
            "",
            "## Key Features",
            "",
        ])
        for th_feat, en_feat in features:
            th_lines.append(f"- **{th_feat}**")
            en_lines.append(f"- **{en_feat}**")
        th_lines.append("")
        en_lines.append("")

    # Default warning
    th_lines.extend([
        f":::warning ต้องติดตั้งโดยช่างผู้เชี่ยวชาญ",
        f"ผลิตภัณฑ์นี้ต้องติดตั้งโดย **ช่างผู้เชี่ยวชาญเท่านั้น** เพื่อให้ได้รับการรับประกันเต็มรูปแบบ ห้ามติดตั้งด้วยตัวเอง",
        ":::",
        "",
        "📖 ดูคู่มือ PDF ต้นฉบับ: [epic.co.kr](https://www.epic.co.kr/home/manual/)",
    ])
    en_lines.extend([
        f":::warning Professional installation required",
        f"This product must be installed by a **qualified technician only** to receive full warranty coverage. Do not install it yourself.",
        ":::",
        "",
        "📖 Original PDF manual: [epic.co.kr](https://www.epic.co.kr/home/manual/)",
    ])

    return "\n".join(th_lines), "\n".join(en_lines)


def gen_specs_from_vision(model, vision):
    """Generate specs.md from vision JSON page 2 (Product Dimension)."""
    th_lines = [fm(f"ข้อมูลจำเพาะ {model}", f"ข้อมูลจำเพาะของ {model}", 2), "", f"# ข้อมูลจำเพาะ"]
    en_lines = [fm("Specifications", f"Specifications of {model}", 2), "", f"# Specifications"]

    for p in vision.get("pages", []):
        if p.get("panel") == "Product Dimension & Components":
            specs_table = p.get("specs", {}).get("table", [])
            rf_table = p.get("rf_specification", {}).get("table", [])
            break
    else:
        specs_table = []
        rf_table = []

    if specs_table:
        th_lines.extend(["", "## ข้อมูลทั่วไป", "", "| รายการ | ค่า |", "|---|---|"])
        en_lines.extend(["", "## General", "", "| Item | Value |", "|---|---|"])
        for row in specs_table:
            label, val1, val2 = row[0], row[1] if len(row) > 1 else "", row[2] if len(row) > 2 else ""
            th_lines.append(f"| **{label}** | {val1} {val2} |".rstrip())
            en_lines.append(f"| **{label}** | {val1} {val2} |".rstrip())

    if rf_table:
        th_lines.extend(["", "## RF Specification", "", "| Item | Frequency | Channel | Modulation | Power |", "|---|---|---|---|---|"])
        en_lines.extend(["", "## RF Specification", "", "| Item | Frequency | Channel | Modulation | Power |", "|---|---|---|---|---|"])
        for row in rf_table:
            line = "| " + " | ".join(str(x) for x in row) + " |"
            th_lines.append(line)
            en_lines.append(line)

    th_lines.append("")
    en_lines.append("")

    return "\n".join(th_lines), "\n".join(en_lines)


def gen_components_from_vision(model, slug, vision):
    """Generate components.md from vision JSON page 3 (Outbody Parts)."""
    th_lines = [fm(f"ส่วนประกอบ {model}", f"ส่วนประกอบของ {model}", 3), "", f"# ส่วนประกอบ"]
    en_lines = [fm("Components", f"Components of {model}", 3), "", f"# Components"]

    outbody = []
    inbody = []
    in_box = []

    for p in vision.get("pages", []):
        if "Outbody Parts" in p.get("panel", ""):
            outbody = p.get("parts", [])
        if "Inbody Parts" in p.get("panel", ""):
            inbody = p.get("parts", [])
        if p.get("panel") == "Product Components":
            in_box = p.get("product_components", [])

    if outbody:
        th_lines.extend(["", "## ตัวล็อกด้านนอก", "", "| # | ชิ้นส่วน | หน้าที่ |", "|---|---|---|"])
        en_lines.extend(["", "## Outer body", "", "| # | Part | Function |", "|---|---|---|"])
        for part in outbody:
            th_lines.append(f"| {part.get('no', '')} | **{part.get('name', '')}** | {part.get('function', '')} |")
            en_lines.append(f"| {part.get('no', '')} | **{part.get('name', '')}** | {part.get('function', '')} |")

    if inbody:
        th_lines.extend(["", "## ตัวล็อกด้านใน", "", "| # | ชิ้นส่วน | หน้าที่ |", "|---|---|---|"])
        en_lines.extend(["", "## Inner body", "", "| # | Part | Function |", "|---|---|---|"])
        for part in inbody:
            th_lines.append(f"| {part.get('no', '')} | **{part.get('name', '')}** | {part.get('function', '')} |")
            en_lines.append(f"| {part.get('no', '')} | **{part.get('name', '')}** | {part.get('function', '')} |")

    if in_box:
        th_lines.extend(["", "## อุปกรณ์ในกล่อง", ""])
        en_lines.extend(["", "## In the box", ""])
        for item in in_box:
            th_lines.append(f"- {item}")
            en_lines.append(f"- {item}")

    th_lines.append("")
    en_lines.append("")

    return "\n".join(th_lines), "\n".join(en_lines)


def gen_programming_from_vision(model, vision, page_titles, position):
    """Generate a programming page (PIN/RFID/FP) from vision JSON."""
    target_panel = None
    for p in vision.get("pages", []):
        panels = p.get("panels", [])
        for panel in panels:
            if panel.get("panel") in page_titles:
                target_panel = panel
                break
        if not target_panel:
            # Maybe the page itself is the panel
            if p.get("panel") in page_titles:
                target_panel = p
                break
        if target_panel:
            break

    if not target_panel:
        return None, None

    panel_title = target_panel.get("panel", "")
    th_title = TH.get(panel_title, panel_title)
    en_title = panel_title

    th_lines = [fm(th_title, f"วิธี{panel_title} บน {model}", position), "", f"# {th_title}"]
    en_lines = [fm(en_title, f"How to {en_title} on {model}", position), "", f"# {en_title}"]

    # Caution
    if target_panel.get("caution"):
        th_lines.extend([
            "",
            f":::caution ข้อควรระวัง",
            target_panel["caution"],
            ":::",
        ])
        en_lines.extend([
            "",
            f":::caution Caution",
            target_panel["caution"],
            ":::",
        ])

    # After caution
    if target_panel.get("after_caution"):
        th_lines.extend([
            "",
            f":::note",
            target_panel["after_caution"],
            ":::",
        ])

    # Steps
    steps = target_panel.get("steps", [])
    if steps:
        th_lines.extend(["", "## ขั้นตอน", ""])
        en_lines.extend(["", "## Steps", ""])
        for i, step in enumerate(steps, 1):
            th_lines.append(f"{i}. {step}")
            en_lines.append(f"{i}. {step}")

    # Notes
    if target_panel.get("notes"):
        th_lines.extend([
            "",
            f":::note หมายเหตุ",
            target_panel["notes"] if isinstance(target_panel["notes"], str) else "\n".join(f"- {n}" for n in target_panel["notes"]),
            ":::",
        ])

    # Error notes
    if target_panel.get("error_notes"):
        th_lines.extend([
            "",
            f":::caution ข้อผิดพลาดที่อาจเกิด",
            "\n".join(f"- {n}" for n in target_panel["error_notes"]),
            ":::",
        ])

    th_lines.append("")
    en_lines.append("")
    return "\n".join(th_lines), "\n".join(en_lines)


def gen_features_alarms_from_vision(model, vision, page_titles, position, kind):
    """Generate features.md or alarms.md from vision JSON."""
    target_panels = []
    for p in vision.get("pages", []):
        panels = p.get("panels", [])
        for panel in panels:
            if panel.get("panel") in page_titles or any(t in panel.get("panel", "") for t in page_titles):
                target_panels.append(panel)

    if not target_panels:
        # Maybe pages
        for p in vision.get("pages", []):
            if p.get("panel") in page_titles:
                if "panels" in p:
                    target_panels.extend(p["panels"])
                else:
                    target_panels.append(p)

    if not target_panels:
        return None, None

    if kind == "features":
        th_title = f"ฟีเจอร์เพิ่มเติม {model}"
        en_title = f"Additional Features"
        th_h1 = "ฟีเจอร์เพิ่มเติม"
        en_h1 = "Additional Features"
    else:
        th_title = f"สัญญาณเตือนฉุกเฉิน {model}"
        en_title = "Emergency Alarm Features"
        th_h1 = "สัญญาณเตือนฉุกเฉิน"
        en_h1 = "Emergency Alarm Features"

    th_lines = [fm(th_title, f"{en_title} of {model}", position), "", f"# {th_h1}"]
    en_lines = [fm(en_title, f"{en_title} of {model}", position), "", f"# {en_h1}"]

    for i, panel in enumerate(target_panels, 1):
        panel_title = panel.get("panel", "")
        # Use the panel title as section title
        section_th = panel_title
        section_en = panel_title
        th_lines.append(f"## {section_th}")
        en_lines.append(f"## {section_en}")
        th_lines.append("")
        en_lines.append("")

        # Description
        if panel.get("description"):
            th_lines.append(panel["description"])
            en_lines.append(panel["description"])
            th_lines.append("")
            en_lines.append("")

        # Steps
        steps = panel.get("steps", [])
        if steps:
            th_lines.append("**ขั้นตอน:**" if kind == "features" else "**Steps:**")
            en_lines.append("**Steps:**")
            th_lines.append("")
            en_lines.append("")
            for j, step in enumerate(steps, 1):
                th_lines.append(f"{j}. {step}")
                en_lines.append(f"{j}. {step}")
            th_lines.append("")
            en_lines.append("")

        # Notes
        for note_key, label in [("caution", ":::caution"), ("notes", ":::note")]:
            note = panel.get(note_key)
            if note:
                if isinstance(note, list):
                    th_lines.extend([f"{label}", *[f"- {n}" for n in note], ":::", ""])
                    en_lines.extend([f"{label}", *[f"- {n}" for n in note], ":::", ""])
                else:
                    th_lines.extend([f"{label}", note, ":::", ""])
                    en_lines.extend([f"{label}", note, ":::", ""])

        # Additional sub-fields
        for sub_key in ["setting_steps", "cancellation"]:
            if panel.get(sub_key):
                th_lines.append(f"**{sub_key.replace('_', ' ').title()}:**")
                en_lines.append(f"**{sub_key.replace('_', ' ').title()}:**")
                th_lines.append("")
                en_lines.append("")
                for item in panel[sub_key]:
                    th_lines.append(f"- {item}")
                    en_lines.append(f"- {item}")
                th_lines.append("")
                en_lines.append("")

    return "\n".join(th_lines), "\n".join(en_lines)


# =============================================================================
# Main pipeline
# =============================================================================
def find_vision(slug):
    """Find vision JSON file for a model slug."""
    for f in VISION_DIR.glob("Manual_*.json"):
        # Slug like 'es-303g' should match 'Manual_ES-303G' or 'Manual_TRIPLEX 2way'
        basename = f.stem.replace("Manual_", "")
        normalized = "".join(c.lower() for c in basename if c.isalnum())
        slug_normalized = "".join(c.lower() for c in slug if c.isalnum())
        if normalized == slug_normalized:
            return json.load(open(f, encoding="utf-8"))
    return None


def write_pages(slug, pages):
    th_dir = DOCS_TH / slug
    en_dir = DOCS_EN / slug
    th_dir.mkdir(parents=True, exist_ok=True)
    en_dir.mkdir(parents=True, exist_ok=True)

    for page_name, content in pages.items():
        if page_name == "_category":
            (th_dir / "_category_.json").write_text(content["th"], encoding="utf-8")
            (en_dir / "_category_.json").write_text(content["en"], encoding="utf-8")
        elif isinstance(content, dict) and "th" in content and "en" in content:
            (th_dir / f"{page_name}.md").write_text(content["th"], encoding="utf-8")
            (en_dir / f"{page_name}.md").write_text(content["en"], encoding="utf-8")


def build_from_vision(slug, model, th_title, en_title, th_desc, en_desc, vision):
    """Build all pages for a model that has vision extraction."""
    pages = {"_category": {
        "th": category_json(slug, th_title, th_desc),
        "en": category_json(slug, en_title, en_desc),
    }}

    # Intro
    th, en = gen_intro_from_vision(model, slug, vision)
    pages["intro"] = {"th": th, "en": en}

    # Specs
    th, en = gen_specs_from_vision(model, vision)
    pages["specs"] = {"th": th, "en": en}

    # Components
    th, en = gen_components_from_vision(model, slug, vision)
    pages["components"] = {"th": th, "en": en}

    # Programming pages
    pin_pages = ["Pin Number Registration", "Guest Pin Number Registration"]
    th, en = gen_programming_from_vision(model, vision, pin_pages, 4)
    if th and en:
        pages["pin-registration"] = {"th": th, "en": en}
    else:
        # Default template
        th, en = gen_default_pin_registration(model)
        pages["pin-registration"] = {"th": th, "en": en}

    rfid_pages = ["Smart Key Registration (Normal)", "Smart Key Registration (Individual)", "RFID Card Registration (Normal)", "RFID Card Registration (Individual)"]
    th, en = gen_programming_from_vision(model, vision, rfid_pages, 5)
    if th and en:
        pages["rfid-registration"] = {"th": th, "en": en}
    else:
        th, en = gen_default_rfid_registration(model)
        pages["rfid-registration"] = {"th": th, "en": en}

    rfid_del_pages = ["Smart Key Deletion (All-at-once)", "Smart Key Deletion (Individual)", "RFID Card Deletion (All-at-once)", "RFID Card Deletion (Individual)"]
    th, en = gen_programming_from_vision(model, vision, rfid_del_pages, 6)
    if th and en:
        pages["rfid-deletion"] = {"th": th, "en": en}
    else:
        th, en = gen_default_rfid_deletion(model)
        pages["rfid-deletion"] = {"th": th, "en": en}

    # Fingerprint pages (only for models with fingerprint)
    fp_reg_pages = ["Fingerprint Registration (Normal)", "Fingerprint Registration (Individual)"]
    th, en = gen_programming_from_vision(model, vision, fp_reg_pages, 7)
    if th and en:
        pages["fingerprint-registration"] = {"th": th, "en": en}

    fp_del_pages = ["Fingerprint Deletion (All-at-once)", "Fingerprint Deletion (Individual)"]
    th, en = gen_programming_from_vision(model, vision, fp_del_pages, 8)
    if th and en:
        pages["fingerprint-deletion"] = {"th": th, "en": en}

    # Features - find all panels that look like features (NOT programming/alarms)
    feature_keywords = ['setting', 'mode', 'mute', 'volume', 'multi-touch', 'multi_touch',
                       'dual-mode', 'dual_mode', 'random', 'melody', 'home_network',
                       'notification', 'sound', 'voice', 'buzzer', 'auto-manual', 'auto_manual']
    alarm_keywords = ['alarm', 'anti-prank', 'anti_prank', 'fire', 'intrusion', 'anti-hacking',
                     'anti_hacking', 'deadbolt', 'replace', 'emergency', 'jammed', 'low_battery']

    feature_panels = []
    alarm_panels = []
    for p in vision.get('pages', []):
        panels = p.get('panels', [])
        for panel in panels:
            title = panel.get('panel', '').lower()
            if any(k in title for k in alarm_keywords):
                alarm_panels.append(panel)
            elif any(k in title for k in feature_keywords):
                feature_panels.append(panel)

    if feature_panels:
        th_lines = [fm(f'ฟีเจอร์เพิ่มเติม {model}', f'ฟีเจอร์เพิ่มเติมของ {model}', 9), '', f'# ฟีเจอร์เพิ่มเติม']
        en_lines = [fm('Additional Features', f'Additional features of {model}', 9), '', f'# Additional Features']
        for panel in feature_panels:
            th_text, en_text = render_panel_bilingual(panel, kind='features')
            th_lines.append(th_text)
            en_lines.append(en_text)
        pages['features'] = {'th': '\n'.join(th_lines), 'en': '\n'.join(en_lines)}

    if alarm_panels:
        th_lines = [fm(f'สัญญาณเตือนฉุกเฉิน {model}', f'สัญญาณเตือนฉุกเฉินของ {model}', 10), '', f'# สัญญาณเตือนฉุกเฉิน']
        en_lines = [fm('Emergency Alarm Features', f'Emergency alarm features of {model}', 10), '', f'# Emergency Alarm Features']
        for panel in alarm_panels:
            th_text, en_text = render_panel_bilingual(panel, kind='alarms')
            th_lines.append(th_text)
            en_lines.append(en_text)
        pages['alarms'] = {'th': '\n'.join(th_lines), 'en': '\n'.join(en_lines)}

    return pages


def render_panel_bilingual(panel, kind='features'):
    """Render a single panel as bilingual markdown."""
    title = panel.get('panel', 'Untitled')
    # Convert snake_case to Title Case
    title_display = ' '.join(word.capitalize() for word in title.replace('_', ' ').split())

    th_lines = [f'## {title_display}', '']
    en_lines = [f'## {title_display}', '']

    if panel.get('description'):
        th_lines.append(panel['description'])
        en_lines.append(panel['description'])
        th_lines.append('')
        en_lines.append('')

    if panel.get('caution'):
        th_lines.extend([f':::caution ข้อควรระวัง', panel['caution'], ':::', ''])
        en_lines.extend([f':::caution', panel['caution'], ':::', ''])

    if panel.get('note'):
        th_lines.extend([f':::note', panel['note'], ':::', ''])
        en_lines.extend([f':::note', panel['note'], ':::', ''])

    if panel.get('notes') and isinstance(panel['notes'], list):
        th_lines.append('**หมายเหตุ:**')
        en_lines.append('**Notes:**')
        th_lines.append('')
        en_lines.append('')
        for n in panel['notes']:
            th_lines.append(f'- {n}')
            en_lines.append(f'- {n}')
        th_lines.append('')
        en_lines.append('')

    steps = panel.get('steps', [])
    if steps:
        th_lines.append('**ขั้นตอน:**')
        en_lines.append('**Steps:**')
        th_lines.append('')
        en_lines.append('')
        for i, step in enumerate(steps, 1):
            th_lines.append(f'{i}. {step}')
            en_lines.append(f'{i}. {step}')
        th_lines.append('')
        en_lines.append('')

    if panel.get('setting'):
        th_lines.append('**การตั้งค่า:**')
        en_lines.append('**Setting:**')
        th_lines.append('')
        en_lines.append('')
        if isinstance(panel['setting'], list):
            for s in panel['setting']:
                th_lines.append(f'- {s}')
                en_lines.append(f'- {s}')
        else:
            th_lines.append(panel['setting'])
            en_lines.append(panel['setting'])
        th_lines.append('')
        en_lines.append('')

    if panel.get('cancellation'):
        th_lines.append('**การยกเลิก:**')
        en_lines.append('**Cancellation:**')
        th_lines.append('')
        en_lines.append('')
        th_lines.append(panel['cancellation'])
        en_lines.append(panel['cancellation'])
        th_lines.append('')
        en_lines.append('')

    if panel.get('setting_steps'):
        th_lines.append('**ขั้นตอนการตั้งค่า:**')
        en_lines.append('**Setting steps:**')
        th_lines.append('')
        en_lines.append('')
        for i, s in enumerate(panel['setting_steps'], 1):
            th_lines.append(f'{i}. {s}')
            en_lines.append(f'{i}. {s}')
        th_lines.append('')
        en_lines.append('')

    return '\n'.join(th_lines), '\n'.join(en_lines)


def gen_default_pin_registration(model):
    th = f"""---
sidebar_position: 4
title: การลงทะเบียนรหัส PIN
description: วิธีเปลี่ยนรหัส PIN บน {model}
---

# การลงทะเบียนรหัส PIN

:::caution ก่อนเริ่ม
- ลงทะเบียนรหัส PIN **ขณะประตูเปิดเสมอ**
- รหัส PIN เริ่มต้นคือ **`1, 2, 3, 4`** เปลี่ยนก่อนใช้งานครั้งแรก
- รหัส PIN ใหม่จะ **ลบรหัสเก่าทั้งหมด**
:::

## ขั้นตอน
1. เปิดฝาครอบแบตเตอรี่ (ด้านใน) กดปุ่ม **Registration** หนึ่งครั้ง
2. ใส่รหัส PIN ปัจจุบัน แล้วกด `*`
3. กดปุ่มหมายเลขตามที่ระบุในคู่มือ
4. ใส่รหัส PIN ใหม่ 4-12 หลัก แล้วกด `*`
5. ใส่รหัส PIN ใหม่อีกครั้ง แล้วกด `*`
6. ล็อกจะเล่นเพลงยืนยัน
"""
    en = f"""---
sidebar_position: 4
title: PIN Registration
description: How to change your PIN on {model}
---

# PIN Registration

:::caution Before you start
- Always register PIN **while door is open**
- Default PIN is **`1, 2, 3, 4`** — change before first use
- New PIN **deletes all previous PINs**
:::

## Steps
1. Open the battery cover (inside). Press **Registration** once.
2. Enter current PIN, then press `*`.
3. Press the number button indicated in the manual.
4. Enter the new PIN (4-12 digits), then press `*`.
5. Re-enter the new PIN, then press `*`.
6. The lock plays a melody to confirm.
"""
    return th, en


def gen_default_rfid_registration(model):
    th = f"""---
sidebar_position: 5
title: การลงทะเบียนบัตร RFID
description: วิธีลงทะเบียนบัตร RFID บน {model}
---

# การลงทะเบียนบัตร RFID

:::tip ความเข้ากันได้
ใช้ได้เฉพาะบัตร RFID 13.56 MHz ที่เข้ากันได้กับ EPIC
:::

## โหมด A — ทั้งหมด
1. เปิดฝาครอบแบตเตอรี่ กดปุ่ม **Registration**
2. ใส่รหัส PIN แล้วกด `*`
3. กดปุ่มหมายเลขสำหรับ RFID
4. วางบัตรบนเครื่องอ่านทีละใบ
5. กด **Registration** เพื่อเสร็จ
"""
    en = f"""---
sidebar_position: 5
title: RFID Card Registration
description: How to register RFID cards on {model}
---

# RFID Card Registration

:::tip Compatibility
Only 13.56 MHz RFID cards compatible with EPIC work.
:::

## Mode A — All at once
1. Open the battery cover. Press **Registration**.
2. Enter PIN, then press `*`.
3. Press the number button for RFID.
4. Place each card on the reader.
5. Press **Registration** to finish.
"""
    return th, en


def gen_default_rfid_deletion(model):
    th = f"""---
sidebar_position: 6
title: การลบบัตร RFID
description: วิธีลบบัตร RFID บน {model}
---

# การลบบัตร RFID

## ลบทั้งหมด
1. เปิดฝาครอบแบตเตอรี่ กด **Registration**
2. ใส่รหัส PIN แล้วกด `*`
3. กดปุ่มลบ
4. กด `*` ค้าง 5 วินาที — เมื่อได้ยินเพลง บัตรถูกลบ

## ลบทีละใบ
1. ทำตามขั้นตอน 1-3 ข้างต้น
2. ใส่หมายเลขช่อง 3 หลัก แล้วกด `#`
"""
    en = f"""---
sidebar_position: 6
title: RFID Card Deletion
description: How to delete RFID cards on {model}
---

# RFID Card Deletion

## Delete all
1. Open the battery cover. Press **Registration**.
2. Enter PIN, then press `*`.
3. Press the delete button.
4. Hold `*` for 5 seconds — when melody plays, cards are deleted.

## Delete one
1. Follow steps 1-3 above.
2. Enter 3-digit slot, then press `#`.
"""
    return th, en


# =============================================================================
# Run
# =============================================================================
def main():
    print(f"=== v2: Building from vision JSON ===")
    print(f"Vision dir: {VISION_DIR}")

    slugs_with_vision = ["es-303g", "ef-p8800k", "es-m50", "es-p9100fk", "es-t153", "n-touch", "touch", "triplex-2way", "triplex-3way", "es-k70", "ef-8000l", "es-809l"]

    titles = {
        "es-303g": ("กุญแจประตูกระจก ES-303G", "ES-303G Glass Door Lock"),
        "ef-p8800k": ("กุญแจดิจิทัล EF-P8800K", "EF-P8800K Digital Lock"),
        "es-m50": ("กุญแจดิจิทัล ES-M50", "ES-M50 Digital Lock"),
        "es-p9100fk": ("กุญแจดิจิทัล ES-P9100FK", "ES-P9100FK Digital Lock"),
        "es-t153": ("กุญแจดิจิทัล ES-T153", "ES-T153 Digital Lock"),
        "n-touch": ("กุญแจดิจิทัล N-TOUCH", "N-TOUCH Digital Lock"),
        "touch": ("กุญแจดิจิทัล TOUCH", "TOUCH Digital Lock"),
        "triplex-2way": ("กุญแจดิจิทัล TRIPLEX 2way", "TRIPLEX 2way Digital Lock"),
        "triplex-3way": ("กุญแจดิจิทัล TRIPLEX 3way", "TRIPLEX 3way Digital Lock"),
        "es-k70": ("กุญแจดิจิทัล ES-K70", "ES-K70 Digital Lock"),
        "ef-8000l": ("กุญแจดิจิทัล EF-8000L", "EF-8000L Digital Lock"),
        "es-809l": ("กุญแจดิจิทัล ES-809L", "ES-809L Digital Lock"),
    }

    descs = {
        "es-303g": ("กุญแจดิจิทัลสำหรับประตูกระจก", "Digital lock for glass doors"),
        "ef-p8800k": ("กุญแจดิจิทัล Main Type", "Main type digital lock"),
        "es-m50": ("กุญแจดิจิทัล", "Digital lock"),
        "es-p9100fk": ("กุญแจดิจิทัล Main Type", "Main type digital lock"),
        "es-t153": ("กุญแจดิจิทัล", "Digital lock"),
        "n-touch": ("กุญแจดิจิทัล PIN เท่านั้น", "PIN-only digital lock"),
        "touch": ("กุญแจดิจิทัล PIN + Smart Card", "Digital lock with PIN + Smart Card"),
        "triplex-2way": ("กุญแจดิจิทัล", "Digital lock"),
        "triplex-3way": ("กุญแจดิจิทัล", "Digital lock"),
        "es-k70": ("กุญแจดิจิทัล", "Digital lock"),
        "ef-8000l": ("กุญแจดิจิทัล", "Digital lock"),
        "es-809l": ("กุญแจดิจิทัล", "Digital lock"),
    }

    for slug in slugs_with_vision:
        print(f"  → {slug}")
        vision = find_vision(slug)
        if not vision:
            print(f"    ⚠ no vision found for {slug}")
            continue

        th_title, en_title = titles[slug]
        th_desc, en_desc = descs[slug]
        model = slug.upper().replace("-", "-")

        pages = build_from_vision(slug, model, th_title, en_title, th_desc, en_desc, vision)
        write_pages(slug, pages)
        print(f"    ✓ {len(pages)} page groups written")

    print(f"\n=== Done ===")


if __name__ == "__main__":
    main()
