import os
import json
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def main():
    outer_parts = set()
    inner_parts = set()
    in_box_items = set()
    
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            data = json.load(open(extracted_dir / f))
            for page in data.get("pages", []):
                panels = page.get("panels", [])
                if not panels:
                    panels = [page]
                for p in panels:
                    # check for components panel
                    if p.get("panel") == "components":
                        if "outer_body" in p:
                            outer_parts.update(p["outer_body"])
                        if "inner_body" in p:
                            inner_parts.update(p["inner_body"])
                        if "in_box" in p:
                            in_box_items.update(p["in_box"])
                    
                    # check for outer_body_parts, inner_body_parts panels
                    if p.get("panel") == "outer_body_parts" and "parts" in p:
                        outer_parts.update(p["parts"])
                    if p.get("panel") == "inner_body_parts" and "parts" in p:
                        inner_parts.update(p["parts"])
                        
                    # check for parts list
                    if "parts" in p and isinstance(p["parts"], list):
                        for part in p["parts"]:
                            if isinstance(part, dict):
                                name = part.get("name")
                                func = part.get("function")
                                if "outbody" in p.get("panel", "").lower():
                                    outer_parts.add((name, func))
                                else:
                                    inner_parts.add((name, func))
                            else:
                                if "outbody" in p.get("panel", "").lower():
                                    outer_parts.add(part)
                                else:
                                    inner_parts.add(part)
                                    
                    # check for product_components list
                    if "product_components" in p:
                        in_box_items.update(p["product_components"])

    print("Outer parts count:", len(outer_parts))
    for p in sorted(list(outer_parts), key=lambda x: str(x)):
        print("  -", p)
    print("\nInner parts count:", len(inner_parts))
    for p in sorted(list(inner_parts), key=lambda x: str(x)):
        print("  -", p)
    print("\nIn-box items count:", len(in_box_items))
    for p in sorted(list(in_box_items)):
        print("  -", p)

if __name__ == "__main__":
    main()
