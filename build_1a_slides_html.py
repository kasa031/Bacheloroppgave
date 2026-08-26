#!/usr/bin/env python3
"""Browser-printable 16:9 slides (Office Online cannot open the PPTX)."""
from pathlib import Path

OUT = Path("/workspace/ACIT4280_1A_presentation.html")
FIG = "figures"


def slide(inner: str, n: int, dark: bool = False) -> str:
    cls = "slide dark" if dark else "slide"
    foot = "" if dark and n == 1 else f"""
    <div class="foot"><span>ACIT4280 Group Assignment 1A  |  3 Sep 2026</span><span>{n} / 17</span></div>"""
    if dark and n in (1, 17):
        foot = ""
    return f'<section class="{cls}">{inner}{foot}</section>\n'


def header(kicker: str, title: str, speaker: str = "") -> str:
    sp = f'<div class="speaker">{speaker}</div>' if speaker else ""
    return f'<header><div class="kicker">{kicker}</div>{sp}<h1>{title}</h1></header>'


def bullets(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ul class="bul">{lis}</ul>'


parts = []

parts.append(slide(f"""
  <div class="title-inner">
    <p class="kicker">ACIT4280 Privacy by Design</p>
    <p class="assign">Group Assignment 1A</p>
    <h1>Analysis of 3rd-party data sharing<br>and data tracking and of GDPR<br>compliance of Norwegian web sites</h1>
    <p class="names">Humna Akhtar  ·  Mithun Chandra Debnath<br>Karina Sætersdal Nilssen  ·  Sumit Prasad Sah</p>
  </div>
  <div class="title-band">Oslo Metropolitan University<br>Due 3 September 2026</div>
""", 1, dark=True))


parts.append(slide(header("Structure", "The report has two parts") + """
<div class="split">
  <div class="pane cream">
    <h2>Part 1  ·  Webbkoll</h2>
    <ul>
      <li>18 Norwegian-facing sites</li>
      <li>Shopping, government, news/media, sport</li>
      <li>Server location, cookies, 3rd-party requests, countries excl. Norway</li>
      <li>Graphics per sector</li>
      <li>Highest and lowest contact; most countries; restrained e-government</li>
    </ul>
  </div>
  <div class="pane navy">
    <h2>Part 2  ·  ICO lawful basis</h2>
    <ul>
      <li>Five privacy notices</li>
      <li>skatteetaten, Netflix, fotball.no, document.no, babyshop.no</li>
      <li>One concrete purpose per ICO run</li>
      <li>Compare notice vs official ICO report</li>
      <li>Cookies, membership and checkout stay separate purposes</li>
    </ul>
  </div>
</div>
""", 2))

parts.append(slide(header("Part 1", "How we measured with Webbkoll") + bullets([
    "English Webbkoll interface",
    "One live Chromium visit: no add-ons, no Do Not Track, no consent click",
    "Scan clock on the result page is part of the measurement",
    "Server country: KeyCDN Country field for the IP",
    "Norway dropped from the shared-country list",
    "If KeyCDN returns no country: recorded as not available",
    "Two tables: Table 2 first measurement, Table 3 repeat measurement",
]), 3))

parts.append(slide(header("Part 1", "What Webbkoll does not do") + bullets([
    "It does not click Yes/No or Cookiebot.",
    "Zero third-party cookies can still mean many third-party requests.",
    "ikea.no is the only row with external cookies (2), after redirect to ikea.com.",
    "The two measurements are not averaged. A later visit can differ (24-hour store).",
    "Article 6 is not on the Webbkoll page. That is the ICO tool.",
]), 4))

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
""", 5))

parts.append(slide(header("Part 1  ·  Figures 2 to 4", "Third-party requests by site and sector") + f"""
<div class="figs">
  <img src="{FIG}/fig3_requests_all18.png" alt="Bar chart of third-party requests for 18 sites">
  <div class="stack">
    <img src="{FIG}/fig5_share_requests_pie.png" alt="Pie chart of request share">
    <img src="{FIG}/fig6_requests_per_sector.png" alt="Requests per sector">
  </div>
</div>
""", 6))

parts.append(slide(header("Part 1  ·  method example", "klassekampen.no: requests without third-party cookies") + f"""
<div class="klass">
  <img src="{FIG}/fig2_webbkoll_results_klassekampen.png" alt="Webbkoll results for klassekampen.no">
  <img class="keycdn" src="{FIG}/fig4_keycdn_lookup_klassekampen.png" alt="KeyCDN lookup for klassekampen server IP">
</div>
""", 7))

parts.append(slide(header("Part 2", "ICO lawful basis: one purpose at a time") + bullets([
    "Tool: ICO Lawful basis interactive guidance (updated 14 April 2026).",
    "Five services, one concrete processing activity per run.",
    "Find the privacy notice, run the tool, save the official Word report.",
    "Compare: what the notice claims vs what ICO marks APPROPRIATE.",
    "Do not mix cookies, marketing, membership and checkout in one run.",
    "UK tool also has recognised legitimate interest (five narrow public purposes). None of our five purposes fitted that list.",
]), 8))

parts.append(slide(header("Part 2", "Article 6 is not a cookie click") + """
<div class="split">
  <div class="pane cream">
    <h2>Article 6 (GDPR)</h2>
    <ul>
      <li>Why may we process this personal data?</li>
      <li>Contract, legal obligation, public task, consent, legitimate interests, vital interests</li>
      <li>Example: tax and folkeregister under named acts</li>
    </ul>
  </div>
  <div class="pane navy">
    <h2>ePrivacy / cookies</h2>
    <ul>
      <li>May we store/read info on the device?</li>
      <li>Necessary cookies: often no extra consent</li>
      <li>Analytics and ads: consent (Yes/No, Cookiebot)</li>
      <li>No test 24 Aug 2026 on skatteetaten.no/person/</li>
    </ul>
  </div>
</div>
""", 9))

table_rows = [
    ("skatteetaten.no", "Tax / folkeregister", "Legal obligation + public task", "Yes", "yes"),
    ("skatteetaten.no", "Optional cookies", "Consent INCONCLUSIVE; none APPROPRIATE", "Partial", "part"),
    ("netflix.no", "Paid streaming", "Contract", "Yes", "yes"),
    ("fotball.no", "Name + club, 13+", "Legitimate interests", "Yes", "yes"),
    ("document.no", "Google Signals", "Consent INCONCLUSIVE; none APPROPRIATE", "Partial", "part"),
    ("babyshop.no", "Checkout / delivery", "Contract", "Yes", "yes"),
]
tr = "".join(
    f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td class='{k}'>{d}</td></tr>"
    for a, b, c, d, k in table_rows
)
parts.append(slide(header("Part 2  ·  Table 5", "ICO result vs the notice") + f"""
<table>
  <thead><tr><th>Service</th><th>Purpose</th><th>ICO</th><th>Match</th></tr></thead>
  <tbody>{tr}</tbody>
</table>
""", 10))

parts.append(slide(header("ICO  ·  government", "skatteetaten.no: law for tax, consent for cookies") + bullets([
    "Purpose 1: identity, income and tax data for tax and folkeregister.",
    "Notice: first and foremost laid down in law. Opt-out generally not possible.",
    "Named acts: skatteforvaltningsloven, folkeregisterloven, skattebetalingsloven.",
    "Controller: the Director General of Taxation (Skattedirektøren).",
    "ICO: legal obligation APPROPRIATE, public task APPROPRIATE.",
    "Consent NOT APPROPRIATE for core tax (no genuine free choice). Contract and LI NOT APPROPRIATE.",
    "Purpose 2: optional stats cookies (Skyra, Matomo, GA, Siteimprove). Yes/No. ICO: consent INCONCLUSIVE (Q6). No basis APPROPRIATE.",
]), 11))

parts.append(slide(header("ICO  ·  news / media", "netflix.no: contract for the paid service") + bullets([
    "Purpose: account and payment data to provide the subscription.",
    "EEA/UK notice: contractual necessity to provide the service to members.",
    "ICO: Contract APPROPRIATE. All other bases NOT APPROPRIATE.",
    "Consent: not appropriate / likely invalid (no real ongoing choice).",
    "LI, legal obligation and consent in the notice apply to other purposes.",
    "Keep ads, recommendations and marketing out of this run.",
]), 12))

parts.append(slide(header("ICO  ·  sport", "fotball.no: legitimate interests for match history") + bullets([
    "Purpose: publish name and club of active players 13+ (kamphistorikk).",
    "Notice: public-interest match history, opt-out via the club.",
    "ICO: Legitimate interests APPROPRIATE after necessity + balancing.",
    "NFF is a sports federation, not a public authority (public task No).",
    "FIKS membership can use contract. That is a different purpose.",
    "Stamdata samtykke om publisering does not match ICO consent (likely invalid).",
    "Cookiebot (Deny on 26 Aug 2026) is also a different purpose.",
]), 13))

parts.append(slide(header("ICO  ·  news  ·  the mismatch", "document.no: Google Signals") + """
<div class="banner-red">ICO marks no basis APPROPRIATE. Consent is INCONCLUSIVE.</div>
""" + bullets([
    "Purpose: Google Signals / ad analytics (demographics, interests, cross-device).",
    "Notice does not name Article 6. Runs only if logged into Google with ad personalization.",
    "Opt-out: Google Ads Settings, mobile, NAI, Analytics add-on.",
    "Q5: consent request is not clear, prominent and separate from terms.",
    "Choice sits at Google. Pluss terms also say you accept the privacy notice by using the service.",
    "Contract and LI correctly rejected for this advertising purpose.",
    "Match: partial. They aim at consent; ICO says fix the request.",
]), 14))

parts.append(slide(header("ICO  ·  shopping", "babyshop.no: contract for checkout") + bullets([
    "Purpose: name, address, contact, order and payment to deliver goods.",
    "Terms point 1: a sales contract (18 years or guardian).",
    "ICO: Contract APPROPRIATE. Other bases NOT APPROPRIATE.",
    "Notice does not label Art. 6(1)(b). Section 5 is profiling, not purchase.",
    "Marketing/profiling: consent (separate). Cookie policy: necessary vs measurement vs marketing.",
    "Bundled consent to cookies inside the terms is not valid Art. 6 consent.",
]), 15))

parts.append(slide(header("Close", "What we want the room to remember") + bullets([
    "Webbkoll measures contact, not lawfulness.",
    "One purpose per ICO run, or the tool mixes bases.",
    "fotball.no has the highest request count and still zero third-party cookies.",
    "Four of five core ICO purposes match the notice.",
    "Two consent tests fail: skatteetaten cookies (Q6) and document.no Signals (Q5).",
    "Legal obligation (tax) is not the same as cookie consent (Yes/No).",
]), 16))

parts.append(slide("""
  <div class="q">
    <h1>Questions</h1>
    <p>ACIT4280 Privacy by Design  ·  Group Assignment 1A</p>
  </div>
""", 17, dark=True))

css = """
:root { --navy:#1B365D; --ink:#1A1A1A; --cream:#FFF1D1; --paper:#FFFEFB; --ok:#1B6B3A; --warn:#9A5B00; --red:#8B1E1E; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #333; font-family: Calibri, "Segoe UI", sans-serif; }
.toolbar { position: sticky; top: 0; z-index: 2; background: #111; color: #fff; padding: 8px 16px; font-size: 14px; }
.toolbar b { color: #FFF1D1; }
.slide {
  width: 13.333in; height: 7.5in; background: var(--paper); color: var(--ink);
  page-break-after: always; break-after: page; position: relative; overflow: hidden;
  margin: 12px auto; box-shadow: 0 8px 24px rgba(0,0,0,.35);
}
.slide.dark { background: var(--navy); color: #fff; }
header { background: var(--navy); color: #fff; height: 1.15in; padding: 0.12in 0.5in 0 0.5in; border-bottom: 0.08in solid var(--cream); }
header h1 { margin: 0; font-size: 28px; line-height: 1.15; }
.kicker { font-size: 12px; font-weight: 700; color: var(--cream); letter-spacing: .02em; }
header .kicker { display: inline-block; }
.speaker { float: right; font-size: 12px; font-weight: 700; color: var(--cream); }
.foot { position: absolute; left: 0; right: 0; bottom: 0; height: 0.22in; background: var(--navy); color: #fff; font-size: 10px; display: flex; justify-content: space-between; align-items: center; padding: 0 0.4in; }
ul.bul { margin: 0.28in 0.55in 0; padding: 0; list-style: none; }
ul.bul li { font-size: 20px; margin: 0 0 10px; padding-left: 0.28in; position: relative; line-height: 1.25; }
ul.bul li::before { content: "•"; position: absolute; left: 0; color: var(--navy); }
.cards { margin: 0.35in 0.5in 0; display: flex; flex-direction: column; gap: 0.12in; }
.card { background: var(--cream); border-left: 8px solid var(--navy); padding: 0.14in 0.22in; display: grid; grid-template-columns: 4.2in 1fr 1.3in; align-items: center; min-height: 1.05in; }
.card strong { font-size: 20px; color: var(--navy); }
.card span { font-size: 16px; }
.card em { font-style: normal; font-weight: 700; color: var(--navy); text-align: right; }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 0.35in; margin: 0.32in 0.5in 0; }
.pane { min-height: 5in; padding: 0.22in 0.28in; }
.pane.cream { background: var(--cream); }
.pane.navy { background: var(--navy); color: #fff; }
.pane h2 { margin: 0 0 0.2in; font-size: 22px; color: var(--navy); }
.pane.navy h2 { color: var(--cream); }
.pane ul { margin: 0; padding-left: 1.1em; }
.pane li { font-size: 16px; margin: 0 0 8px; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 0.35in; margin: 0.2in 0.5in 0; }
.two-col h3 { margin: 0 0 0.1in; color: var(--navy); font-size: 18px; }
.rank { padding: 0.08in 0.14in; margin-bottom: 0.08in; min-height: 0.85in; }
.rank.cream { background: var(--cream); }
.rank.grey { background: #F4F6F8; }
.rank strong { display: block; font-size: 16px; color: var(--navy); }
.rank span { font-size: 14px; }
.figs { display: grid; grid-template-columns: 6.5in 6in; gap: 0.15in; margin: 0.18in 0.3in 0; }
.figs img, .klass img { width: 100%; height: auto; display: block; }
.stack { display: flex; flex-direction: column; gap: 0.1in; }
.stack img { height: 2.65in; object-fit: contain; background: #fff; }
.figs > img { height: 5.5in; object-fit: contain; background: #fff; }
.klass { margin: 0.12in 0.4in 0; display: flex; flex-direction: column; align-items: center; gap: 0.08in; }
.klass img { max-height: 2.5in; width: auto; max-width: 12.5in; }
.klass img.keycdn { max-height: 2.95in; }
table { width: 12.5in; margin: 0.22in 0.4in 0; border-collapse: collapse; font-size: 13px; }
th { background: var(--navy); color: #fff; text-align: left; padding: 8px; }
td { border: 1px solid #D0D5DD; padding: 9px 8px; }
tr:nth-child(even) td { background: #F4F6F8; }
td.yes { color: var(--ok); font-weight: 700; }
td.part { color: var(--warn); font-weight: 700; background: var(--cream) !important; }
.banner-red { margin: 0.22in 0.5in 0.1in; background: var(--cream); color: var(--red); font-size: 22px; font-weight: 700; padding: 0.18in 0.22in; }
.title-inner { padding: 0.9in 0.7in 0; }
.title-inner h1 { font-size: 28px; line-height: 1.2; margin: 0.12in 0 0.35in; }
.title-inner .assign { font-size: 22px; font-weight: 700; color: var(--cream); margin: 0.08in 0 0; }
.title-inner .names { font-size: 18px; }
.title-band { position: absolute; left: 0; right: 0; bottom: 0; height: 1.65in; background: var(--cream); color: var(--navy); padding: 0.28in 0.7in; font-size: 16px; }
.q { text-align: center; padding-top: 2.4in; }
.q h1 { font-size: 48px; margin: 0 0 0.3in; }
.q p { font-size: 20px; color: var(--cream); }
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
