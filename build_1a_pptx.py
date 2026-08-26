#!/usr/bin/env python3
"""Build the ACIT4280 1A group presentation (16:9, 17 slides)."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import nsmap
from pptx.oxml import parse_xml
from pptx.util import Emu, Inches, Pt
from pathlib import Path

FIG = Path("/workspace/figures")

NAVY = RGBColor(0x1B, 0x36, 0x5D)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x4A, 0x55, 0x68)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CREAM = RGBColor(0xFF, 0xF1, 0xD1)
LINE = RGBColor(0xD0, 0xD5, 0xDD)
GREEN = RGBColor(0x1B, 0x6B, 0x3A)
AMBER = RGBColor(0x9A, 0x5B, 0x00)
RED = RGBColor(0x8B, 0x1E, 0x1E)
PAPER = RGBColor(0xFF, 0xFE, 0xFB)

W = Inches(13.333)
H = Inches(7.5)


def set_run(run, text, size=18, bold=False, color=INK, font="Calibri"):
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    run.font.italic = False


def add_rect(slide, l, t, w, h, fill):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background()
    return sh


def add_tb(slide, l, t, w, h, text, size=18, bold=False, color=INK, align=PP_ALIGN.LEFT, font="Calibri"):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    set_run(p.add_run() if p.runs else p.runs[0] if False else _first_run(p), text, size, bold, color, font)
    return box


def _first_run(p):
    if p.runs:
        return p.runs[0]
    return p.add_run()


def textbox(slide, l, t, w, h):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    return tf


def p_run(tf, text, size=18, bold=False, color=INK, space_before=0, space_after=6, align=PP_ALIGN.LEFT, font="Calibri"):
    if not tf.paragraphs[0].runs and not tf.paragraphs[0].text:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    r = p.add_run()
    set_run(r, text, size, bold, color, font)
    return p


def footer(slide, n, total=17):
    add_rect(slide, 0, Inches(7.28), W, Inches(0.22), NAVY)
    add_tb(slide, Inches(0.4), Inches(7.28), Inches(10), Inches(0.22),
           "ACIT4280 Group Assignment 1A  |  3 Sep 2026",
           size=10, color=WHITE)
    add_tb(slide, Inches(11.4), Inches(7.28), Inches(1.5), Inches(0.22),
           f"{n} / {total}", size=10, color=WHITE, align=PP_ALIGN.RIGHT)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def header_bar(slide, kicker, title, speaker=""):
    add_rect(slide, 0, 0, W, Inches(1.15), NAVY)
    add_rect(slide, 0, Inches(1.15), W, Inches(0.08), CREAM)
    add_tb(slide, Inches(0.5), Inches(0.12), Inches(8.2), Inches(0.32),
           kicker, size=12, color=CREAM, bold=True)
    if speaker:
        add_tb(slide, Inches(8.8), Inches(0.12), Inches(4.0), Inches(0.32),
               speaker, size=12, color=CREAM, bold=True, align=PP_ALIGN.RIGHT)
    add_tb(slide, Inches(0.5), Inches(0.42), Inches(12.3), Inches(0.62),
           title, size=28, color=WHITE, bold=True)


def bullet_slide(prs, n, kicker, title, bullets, note, sizes=None, speaker=""):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, kicker, title, speaker=speaker)
    tf = textbox(s, Inches(0.55), Inches(1.5), Inches(12.2), Inches(5.5))
    for i, b in enumerate(bullets):
        sz = (sizes[i] if sizes else 20)
        p_run(tf, b, size=sz, space_after=10)
    footer(s, n)
    notes(s, note)
    return s


def main():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]
    total = 17

    # 1 title
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, NAVY)
    add_rect(s, 0, Inches(5.85), W, Inches(1.65), CREAM)
    add_tb(s, Inches(0.7), Inches(0.85), Inches(12), Inches(0.35),
           "ACIT4280 Privacy by Design",
           size=16, color=CREAM, bold=True)
    add_tb(s, Inches(0.7), Inches(1.22), Inches(12), Inches(0.38),
           "Group Assignment 1A",
           size=22, color=CREAM, bold=True)
    add_tb(s, Inches(0.7), Inches(1.7), Inches(12), Inches(2.15),
           "Analysis of 3rd-party data sharing\nand data tracking and of GDPR\ncompliance of Norwegian web sites",
           size=28, color=WHITE, bold=True)
    add_tb(s, Inches(0.7), Inches(4.15), Inches(12), Inches(0.9),
           "Humna Akhtar  ·  Mithun Chandra Debnath  ·  Karina Sætersdal Nilssen",
           size=18, color=WHITE)
    add_tb(s, Inches(0.7), Inches(6.1), Inches(12), Inches(1.0),
           "Oslo Metropolitan University\nDue 3 September 2026",
           size=16, color=NAVY)
    notes(s, "Welcome. Two parts: Webbkoll on 18 sites, then ICO on five privacy notices.")

    # 2 two parts
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Structure", "The report has two parts")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(5.9), Inches(5.0), CREAM)
    add_tb(s, Inches(0.75), Inches(1.75), Inches(5.4), Inches(0.4), "Part 1  ·  Webbkoll", size=22, bold=True, color=NAVY)
    tf = textbox(s, Inches(0.75), Inches(2.3), Inches(5.4), Inches(4.0))
    for line in [
        "18 course-listed sites (Table 1)",
        "Shopping, government, news/media/entertainment, spare time/sports",
        "Columns: server country, internal/external cookies, 3rd-party requests, countries excl. Norway",
        "Figures 2-4: all 18 sites, share, sector totals",
        "Rank on Table 2 requests, not cookies",
    ]:
        p_run(tf, "•  " + line, size=16, space_after=8)
    add_rect(s, Inches(6.9), Inches(1.55), Inches(5.9), Inches(5.0), NAVY)
    add_tb(s, Inches(7.15), Inches(1.75), Inches(5.4), Inches(0.4), "Part 2  ·  ICO lawful basis", size=22, bold=True, color=CREAM)
    tf = textbox(s, Inches(7.15), Inches(2.3), Inches(5.4), Inches(4.0))
    for line in [
        "Five notices from Table 1a (one shopping, one government, two news, one sport)",
        "babyshop, skatteetaten, Netflix, document.no, fotball.no",
        "One concrete purpose per ICO run",
        "Compare notice vs official ICO Word report (26 Aug 2026)",
        "Cookies, membership and checkout stay separate purposes",
    ]:
        p_run(tf, "•  " + line, size=16, color=WHITE, space_after=8)
    footer(s, 2, total)
    notes(s, "Table 1 is the 18 Canvas names. Table 1a is why we picked the five. Stress one purpose at a time.")

    # 4 method
    bullet_slide(
        prs, 3, "Part 1", "How we measured with Webbkoll",
        [
            "English Webbkoll; one live Chromium visit: no add-ons, no Do Not Track",
            "Server country = KeyCDN of the site IP; country list = KeyCDN of third-party IPs",
            "Norway dropped from the country count (the list may still print NO)",
            "n/a = KeyCDN returned no country (dnt.no, babyshop.no, altinn.no on Table 3)",
            "Table 2 = first scan and ranking base; Table 3 = later check, not averaged",
            "Request count is not the same as cookie count",
        ],
        "Webbkoll does not read a privacy notice and does not decide Article 6. Request volume is not cookie volume.",
        sizes=[18]*6,
    )

    # 5 rules
    bullet_slide(
        prs, 4, "Part 1", "What Webbkoll does not do",
        [
            "It does not decide Article 6. That is the ICO tool.",
            "A high request count is not a cookie count.",
            "ikea.no is the only row with external cookies (2), after redirect to ikea.com.",
            "babyshop.no is 101 requests on Table 3, but 45 on Table 2. Rankings stay on Table 2.",
            "Article 6 is not on the Webbkoll page. That is the ICO tool.",
        ],
        "skatteetaten.no: 5 internal cookies, 0 external cookies on Table 2. The ICO cookie row tests the notice, not that Webbkoll count.",
    )

    # 6 highest lowest
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  Table 4", "Highest and lowest third-party requests")
    # two columns of cards
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
    add_tb(s, Inches(0.5), Inches(1.4), Inches(6), Inches(0.4), "Highest five", size=18, bold=True, color=NAVY)
    add_tb(s, Inches(7.0), Inches(1.4), Inches(6), Inches(0.4), "Lowest five", size=18, bold=True, color=NAVY)
    y = Inches(1.78)
    for (a, b), (c, d) in zip(high, low):
        add_rect(s, Inches(0.5), y, Inches(5.9), Inches(0.82), CREAM)
        add_tb(s, Inches(0.7), y + Inches(0.06), Inches(5.5), Inches(0.32), a, size=16, bold=True, color=NAVY)
        add_tb(s, Inches(0.7), y + Inches(0.38), Inches(5.5), Inches(0.32), b, size=14, color=INK)
        add_rect(s, Inches(7.0), y, Inches(5.8), Inches(0.82), RGBColor(0xF4, 0xF6, 0xF8))
        add_tb(s, Inches(7.2), y + Inches(0.06), Inches(5.4), Inches(0.32), c, size=16, bold=True, color=NAVY)
        add_tb(s, Inches(7.2), y + Inches(0.38), Inches(5.4), Inches(0.32), d, size=14, color=INK)
        y += Inches(0.9)
    add_tb(s, Inches(0.5), Inches(6.85), Inches(12.3), Inches(0.38),
           "Table 2 request column. Highest 1 = worst sharer. Lowest 1 = most restrained. babyshop 101 is Table 3 only.",
           size=13, color=MUTED)
    footer(s, 5, total)
    notes(s, "Rank is third-party REQUESTS on Table 2, not cookies. The repeat measurement puts babyshop.no at 101; rankings follow the first measurement. skatteetaten.no also 14 requests; skiforeningen listed because fewer countries.")

    # 7 findings + charts
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  Figures 2 to 4", "Third-party requests by site and sector")
    s.shapes.add_picture(str(FIG / "fig3_requests_all18.png"), Inches(0.3), Inches(1.32), Inches(6.5), Inches(5.15))
    s.shapes.add_picture(str(FIG / "fig5_share_requests_pie.png"), Inches(6.95), Inches(1.32), Inches(6.0), Inches(2.5))
    s.shapes.add_picture(str(FIG / "fig6_requests_per_sector.png"), Inches(6.95), Inches(3.9), Inches(6.0), Inches(2.55))
    add_tb(s, Inches(0.4), Inches(6.85), Inches(12.5), Inches(0.38),
           "All three charts use Table 2. News/media is the largest sector total; government is the smallest; sport is high because of fotball.no.",
           size=13, color=MUTED)
    footer(s, 6, total)
    notes(s, "Point to fotball.no at 113 and lanekassen.no at 1. Request volume is not cookie volume. Do not read the pie as cookies.")

    # 8 klassekampen
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  method example", "klassekampen.no: 46 on the ranking, 56 on the screenshot")
    s.shapes.add_picture(str(FIG / "fig2_webbkoll_results_klassekampen.png"), Inches(0.4), Inches(1.32), Inches(12.5), Inches(2.35))
    s.shapes.add_picture(str(FIG / "fig4_keycdn_lookup_klassekampen.png"), Inches(2.4), Inches(3.78), Inches(8.5), Inches(2.85))
    add_tb(s, Inches(0.4), Inches(6.7), Inches(12.5), Inches(0.5),
           "Table 2 rank: 46 requests, 0 third-party cookies. Screenshots = later visit (Table 3: 56 requests to 13 hosts). Server KeyCDN: United States, Google.",
           size=13, color=MUTED)
    footer(s, 7, total)
    notes(s, "Say the number on the screenshot is 56 because that is the later scan. The ranking in Table 4 is 46 from Table 2. Zero third-party cookies either way.")

    # 9 ICO intro
    bullet_slide(
        prs, 8, "Part 2", "ICO lawful basis: one purpose at a time",
        [
            "Tool: ICO Lawful basis interactive guidance. Official Word reports dated 26 August 2026.",
            "Five services from Table 1a. One concrete processing activity per run.",
            "Compare: what the notice claims vs what ICO marks APPROPRIATE.",
            "Match Yes = they line up for that purpose. Partial = notice aims at consent, ICO marks INCONCLUSIVE.",
            "Do not mix cookies, marketing, membership and checkout in one run.",
            "UK recognised legitimate interest did not fit any of our five purposes.",
        ],
        "Hold up that we used official ICO reports dated 26 August 2026.",
        sizes=[18]*6,
    )

    # 10 art 6 vs cookies
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2", "One purpose per ICO run")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(5.9), Inches(5.0), CREAM)
    add_tb(s, Inches(0.75), Inches(1.8), Inches(5.4), Inches(0.5), "Article 6 (GDPR)", size=22, bold=True, color=NAVY)
    tf = textbox(s, Inches(0.75), Inches(2.45), Inches(5.4), Inches(3.8))
    for line in [
        "Why may we process this personal data?",
        "Contract, legal obligation, public task, consent, legitimate interests",
        "Example: tax and folkeregister under named acts",
    ]:
        p_run(tf, "•  " + line, size=16, space_after=10)
    add_rect(s, Inches(6.9), Inches(1.55), Inches(5.9), Inches(5.0), NAVY)
    add_tb(s, Inches(7.15), Inches(1.8), Inches(5.4), Inches(0.5), "Keep purposes apart", size=22, bold=True, color=CREAM)
    tf = textbox(s, Inches(7.15), Inches(2.45), Inches(5.4), Inches(3.8))
    for line in [
        "Tax data is not optional statistics cookies",
        "Checkout is not marketing",
        "Match lists are not FIKS membership",
        "Mix them in one ICO run and the tool mixes the bases",
    ]:
        p_run(tf, "•  " + line, size=16, color=WHITE, space_after=10)
    footer(s, 9, total)
    notes(s, "skatteetaten has two ICO rows because the notice has two purposes. The 18-site Webbkoll table is Part 1 only.")

    # 11 table 5
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2  ·  Table 5", "ICO result vs the notice")
    data = [
        ("Service", "Purpose", "ICO", "Match"),
        ("skatteetaten.no", "Tax / folkeregister", "Legal obligation + public task", "Yes"),
        ("skatteetaten.no", "Optional cookies", "Consent INCONCLUSIVE; none APPROPRIATE", "Partial"),
        ("netflix.no", "Paid streaming", "Contract", "Yes"),
        ("fotball.no", "Name + club, 13+", "Legitimate interests", "Yes"),
        ("document.no", "Google Signals", "Consent INCONCLUSIVE; none APPROPRIATE", "Partial"),
        ("babyshop.no", "Checkout / delivery", "Contract", "Yes"),
    ]
    left = Inches(0.4)
    top = Inches(1.4)
    widths = [Inches(2.6), Inches(3.2), Inches(5.3), Inches(1.4)]
    row_h = Inches(0.68)
    x = left
    for w, htxt in zip(widths, data[0]):
        add_rect(s, x, top, w, row_h, NAVY)
        add_tb(s, x + Inches(0.08), top + Inches(0.18), w - Inches(0.1), Inches(0.4), htxt, size=13, bold=True, color=WHITE)
        x += w
    for i, row in enumerate(data[1:]):
        y = top + row_h * (i + 1)
        bg = CREAM if row[3] == "Partial" else (RGBColor(0xF4, 0xF6, 0xF8) if i % 2 else WHITE)
        x = left
        colors = [INK, INK, INK, GREEN if row[3] == "Yes" else AMBER]
        bolds = [True, False, False, True]
        for j, (w, cell) in enumerate(zip(widths, row)):
            add_rect(s, x, y, w, row_h, bg)
            add_tb(s, x + Inches(0.08), y + Inches(0.18), w - Inches(0.12), Inches(0.45), cell, size=13, bold=bolds[j], color=colors[j])
            x += w
    add_tb(s, Inches(0.4), Inches(6.72), Inches(12.5), Inches(0.5),
           "Each row is one purpose. Yes = notice and ICO line up. Partial = they aim at consent, but ICO marks consent INCONCLUSIVE and no basis APPROPRIATE.",
           size=13, color=MUTED)
    footer(s, 10, total)
    notes(s, "Four of five core purposes match. Two consent tests fail: skatteetaten cookies (Q6) and document.no Signals (request not separate from terms).")

    # 12 skatteetaten
    bullet_slide(
        prs, 11, "ICO  ·  government", "skatteetaten.no: law for tax, consent for cookies",
        [
            "Purpose 1: identity, income and tax data for tax and folkeregister.",
            "Notice: first and foremost laid down in law. Opt-out generally not possible.",
            "Named acts: skatteforvaltningsloven, folkeregisterloven, skattebetalingsloven.",
            "Controller: the Director General of Taxation (Skattedirektøren).",
            "ICO: legal obligation APPROPRIATE, public task APPROPRIATE.",
            "Consent NOT APPROPRIATE for core tax (no genuine free choice). Contract and LI NOT APPROPRIATE.",
            "Purpose 2: optional stats cookies in the notice. ICO: consent INCONCLUSIVE (Q6). No basis APPROPRIATE.",
        ],
        "Two purposes, two reports. Table 5 cookie row tests the notice.",
        sizes=[16]*7,
    )

    # 13 netflix
    bullet_slide(
        prs, 12, "ICO  ·  news / media", "netflix.no: contract for the paid service",
        [
            "Purpose: account and payment data to provide the subscription.",
            "EEA/UK notice: contractual necessity to provide the service to members.",
            "ICO: Contract APPROPRIATE. All other bases NOT APPROPRIATE.",
            "Consent: not appropriate / likely invalid (no real ongoing choice).",
            "LI, legal obligation and consent in the notice apply to other purposes.",
            "Keep ads, recommendations and marketing out of this run.",
        ],
        "Netflix requires 18 or a parent.",
        sizes=[18]*6,
    )

    # 14 fotball
    bullet_slide(
        prs, 13, "ICO  ·  sport", "fotball.no: legitimate interests for match history",
        [
            "Purpose: publish name and club of active players 13+ (kamphistorikk).",
            "Notice: public-interest match history, opt-out via the club.",
            "ICO: Legitimate interests APPROPRIATE after necessity + balancing.",
            "NFF is a sports federation, not a public authority (public task No).",
            "FIKS membership can use contract. That is a different purpose and was not this run.",
            "This ICO run is match-history publication only.",
        ],
        "ICO also points to an LIA and children's-data guidance for 13-17.",
        sizes=[17]*6,
    )

    # 15 document
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "ICO  ·  news  ·  the mismatch", "document.no: Google Signals")
    add_rect(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(1.2), CREAM)
    add_tb(s, Inches(0.7), Inches(1.65), Inches(12), Inches(0.9),
           "ICO marks no basis APPROPRIATE. Consent is INCONCLUSIVE.",
           size=22, bold=True, color=RED)
    tf = textbox(s, Inches(0.55), Inches(2.9), Inches(12.2), Inches(4.0))
    for line in [
        "Purpose: Google Signals / ad analytics (demographics, interests, cross-device).",
        "Notice does not name Article 6. Runs only if logged into Google with ad personalization.",
        "Opt-out: Google Ads Settings, mobile, NAI, Analytics add-on.",
        "Q5: consent request is not clear, prominent and separate from terms.",
        "Choice sits at Google. Pluss terms also say you accept the privacy notice by using the service.",
        "Contract and LI correctly rejected for this advertising purpose.",
        "Match: partial. They aim at consent; ICO says fix the request.",
    ]:
        p_run(tf, "•  " + line, size=17, space_after=8)
    footer(s, 14, total)
    notes(s, "This is the strongest 1A finding: a notice can talk like consent and still fail the ICO consent standard.")

    # 16 babyshop
    bullet_slide(
        prs, 15, "ICO  ·  shopping", "babyshop.no: contract for checkout",
        [
            "Purpose: name, address, contact, order and payment to deliver goods.",
            "Terms point 1: a sales contract (18 years or guardian).",
            "ICO: Contract APPROPRIATE. Other bases NOT APPROPRIATE.",
            "Notice does not label Art. 6(1)(b). Section 5 is profiling, not purchase.",
            "Marketing/profiling: consent (separate purpose). Cookie categories in the notice stay off this ICO run.",
        ],
        "Same pattern as Netflix: contract for the core service, consent for ads.",
        sizes=[18]*5,
    )

    # 17 takeaways
    bullet_slide(
        prs, 16, "Close", "What we want the room to remember",
        [
            "Webbkoll measures contact, not lawfulness.",
            "Rankings follow Table 2. Table 3 is a check. Do not average them.",
            "fotball.no has the highest request count (113) and still zero third-party cookies.",
            "Four of five core ICO purposes match the notice (Table 5).",
            "Two consent tests fail: skatteetaten cookies (Q6) and document.no Signals (Q5).",
            "Legal obligation (tax) is not the same ICO purpose as optional cookies.",
        ],
        "Then questions. If asked about access requests: that is outside the scope of this report.",
        sizes=[20]*6,
    )

    # 18 questions
    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, NAVY)
    add_tb(s, Inches(0.7), Inches(2.4), Inches(12), Inches(1.2),
           "Questions", size=48, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_tb(s, Inches(0.7), Inches(3.8), Inches(12), Inches(1.4),
           "ACIT4280 Privacy by Design  ·  Group Assignment 1A",
           size=20, color=CREAM, align=PP_ALIGN.CENTER)
    notes(s, "Likely questions: why not test Document Pluss as contract (would duplicate Netflix); why LI for football names (notice + opt-out + limited data).")

    out = "/workspace/ACIT4280_1A_presentation.pptx"
    prs.save(out)
    print("Wrote", out, "slides", len(prs.slides))


if __name__ == "__main__":
    main()
