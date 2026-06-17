# EPIC Manuals — manual.mssiv.com

Docusaurus site hosting EPIC door-lock manuals online.

- **ES-K70** is transcribed page-by-page into web pages (sidebar nav, search-friendly, mobile-friendly).
- The other **21 manuals** are listed at `/catalog` as PDF download cards.
- All PDFs are unmodified copies of the documents published at <https://www.epic.co.kr/home/manual/>.

## Local development

```bash
nvm use            # uses Node 24 from .nvmrc
npm install
npm start          # http://localhost:3000
npm run build      # → ./build
```

## Deploy

This repo is set up for **Cloudflare Pages** via the GitHub integration:

1. Cloudflare dashboard → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
2. Select this repo (`adct2luv/manual-mssiv`).
3. Build settings:
   - **Framework preset:** Docusaurus
   - **Build command:** `npm run build`
   - **Build output directory:** `build`
   - **Node version:** `24` (set via `.nvmrc`)
4. After first deploy succeeds → **Custom domains** → **Set up a custom domain** → `manual.mssiv.com`

Subsequent pushes to `main` auto-deploy.

## Project layout

```
docs/es-k70/             # ES-K70 online manual (intro, safety, specs, components,
                         #   pin-registration, rfid-registration, rfid-deletion)
src/pages/
  index.tsx              # homepage
  catalog.tsx            # /catalog — all 22 manuals
static/
  img/                   # EPIC logo SVGs
  manuals/               # 22 PDFs from epic.co.kr
docusaurus.config.ts
sidebars.ts
```

## Source attribution

PDFs and original document content © EPIC Systems (<info@epic.co.kr>).
Downloaded from <https://www.epic.co.kr/home/manual/> on 2026-06-16.
This site is a community-built online mirror for easier reading and searching.
