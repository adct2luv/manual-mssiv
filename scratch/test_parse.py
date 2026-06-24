import os
import json
from pathlib import Path

ROOT = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads")
KB = ROOT / "knowledge-base"
extracted_dir = KB / "extracted/vision"

def main():
    print("Files in extracted/vision:")
    for f in sorted(os.listdir(extracted_dir)):
        if f.endswith(".json"):
            print(f"- {f}")
            data = json.load(open(extracted_dir / f))
            print("  Model:", data.get("model"))
            
if __name__ == "__main__":
    main()
