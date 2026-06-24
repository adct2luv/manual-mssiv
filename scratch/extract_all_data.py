import os
import json
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def check_specs(data):
    specs = {}
    for page in data.get("pages", []):
        for panel in page.get("panels", []):
            if "dimension" in panel.get("panel", "").lower() or "spec" in panel.get("panel", "").lower():
                # check for table
                if "table" in panel:
                    specs[panel.get("panel")] = panel["table"]
                elif "product_dimension" in panel and "table" in panel["product_dimension"]:
                    specs[panel.get("panel")] = panel["product_dimension"]["table"]
                else:
                    # just print keys
                    specs[panel.get("panel")] = list(panel.keys())
    return specs

def check_components(data):
    components = {}
    for page in data.get("pages", []):
        for panel in page.get("panels", []):
            if "component" in panel.get("panel", "").lower() or "parts" in panel.get("panel", "").lower():
                components[panel.get("panel")] = {k: v for k, v in panel.items() if k not in ["panel", "title"]}
    return components

def main():
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            print("==================================================")
            print("File:", f)
            data = json.load(open(extracted_dir / f))
            print("Specs found:")
            specs = check_specs(data)
            for k, v in specs.items():
                print(f"  Panel {k}:")
                if isinstance(v, list):
                    for row in v[:4]:
                        print(f"    {row}")
                    if len(v) > 4:
                        print("    ...")
                else:
                    print(f"    {v}")
            
            print("Components found:")
            components = check_components(data)
            for k, v in components.items():
                print(f"  Panel {k}:")
                print(f"    Keys: {list(v.keys())}")
                if "in_box" in v:
                    print(f"    in_box: {v['in_box']}")
                if "outer_body" in v:
                    print(f"    outer_body: {v['outer_body'][:3]} ...")
                if "inner_body" in v:
                    print(f"    inner_body: {v['inner_body'][:3]} ...")

if __name__ == "__main__":
    main()
