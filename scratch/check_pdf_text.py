import os
from pathlib import Path
from pypdf import PdfReader

manual_dir = Path("/Users/mash/Documents/AntiGravity Playground/FB-Ads/Manual")

print(f"{'PDF File':<50} | {'Pages':<5} | {'Text Length':<10}")
print("-" * 75)

for f in sorted(manual_dir.glob("*.pdf")):
    try:
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t
        print(f"{f.name:<50} | {len(reader.pages):<5} | {len(text):<10}")
    except Exception as e:
        print(f"{f.name:<50} | Error: {e}")
