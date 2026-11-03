# BI Team Lead – case study

**Web:** https://dvorpet.github.io/BI-Team-Lead/

My solution of a two-part case study for a BI Team Lead interview:

1. **Presentation 1 – Group BI project:** how I would lead the BI implementation for a group of 25 entities (Microsoft Fabric data layer, one semantic model, reporting products, roadmap, compliance, AI, team).
2. **Presentation 2 – Supplier invoice analysis:** data quality, key metrics, alternative calculations, users, missing data and working-capital recommendations for Company AB.
3. **Data:** aggregated results of the analysis.

The page switches between Czech and English and between light and dark mode. Each presentation can be paged through, shown full-screen (▶ / F, arrow keys) and downloaded as PDF in both languages.

## Contents

| Path | What it is |
|---|---|
| `index.html` | The whole web page (generated) |
| `pdf/` | Presentations as PDF: `p1-cs`, `p1-en`, `p2-cs`, `p2-en` |
| `data/analysis-summary.xlsx` | Aggregated results (no row-level data) |
| `tools/` | Source: `content.py` (bilingual slide content), `build.py`, `style.css`, `app.js`, `pdf.js` |
| `assets/fonts/` | IBM Plex Sans, Space Grotesk (SIL Open Font License) |

Rebuild: `python3 tools/build.py`, then `node tools/pdf.js` (requires Playwright).

## Note

The original case-study brief and the row-level invoice data were provided for the interview and are **not** published here. This is a personal solution, not an official Škoda Group website, and it is not affiliated with Škoda Group. No logos are used.

---

*Řešení případové studie k pohovoru na pozici BI Team Lead. Web je česky i anglicky; původní zadání ani řádková data nejsou zveřejněna. Nejde o oficiální stránku Škoda Group.*
