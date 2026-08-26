#!/usr/bin/env python3
"""Browser-printable 16:9 slides (Office Online cannot open the PPTX)."""
from pathlib import Path

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


parts = []

parts.append(slide(f"""
  <div class="title-inner">
    <p class="kicker">ACIT4280 Privacy by Design</p>
    <p class="assign">Group Assignment 1A</p>
    <h1>Analysis of 3rd-party Data Sharing<br>and Data Tracking and of GDPR<br>Compliance of Norwegian Web Sites</h1>
    <ul class="title-questions">
      <li>When you open a front page, who else does it contact - and where in the world are those servers?</li>
      <li>When a site uses personal data, does it have a lawful basis - and does that claim hold up?</li>
    </ul>
    <p class="names">Humna Akhtar  ·  Mithun Chandra Debnath  ·  Karina Sætersdal Nilssen</p>
  </div>
  <div class="title-band"><span class="title-date">3 September 2026</span><img class="title-logo" src="{FIG}/oslomet_logo.svg" alt="OsloMet logo"></div>
""", 1, dark=True))


parts.append(slide(header("Our approach", "Two questions, two tools") + """
<div class="split compact-split">
  <div class="pane cream">
    <h2>Part 1  ·  Webbkoll</h2>
    <ul class="pane-list compact">
      <li>18 Norwegian front pages - one clean visit each</li>
      <li>Who do they call? Cookies, requests, server country (first scan, 20 Aug)</li>
      <li>KeyCDN shows where servers sit - a guess, not proof of lawful transfer</li>
    </ul>
    <img class="pane-shot compact webbkoll-results" src="{FIG}/fig2_webbkoll_results_klassekampen.png" alt="Webbkoll results for klassekampen.no">
  </div>
  <div class="pane navy">
    <h2>Part 2  ·  ICO</h2>
    <ul class="pane-list compact">
      <li>Five sites - one purpose per run, because mixed questions break the test</li>
      <li>Does the privacy notice match the ICO report? (26 Aug 2026)</li>
      <li>Yes when notice and ICO tell the same story</li>
      <li>Partial when consent wording fails the checklist</li>
      <li>Tax, cookies, checkout and ads are not the same question</li>
    </ul>
  </div>
</div>
""", 2))

parts.append(slide(header("Part 1", "Your browser talks to strangers") + """
<div class="split">
  <div class="pane cream">
    <h2>What Webbkoll reveals</h2>
    <p class="pane-lead">Every front page starts a conversation - Webbkoll records who joins it.</p>
    <p class="lead-finding">Many requests does not mean many cookies.</p>
    <img class="pane-shot keycdn-shot" src="{FIG}/fig4_keycdn_lookup_klassekampen.png" alt="KeyCDN lookup for klassekampen server IP">
  </div>
  <div class="pane dark">
    <h2>Key findings</h2>
    <ul>
      <li>fotball.no: 113 hosts, zero third-party cookies - loud, but not cookie-heavy.</li>
      <li>17 of 18 sites: no third-party cookies on load. ikea.no was the exception (2).</li>
      <li>lanekassen.no (1) and altinn.no (5): the quietest public-sector doors.</li>
      <li>document.no: data paths touch 6 countries, excluding Norway.</li>
      <li>News and media reach out most. Government pages reach out least.</li>
      <li>babyshop.no doubled on repeat scan (45 to 101) - rankings stay on the first scan.</li>
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
parts.append(slide(header("Part 1", "The loud and the quiet") + f"""
<div class="two-col">
  <div><h3>Highest five</h3>{hi_html}</div>
  <div><h3>Lowest five</h3>{lo_html}</div>
</div>
<p class="caption">Same question, different answers: fotball.no shouts (113), lanekassen.no barely whispers (1). Rankings follow the first scan.</p>
""", 4))

parts.append(slide(header("Part 1  ·  Figures 2 to 4", "Where the traffic goes") + f"""
<div class="figs">
  <img src="{FIG}/fig3_requests_all18.png" alt="Bar chart of third-party requests for 18 sites">
  <div class="stack">
    <img src="{FIG}/fig5_share_requests_pie.png" alt="Pie chart of request share">
    <img src="{FIG}/fig6_requests_per_sector.png" alt="Requests per sector">
  </div>
</div>
<p class="caption">News and media pull the most strings on load. Government pages keep the fewest.</p>
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

parts.append(slide(header("Part 2", "Does the privacy notice mean what it says?") + f"""
<p class="ico-intro">One purpose per ICO run (26 Aug 2026). We ask: does the site\'s legal story hold up? Yes when notice and ICO agree. Partial when consent is INCONCLUSIVE.</p>
<table class="compact-table">
  <thead><tr><th>Service</th><th>Purpose</th><th>ICO</th><th>Match</th></tr></thead>
  <tbody>{tr}</tbody>
</table>
<p class="caption ico-cap">ICO guidance is not a court verdict - but it shows where the story breaks.</p>
""", 6))

parts.append(slide(header("Part 2", "Four honest answers, two broken promises") + """
<div class="summary-box ico-summary">
  <p class="lead">Four purposes hold up: tax by law, streaming by contract, match history by interest, checkout by contract.</p>
  <p class="lead accent">Two consent claims fail: Skatteetaten optional cookies and document.no Google Signals.</p>
  <p>Both notices say consent - but the ICO marks consent INCONCLUSIVE.</p>
  <p>Skatteetaten does not say clearly enough who runs the optional cookies or how to refuse. document.no sends you to Google ad settings - not a clear, separate choice - and Pluss terms bundle the notice.</p>
</div>
""", 7))

parts.append(slide(header("Part 2", "skatteetaten.no: duty and choice") + bullets([
    "Tax and registry data: the law requires it. You cannot opt out of being counted.",
    "ICO: legal obligation and public task APPROPRIATE. Consent NOT APPROPRIATE. Match: Yes.",
    "Optional statistics cookies: the notice says you can choose - but does it explain how?",
    "ICO: consent INCONCLUSIVE; no basis APPROPRIATE. Match: Partial.",
]), 8))

parts.append(slide(header("Part 2", "netflix.no: pay to watch") + bullets([
    "Purpose: account and payment data to deliver what you paid for.",
    "Notice (EEA/UK): contractual necessity - not consent.",
    "ICO: contract APPROPRIATE. Consent marked likely invalid for this purpose.",
    "Ads and marketing in the same notice were left out - different purpose, different basis.",
]), 9))

parts.append(slide(header("Part 2", "fotball.no: a name on the team sheet") + bullets([
    "Purpose: name and club of active players aged 13+, with club opt-out.",
    "ICO: legitimate interests APPROPRIATE - sport transparency, not blanket consent.",
    "NFF is not a public authority, so public task does not fit.",
    "FIKS membership is a different purpose and was not this run.",
]), 10))

parts.append(slide(header("Part 2", "document.no: consent without a real choice") + """
<div class="banner-accent">ICO: no basis APPROPRIATE. Consent INCONCLUSIVE. Match: Partial.</div>
""" + bullets([
    "Purpose: advertising analytics built from what you read and click.",
    "The notice never names Article 6 - but it reads like consent.",
    "ICO: the request is not clear, prominent and separate from terms.",
    "The choice lives in Google settings. Pluss terms also bundle the notice.",
]), 11))

parts.append(slide(header("Part 2", "babyshop.no: pay to receive") + bullets([
    "Purpose: name, address, contact, order and payment to deliver goods.",
    "The sales terms are a purchase contract - you pay, they ship.",
    "ICO: contract APPROPRIATE. Match: Yes for checkout.",
    "The notice does not label Article 6(1)(b). Marketing is a separate purpose.",
]), 12))

parts.append(slide(header("Close", "What we learned") + """
<div class="summary-box close-summary">
  <p>Opening a Norwegian front page starts a hidden conversation - we mapped 18 of them.</p>
  <p>Many sites reach out widely without setting a single third-party cookie.</p>
  <p>Four of five ICO purposes match what the notice claims.</p>
  <p class="accent">Where sites say consent, the wording must be real - in two cases, the ICO says it is not.</p>
</div>
""", 13))

parts.append(slide("""
  <div class="q">
    <h1>Questions?</h1>
    <p class="q-hook">Who else does your browser meet - and does the privacy notice tell the truth?</p>
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
.compact-split .pane h2 { font-size: 20px; margin-bottom: 0.12in; }
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
.pane-shot.keycdn-shot { max-height: 2.25in; margin-top: 0.1in; }
.pane-lead { margin: 0 0 0.08in; font-size: 15px; line-height: 1.3; }
.pane li { font-size: 16px; margin: 0 0 8px; }
.lead-finding { margin: 0.18in 0 0; font-size: 18px; font-weight: 700; color: var(--orange); line-height: 1.3; }
.summary-box { margin: 0.32in 0.5in 0; background: var(--teal); padding: 0.35in 0.4in; min-height: 4.85in; }
.summary-box p { font-size: 22px; line-height: 1.35; color: var(--dark); margin: 0 0 0.22in; }
.summary-box p:last-child { margin-bottom: 0; }
.summary-box p.lead { font-weight: 700; font-size: 20px; }
.summary-box p.lead.accent { color: var(--orange); }
.summary-box p.accent { color: var(--orange); }
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
.q h1 { font-size: 48px; margin: 0 0 0.22in; }
.q p { font-size: 18px; color: var(--teal); margin: 0 0 0.12in; }
.q p.q-hook { font-size: 20px; max-width: 10in; margin: 0 auto 0.28in; line-height: 1.35; }
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
