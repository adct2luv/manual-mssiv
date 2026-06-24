import os
import json
import re
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def parse_specs_from_json(data):
    table = None
    for page in data.get("pages", []):
        panels = page.get("panels", [])
        if not panels:
            panels = [page]
        for p in panels:
            # Check for dimensions or specs
            panel_name = (p.get("panel") or "").lower()
            if "dimension" in panel_name or "spec" in panel_name or "specs" in panel_name:
                if "table" in p:
                    table = p["table"]
                    break
                elif "product_dimension" in p and isinstance(p["product_dimension"], dict) and "table" in p["product_dimension"]:
                    table = p["product_dimension"]["table"]
                    break
                elif "specs" in p and isinstance(p["specs"], dict) and "table" in p["specs"]:
                    table = p["specs"]["table"]
                    break
        if table:
            break
            
    if not table:
        return None
        
    specs_list = []
    for row in table:
        if not row:
            continue
        # Check if it is a header row
        if row[0] in ["Item", "Items", "Spec", "Item Name", "Description"]:
            continue
        if len(row) == 3:
            label = row[1]
            val = row[2]
            if "tempered glass door" in row[1]:
                label = "Installation"
                val = f"Tempered glass door ({row[2]})"
        elif len(row) == 2:
            label = row[0]
            val = row[1]
        else:
            label = row[0]
            val = ", ".join(row[1:])
            
        # Clean label & val
        label = label.strip()
        val = val.strip()
        if label or val:
            specs_list.append((label, val))
            
    return specs_list

def main():
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            print("==================================================")
            print("File:", f)
            data = json.load(open(extracted_dir / f))
            specs = parse_specs_from_json(data)
            if specs:
                for label, val in specs:
                    print(f"  {label} -> {val}")
            else:
                print("  No specs table found!")

if __name__ == "__main__":
    main()
