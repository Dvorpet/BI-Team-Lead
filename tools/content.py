# -*- coding: utf-8 -*-
"""Bilingual slide content for both decks. T(en, cs) renders both languages; CSS shows one."""

def T(en, cs):
    return f'<span class="l-en">{en}</span><span class="l-cs">{cs}</span>'

ARROW = '<svg class="arr" viewBox="0 0 60 40" aria-hidden="true"><path d="M0 14h34V2l26 18-26 18V26H0z"/></svg>'

ICONS = {
 'lock': '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 'link': '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>',
 'check': '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>',
 'users': '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5.5"/></svg>',
}

def head(eyebrow, title):
    return f'<div class="hd"><p class="eyebrow">{eyebrow}</p><h2 class="title">{title}</h2></div>'

def foot(text):
    return f'<p class="foot">{text}</p>'

def table(cols, rows, widths, right=(), hl=()):
    h = ''.join(f'<th style="width:{w}%"{" class=r" if i in right else ""}>{c}</th>' for i, (c, w) in enumerate(zip(cols, widths)))
    b = ''
    for ri, r in enumerate(rows):
        cls = ' class="hl"' if ri in hl else (' class="tot"' if r and r[0] == 'TOTAL' else '')
        cells = r[1:] if r and r[0] == 'TOTAL' else r
        b += f'<tr{cls}>' + ''.join(f'<td{" class=r" if i in right else ""}>{c}</td>' for i, c in enumerate(cells)) + '</tr>'
    return f'<table class="t"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'

# ---------------------------------------------------------------- PART 1
P1 = []

P1.append(dict(kind='cover', html=f'''
<p class="eyebrow">{T('Case study · Part 1', 'Případová studie · Část 1')}</p>
<h1 class="cover-title">{T('One trusted data layer<br>for the whole Group', 'Jedna důvěryhodná<br>datová vrstva pro celou skupinu')}</h1>
<p class="cover-sub">{T('How I would lead the Group BI project', 'Jak bych vedl projekt BI pro skupinu')}</p>
{foot(T('BI Team Lead interview · 10 minutes', 'Pohovor BI Team Lead · 10 minut'))}''',
 title=T('One trusted data layer for the whole Group', 'Jedna důvěryhodná datová vrstva pro celou skupinu'),
 notes=T('(~20 s) Ten minutes, nine slides. One message: the Group needs one trusted data layer that every report, automation and AI agent uses. Tools come second.',
         '(~20 s) Deset minut, devět slajdů. Jedno sdělení: skupina potřebuje jednu důvěryhodnou datovou vrstvu, kterou používají všechny reporty, automatizace i AI agenti. Nástroje jsou až na druhém místě.')))

P1.append(dict(html=f'''
{head(T('Starting point', 'Výchozí stav'), T('Today, 25 entities give 25 different answers to the same question', 'Dnes dává 25 společností na stejnou otázku 25 různých odpovědí'))}
<div class="row center">
 <div class="col stack">
  <p class="pill">{T('Entity 1 · ERP A', 'Společnost 1 · ERP A')}</p>
  <p class="pill">{T('Entity 2 · ERP B', 'Společnost 2 · ERP B')}</p>
  <p class="pill">{T('… Entity 25 · ERP C', '… Společnost 25 · ERP C')}</p>
 </div>
 {ARROW}
 <div class="col box"><p class="big-label">{T('Manual consolidation in Excel', 'Ruční slučování v Excelu')}</p></div>
 {ARROW}
 <div class="col box strong"><p class="big-label">{T('Late, disputed numbers for management', 'Pozdní a sporná čísla pro management')}</p></div>
</div>
{foot(T('Part 1 · 2', 'Část 1 · 2'))}''',
 title=T('Today, 25 entities give 25 different answers', 'Dnes 25 společností, 25 různých odpovědí'),
 notes=T('(~60 s) The problem is not a lack of data. Every entity has its own ERP and its own definitions, so Group numbers are assembled by hand and argued about. Project delays and cost overruns are seen too late. The goal of the project: decisions on projects, costs and staffing from one trusted source.',
         '(~60 s) Problém není v nedostatku dat. Každá společnost má vlastní ERP a vlastní definice, takže čísla za skupinu se skládají ručně a vedou se o nich spory. Zpoždění projektů a překročení nákladů se ukážou pozdě. Cíl projektu: rozhodovat o projektech, nákladech a kapacitách z jednoho důvěryhodného zdroje.')))

P1.append(dict(html=f'''
{head(T('Target solution', 'Cílové řešení'), T('Build one shared data layer in Microsoft Fabric, not 25 reporting projects', 'Postavit jednu sdílenou datovou vrstvu v Microsoft Fabric, ne 25 reportingových projektů'))}
<div class="row stretch">
 <div class="col box muted"><h3>{T('Sources', 'Zdroje')}</h3><p>{T('SAP, legacy ERPs, project and HR systems', 'SAP, starší ERP, projektové a HR systémy')}</p></div>
 {ARROW}
 <div class="col box"><h3>Microsoft Fabric</h3><p>{T('raw → cleaned → business-ready data', 'surová → vyčištěná → data připravená pro byznys')}</p></div>
 {ARROW}
 <div class="col box accent"><h3>{T('One semantic model', 'Jeden sémantický model')}</h3><p>{T('shared KPI definitions', 'společné definice KPI')}</p></div>
 {ARROW}
 <div class="col box strong"><h3 class="acc">{T('Used by', 'Využívají')}</h3><p>{T('Power BI, automated reports, AI agents', 'Power BI, automatické reporty, AI agenti')}</p></div>
</div>
<p class="lead"><b>{T('Result:', 'Výsledek:')}</b> {T('insights available on demand, no manual consolidation. Builds on today’s Power BI and SQL data warehouse.', 'přehledy kdykoli k dispozici, bez ručního slučování. Navazuje na dnešní Power BI a SQL datový sklad.')}</p>
{foot(T('Part 1 · 3', 'Část 1 · 3'))}''',
 title=T('One shared data layer in Microsoft Fabric', 'Jedna sdílená datová vrstva v Microsoft Fabric'),
 notes=T('(~70 s) Entities keep their systems; SAP is being rolled out and older ERPs stay for a while. All data lands in Microsoft Fabric, is cleaned and mapped to Group master data. The heart of the solution is one semantic model: every KPI is calculated once, the same way, and reused by Power BI reports, automated outputs and AI agents. This is an evolution of the existing Power BI and SQL data warehouse, not a restart.',
         '(~70 s) Společnosti si ponechají své systémy; SAP se zavádí a starší ERP ještě nějakou dobu zůstanou. Všechna data se načtou do Microsoft Fabric, vyčistí se a namapují na kmenová data skupiny. Jádrem řešení je jeden sémantický model: každý ukazatel se počítá jednou a stejně a používají ho reporty v Power BI, automatické výstupy i AI agenti. Je to rozvoj dnešního Power BI a SQL datového skladu, ne začátek od nuly.')))

P1.append(dict(html=f'''
{head(T('Shared definitions', 'Společné definice'), T('Agree what a number means before anyone builds a report', 'Nejdřív se dohodnout, co číslo znamená, pak teprve stavět report'))}
{table([T('KPI','KPI'), T('One definition','Jedna definice'), T('Owner','Vlastník')],
 [[f"<b>{T('Project delay','Zpoždění zakázky')}</b>", T('Forecast vs baseline milestone, in days','Prognóza vs. plánovaný milník, ve dnech'), T('Project office','Projektová kancelář')],
  [f"<b>{T('Project cost','Náklady projektu')}</b>", T('Actual + committed vs budget','Skutečné + závazné náklady vs. rozpočet'), T('Group controlling','Controlling skupiny')],
  [f"<b>{T('Utilisation','Vytížení')}</b>", T('Project hours ÷ available hours','Hodiny na projektech ÷ dostupné hodiny'), T('Operations','Provoz')]],
 [26, 46, 28])}
{foot(T('Part 1 · 4 · Example entries from a KPI dictionary', 'Část 1 · 4 · Ukázka ze slovníku KPI'))}''',
 title=T('Agree what a number means first', 'Nejdřív shoda na významu čísel'),
 notes=T('(~60 s) The hardest part of a group BI project is not technology but meaning. If two entities calculate project delay differently, no dashboard can fix it. So every KPI gets one definition, one owner who confirms rules and exceptions, and one source. This dictionary also becomes the shared context that AI agents need to give correct answers.',
         '(~60 s) Nejtěžší na BI projektu pro skupinu není technologie, ale význam čísel. Když dvě společnosti počítají zpoždění zakázky jinak, žádný dashboard to nespraví. Každý ukazatel proto dostane jednu definici, jednoho vlastníka, který potvrdí pravidla a výjimky, a jeden zdroj. Tento slovník je zároveň společným kontextem, který potřebují AI agenti, aby odpovídali správně.')))

P1.append(dict(html=f'''
{head(T('What management gets', 'Co dostane management'), T('Each project objective becomes one automated reporting product', 'Každý cíl projektu se promění v jeden automatizovaný reportingový produkt'))}
{table([T('Objective','Cíl'), T('Reporting product','Reportingový produkt'), T('Example KPIs','Příklady KPI')],
 [[f"<b>{T('Data integration','Integrace dat')}</b>", T('Group data layer, all entities','Datová vrstva skupiny, všechny společnosti'), T('Entities onboarded','Připojené společnosti')],
  [f"<b>{T('Operational reporting','Provozní reporting')}</b>", T('Timeline, budget and equipment dashboard','Dashboard termínů, rozpočtu a vybavení'), T('Delay days · budget variance · equipment availability','Dny zpoždění · odchylka od rozpočtu · dostupnost vybavení')],
  [f"<b>{T('Cost control and staffing','Řízení nákladů a kapacit')}</b>", T('Running cost and utilisation report','Report průběžných nákladů a vytížení'), T('Committed cost · utilisation %','Závazné náklady · vytížení v %')],
  [f"<b>{T('Compliance','Compliance')}</b>", T('Access, audit and quality monitor','Přehled přístupů, auditu a kvality'), T('Open audit and quality issues','Otevřená zjištění z auditu a kvality')]],
 [28, 36, 36])}
{foot(T('Part 1 · 5', 'Část 1 · 5'))}''',
 title=T('Each objective becomes a reporting product', 'Každý cíl = jeden reportingový produkt'),
 notes=T('(~60 s) This maps the four objectives from the brief to concrete products. The first one users see is project timeline and cost, because delays and overruns are where money is lost. Each product refreshes automatically from the semantic model, so nobody rebuilds numbers in Excel.',
         '(~60 s) Tady jsou čtyři cíle ze zadání převedené na konkrétní produkty. Jako první uvidí uživatelé termíny a náklady projektů, protože na zpožděních a překročení rozpočtu se ztrácejí peníze. Každý produkt se automaticky aktualizuje ze sémantického modelu, takže už nikdo čísla neskládá v Excelu.')))

def phase(when, name, desc, cls=''):
    return f'<div class="col box phase {cls}"><p class="when">{when}</p><h3 class="ph">{name}</h3><p>{desc}</p></div>'

P1.append(dict(html=f'''
{head(T('Roadmap', 'Plán'), T('Deliver in waves that follow the SAP and Fabric rollout', 'Dodávat ve vlnách, které sledují zavádění SAP a Fabric'))}
<div class="row stretch gap-l">
 {phase(T('Months 0–3','Měsíce 0–3'), T('Define','Definovat'), T('KPIs, sources, pilot entity','KPI, zdroje, pilotní společnost'))}
 {phase(T('Months 3–6','Měsíce 3–6'), T('Pilot','Pilot'), T('Project cost and delay report','Report nákladů a zpoždění zakázek'))}
 {phase(T('Months 6–12','Měsíce 6–12'), T('Scale','Škálovat'), T('Entities in waves, staffing, equipment','Společnosti ve vlnách, kapacity, vybavení'), 'hot')}
 {phase(T('Month 12+','Měsíc 12+'), T('Automate','Automatizovat'), T('Alerts and AI agents','Upozornění a AI agenti'), 'strong hot')}
</div>
<p class="lead"><b>{T('During SAP migration:', 'Během migrace na SAP:')}</b> {T('old and new data run in parallel until the numbers reconcile.', 'stará a nová data běží souběžně, dokud se čísla neshodují.')}</p>
{foot(T('Part 1 · 6 · Timing indicative', 'Část 1 · 6 · Časování orientační'))}''',
 title=T('Deliver in waves with SAP and Fabric', 'Dodávat ve vlnách se SAP a Fabric'),
 notes=T('(~60 s) Waves follow the SAP and Fabric rollout, so we do not build twice. The pilot picks one entity with a motivated sponsor. The key risk is the SAP migration: reports must not break. The semantic model stays stable while sources change underneath, and old and new data run in parallel until the numbers reconcile.',
         '(~60 s) Vlny sledují zavádění SAP a Fabric, abychom nic nestavěli dvakrát. Pro pilot vybereme jednu společnost s motivovaným sponzorem. Hlavním rizikem je migrace na SAP: reporty se nesmí rozbít. Sémantický model zůstává stabilní, zatímco se pod ním mění zdroje, a stará a nová data běží souběžně, dokud se čísla neshodují.')))

def tile(icon, text):
    return f'<div class="box tile">{ICONS[icon]}<p>{text}</p></div>'

P1.append(dict(html=f'''
{head(T('Compliance and data quality', 'Compliance a kvalita dat'), T('Safety and regulatory controls are built into the data layer, not added later', 'Bezpečnostní a regulatorní kontroly jsou součástí datové vrstvy, ne dodatkem'))}
<div class="grid2">
 {tile('lock', T('Access by role and entity','Přístup podle role a společnosti'))}
 {tile('link', T('Traceable numbers as evidence for safety and regulatory audits','Dohledatelná čísla jako doklad pro bezpečnostní a regulatorní audity'))}
 {tile('check', T('Automated data-quality checks','Automatické kontroly kvality dat'))}
 {tile('users', T('GDPR rules for HR and timesheet data','Pravidla GDPR pro data HR a výkazů práce'))}
</div>
{foot(T('Part 1 · 7', 'Část 1 · 7'))}''',
 title=T('Safety and regulatory controls built in', 'Bezpečnostní a regulatorní kontroly v základu'),
 notes=T('(~50 s) For a rolling-stock manufacturer, reports can serve as evidence for safety and regulatory audits, so lineage and audit trail are not optional. Access follows role and entity. Data-quality rules run automatically and alert the data owner, who fixes the problem at source. Staffing data falls under GDPR, so personal data is protected by design. Part 2 shows what happens without such checks.',
         '(~50 s) U výrobce kolejových vozidel mohou reporty sloužit jako doklad při bezpečnostních a regulatorních auditech, takže dohledatelnost původu dat a auditní stopa nejsou volitelné. Přístup se řídí rolí a společností. Pravidla kvality dat běží automaticky a upozorní vlastníka dat, který problém opraví u zdroje. Data o kapacitách spadají pod GDPR, takže osobní údaje jsou chráněné už v návrhu. Část 2 ukazuje, co se stane bez takových kontrol.')))

def step(num, label, text, cls=''):
    return f'<div class="col box step {cls}"><p class="when">{num} · {label}</p><p class="big-label">{text}</p></div>'

P1.append(dict(html=f'''
{head(T('Automation and AI', 'Automatizace a AI'), T('AI agents draft the variance commentary, people approve it', 'AI agenti připraví komentář k odchylkám, lidé ho schválí'))}
<div class="row center">
 {step('1', T('Data','Data'), T('Trusted semantic model','Důvěryhodný sémantický model'), 'accent')}
 {ARROW}
 {step('2', T('AI agent','AI agent'), T('Finds variances, drafts comment with sources','Najde odchylky, připraví komentář se zdroji'))}
 {ARROW}
 {step('3', T('Person','Člověk'), T('Controller reviews and approves','Controller zkontroluje a schválí'), 'strong')}
</div>
<p class="lead">{T('Start with one prototype, measure accuracy, then scale.', 'Začít jedním prototypem, změřit přesnost, pak rozšířit.')}</p>
{foot(T('Part 1 · 8', 'Část 1 · 8'))}''',
 title=T('AI drafts, people approve', 'AI připraví, lidé schválí'),
 notes=T('(~60 s) AI is only as good as the definitions behind it, which is why it comes after the semantic model. A practical first use case: monthly variance commentary. The agent finds the deviations, looks up the supporting records and drafts a comment with sources; a controller approves. We test it on accuracy, freshness and how it behaves with incomplete data before it goes into regular use.',
         '(~60 s) AI je jen tak dobrá, jak dobré jsou definice za ní, proto přichází až po sémantickém modelu. Praktický první případ: měsíční komentář k odchylkám. Agent najde odchylky, dohledá podklady a připraví komentář se zdroji; controller ho schválí. Před běžným nasazením ho otestujeme na přesnost, aktuálnost a chování při neúplných datech.')))

P1.append(dict(html=f'''
{head(T('Team and ways of working', 'Tým a způsob práce'), T('A small central team, one shared backlog, a champion in every entity', 'Malý centrální tým, jeden společný backlog, ambasador v každé společnosti'))}
<div class="row center">
 <div class="col box strong"><h3 class="acc xl">{T('BI team','BI tým')}</h3><p class="lead-in">{T('Business analysts and Power BI developers','Business analytici a vývojáři Power BI')}</p></div>
 {ARROW}
 <div class="col stack">
  <p class="pill solid"><b>{T('Group Finance','Finance skupiny')}</b> · {T('KPI owners','vlastníci KPI')}</p>
  <p class="pill solid"><b>{T('DWH, SAP and IT','DWH, SAP a IT')}</b> · {T('platform','platforma')}</p>
  <p class="pill solid"><b>{T('Entity champions','Ambasadoři ve společnostech')}</b> · {T('local data','lokální data')}</p>
 </div>
</div>
{foot(T('Part 1 · 9', 'Část 1 · 9'))}''',
 title=T('Small central team, champions in every entity', 'Malý tým, ambasadoři ve společnostech'),
 notes=T('(~50 s) As Team Lead I set priorities with Finance, keep one backlog and protect the team from ad-hoc requests. Analysts translate business needs into shared definitions and models, together with the DWH and SAP specialists. Champions in each entity know why local data looks the way it does and train colleagues. Standards for Power BI make every report look and behave the same.',
         '(~50 s) Jako Team Lead nastavuji priority s financemi, držím jeden backlog a chráním tým před nahodilými požadavky. Analytici převádějí potřeby byznysu do společných definic a modelů, spolu se specialisty na DWH a SAP. Ambasadoři v jednotlivých společnostech vědí, proč lokální data vypadají tak, jak vypadají, a školí kolegy. Standardy pro Power BI zajistí, že všechny reporty vypadají a fungují stejně.')))

def three(items):
    return '<div class="row stretch gap-l">' + ''.join(f'<div class="col tri"><p class="tri-h">{a}</p><p class="tri-p">{b}</p></div>' for a, b in items) + '</div>'

P1.append(dict(kind='dark', html=f'''
{head(T('If I start tomorrow', 'Kdybych nastoupil zítra'), T('First 90 days: listen, define, and deliver one quick win', 'Prvních 90 dní: naslouchat, definovat a dodat první rychlý výsledek'))}
{three([(T('Listen','Naslouchat'), T('Group Finance and key entities','Finance skupiny a klíčové společnosti')),
        (T('Define','Definovat'), T('KPI dictionary and pilot scope','Slovník KPI a rozsah pilotu')),
        (T('Deliver','Dodat'), T('First project-cost report live','První report nákladů projektů v provozu'))])}
{foot(T('Part 1 · 10', 'Část 1 · 10'))}''',
 title=T('First 90 days', 'Prvních 90 dní'),
 notes=T('(~40 s) Close with action. First listen: what decisions do Group Finance and the entities struggle with. Then define the first KPIs and pilot scope with their owners. And within 90 days, one visible result: a project-cost report on the new data layer. A quick win builds trust for the larger programme. Then questions.',
         '(~40 s) Závěr akcí. Nejdřív naslouchat: s jakými rozhodnutími mají finance skupiny a jednotlivé společnosti potíže. Pak s vlastníky definovat první KPI a rozsah pilotu. A do 90 dní jeden viditelný výsledek: report nákladů projektů nad novou datovou vrstvou. Rychlý výsledek buduje důvěru pro větší program. Pak prostor pro otázky.')))

# ---------------------------------------------------------------- PART 2
P2 = []

P2.append(dict(kind='cover', html=f'''
<p class="eyebrow">{T('Case study · Part 2 · Company AB', 'Případová studie · Část 2 · Company AB')}</p>
<h1 class="cover-title">{T('Supplier invoices:<br>fix the data, release the cash', 'Faktury dodavatelů:<br>opravit data, uvolnit hotovost')}</h1>
<p class="cover-sub">{T('Data quality, business value and answers to six questions', 'Kvalita dat, přínos pro firmu a odpovědi na šest otázek')}</p>
{foot(T('3,349 invoices · January–August 2024 · amounts in local currency', '3 349 faktur · leden–srpen 2024 · částky v místní měně'))}''',
 title=T('Supplier invoices: fix the data, release the cash', 'Faktury dodavatelů: opravit data, uvolnit hotovost'),
 notes=T('(~20 s) Eight months of supplier invoices. I will start with the conclusion, then answer the six questions in order. Every number comes from the analysis workbook and is calculated with formulas.',
         '(~20 s) Osm měsíců faktur od dodavatelů. Začnu závěrem a pak odpovím na šest otázek v pořadí. Všechna čísla pocházejí z analytického sešitu a jsou spočítaná vzorci.')))

P2.append(dict(html=f'''
{head(T('Summary', 'Shrnutí'), T('Clean data and a better payment routine can release about 12.7 m of cash', 'Čistá data a lepší platební režim mohou uvolnit zhruba 12,7 mil. hotovosti'))}
<div class="row center gap-xl">
 <p class="mega">{T('12.7 m','12,7 mil.')}</p>
 <div class="col list">
  <p>{T('one-off, about 8.5 % of the period’s spend','jednorázově, asi 8,5 % výdajů za období')}</p>
  <p>{T('invoices are paid 5 days earlier than contracts require','faktury se platí o 5 dní dřív, než vyžadují smlouvy')}</p>
  <p><b>{T('Data quality:','Kvalita dat:')}</b> {T('usable after cleaning, but not reliable as delivered','po vyčištění použitelná, v dodané podobě nespolehlivá')}</p>
 </div>
</div>
{foot(T('Part 2 · 2', 'Část 2 · 2'))}''',
 title=T('About 12.7 m of cash can be released', 'Lze uvolnit zhruba 12,7 mil. hotovosti'),
 notes=T('(~40 s) The headline: the company pays its suppliers earlier than it has to. Fixing that, plus a few related levers, releases about 12.7 million of cash once. To get there I first had to fix the data, which is where I start.',
         '(~40 s) Hlavní zjištění: firma platí dodavatelům dřív, než musí. Když to napraví, spolu s několika dalšími opatřeními, uvolní jednorázově zhruba 12,7 milionu hotovosti. Abych se k tomu dostal, musel jsem nejdřív opravit data, a tím začnu.')))

P2.append(dict(html=f'''
{head(T('Q1 · Inconsistencies in the file', 'Q1 · Nekonzistence v souboru'), T('File errors hide 12.3 m and make duplicates impossible to prove', 'Chyby v souboru skrývají 12,3 mil. a znemožňují prokázat duplicity'))}
{table([T('Issue','Problém'), T('Rows','Řádky')],
 [[T('Amounts stored as text, ignored by SUM','Částky uložené jako text, SUM je ignoruje'), '216'],
  [T('Rows shifted one column to the right','Řádky posunuté o sloupec doprava'), '58'],
  [T('Invoice number empty in every row','Číslo faktury chybí ve všech řádcích'), T('3,349','3 349')],
  [T('Identical rows, both paid: likely double payment','Totožné řádky, obě zaplacené: pravděpodobná dvojí platba'), '2']],
 [78, 22], right=(1,))}
{foot(T('Part 2 · 3 · Also: 5 rows with #N/A instead of supplier ID; “Extra Days” always 0', 'Část 2 · 3 · Dále: 5 řádků s #N/A místo ID dodavatele; „Extra Days“ vždy 0'))}''',
 title=T('File errors hide 12.3 m', 'Chyby v souboru skrývají 12,3 mil.'),
 notes=T('(~60 s) Loaded as-is, the file gives wrong totals: 216 rows have amounts stored as text with comma decimals, so 12.3 million silently drops out of SUM. 58 rows at the end are shifted one column, so supplier, dates and amounts land in the wrong fields. The invoice number is empty everywhere, so there is no unique key. Rows 3274 and 3275 are identical and both paid: a likely double payment of 16.6 thousand.',
         '(~60 s) Načtený tak, jak je, dává soubor špatné součty: 216 řádků má částky uložené jako text s desetinnou čárkou, takže 12,3 milionu tiše vypadne ze SUM. 58 řádků na konci je posunutých o sloupec, takže dodavatel, data i částky jsou ve špatných polích. Číslo faktury chybí všude, takže neexistuje jedinečný klíč. Řádky 3274 a 3275 jsou totožné a oba zaplacené: pravděpodobná dvojí platba 16,6 tisíce.')))

P2.append(dict(html=f'''
{head(T('Q1 · Inconsistencies in the business logic', 'Q1 · Nekonzistence v obchodní logice'), T('Business rules are broken too, and the due-date error costs cash', 'Porušená jsou i obchodní pravidla a chyba ve splatnosti stojí peníze'))}
{table([T('Issue','Problém'), T('Rows','Řádky')],
 [[f"<b>{T('Due date earlier than issue date + terms','Splatnost dřív, než odpovídá datu vystavení + lhůtě')}</b>", f"<b>{T('1,586','1 586')}</b>"],
  [T('Order terms differ from supplier master data','Splatnost na objednávce se liší od kmenových dat'), '135'],
  [T('“Matched” flag without an order number','Příznak „Matched“ bez čísla objednávky'), '352'],
  [T('Non-standard VAT rates, e.g. 10 % or 15 %','Nestandardní sazby DPH, např. 10 % nebo 15 %'), '22'],
  [T('Credit-note loop: supplier 235 owes about 3.3 m','Smyčka dobropisů: dodavatel 235 dluží asi 3,3 mil.'), '8']],
 [78, 22], right=(1,), hl=(0,))}
{foot(T('Part 2 · 4 · In Czechia, 10 % and 15 % VAT rates were abolished in 2024 (if the currency is CZK)', 'Část 2 · 4 · Sazby DPH 10 % a 15 % byly v ČR v roce 2024 zrušeny (pokud jde o CZK)'))}''',
 title=T('Business rules are broken too', 'Porušená jsou i obchodní pravidla'),
 notes=T('(~60 s) The highlighted row matters most: for almost half of the invoices (1,586) the system sets the due date earlier than the contract allows, mostly by 1 to 10 days, so cash leaves early. Another 196 invoices have a later due date, so 1,782 differ in total. Either a different baseline date is used, which is not in the data, or the logic is wrong. Order terms are overridden, the matched flag contradicts the order number, VAT rates look invalid if the currency is CZK, and supplier 235 was paid 3.84 million, then credited twice: net, they owe us about 3.3 million. All of these are candidates to verify with accounts payable.',
         '(~60 s) Nejdůležitější je zvýrazněný řádek: u téměř poloviny faktur (1 586) nastavuje systém splatnost dřív, než dovoluje smlouva, většinou o 1 až 10 dní, takže peníze odcházejí dřív. Dalších 196 faktur má splatnost pozdější, celkem se tedy liší 1 782. Buď se používá jiné výchozí datum, které v datech není, nebo je chybná logika. Splatnost na objednávkách je přepisovaná, příznak „Matched“ odporuje číslu objednávky, sazby DPH vypadají neplatně, pokud jde o CZK, a dodavatel 235 dostal zaplaceno 3,84 milionu a pak dvakrát dobropis: v součtu nám dluží zhruba 3,3 milionu. To vše jsou kandidáti k ověření s účtárnou.')))

P2.append(dict(kind='alt', html=f'''
{head(T('Q2 · Key metrics', 'Q2 · Klíčové metriky'), T('We pay after 25 days although contracts give us 30', 'Platíme po 25 dnech, i když smlouvy dávají 30'))}
{table([T('Metric','Metrika'), T('Value','Hodnota')],
 [[T('Spend, 8 months, gross','Výdaje za 8 měsíců, brutto'), T('148.7 m','148,7 mil.')],
  [T('Share of the top 10 suppliers','Podíl 10 největších dodavatelů'), '59 %'],
  [T('Contractual payment terms','Smluvní splatnost'), T('30.0 days','30,0 dne')],
  [f"<b>{T('Actual days to pay','Skutečná doba úhrady')}</b>", f"<b>{T('24.9 days','24,9 dne')}</b>"],
  [T('Invoices paid before the due date','Faktury zaplacené před splatností'), '91 %'],
  [T('Spend without a purchase order','Výdaje bez objednávky'), '56–70 %']],
 [70, 30], right=(1,), hl=(3,))}
{foot(T('Part 2 · 5 · Day figures weighted by invoice value', 'Část 2 · 5 · Dny vážené hodnotou faktury'))}''',
 title=T('We pay after 25 days, contracts give 30', 'Platíme po 25 dnech, smlouvy dávají 30'),
 notes=T('(~50 s) Three groups of metrics: spend, payment behaviour and process compliance. The key pair is 30 days contractual versus 24.9 days actual. Spend is concentrated: ten suppliers make up 59 percent, which matters for negotiation. The purchase-order share is a range because two fields disagree, which is itself a finding.',
         '(~50 s) Tři skupiny metrik: výdaje, platební chování a dodržování procesu. Klíčová dvojice je 30 dní podle smluv proti skutečným 24,9 dne. Výdaje jsou koncentrované: deset dodavatelů tvoří 59 procent, což je důležité pro vyjednávání. Podíl výdajů bez objednávky je rozpětí, protože dvě pole si odporují, a to je samo o sobě zjištění.')))

BARS = [('≤−7', 22, 'g'), ('−6', 321, 'h'), ('−5', 538, 'h'), ('−4', 501, 'h'), ('−3', 545, 'h'), ('−2', 510, 'h'), ('−1', 349, 'h'), ('0', 115, 'a'), ('+1…7', 130, 'm'), ('≥+8', 15, 'm')]
def chart():
    mx = max(v for _, v, _ in BARS)
    cols = ''.join(f'<div class="bc"><p class="bv">{v}</p><div class="bar {c}" style="height:{max(0.5, v / mx * 18.2):.2f}cqw"></div><p class="bl">{l}</p></div>' for l, v, c in BARS)
    return f'<div class="chart">{cols}</div>'

P2.append(dict(html=f'''
{head(T('Why we pay early', 'Proč platíme dřív'), T('One weekly Tuesday payment run pays most invoices 1–6 days early', 'Jeden úterní platební běh týdně platí většinu faktur o 1–6 dní dřív'))}
{chart()}
<p class="caption">{T('Number of paid invoices by days before (−) or after (+) the due date. Highlighted: paid 1–6 days early.', 'Počet zaplacených faktur podle dnů před (−) nebo po (+) splatnosti. Zvýrazněno: zaplaceno 1–6 dní předem.')}</p>
{foot(T('Part 2 · 6 · 86 % of payment value leaves on a Tuesday', 'Část 2 · 6 · 86 % hodnoty plateb odchází v úterý'))}''',
 title=T('A Tuesday payment run pays 1–6 days early', 'Úterní běh platí o 1–6 dní dřív'),
 notes=T('(~50 s) This is why. Payments go out once a week, on Tuesday, and the run pays everything that falls due before the next run. That produces exactly this block from six days to one day early. On average invoices leave 2.9 days before they are due. The fix is cheap: select invoices by due date, or run payments twice a week.',
         '(~50 s) Tady je příčina. Platby odcházejí jednou týdně, v úterý, a běh zaplatí vše, co je splatné před dalším během. Vzniká přesně tento blok od šesti do jednoho dne předem. V průměru faktury odcházejí 2,9 dne před splatností. Náprava je levná: vybírat faktury podle splatnosti, nebo platit dvakrát týdně.')))

P2.append(dict(html=f'''
{head(T('Q3 · Alternative approaches', 'Q3 · Alternativní přístupy'), T('The definition changes the answer, so it must be agreed first', 'Definice mění výsledek, proto se musí dohodnout předem'))}
<div class="row stretch">
 <div class="col box strong numcard"><p class="num acc">{T('24.9','24,9')}</p><p>{T('days, weighted by invoice value','dne, průměr vážený hodnotou faktury')}</p></div>
 <div class="col box numcard"><p class="num grn">{T('26.3','26,3')}</p><p>{T('days, simple average','dne, prostý průměr')}</p></div>
</div>
<p class="lead"><b>{T('Other choices:','Další možnosti:')}</b> {T('balance-sheet DPO · receipt date instead of issue date · net instead of gross','DPO z rozvahy · datum doručení místo data vystavení · netto místo brutto')}</p>
{foot(T('Part 2 · 7', 'Část 2 · 7'))}''',
 title=T('The definition changes the answer', 'Definice mění výsledek'),
 notes=T('(~50 s) Same data, two answers. Large invoices are paid faster, so the value-weighted average is lower. Other valid choices: a balance-sheet DPO, payables divided by purchases, which matches financial reporting but is unreliable on an eight-month extract; measuring from receipt date, which is fairer to accounts payable; net instead of gross for cost analysis. The lesson for the BI team: one agreed definition per KPI.',
         '(~50 s) Stejná data, dvě odpovědi. Velké faktury se platí rychleji, proto je průměr vážený hodnotou nižší. Další platné možnosti: DPO z rozvahy, tedy závazky dělené nákupy, které odpovídá finančnímu výkaznictví, ale na osmiměsíčním výřezu je nespolehlivé; měření od data doručení, které je spravedlivější vůči účtárně; netto místo brutto pro analýzu nákladů. Ponaučení pro BI tým: jedna dohodnutá definice pro každý ukazatel.')))

P2.append(dict(html=f'''
{head(T('Q4 · Who uses it &amp; Q5 · What is missing', 'Q4 · Kdo data využije a Q5 · Co chybí'), T('Five teams can act on this data once key fields are added', 'Pět týmů může data využít, jakmile se doplní klíčová pole'))}
{table([T('Team','Tým'), T('Uses it for','Využití'), T('Missing field','Chybějící pole')],
 [[f"<b>{T('Accounts payable','Účtárna závazků')}</b>", T('Duplicate check','Kontrola duplicit'), T('Invoice number','Číslo faktury')],
  [f"<b>{T('Treasury','Treasury')}</b>", T('Cash forecast','Prognóza hotovosti'), T('Currency, company code','Měna, účetní jednotka')],
  [f"<b>{T('Procurement','Nákup')}</b>", T('Terms, spend without orders','Podmínky, výdaje bez objednávek'), T('Supplier category, order value','Kategorie dodavatele, hodnota objednávky')],
  [f"<b>{T('Controlling','Controlling')}</b>", T('Cost analysis','Analýza nákladů'), T('Cost centre, project','Nákladové středisko, projekt')],
  [f"<b>{T('Tax','Daně')}</b>", T('VAT check','Kontrola DPH'), T('VAT code per line','Kód DPH po řádcích')]],
 [26, 34, 40])}
{foot(T('Part 2 · 8 · Also missing: receipt date, early-payment discounts, 12+ months of history', 'Část 2 · 8 · Dále chybí: datum doručení, skonta, historie za 12+ měsíců'))}''',
 title=T('Five teams can act on this data', 'Pět týmů může data využít'),
 notes=T('(~50 s) Each team that could use the data is blocked by a specific missing field. Without the invoice number there is no reliable duplicate check. Without currency and company code treasury cannot forecast cash. Procurement needs supplier category and order value for a three-way match. Also missing: receipt date, early-payment discount terms, and a full year of history to see seasonality.',
         '(~50 s) Každý tým, který by data mohl využít, brzdí konkrétní chybějící pole. Bez čísla faktury není spolehlivá kontrola duplicit. Bez měny a účetní jednotky nemůže treasury plánovat hotovost. Nákup potřebuje kategorii dodavatele a hodnotu objednávky pro trojí párování. Dále chybí datum doručení, podmínky skont a celý rok historie, aby byla vidět sezónnost.')))

P2.append(dict(html=f'''
{head(T('Q6 · Working capital', 'Q6 · Pracovní kapitál'), T('Four levers release about 12.7 m of cash', 'Čtyři opatření uvolní zhruba 12,7 mil. hotovosti'))}
{table([T('Lever','Opatření'), T('Cash, one-off','Hotovost jednorázově')],
 [[T('Pay on the due date, not before','Platit v den splatnosti, ne dřív'), T('1.6 m','1,6 mil.')],
  [T('Calculate due dates from contract terms','Počítat splatnost podle smluvních podmínek'), T('2.3 m','2,3 mil.')],
  [T('Agree 45-day terms with the top 10 suppliers','Dohodnout 45denní splatnost s 10 největšími dodavateli'), T('5.5 m','5,5 mil.')],
  [T('Recover the credit from supplier 235','Získat zpět kredit od dodavatele 235'), T('3.3 m','3,3 mil.')],
  ['TOTAL', f"<b>{T('Total','Celkem')}</b>", f"<b>{T('12.7 m','12,7 mil.')}</b>"]],
 [74, 26], right=(1,))}
{foot(T('Part 2 · 9 · Check early-payment discounts first; protect small and strategic suppliers', 'Část 2 · 9 · Nejdřív prověřit skonta; chránit malé a strategické dodavatele'))}''',
 title=T('Four levers release about 12.7 m', 'Čtyři opatření uvolní zhruba 12,7 mil.'),
 notes=T('(~60 s) The first two levers are internal process fixes, no negotiation needed: 3.9 million together. Longer terms need procurement and should target large suppliers where we have leverage; 45 days is an assumption. Supplier 235 is one-off but real money. Method: invoice value times days gained, divided by 244 days in the period. Recurring benefit is the interest saved, about 0.6 million a year at an assumed 6 percent. Before paying later, check whether any supplier offers an early-payment discount worth more than the cash.',
         '(~60 s) První dvě opatření jsou interní úpravy procesu bez vyjednávání: dohromady 3,9 milionu. Delší splatnost potřebuje nákup a měla by cílit na velké dodavatele, u kterých máme vyjednávací sílu; 45 dní je předpoklad. Dodavatel 235 je jednorázový, ale jde o skutečné peníze. Metoda: hodnota faktury krát získané dny, děleno 244 dny období. Opakovaný přínos jsou ušetřené úroky, asi 0,6 milionu ročně při předpokládaných 6 procentech. Než začneme platit později, je třeba prověřit, zda některý dodavatel nenabízí skonto, které má větší hodnotu než hotovost.')))

P2.append(dict(kind='dark', html=f'''
{head(T('Next steps', 'Další kroky'), T('Automate the checks so the cash stays visible every week', 'Automatizovat kontroly, aby byla hotovost vidět každý týden'))}
{three([(T('Verify','Ověřit'), T('Double payments and supplier 235 with accounts payable','Dvojí platby a dodavatele 235 s účtárnou')),
        (T('Fix','Opravit'), T('Invoice number, terms and data types in SAP','Číslo faktury, podmínky a datové typy v SAP')),
        (T('Automate','Automatizovat'), T('Quality rules in Fabric, payables report in Power BI','Pravidla kvality ve Fabricu, report závazků v Power BI'))])}
{foot(T('Part 2 · 10', 'Část 2 · 10'))}''',
 title=T('Automate the checks', 'Automatizovat kontroly'),
 notes=T('(~40 s) First verify the suspected double payments and supplier 235 with accounts payable; that is real money now. Then fix the causes in the source system, ideally as part of the SAP rollout. Finally automate: quality rules in the Fabric data layer and a payables report in Power BI, so this analysis runs every week instead of once. This is exactly the shared data layer from Part 1.',
         '(~40 s) Nejdřív ověřit s účtárnou podezřelé dvojí platby a dodavatele 235; to jsou skutečné peníze už teď. Pak opravit příčiny ve zdrojovém systému, ideálně v rámci zavádění SAP. Nakonec automatizovat: pravidla kvality v datové vrstvě Fabric a report závazků v Power BI, aby tato analýza běžela každý týden, ne jednou. Přesně to je sdílená datová vrstva z části 1.')))

DECKS = {'p1': P1, 'p2': P2}
