# Findings & Decisions: Compare Manual and Wiki Content

## Requirements
- Check `/Users/mash/Documents/AntiGravity Playground/FB-Ads/Manual` and compare its content with the Docusaurus wiki (`/Users/mash/Documents/AntiGravity Playground/FB-Ads/manual-site`).
- Identify what content is missing from the wiki.
- Add the missing content to the wiki to make it complete.
- Follow a structured workflow:
  1. Make a checklist/list first.
  2. Implement/add the missing content step-by-step.
  3. Perform a verification check after completion.
  4. If gaps are found, add the missing content.
  5. Check one more time to confirm completeness, then stop.

## Research Findings
- The source `Manual` folder contains 22 PDF files.
- The wiki `docs/` and `i18n/` directories contain 28 manuals/guides, including 10 models that are generated from `Consolidated-Manual-Rev.09.pdf`.
- The 4 reference guides (`Assembly Guide for Key Tail.pdf`, `IR Sensor Usage Guide for Face ID.pdf`, `Outer Body Cable Management Guide.pdf`, `Remote-Control-Module-Compatibility-Guide.pdf`) were deleted from the wiki in commit `8f3653537e647be4d4285febed2bd911d30b4f5b` because they had "thin content".
- The 4 reference guides exist in the `Manual` directory and are part of the original manuals set, so deleting them entirely might violate the requirement to have all source Manual contents represented on the wiki.
- The actual content of the 4 reference guides needs to be extracted from their PDFs and added back to the wiki as complete pages rather than thin stubs.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Restore the 4 reference guides | The user asked to compare `/Users/mash/Documents/AntiGravity Playground/FB-Ads/Manual` (which includes these 4 files) and add any missing information. Deleting them created a gap. |
| Extract PDF contents using a python script | We need to read the text in these 4 PDF files to populate them with high-quality content instead of empty stubs. |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
|       |            |

## Resources
- Source Manual directory: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/Manual`
- Wiki docs directory: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/manual-site/docs`
- Wiki English translations: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/manual-site/i18n/en/docusaurus-plugin-content-docs/current`
- Extraction json output directory: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/knowledge-base/extracted/vision/`
- Build manuals script: `/Users/mash/Documents/AntiGravity Playground/FB-Ads/manual-site/scripts/build_manuals.py`

## Visual/Browser Findings
- None yet.
