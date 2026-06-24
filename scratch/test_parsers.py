#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

# Add the scripts directory to sys.path so we can import from build_manuals
sys.path.append(str(Path(__file__).parent.parent / "scripts"))

from build_manuals import (
    parse_door_operations_from_json,
    parse_specs_from_json,
    parse_components_from_json,
    NON_HANDLE_MODELS,
    PRODUCT_FEATURES
)

class TestParsers(unittest.TestCase):

    def test_door_operations_fallback_no_handle(self):
        # es-303g is a non-handle, non-key model, with RFID
        slug = "es-303g"
        th_content, en_content = parse_door_operations_from_json(slug, None, None)
        
        # Test English output
        self.assertIn("Opening by PIN Code", en_content)
        self.assertIn("Opening by RFID Card / Key Tag", en_content)
        self.assertNotIn("Opening by Fingerprint", en_content)
        self.assertNotIn("Opening by Mechanical Key", en_content)
        self.assertIn("Opening by Open/Close Button", en_content)
        self.assertIn("Opening by Manual Lock/Unlock Knob", en_content)
        self.assertNotIn("Opening by Handle", en_content)
        
        # Test Thai output
        self.assertIn("เปิดด้วยรหัส PIN", th_content)
        self.assertIn("เปิดด้วยบัตร RFID", th_content)
        self.assertIn("เปิดด้วยปุ่ม Open/Close", th_content)

    def test_door_operations_fallback_with_handle(self):
        # es-k70 is a handle model with RFID and Mechanical Key
        slug = "es-k70"
        th_content, en_content = parse_door_operations_from_json(slug, None, None)
        
        # Test English output
        self.assertIn("Opening by PIN Code", en_content)
        self.assertIn("Opening by RFID Card / Key Tag", en_content)
        self.assertIn("Opening by Mechanical Key", en_content)
        self.assertIn("Opening by Handle", en_content)
        self.assertNotIn("Opening by Open/Close Button", en_content)
        
        # Test Thai output
        self.assertIn("เปิดด้วยรหัส PIN", th_content)
        self.assertIn("เปิดด้วยบัตร RFID", th_content)
        self.assertIn("เปิดด้วยกุญแจกลไก", th_content)
        self.assertIn("เปิดด้วยมือจับ", th_content)

    def test_door_operations_no_duplicate_procedure(self):
        # Construct mock vision data with a procedure but no steps
        mock_data = {
            "pages": [
                {
                    "page_number": 1,
                    "panels": [
                        {
                            "panel": "open_outside",
                            "title": "Opening Door Outside",
                            "methods": [
                                {
                                    "name": "Opening with Random Number Feature",
                                    "procedure": "(Before) Enter any random number + Enter Pin number + [✱] button. (After) Enter Pin number + Enter any random number + [✱] button. Either way, when the melody is heard, the door open.",
                                    "description": "Use this function to prevent password exposure."
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        # By setting granular fallback, the other operations will fallback, but open_outside will use this mock panel
        th_content, en_content = parse_door_operations_from_json("es-303g", mock_data, "vision")
        
        # In the English content, verify that procedure string is not duplicated.
        # It should appear only once (either as step 1 or as procedure text)
        self.assertEqual(en_content.count("Either way, when the melody is heard, the door open."), 1)
        self.assertEqual(th_content.count("ไม่ว่าจะวิธีใด เมื่อเสียงเพลงเมโลดี้ดังขึ้น ประตูจะเปิดออก"), 1)

    def test_granular_fallback(self):
        # Construct mock vision data where ONLY open_outside is parsed from JSON, other operations are missing
        mock_data = {
            "pages": [
                {
                    "page_number": 1,
                    "panels": [
                        {
                            "panel": "open_outside",
                            "title": "Opening Door Outside",
                            "methods": [
                                {
                                    "name": "Custom Method",
                                    "steps": ["Step 1 from JSON"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        th_content, en_content = parse_door_operations_from_json("es-303g", mock_data, "vision")
        
        # Custom Method from JSON should be present
        self.assertIn("Custom Method", en_content)
        self.assertIn("Step 1 from JSON", en_content)
        
        # Other operations (close_outside, open_inside, close_inside) should still have their fallback content
        self.assertIn("Automatic Lock Mode", en_content)
        self.assertIn("Opening by Open/Close Button", en_content)

    def test_specs_override_es_303g(self):
        # Test that specs parsing handles the ES-303G glass door thickness override correctly
        mock_data = {
            "th": {
                "specs": {
                    "door_thickness": "40~50mm",
                    "power": "DC 6V",
                    "max_user_codes": "Up to 30",
                    "max_cards": "Up to 100"
                }
            },
            "en": {
                "specs": {
                    "door_thickness": "40~50mm",
                    "power": "DC 6V",
                    "max_user_codes": "Up to 30",
                    "max_cards": "Up to 100"
                }
            }
        }
        specs_th, specs_en = parse_specs_from_json("es-303g", mock_data, "product")
        
        # Verify thickness is overridden
        thick_en = next(item for item in specs_en if item[0] == "Door Thickness")
        thick_th = next(item for item in specs_th if item[0] == "ความหนาประตูที่รองรับ")
        self.assertEqual(thick_en[1], "12mm tempered glass only")
        self.assertEqual(thick_th[1], "กระจกนิรภัยเทมเปอร์หนา 12 มม. เท่านั้น")
        
        # Verify Product Type is overridden
        type_en = next(item for item in specs_en if item[0] == "Product Type")
        type_th = next(item for item in specs_th if item[0] == "ประเภทผลิตภัณฑ์")
        self.assertEqual(type_en[1], "Non-key")
        self.assertEqual(type_th[1], "ไม่มีกุญแจกลไก")

    def test_components_non_handle_and_non_key(self):
        # es-303g has no handles and no mechanical key
        mock_data = {
            "pages": [
                {
                    "page_number": 1,
                    "panels": [
                        {
                            "panel": "outer_body",
                            "outer_body_parts": [
                                "Lever handle",
                                "Mechanical key"
                            ]
                        },
                        {
                            "panel": "in_box",
                            "in_box": [
                                "Mechanical Key 2EA",
                                "RFID Card 2EA"
                            ]
                        }
                    ]
                }
            ]
        }
        outer_parts, inner_parts, in_box = parse_components_from_json("es-303g", mock_data, "vision")
        
        # Handles and keys should be completely stripped
        for name, func in outer_parts:
            self.assertNotIn("handle", name.lower())
            self.assertNotIn("mechanical key", name.lower())
            
        for item in in_box:
            self.assertNotIn("handle", item.lower())
            self.assertNotIn("mechanical key", item.lower())
                
        # RFID Card should be present
        self.assertTrue(any("rfid" in item.lower() for item in in_box))

if __name__ == "__main__":
    unittest.main()
