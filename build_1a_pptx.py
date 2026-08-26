#!/usr/bin/env python3
"""Build the ACIT4280 1A group presentation (16:9, 15 slides)."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from pathlib import Path

FIG = Path("/workspace/figures")

NAVY = RGBColor(0x1B, 0x36, 0x5D)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x4A, 0x55, 0x68)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CREAM = RGBColor(0xFF, 0xF1, 0xD1)
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
    set_run(_first_run(p), text, size, bold, color, font)
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


def footer(slide, n, total=15):
    add_rect(slide, 0, Inches(7.28), W, Inches(0.22), NAVY)
    add_tb(slide, Inches(0.4), Inches(7.28), Inches(10), Inches(0.22),
           "ACIT4280 Group Assignment 1A  |  3 Sep 2026",
           size=10, color=WHITE)
    add_tb(slide, Inches(11.4), Inches(7.28), Inches(1.5), Inches(0.22),
           f"{n} / {total}", size=10, color=WHITE, align=PP_ALIGN.RIGHT)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def header_bar(slide, kicker, title):
    add_rect(slide, 0, 0, W, Inches(1.15), NAVY)
    add_rect(slide, 0, Inches(1.15), W, Inches(0.08), CREAM)
    add_tb(slide, Inches(0.5), Inches(0.12), Inches(12.3), Inches(0.32),
           kicker, size=12, color=CREAM, bold=True)
    add_tb(slide, Inches(0.5), Inches(0.42), Inches(12.3), Inches(0.62),
           title, size=28, color=WHITE, bold=True)


def bullet_slide(prs, n, kicker, title, bullets, note, sizes=None):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, kicker, title)
    tf = textbox(s, Inches(0.55), Inches(1.5), Inches(12.2), Inches(5.5))
    for i, b in enumerate(bullets):
        sz = (sizes[i] if sizes else 22)
        p_run(tf, b, size=sz, space_after=12)
    footer(s, n)
    notes(s, note)
    return s


def main():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]
    total = 15

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, NAVY)
    add_rect(s, 0, Inches(5.85), W, Inches(1.65), CREAM)
    add_tb(s, Inches(0.7), Inches(0.85), Inches(12), Inches(0.35),
           "ACIT4280 Privacy by Design",
           size=16, color=CREAM, bold=True)
    add_tb(s, Inches(0.7), Inches(1.22), Inches(12), Inches(0.38),
           "Group Assignment 1A",
           size=22, color=CREAM, bold=True)
    add_tb(s, Inches(0.7), Inches(1.7), Inches(12), Inches(1.85),
           "Analysis of 3rd-party Data Sharing\nand Data Tracking and of GDPR\nCompliance of Norwegian Web Sites",
           size=26, color=WHITE, bold=True)
    tf_q = textbox(s, Inches(0.7), Inches(3.62), Inches(12), Inches(1.35))
    p_run(tf_q,
          "When a person opens a Norwegian-facing front page, how many other companies does that page contact, "
          "and in which countries do those machines appear to sit?",
          size=15, color=CREAM, space_after=8)
    p_run(tf_q,
          "When a site uses personal data, has it named a GDPR Article 6 basis, "
          "and does that basis hold in the ICO tool?",
          size=15, color=CREAM, space_after=0)
    add_tb(s, Inches(0.7), Inches(5.05), Inches(12), Inches(0.55),
           "Humna Akhtar  ·  Mithun Chandra Debnath  ·  Karina Sætersdal Nilssen",
           size=16, color=WHITE)
    add_tb(s, Inches(0.7), Inches(6.1), Inches(12), Inches(1.0),
           "Oslo Metropolitan University\n3 September 2026",
           size=16, color=NAVY)
    notes(s, "Part 1 measures contact. Part 2 tests one purpose at a time.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "The report", "Two questions")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(5.9), Inches(5.0), CREAM)
    add_tb(s, Inches(0.75), Inches(1.75), Inches(5.4), Inches(0.4), "Part 1  ·  Webbkoll", size=22, bold=True, color=NAVY)
    tf = textbox(s, Inches(0.75), Inches(2.3), Inches(5.4), Inches(4.0))
    for line in [
        "18 sites in four sectors (Table 1)",
        "Cookies, third-party requests, KeyCDN countries",
        "Rank Table 2 requests, not cookies",
        "Figures 2 to 4: counts, share, sectors",
    ]:
        p_run(tf, "•  " + line, size=18, space_after=10)
    add_rect(s, Inches(6.9), Inches(1.55), Inches(5.9), Inches(5.0), NAVY)
    add_tb(s, Inches(7.15), Inches(1.75), Inches(5.4), Inches(0.4), "Part 2  ·  ICO", size=22, bold=True, color=CREAM)
    tf = textbox(s, Inches(7.15), Inches(2.3), Inches(5.4), Inches(4.0))
    for line in [
        "Five sites from Table 1a",
        "One purpose per ICO run",
        "Notice versus ICO Word report (26 Aug 2026)",
        "Table 5: Yes or Partial",
    ]:
        p_run(tf, "•  " + line, size=18, color=WHITE, space_after=10)
    footer(s, 2, total)
    notes(s, "Contact and lawful basis are different questions. A high request count is not a finding of unlawful processing.")

    bullet_slide(
        prs, 3, "Part 1", "How we measured",
        [
            "English Webbkoll. One load per visit. No add-ons. Do Not Track off.",
            "Table 2 (20 Aug 2026) is the ranking. Table 3 is a later check, not averaged.",
            "KeyCDN country is a geolocation guess from the IP, not a legal transfer register.",
            "Requests are not cookies. 17 of 18 sites had zero external cookies. ikea.no had 2.",
        ],
        "Webbkoll records what one load contacted. It does not read the notice or decide Article 6.",
        sizes=[20]*4,
    )

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  Table 4", "Highest and lowest third-party requests")
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
           "Ranked on Table 2 requests. lanekassen.no and altinn.no have the fewest government requests. babyshop.no is 101 on Table 3; rankings stay on Table 2.",
           size=13, color=MUTED)
    footer(s, 4, total)
    notes(s, "fotball.no has 113 requests and zero third-party cookies. document.no has the widest country list (6).")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  Figures 2 to 4", "Third-party requests by site and sector")
    s.shapes.add_picture(str(FIG / "fig3_requests_all18.png"), Inches(0.3), Inches(1.32), Inches(6.5), Inches(5.15))
    s.shapes.add_picture(str(FIG / "fig5_share_requests_pie.png"), Inches(6.95), Inches(1.32), Inches(6.0), Inches(2.5))
    s.shapes.add_picture(str(FIG / "fig6_requests_per_sector.png"), Inches(6.95), Inches(3.9), Inches(6.0), Inches(2.55))
    add_tb(s, Inches(0.4), Inches(6.85), Inches(12.5), Inches(0.38),
           "Table 2. News/media is the highest sector. Government is the lowest. Sport is high because of fotball.no.",
           size=13, color=MUTED)
    footer(s, 5, total)
    notes(s, "fotball.no 113. lanekassen.no 1. The pie is request share, not cookies.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  one example", "klassekampen.no: 46 in Table 2, 56 on the screenshot")
    s.shapes.add_picture(str(FIG / "fig2_webbkoll_results_klassekampen.png"), Inches(0.4), Inches(1.32), Inches(12.5), Inches(2.35))
    s.shapes.add_picture(str(FIG / "fig4_keycdn_lookup_klassekampen.png"), Inches(2.4), Inches(3.78), Inches(8.5), Inches(2.85))
    add_tb(s, Inches(0.4), Inches(6.7), Inches(12.5), Inches(0.5),
           "Table 2: 46 requests, 0 third-party cookies. Screenshot = Table 3 (56 requests to 13 hosts). Server: United States, Google.",
           size=13, color=MUTED)
    footer(s, 6, total)
    notes(s, "The ranking stays on Table 2. The screenshot is the later visit.")

    bullet_slide(
        prs, 7, "Part 2", "ICO: one purpose at a time",
        [
            "Official ICO Word reports dated 26 August 2026. The labels are guidance, not a court finding.",
            "One purpose per run. Compare what the notice claims with what ICO marks.",
            "Yes: notice and ICO line up for that purpose. Partial: the notice aims at consent; ICO marks INCONCLUSIVE.",
            "Tax, cookies, checkout and marketing are different purposes.",
        ],
        "Each Table 5 row is one purpose from Table 1a.",
        sizes=[20]*4,
    )

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2  ·  Table 5", "ICO result versus the notice")
    data = [
        ("Service", "Purpose", "ICO", "Match"),
        ("skatteetaten.no", "Tax / folkeregister", "Legal obligation + public task", "Yes"),
        ("skatteetaten.no", "Optional cookies", "Consent INCONCLUSIVE", "Partial"),
        ("netflix.no", "Paid streaming", "Contract", "Yes"),
        ("fotball.no", "Name + club, 13+", "Legitimate interests", "Yes"),
        ("document.no", "Google Signals", "Consent INCONCLUSIVE", "Partial"),
        ("babyshop.no", "Checkout", "Contract", "Yes"),
    ]
    left = Inches(0.4)
    top = Inches(1.4)
    widths = [Inches(2.8), Inches(3.4), Inches(4.8), Inches(1.5)]
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
        colors = [INK, INK, INK, NAVY if row[3] == "Yes" else AMBER]
        bolds = [True, False, False, True]
        for j, (w, cell) in enumerate(zip(widths, row)):
            add_rect(s, x, y, w, row_h, bg)
            add_tb(s, x + Inches(0.08), y + Inches(0.18), w - Inches(0.12), Inches(0.45), cell, size=14, bold=bolds[j], color=colors[j])
            x += w
    add_tb(s, Inches(0.4), Inches(6.72), Inches(12.5), Inches(0.5),
           "ICO labels are guidance. Partial: the notice aims at consent; ICO does not mark consent APPROPRIATE.",
           size=16, color=MUTED)
    footer(s, 8, total)
    notes(s, "Partial means the notice aims at consent, but ICO marks consent INCONCLUSIVE and no basis APPROPRIATE.")

    bullet_slide(
        prs, 9, "Part 2", "skatteetaten.no: two purposes",
        [
            "Tax and registry data: the law requires it. Opt-out is generally not possible.",
            "ICO: legal obligation and public task APPROPRIATE. Consent NOT APPROPRIATE. Match: Yes.",
            "Optional statistics cookies: the notice claims consent.",
            "ICO: consent INCONCLUSIVE; no basis APPROPRIATE. Match: Partial.",
        ],
        "Two purposes in the notice, two ICO runs. Figure 7 in the report is the hub that splits those pages.",
        sizes=[20]*4,
    )

    bullet_slide(
        prs, 10, "Part 2", "netflix.no: paid streaming",
        [
            "Purpose: account and payment data needed to provide the paid service.",
            "Notice (EEA/UK): contractual necessity.",
            "ICO: contract APPROPRIATE. Consent marked likely invalid for this purpose.",
            "Ads and marketing in the same notice were left out.",
        ],
        "Same split as elsewhere: one purpose, one basis.",
        sizes=[20]*4,
    )

    bullet_slide(
        prs, 11, "Part 2", "fotball.no: match history",
        [
            "Purpose: name and club of active players aged 13+, with club opt-out.",
            "ICO: legitimate interests APPROPRIATE.",
            "NFF is not a public authority, so public task does not fit.",
            "FIKS membership is a different purpose and was not this run.",
        ],
        "fotball.no also has the highest Webbkoll request count. That does not decide Article 6.",
        sizes=[20]*4,
    )

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2", "document.no: Google Signals")
    add_rect(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(1.15), CREAM)
    add_tb(s, Inches(0.7), Inches(1.7), Inches(12), Inches(0.8),
           "ICO: no basis APPROPRIATE. Consent INCONCLUSIVE. Match: Partial.",
           size=22, bold=True, color=NAVY)
    tf = textbox(s, Inches(0.55), Inches(2.9), Inches(12.2), Inches(3.8))
    for line in [
        "Purpose: advertising analytics from site activity.",
        "The notice does not name Article 6. It looks like consent.",
        "ICO: the request is not clear, prominent and separate from terms.",
        "The choice sits in Google settings. Pluss terms also bundle the notice.",
    ]:
        p_run(tf, "•  " + line, size=20, space_after=12)
    footer(s, 12, total)
    notes(s, "Contract and legitimate interests do not fit this advertising purpose.")

    bullet_slide(
        prs, 13, "Part 2", "babyshop.no: checkout",
        [
            "Purpose: name, address, contact, order and payment to deliver goods.",
            "The sales terms are a purchase contract.",
            "ICO: contract APPROPRIATE. Match: Yes for checkout.",
            "The notice does not label Article 6(1)(b). Marketing is a separate purpose.",
        ],
        "Same pattern as Netflix: contract for the core service.",
        sizes=[20]*4,
    )

    bullet_slide(
        prs, 14, "Close", "What the report shows",
        [
            "fotball.no has the most requests (113) and zero third-party cookies.",
            "document.no maps to the most countries. lanekassen.no and altinn.no have the fewest government requests.",
            "News and media is the highest sector total. Government is the lowest.",
            "Four core ICO purposes match the notice. Two consent claims are INCONCLUSIVE in the ICO reports.",
            "One purpose needs one basis. Contact and lawfulness are different questions.",
        ],
        "Together the two parts show how the page loads, and why the controller may use the data.",
        sizes=[20]*5,
    )

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, NAVY)
    add_tb(s, Inches(0.7), Inches(2.4), Inches(12), Inches(1.2),
           "Questions", size=48, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_tb(s, Inches(0.7), Inches(3.8), Inches(12), Inches(1.4),
           "ACIT4280 Privacy by Design  ·  Group Assignment 1A",
           size=20, color=CREAM, align=PP_ALIGN.CENTER)
    notes(s, "")

    out = "/workspace/ACIT4280_1A_presentation.pptx"
    prs.save(out)
    print("Wrote", out, "slides", len(prs.slides))


if __name__ == "__main__":
    main()
