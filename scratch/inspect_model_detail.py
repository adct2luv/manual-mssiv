import os
import json
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def main():
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            print("==================================================")
            print("File:", f)
            data = json.load(open(extracted_dir / f))
            for page in data.get("pages", []):
                p_num = page.get("page")
                # EF-8000L and ES-809L have flat page objects containing panels
                # others have panels list
                panels = page.get("panels", [])
                if panels:
                    for p in panels:
                        print(f"  Page {p_num} Panel {p.get('panel') or p.get('title')}: keys={list(p.keys())}")
                        if "title" in p:
                            print(f"    title: {p['title']}")
                else:
                    # Flat page
                    print(f"  Page {p_num} Panel {page.get('panel') or page.get('title') or 'Flat'}: keys={list(page.keys())}")
                    if "title" in page:
                        print(f"    title: {page['title']}")

if __name__ == "__main__":
    main()
