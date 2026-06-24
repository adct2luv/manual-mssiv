import os
import json
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def get_components_from_tier_c(data):
    outer = []
    inner = []
    in_box = []
    
    for page in data.get("pages", []):
        panels = page.get("panels", [])
        if not panels:
            panels = [page]
            
        for p in panels:
            panel_name = (p.get("panel") or p.get("title") or "").lower()
            
            # Check direct keys
            if "outer_body_parts" in p and isinstance(p["outer_body_parts"], list):
                for part in p["outer_body_parts"]:
                    outer.append((part, ""))
            if "inner_body_parts" in p and isinstance(p["inner_body_parts"], list):
                for part in p["inner_body_parts"]:
                    inner.append((part, ""))
            if "outer_body" in p and isinstance(p["outer_body"], list):
                for part in p["outer_body"]:
                    outer.append((part, ""))
            if "inner_body" in p and isinstance(p["inner_body"], list):
                for part in p["inner_body"]:
                    inner.append((part, ""))
                    
            # check parts
            if "parts" in p:
                parts_list = p["parts"]
                is_outer = "out" in p.get("panel", "").lower() or "out" in p.get("title", "").lower()
                is_inner = "in" in p.get("panel", "").lower() or "in" in p.get("title", "").lower()
                
                # Special cases
                if "outer_body_parts" in panel_name or "outbody" in panel_name:
                    is_outer = True
                    is_inner = False
                elif "inner_body_parts" in panel_name or "inbody" in panel_name or "inner_body_pin" in panel_name:
                    is_inner = True
                    is_outer = False
                    
                for part in parts_list:
                    if isinstance(part, dict):
                        name = part.get("name", "")
                        func = part.get("function", "")
                        if not name and "part" in part:
                            name = part["part"]
                    else:
                        name = part
                        func = ""
                    if is_outer:
                        outer.append((name, func))
                    elif is_inner:
                        inner.append((name, func))
            
            # check components in-box
            if "in_box" in p and isinstance(p["in_box"], list):
                in_box.extend(p["in_box"])
            if "product_components" in p and isinstance(p["product_components"], list):
                in_box.extend(p["product_components"])
            if "components" in p:
                comp_data = p["components"]
                if isinstance(comp_data, list):
                    in_box.extend(comp_data)
                elif isinstance(comp_data, str):
                    in_box.append(comp_data)
                elif isinstance(comp_data, dict):
                    if "in_box" in comp_data:
                        in_box.extend(comp_data["in_box"])
                    if "outer_body" in comp_data:
                        for part in comp_data["outer_body"]:
                            outer.append((part, ""))
                    if "inner_body" in comp_data:
                        for part in comp_data["inner_body"]:
                            inner.append((part, ""))
                
    # Remove duplicates preserving order
    seen_outer = set()
    unique_outer = []
    for name, func in outer:
        if not name:
            continue
        if name.lower() not in seen_outer:
            seen_outer.add(name.lower())
            unique_outer.append((name, func))
            
    seen_inner = set()
    unique_inner = []
    for name, func in inner:
        if not name:
            continue
        if name.lower() not in seen_inner:
            seen_inner.add(name.lower())
            unique_inner.append((name, func))
            
    seen_box = set()
    unique_box = []
    for item in in_box:
        if not item:
            continue
        if item.lower() not in seen_box:
            seen_box.add(item.lower())
            unique_box.append(item)
            
    return unique_outer, unique_inner, unique_box

def main():
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            print("==================================================")
            print("File:", f)
            data = json.load(open(extracted_dir / f))
            outer, inner, box = get_components_from_tier_c(data)
            print(f"  Outer parts: {[o[0] for o in outer]}")
            print(f"  Inner parts: {[i[0] for i in inner]}")
            print(f"  In-box items: {box}")

if __name__ == "__main__":
    main()
