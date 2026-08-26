#!/usr/bin/env python3
"""Browser-printable 16:9 slides (Office Online cannot open the PPTX)."""
from pathlib import Path

from site_slides_data import SITE_SLIDES

OUT = Path("/workspace/ACIT4280_1A_presentation.html")
FIG = "figures"
TOTAL = 14


def slide(inner: str, n: int, dark: bool = False) -> str:
    cls = "slide dark" if dark else "slide"
    foot = "" if dark and n == 1 else f"""
    <div class="foot"><span>ACIT4280 Group Assignment 1A  |  3 Sep 2026</span><span>{n} / {TOTAL}</span></div>"""
    if dark and n == TOTAL:
        foot = ""
    return f'<section class="{cls}">{inner}{foot}</section>\n'


def header(kicker: str, title: str) -> str:
    return f'<header><div class="kicker">{kicker}</div><h1>{title}</h1></header>'


def bullets(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ul class="bul">{lis}</ul>'


def site_card(block: dict, dual: bool) -> str:
    partial = block["match"] == "Partial"
    cls = "site-card partial" if partial else "site-card"
    match_cls = "part" if partial else "yes"
    extra = f'<p class="extra">{block["extra"]}</p>' if block.get("extra") else ""
    return f"""
    <article class="{cls}">
      <p class="label">Purpose</p>
      <h3>{block["purpose"]}</h3>
      <p class="label">Notice</p>
      <p class="body">{block["notice"]}</p>
      <p class="label">ICO result</p>
      <p class="body">{block["ico"]}</p>
      <p class="match {match_cls}">Match: {block["match"]}</p>
      {extra}
    </article>"""


def site_slide_html(slide_data: dict) -> str:
    dual = len(slide_data["blocks"]) == 2
    cards = "".join(site_card(block, dual) for block in slide_data["blocks"])
    layout_cls = "site-layout dual" if dual else "site-layout"
    return f"""
<div class="{layout_cls}">
  <div class="site-logo-pane">
    <img src="{FIG}/{slide_data["logo"]}" alt="{slide_data["title"]} logo">
    <p class="site-sector">{slide_data["sector"]}</p>
  </div>
  <div class="site-cards">{cards}</div>
</div>"""


parts = []

parts.append(slide(f"""
  <div class="title-inner">
    <p class="kicker">ACIT4280 Privacy by Design</p>
    <p class="assign">Group Assignment 1A</p>
    <h1>Analysis of 3rd-party Data Sharing<br>and Data Tracking and of GDPR<br>Compliance of Norwegian Web Sites</h1>
    <ul class="title-questions">
      <li>When a front page loads, how many third parties does it contact, and in which countries do those servers appear to be located?</li>
      <li>When a site processes personal data, has it named a GDPR Article 6 lawful basis, and does the ICO tool agree?</li>
    </ul>
    <p class="names">Humna Akhtar  ·  Mithun Chandra Debnath  ·  Karina Sætersdal Nilssen</p>
  </div>
  <div class="title-band"><span class="title-date">3 September 2026</span><img class="title-logo" src="{FIG}/oslomet_logo.svg" alt="OsloMet logo"></div>
""", 1, dark=True))


parts.append(slide(header("The report", "Two questions and how we measured") + f"""
<div class="split compact-split">
  <div class="pane cream">
    <h2>Part 1  ·  Webbkoll</h2>
    <ul class="pane-list compact">
      <li>18 sites: cookies, requests, KeyCDN country</li>
      <li>One clean load per site; rank on Table 2 (20 Aug)</li>
      <li>KeyCDN = IP geolocation guess, not legal transfer proof</li>
    </ul>
    <img class="pane-shot compact tool-logo webbkoll-results" src="{FIG}/fig2_webbkoll_results_klassekampen.png" alt="Webbkoll results for klassekampen.no">
  </div>
  <div class="pane navy">
    <h2>Part 2  ·  ICO</h2>
    <ul class="pane-list compact">
      <li>Five sites, one purpose per run</li>
      <li>Notice vs ICO Word report (26 Aug 2026)</li>
      <li>Yes if notice and ICO agree</li>
      <li>Partial if consent is INCONCLUSIVE</li>
      <li>Tax, cookies, checkout and marketing are different purposes</li>
    </ul>
    <img class="pane-shot compact tool-logo ico-logo" src="{FIG}/ico_logo.png" alt="Information Commissioner's Office logo">
  </div>
</div>
""", 2))

parts.append(slide(header("Part 1", "What Webbkoll shows and key findings") + f"""
<div class="split">
  <div class="pane cream">
    <h2>What Webbkoll shows</h2>
    <p class="pane-lead">Cookies, third-party requests and server country.</p>
    <p class="lead-finding">Many requests does not mean many cookies.</p>
    <img class="pane-shot keycdn-shot" src="{FIG}/fig4_keycdn_lookup_klassekampen.png" alt="KeyCDN lookup for klassekampen server IP">
  </div>
  <div class="pane dark">
    <h2>Key findings</h2>
    <ul>
      <li>fotball.no: 113 requests, zero third-party cookies.</li>
      <li>17 of 18 sites: zero third-party cookies. ikea.no had 2.</li>
      <li>lanekassen.no (1) and altinn.no (5): quietest e-government pages.</li>
      <li>document.no: widest country list (6 excluding Norway).</li>
      <li>News/media contacted the most. Government the fewest.</li>
      <li>babyshop.no: 45 on first scan, 101 on repeat scan.</li>
    </ul>
  </div>
</div>
""", 3))

high = [
    ("1  fotball.no", "Sport  ·  113 requests  ·  5 countries"),
    ("2  worldofwarcraft.com", "News/media  ·  90  ·  4"),
    ("3  document.no", "News/media  ·  51  ·  6 (widest list)"),
    ("4  aftenposten.no", "News/media  ·  48  ·  5"),
    ("5  klassekampen.no", "News/media  ·  46  ·  2"),
]
low = [
    ("1  lanekassen.no", "Government  ·  1 request"),
    ("2  altinn.no", "Government  ·  5"),
    ("3  nrk.no", "News/media  ·  7"),
    ("4  spotify.no", "News/media  ·  10"),
    ("5  skiforeningen.no", "Sport  ·  14"),
]
hi_html = "".join(f'<div class="rank cream"><strong>{a}</strong><span>{b}</span></div>' for a, b in high)
lo_html = "".join(f'<div class="rank grey"><strong>{a}</strong><span>{b}</span></div>' for a, b in low)
parts.append(slide(header("Part 1  ·  Table 4", "Highest and lowest third-party requests") + f"""
<div class="two-col">
  <div><h3>Highest five</h3>{hi_html}</div>
  <div><h3>Lowest five</h3>{lo_html}</div>
</div>
""", 4))

parts.append(slide(header("Part 1  ·  Figures 2 to 4", "Third-party requests by site and sector") + f"""
<div class="figs">
  <img src="{FIG}/fig3_requests_all18.png" alt="Bar chart of third-party requests for 18 sites">
  <div class="stack">
    <img src="{FIG}/fig5_share_requests_pie.png" alt="Pie chart of request share">
    <img src="{FIG}/fig6_requests_per_sector.png" alt="Requests per sector">
  </div>
</div>
<p class="caption">News/media is the highest sector. Government is the lowest.</p>
""", 5))

table_rows = [
    ("skatteetaten.no", "Tax / folkeregister", "Legal obligation + public task", "Yes", "yes"),
    ("skatteetaten.no", "Optional cookies", "Consent INCONCLUSIVE", "Partial", "part"),
    ("netflix.no", "Paid streaming", "Contract", "Yes", "yes"),
    ("fotball.no", "Name + club, 13+", "Legitimate interests", "Yes", "yes"),
    ("document.no", "Google Signals", "Consent INCONCLUSIVE", "Partial", "part"),
    ("babyshop.no", "Checkout", "Contract", "Yes", "yes"),
]
tr = "".join(
    f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td class='{k}'>{d}</td></tr>"
    for a, b, c, d, k in table_rows
)

parts.append(slide(header("Part 2", "ICO: one purpose at a time") + f"""
<p class="ico-intro">One purpose per ICO run (26 Aug 2026). Yes if notice and ICO agree; Partial if consent is INCONCLUSIVE. Tax, cookies, checkout and marketing are different purposes.</p>
<table class="compact-table">
  <thead><tr><th>Service</th><th>Purpose</th><th>ICO</th><th>Match</th></tr></thead>
  <tbody>{tr}</tbody>
</table>
""", 6))

parts.append(slide(header("Part 2  ·  Table 5", "Four match, two consent tests Partial") + """
<div class="summary-box ico-summary">
  <p class="lead">Four core purposes match the notice: tax, paid streaming, match history, checkout.</p>
  <p class="lead accent">Two consent tests are Partial: Skatteetaten optional cookies and document.no Google Signals.</p>
  <p>In both cases the notice claims consent, but the ICO marks consent INCONCLUSIVE.</p>
  <p>Skatteetaten does not spell out clearly enough who processes the optional cookies and how to refuse them. document.no points users to Google ad settings; the ICO says that is not a clear, separate consent request, and Pluss terms bundle the notice.</p>
</div>
""", 7))

for site in SITE_SLIDES:
    parts.append(slide(header(site["kicker"], site["title"]) + site_slide_html(site), site["n"]))

parts.append(slide(header("Close", "What the report shows") + """
<div class="summary-box close-summary">
  <p>We measured how much 18 sites contact others on load, and we checked whether five of them have a valid GDPR basis for one specific purpose.</p>
  <p>Many sites reach out to many others without setting cookies.</p>
  <p>Four of five ICO purposes match the notice.</p>
  <p>In two places where the site claims consent, the ICO is not satisfied with how consent is formulated.</p>
</div>
""", 13))

parts.append(slide("""
  <div class="q">
    <h1>¿Questions?</h1>
    <p>ACIT4280 Privacy by Design  ·  Group Assignment 1A</p>
  </div>
""", 14, dark=True))

css = """
:root { --dark:#224248; --mid:#325E6A; --teal:#44A1A4; --orange:#FF9A00; --ink:#1A1A1A; --paper:#FFFEFB; --light:#E8F4F4; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #333; font-family: Calibri, "Segoe UI", sans-serif; }
.toolbar { position: sticky; top: 0; z-index: 2; background: var(--dark); color: #fff; padding: 8px 16px; font-size: 14px; }
.toolbar b { color: var(--orange); }
.slide {
  width: 13.333in; height: 7.5in; background: var(--paper); color: var(--ink);
  page-break-after: always; break-after: page; position: relative; overflow: hidden;
  margin: 12px auto; box-shadow: 0 8px 24px rgba(0,0,0,.35);
}
.slide.dark { background: var(--dark); color: #fff; }
header { background: var(--dark); color: #fff; height: 1.15in; padding: 0.12in 0.5in 0 0.5in; border-bottom: 0.08in solid var(--orange); }
header h1 { margin: 0; font-size: 28px; line-height: 1.15; }
.kicker { font-size: 12px; font-weight: 700; color: var(--teal); letter-spacing: .02em; }
header .kicker { display: inline-block; }
.foot { position: absolute; left: 0; right: 0; bottom: 0; height: 0.22in; background: var(--dark); color: #fff; font-size: 10px; display: flex; justify-content: space-between; align-items: center; padding: 0 0.4in; }
ul.bul { margin: 0.28in 0.55in 0; padding: 0; list-style: none; }
ul.bul li { font-size: 20px; margin: 0 0 10px; padding-left: 0.28in; position: relative; line-height: 1.25; }
ul.bul li::before { content: "•"; position: absolute; left: 0; color: var(--dark); }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 0.35in; margin: 0.32in 0.5in 0; }
.compact-split { margin-top: 0.22in; }
.compact-split .pane { display: flex; flex-direction: column; min-height: 5in; }
.compact-split .pane h2 { font-size: 20px; margin-bottom: 0.12in; }
.compact-split .pane-list.compact { flex: 1 1 auto; margin-bottom: 0.08in; }
.compact-split .pane-list.compact li { font-size: 13px; margin: 0 0 3px; }
.compact-split .pane-shot.tool-logo { margin-top: auto; }
.pane { min-height: 5in; padding: 0.22in 0.28in; }
.pane.cream { background: var(--teal); }
.pane.navy { background: var(--mid); color: #fff; }
.pane.dark { background: var(--dark); color: #fff; }
.pane h2 { margin: 0 0 0.2in; font-size: 22px; color: var(--dark); }
.pane.navy h2 { color: var(--orange); }
.pane.dark h2 { color: var(--teal); }
.pane ul { margin: 0; padding-left: 1.1em; }
.pane ul.compact li { font-size: 14px; margin: 0 0 4px; }
.pane-shot { display: block; width: 100%; max-height: 2.55in; margin-top: 0.1in; object-fit: contain; background: #fff; border: 1px solid rgba(34,66,72,.12); }
.pane-shot.compact { max-height: 2.05in; margin-top: 0.08in; }
.pane-shot.webbkoll-results { max-height: 1.35in; }
.pane-shot.ico-logo { max-height: 1.35in; background: #fff; padding: 0.05in; object-fit: contain; }
.pane-shot.keycdn-shot { max-height: 2.25in; margin-top: 0.1in; }
.pane-lead { margin: 0 0 0.08in; font-size: 15px; line-height: 1.3; }
.pane li { font-size: 16px; margin: 0 0 8px; }
.lead-finding { margin: 0.18in 0 0; font-size: 18px; font-weight: 700; color: var(--orange); line-height: 1.3; }
.summary-box { margin: 0.32in 0.5in 0; background: var(--teal); padding: 0.35in 0.4in; min-height: 4.85in; }
.summary-box p { font-size: 22px; line-height: 1.35; color: var(--dark); margin: 0 0 0.22in; }
.summary-box p:last-child { margin-bottom: 0; }
.summary-box p.lead { font-weight: 700; font-size: 20px; }
.summary-box p.lead.accent { color: var(--orange); }
.summary-box.close-summary p { color: var(--ink); font-weight: 700; }
.summary-box.close-summary p.accent { color: var(--ink); }
.summary-box.ico-summary p:not(.lead) { font-size: 18px; color: var(--dark); }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 0.35in; margin: 0.2in 0.5in 0; }
.two-col h3 { margin: 0 0 0.1in; font-size: 18px; }
.two-col > div:first-child h3 { color: var(--dark); }
.two-col > div:last-child h3 { color: var(--mid); }
.rank { padding: 0.06in 0.14in; margin-bottom: 0.06in; min-height: 0.78in; }
.rank.cream { background: var(--teal); }
.rank.grey { background: var(--mid); color: #fff; }
.rank strong { display: block; font-size: 16px; color: var(--dark); }
.rank.grey strong, .rank.grey span { color: #fff; }
.rank span { font-size: 14px; }
.caption { position: absolute; left: 0.4in; right: 0.4in; bottom: 0.32in; margin: 0; font-size: 13px; color: #4A5568; line-height: 1.3; }
.figs { display: grid; grid-template-columns: 6.5in 6in; gap: 0.15in; margin: 0.12in 0.3in 0; }
.figs img, .klass img { width: 100%; height: auto; display: block; }
.stack { display: flex; flex-direction: column; gap: 0.1in; }
.stack img { height: 2.45in; object-fit: contain; background: #fff; }
.figs > img { height: 5.15in; object-fit: contain; background: #fff; }
.klass { margin: 0.08in 0.4in 0; display: flex; flex-direction: column; align-items: center; gap: 0.06in; }
.klass img { max-height: 2.3in; width: auto; max-width: 12.5in; }
.klass img.keycdn { max-height: 2.7in; }
table { width: 12.5in; margin: 0.18in 0.4in 0; border-collapse: collapse; font-size: 13px; }
table.compact-table { margin-top: 0.08in; font-size: 12px; }
table.compact-table th, table.compact-table td { padding: 6px 8px; }
.ico-intro { margin: 0.12in 0.5in 0; font-size: 15px; line-height: 1.35; max-width: 12.3in; }
.ico-cap { bottom: 0.28in; }
th { background: var(--dark); color: #fff; text-align: left; padding: 8px; }
td { border: 1px solid #D0D5DD; padding: 9px 8px; }
tr:nth-child(even) td { background: var(--light); }
td.yes { color: var(--dark); font-weight: 700; }
td.part { color: var(--orange); font-weight: 700; background: var(--teal) !important; }
.banner-accent { margin: 0.22in 0.5in 0.1in; background: var(--orange); color: var(--dark); font-size: 22px; font-weight: 700; padding: 0.18in 0.22in; }
.site-layout { display: grid; grid-template-columns: 2.35in 1fr; gap: 0.2in; margin: 0.2in 0.5in 0; min-height: 5.72in; }
.site-logo-pane { background: var(--light); display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 0.45in 0.25in; }
.site-logo-pane img { width: 1.7in; height: 1.7in; object-fit: contain; background: #fff; border-radius: 0.08in; padding: 0.12in; }
.site-sector { margin: 0.28in 0 0; font-size: 13px; font-weight: 700; color: var(--mid); text-align: center; }
.site-cards { display: flex; flex-direction: column; gap: 0.22in; }
.site-layout:not(.dual) .site-cards { height: 100%; }
.site-layout:not(.dual) .site-card { flex: 1; }
.site-card { background: var(--teal); padding: 0.22in 0.28in 0.24in 0.34in; border-left: 0.12in solid transparent; }
.site-card.partial { background: var(--light); border-left-color: var(--orange); }
.site-card .label { margin: 0 0 0.04in; font-size: 10px; font-weight: 700; color: var(--mid); text-transform: uppercase; letter-spacing: .03em; }
.site-card h3 { margin: 0 0 0.12in; font-size: 17px; line-height: 1.25; color: var(--dark); }
.site-layout.dual .site-card h3 { font-size: 16px; }
.site-card .body { margin: 0 0 0.12in; font-size: 15px; line-height: 1.3; color: var(--ink); }
.site-layout.dual .site-card .body { font-size: 14px; }
.site-card .match { margin: 0; font-size: 15px; font-weight: 700; }
.site-card .match.yes { color: var(--dark); }
.site-card .match.part { color: var(--orange); }
.site-card .extra { margin: 0.1in 0 0; font-size: 12px; line-height: 1.3; color: #4A5568; }
.title-inner { padding: 0.9in 0.7in 0; }
.title-inner h1 { font-size: 28px; line-height: 1.2; margin: 0.12in 0 0.18in; }
.title-inner .assign { font-size: 24px; font-weight: 700; color: var(--teal); margin: 0.08in 0 0; }
.title-questions { margin: 0 0 0.22in; max-width: 11.8in; padding: 0; list-style: none; }
.title-questions li { font-size: 17px; line-height: 1.35; color: #fff; margin: 0 0 0.16in; padding-left: 0.28in; position: relative; }
.title-questions li::before { content: "•"; position: absolute; left: 0; color: #fff; }
.title-questions li:last-child { margin-bottom: 0; }
.title-inner .names { font-size: 16px; margin: 0; }
.title-band { position: absolute; left: 0; right: 0; bottom: 0; height: 1.65in; background: var(--orange); color: var(--dark); padding: 0 0.7in; font-size: 16px; display: flex; align-items: center; justify-content: space-between; }
.title-date { font-size: 16px; line-height: 1; }
.title-logo { width: 3.1in; height: auto; display: block; }
.q { text-align: center; padding-top: 2.4in; }
.q h1 { font-size: 48px; margin: 0 0 0.3in; }
.q p { font-size: 20px; color: var(--teal); }
@page { size: 13.333in 7.5in; margin: 0; }
@media print {
  html, body { background: #fff; }
  .toolbar { display: none; }
  .slide { margin: 0; box-shadow: none; }
}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ACIT4280 1A presentation</title>
  <style>{css}</style>
</head>
<body>
<div class="toolbar">Presentasjon i nettleseren. Trykk <b>Ctrl+P</b> og velg Lagre som PDF. Ikke bruk Microsoft Office Online (den siden feiler).</div>
{''.join(parts)}
</body>
</html>
"""
OUT.write_text(html, encoding="utf-8")
print("Wrote", OUT, "bytes", OUT.stat().st_size)
