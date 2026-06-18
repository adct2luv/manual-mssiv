import sys
from pathlib import Path

# Add the project root directory to sys.path so we can import from scripts
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from scripts.build_manuals import load_source_json, MANUALS

def test_load_all():
    print("Starting automated verification test for load_source_json...")
    success = True
    for entry in MANUALS:
        slug = entry[0]
        model = entry[1]
        print(f"Testing slug: {slug} ({model})")
        data, src_type = load_source_json(slug)
        if data is None or src_type is None:
            print(f"❌ Failed to load source JSON for slug '{slug}'")
            success = False
            continue
            
        if not isinstance(data, dict):
            print(f"❌ Loaded data for slug '{slug}' is of type {type(data)}, expected dict")
            success = False
            continue
            
        if len(data) == 0:
            print(f"❌ Loaded dictionary for slug '{slug}' is empty")
            success = False
            continue
            
        print(f"✅ Loaded successfully. Type: {src_type}, keys: {len(data)}")
        
    if success:
        print("\n🎉 All manuals verified successfully!")
        sys.exit(0)
    else:
        print("\n❌ One or more manuals failed verification!")
        sys.exit(1)

if __name__ == "__main__":
    test_load_all()
