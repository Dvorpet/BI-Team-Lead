// Exports the decks to PDF: node tools/pdf.js  (needs playwright)
const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const deck of ['p1', 'p2']) for (const lang of ['cs', 'en']) {
    await p.goto(`file://${root}/index.html?print=${deck}&lang=${lang}`);
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: `${root}/pdf/${deck}-${lang}.pdf`, width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  }
  await b.close();
})();
