# -*- coding: utf-8 -*-
"""Builds index.html (GitHub Pages) from tools/content.py. Run: python3 tools/build.py"""
import os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import DECKS, T, BARS, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slide_html(deck, i, s):
    kind = s.get('kind', '')
    extra = '<div class="cover-bar"></div>' if kind == 'cover' else ''
    return (f'<div class="slide {kind}" data-deck="{deck}" data-i="{i}" role="group" aria-roledescription="slide">'
            f'{extra}<div class="si">{s["html"]}</div></div>')

def notes_html(deck, i, s):
    return f'<div class="note" data-deck="{deck}" data-i="{i}">{s["notes"]}</div>'

DECK_META = {
 'p1': dict(tab=T('Presentation 1', 'Prezentace 1'),
            h=T('Part 1 · Group BI project', 'Část 1 · Projekt BI pro skupinu'),
            d=T('How I would lead the BI implementation for a group of 25 entities: one shared data layer in Microsoft Fabric, one semantic model, reporting products for every project objective.',
                'Jak bych vedl zavedení BI ve skupině 25 společností: jedna sdílená datová vrstva v Microsoft Fabric, jeden sémantický model a reportingové produkty pro každý cíl projektu.')),
 'p2': dict(tab=T('Presentation 2', 'Prezentace 2'),
            h=T('Part 2 · Supplier invoice analysis', 'Část 2 · Analýza faktur dodavatelů'),
            d=T('Data quality, business value and answers to the six questions about Company AB’s supplier invoices.',
                'Kvalita dat, přínos pro firmu a odpovědi na šest otázek k fakturám dodavatelů společnosti Company AB.')),
}

def deck_panel(deck):
    m = DECK_META[deck]; slides = DECKS[deck]
    toc = ''.join(f'<li><button class="toc-btn" data-deck="{deck}" data-i="{i}"><span class="toc-n">{i+1:02d}</span>{s["title"]}</button></li>' for i, s in enumerate(slides))
    return f'''
<section class="panel" id="panel-{deck}" data-panel="{deck}" hidden>
 <div class="panel-head">
  <div><h1 class="panel-title">{m['h']}</h1><p class="panel-desc">{m['d']}</p></div>
  <div class="dl">
   <a class="btn ghost" href="pdf/{deck}-cs.pdf" download>PDF · CZ</a>
   <a class="btn ghost" href="pdf/{deck}-en.pdf" download>PDF · EN</a>
  </div>
 </div>
 <div class="toolbar">
  <button class="btn icon prev" data-deck="{deck}" aria-label="Previous">←</button>
  <span class="counter" data-deck="{deck}">1 / {len(slides)}</span>
  <button class="btn icon next" data-deck="{deck}" aria-label="Next">→</button>
  <span class="sp"></span>
  <button class="btn ghost notes-toggle" data-deck="{deck}" aria-pressed="false">{T('Speaker notes', 'Poznámky')}</button>
  <button class="btn primary present" data-deck="{deck}">▶ {T('Present', 'Prezentovat')}</button>
 </div>
 <div class="stage" data-deck="{deck}" tabindex="0">
  {''.join(slide_html(deck, i, s) for i, s in enumerate(slides))}
  <div class="fs-hint">{T('← → to move · Esc to exit', '← → pro listování · Esc pro ukončení')}</div>
 </div>
 <div class="notes" data-deck="{deck}" hidden>{''.join(notes_html(deck, i, s) for i, s in enumerate(slides))}</div>
 <ol class="toc">{toc}</ol>
</section>'''

def kpi(v, l):
    return f'<div class="kpi"><p class="kpi-v">{v}</p><p class="kpi-l">{l}</p></div>'

DQ = [
 (T('Rows shifted one column to the right (rows 3274–3331)', 'Řádky posunuté o sloupec doprava (řádky 3274–3331)'), '58', T('2.76 m', '2,76 mil.'), T('Supplier, dates and amounts in wrong columns', 'Dodavatel, data a částky ve špatných sloupcích')),
 (T('Amounts stored as text (’16630,75)', 'Částky uložené jako text (’16630,75)'), '216', T('12.26 m', '12,26 mil.'), T('Ignored by SUM and pivot tables', 'SUM a kontingenční tabulky je ignorují')),
 (T('Invoice number empty in every row', 'Číslo faktury chybí ve všech řádcích'), T('3,349', '3 349'), '—', T('No unique key, duplicates cannot be proven', 'Chybí jedinečný klíč, duplicity nelze prokázat')),
 (T('#N/A instead of supplier ID (rows 103–107)', '#N/A místo ID dodavatele (řádky 103–107)'), '5', T('0.12 m', '0,12 mil.'), T('Spend cannot be attributed; broken lookup', 'Výdaje nelze přiřadit; rozbitý VLOOKUP')),
 (T('Fully identical rows, both paid (3274, 3275)', 'Zcela totožné řádky, oba zaplacené (3274, 3275)'), '2', T('16.6 k', '16,6 tis.'), T('Likely double payment', 'Pravděpodobná dvojí platba')),
 (T('Due date differs from issue date + terms', 'Splatnost neodpovídá datu vystavení + lhůtě'), T('1,782', '1 782'), T('101.4 m', '101,4 mil.'), T('1,586 earlier than the contract allows, 196 later', '1 586 dřív, než dovoluje smlouva, 196 později')),
 (T('Order terms differ from supplier master data', 'Splatnost na objednávce se liší od kmenových dat'), '135', T('10.2 m', '10,2 mil.'), T('Negotiated terms overridden', 'Vyjednané podmínky přepsané')),
 (T('“Matched” flag without an order number', 'Příznak „Matched“ bez čísla objednávky'), '352', T('19.8 m', '19,8 mil.'), T('Spend without orders is 56 % or 70 %', 'Výdaje bez objednávky 56 % nebo 70 %')),
 (T('Non-standard VAT rates (10 %, 15 %, 17–20 %)', 'Nestandardní sazby DPH (10 %, 15 %, 17–20 %)'), '22', T('5.95 m', '5,95 mil.'), T('VAT risk; 10 % and 15 % abolished in CZ in 2024', 'Daňové riziko; 10 % a 15 % v ČR od 2024 neplatí')),
 (T('Duplicate candidates (same supplier, date, amount)', 'Kandidáti na duplicitu (stejný dodavatel, datum, částka)'), '72', T('1.07 m', '1,07 mil.'), T('To verify with accounts payable', 'K ověření s účtárnou')),
 (T('Open credit notes without due date', 'Otevřené dobropisy bez splatnosti'), '5', T('−10.2 m', '−10,2 mil.'), T('Supplier 235: net credit of 3.3 m in our favour', 'Dodavatel 235: čistý kredit 3,3 mil. v náš prospěch')),
 (T('Unpaid invoices with zero balance', 'Nezaplacené faktury s nulovým zůstatkem'), '45', '—', T('Settled by credit notes; clearing not visible', 'Vyrovnáno dobropisy; zúčtování není vidět')),
 (T('“Extra Days” always 0', '„Extra Days“ vždy 0'), T('3,349', '3 349'), '—', T('Redundant column', 'Nadbytečný sloupec')),
]

def data_panel():
    kpis = ''.join([
        kpi(T('3,349', '3 349'), T('documents (47 credit notes)', 'dokladů (47 dobropisů)')),
        kpi('362', T('suppliers', 'dodavatelů')),
        kpi(T('148.7 m', '148,7 mil.'), T('gross spend, Jan–Aug 2024', 'výdaje brutto, leden–srpen 2024')),
        kpi('59 %', T('spend with top 10 suppliers', 'výdajů u 10 největších dodavatelů')),
        kpi(T('30.0 d', '30,0 dne'), T('contractual payment terms', 'smluvní splatnost')),
        kpi(T('24.9 d', '24,9 dne'), T('actual days to pay', 'skutečná doba úhrady')),
        kpi('91 %', T('invoices paid before due date', 'faktur zaplaceno před splatností')),
        kpi('86 %', T('payment value leaving on Tuesday', 'hodnoty plateb odchází v úterý')),
    ])
    dq = table([T('Issue', 'Problém'), T('Rows', 'Řádky'), T('Value', 'Hodnota'), T('Impact', 'Dopad')],
               [list(r) for r in DQ], [38, 10, 12, 40], right=(1, 2))
    proof = table([T('Check after shifting the 58 rows back', 'Kontrola po posunutí 58 řádků zpět'), T('Passed', 'Splněno')],
        [[T('Supplier ID is a whole number 339–353', 'ID dodavatele je celé číslo 339–353'), '58 / 58'],
         [T('Issue date is a valid date', 'Datum vystavení je platné datum'), '58 / 58'],
         [T('“Matched” is 1 or 2 and “Extra Days” is 0', '„Matched“ je 1 nebo 2 a „Extra Days“ je 0'), '58 / 58'],
         [T('Gross = net + VAT', 'Brutto = netto + DPH'), '58 / 58'],
         [T('Payment not before issue date', 'Platba není dřív než vystavení'), '58 / 58']], [80, 20], right=(1,))
    mx = max(v for _, v, _ in BARS)
    bars = ''.join(f'<div class="bc"><p class="bv">{v}</p><div class="bar {c}" style="height:{max(0.5, v / mx * 18.2):.2f}cqw"></div><p class="bl">{l}</p></div>' for l, v, c in BARS)
    levers = table([T('Lever', 'Opatření'), T('Cash, one-off', 'Hotovost jednorázově')],
        [[T('Pay on the due date, not before', 'Platit v den splatnosti, ne dřív'), T('1.6 m', '1,6 mil.')],
         [T('Calculate due dates from contract terms', 'Počítat splatnost podle smluvních podmínek'), T('2.3 m', '2,3 mil.')],
         [T('Agree 45-day terms with the top 10 suppliers', 'Dohodnout 45denní splatnost s 10 největšími dodavateli'), T('5.5 m', '5,5 mil.')],
         [T('Recover the credit from supplier 235', 'Získat zpět kredit od dodavatele 235'), T('3.3 m', '3,3 mil.')],
         ['TOTAL', f"<b>{T('Total', 'Celkem')}</b>", f"<b>{T('12.7 m', '12,7 mil.')}</b>"]], [74, 26], right=(1,))
    return f'''
<section class="panel" id="panel-data" data-panel="data" hidden>
 <div class="panel-head">
  <div><h1 class="panel-title">{T('Data and analysis', 'Data a analýza')}</h1>
  <p class="panel-desc">{T('Supplier invoices of Company AB, January–August 2024, amounts in local currency (not stated in the data). The row-level data were provided for the interview and are not published here; this page shows the aggregated results behind Presentation 2.',
     'Faktury dodavatelů společnosti Company AB za leden–srpen 2024, částky v místní měně (v datech neuvedené). Řádková data byla poskytnuta k pohovoru a nejsou zde zveřejněna; stránka ukazuje agregované výsledky, ze kterých vychází Prezentace 2.')}</p></div>
  <div class="dl"><a class="btn primary" href="data/analysis-summary.xlsx" download>{T('Summary (Excel)', 'Souhrn (Excel)')}</a></div>
 </div>

 <div class="card"><h2 class="card-h">{T('Key metrics', 'Klíčové metriky')}</h2><div class="kpis">{kpis}</div>
 <p class="small">{T('Day figures are weighted by invoice value; the simple average is 26.3 days.', 'Dny jsou vážené hodnotou faktury; prostý průměr je 26,3 dne.')}</p></div>

 <div class="card"><h2 class="card-h">{T('How the data was checked', 'Jak byla data ověřena')}</h2>
 <p class="txt">{T('Every column was profiled for type, range and blanks, then the business rules were reconciled. The key finding: rows 3274–3331 are not corrupt but shifted one column to the right – the supplier ID sits in “Invoice Number” and the balance in an unnamed column P. Shifted back, they pass every check, so they were repaired, not excluded (2.76 m of spend).',
   'Každý sloupec byl prověřen na typ, rozsah a prázdné hodnoty a poté byla odsouhlasena obchodní pravidla. Hlavní zjištění: řádky 3274–3331 nejsou poškozené, ale posunuté o sloupec doprava – ID dodavatele je ve sloupci „Invoice Number“ a zůstatek v nepojmenovaném sloupci P. Po posunutí zpět projdou všemi kontrolami, proto byly opraveny, ne vyřazeny (2,76 mil. výdajů).')}</p>
 <div class="tbl">{proof}</div></div>

 <div class="card"><h2 class="card-h">{T('Data-quality issues', 'Problémy v kvalitě dat')}</h2><div class="tbl">{dq}</div>
 <p class="small">{T('Candidates to verify with accounts payable before any correction.', 'Kandidáti k ověření s účtárnou před jakoukoli opravou.')}</p></div>

 <div class="card"><h2 class="card-h">{T('Payment timing', 'Načasování plateb')}</h2>
 <p class="txt">{T('Number of paid invoices by days before (−) or after (+) the due date. A weekly Tuesday payment run pays everything due before the next run, so most invoices leave 1–6 days early (2.9 days on average).',
   'Počet zaplacených faktur podle dnů před (−) nebo po (+) splatnosti. Týdenní úterní platební běh zaplatí vše, co je splatné do dalšího běhu, takže většina faktur odchází o 1–6 dní dřív (v průměru o 2,9 dne).')}</p>
 <div class="chart-wrap"><div class="chart">{bars}</div></div></div>

 <div class="card"><h2 class="card-h">{T('Working capital levers', 'Opatření pro pracovní kapitál')}</h2><div class="tbl">{levers}</div>
 <p class="small">{T('Method: Σ(invoice value × days gained) ÷ 244 days in the period. Assumptions: 45-day target terms for the top 10 suppliers; 6 % cost of capital gives about 0.6 m of interest a year. Check early-payment discounts first.',
   'Metoda: Σ(hodnota faktury × získané dny) ÷ 244 dní období. Předpoklady: cílová splatnost 45 dní u 10 největších dodavatelů; při nákladech kapitálu 6 % to dává asi 0,6 mil. úroků ročně. Nejdřív je třeba prověřit skonta.')}</p></div>
</section>'''

CSS = open(os.path.join(os.path.dirname(__file__), 'style.css'), encoding='utf-8').read()
JS = open(os.path.join(os.path.dirname(__file__), 'app.js'), encoding='utf-8').read()

PAGE = f'''<!DOCTYPE html>
<html lang="cs" data-lang="cs" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BI Team Lead – případová studie</title>
<meta name="description" content="BI Team Lead case study: Group BI approach and supplier invoice analysis.">
<script>try{{var l=localStorage.getItem('lang'),t=localStorage.getItem('theme');if(l)document.documentElement.dataset.lang=l;document.documentElement.dataset.theme=t||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');}}catch(e){{}}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top">
 <div class="brand"><span class="mark"></span><span class="brand-t">BI Team Lead <span class="brand-s">· {T('Case study', 'Případová studie')}</span></span></div>
 <div class="ctrls">
  <div class="seg" role="group" aria-label="Language"><button data-setlang="cs">CZ</button><button data-setlang="en">EN</button></div>
  <button class="btn icon theme" aria-label="Light / dark"><span class="sun">☀</span><span class="moon">☾</span></button>
  <a class="btn ghost gh" href="https://github.com/Dvorpet/BI-Team-Lead">GitHub</a>
 </div>
</header>
<nav class="tabs" role="tablist">
 <a href="#p1" role="tab" data-tab="p1">{DECK_META['p1']['tab']}</a>
 <a href="#p2" role="tab" data-tab="p2">{DECK_META['p2']['tab']}</a>
 <a href="#data" role="tab" data-tab="data">Data</a>
</nav>
<main>
{deck_panel('p1')}
{deck_panel('p2')}
{data_panel()}
</main>
<footer class="foot-page">
 <p>{T('Personal solution of a case study for a job interview. Not an official Škoda Group website and not affiliated with Škoda Group; colours follow its blue-and-white style, no logos used.',
       'Osobní řešení případové studie k pracovnímu pohovoru. Nejde o oficiální web Škoda Group a stránka se Škoda Group nijak nesouvisí; barvy vycházejí z jejího modrobílého stylu, bez použití log.')}</p>
 <p>{T('Fonts: IBM Plex Sans and Space Grotesk (SIL Open Font License).', 'Písma: IBM Plex Sans a Space Grotesk (SIL Open Font License).')}</p>
</footer>
<script>{JS}</script>
</body>
</html>'''

with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(PAGE)
print('index.html written', len(PAGE))
