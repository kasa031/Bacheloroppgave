#!/usr/bin/env python3
"""Build the ACIT4280 1A group presentation (16:9, 14 slides)."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE, MSO_ANCHOR
from pptx.util import Inches, Pt
from pathlib import Path

FIG = Path("/workspace/figures")
LOGO = FIG / "oslomet_logo.png"

DARK = RGBColor(0x22, 0x42, 0x48)
MID = RGBColor(0x32, 0x5E, 0x6A)
TEAL = RGBColor(0x44, 0xA1, 0xA4)
ORANGE = RGBColor(0xFF, 0x9A, 0x00)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x4A, 0x55, 0x68)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PAPER = RGBColor(0xFF, 0xFE, 0xFB)
LIGHT = RGBColor(0xE8, 0xF4, 0xF4)

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


def _prep_tf(tf):
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = Pt(0)
    tf.margin_right = Pt(0)
    tf.margin_top = Pt(0)
    tf.margin_bottom = Pt(0)


def add_tb(slide, l, t, w, h, text, size=18, bold=False, color=INK, align=PP_ALIGN.LEFT, font="Calibri"):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    _prep_tf(tf)
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
    _prep_tf(tf)
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


def footer(slide, n, total=14):
    add_rect(slide, 0, Inches(7.28), W, Inches(0.22), DARK)
    add_tb(slide, Inches(0.4), Inches(7.28), Inches(10), Inches(0.22),
           "ACIT4280 Group Assignment 1A  |  3 Sep 2026",
           size=11, color=WHITE)
    add_tb(slide, Inches(11.4), Inches(7.28), Inches(1.5), Inches(0.22),
           f"{n} / {total}", size=11, color=WHITE, align=PP_ALIGN.RIGHT)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def header_bar(slide, kicker, title):
    add_rect(slide, 0, 0, W, Inches(1.15), DARK)
    add_rect(slide, 0, Inches(1.15), W, Inches(0.08), ORANGE)
    add_tb(slide, Inches(0.5), Inches(0.12), Inches(12.3), Inches(0.32),
           kicker, size=12, color=TEAL, bold=True)
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
    total = 14

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, DARK)
    add_rect(s, 0, Inches(5.85), W, Inches(1.65), ORANGE)
    add_tb(s, Inches(0.7), Inches(0.85), Inches(12), Inches(0.35),
           "ACIT4280 Privacy by Design",
           size=18, color=TEAL, bold=True)
    add_tb(s, Inches(0.7), Inches(1.22), Inches(12), Inches(0.38),
           "Group Assignment 1A",
           size=24, color=TEAL, bold=True)
    add_tb(s, Inches(0.7), Inches(1.7), Inches(12), Inches(1.85),
           "Analysis of 3rd-party Data Sharing\nand Data Tracking and of GDPR\nCompliance of Norwegian Web Sites",
           size=28, color=WHITE, bold=True)
    tf_q = textbox(s, Inches(0.7), Inches(3.62), Inches(12), Inches(1.55))
    p_run(tf_q,
          "•  When a front page loads, how many third parties does it contact, "
          "and in which countries do those servers appear to be located?",
          size=17, color=WHITE, space_after=14)
    p_run(tf_q,
          "•  When a site processes personal data, has it named a GDPR Article 6 lawful basis, "
          "and does the ICO tool agree?",
          size=17, color=WHITE, space_after=0)
    add_tb(s, Inches(0.7), Inches(5.05), Inches(12), Inches(0.55),
           "Humna Akhtar  ·  Mithun Chandra Debnath  ·  Karina Sætersdal Nilssen",
           size=16, color=WHITE)
    band_top = Inches(5.85)
    band_h = Inches(1.65)
    logo_w = Inches(3.1)
    logo_h = Inches(0.55)
    band_center_y = band_top + (band_h - logo_h) / 2
    date_box = add_tb(s, Inches(0.7), band_center_y, Inches(6), logo_h,
           "3 September 2026",
           size=16, color=DARK)
    date_box.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    s.shapes.add_picture(
        str(LOGO),
        W - Inches(0.55) - logo_w,
        band_center_y,
        logo_w,
        logo_h,
    )
    notes(s, "Part 1 measures contact. Part 2 tests one purpose at a time.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "The report", "Two questions and how we measured")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(5.9), Inches(5.0), TEAL)
    add_tb(s, Inches(0.75), Inches(1.72), Inches(5.4), Inches(0.35), "Part 1  ·  Webbkoll", size=20, bold=True, color=DARK)
    tf = textbox(s, Inches(0.75), Inches(2.08), Inches(5.4), Inches(1.05))
    for line in [
        "18 sites: cookies, requests, KeyCDN country",
        "One clean load per site; rank on Table 2 (20 Aug)",
        "KeyCDN = IP geolocation guess, not legal transfer proof",
    ]:
        p_run(tf, "•  " + line, size=14, space_after=4)
    s.shapes.add_picture(
        str(FIG / "fig2_webbkoll_results_klassekampen.png"),
        Inches(0.75),
        Inches(3.05),
        Inches(5.4),
        Inches(1.4),
    )
    add_rect(s, Inches(6.9), Inches(1.55), Inches(5.9), Inches(5.0), MID)
    add_tb(s, Inches(7.15), Inches(1.72), Inches(5.4), Inches(0.35), "Part 2  ·  ICO", size=20, bold=True, color=ORANGE)
    tf = textbox(s, Inches(7.15), Inches(2.15), Inches(5.4), Inches(3.8))
    for line in [
        "Five sites, one purpose per run",
        "Notice vs ICO Word report (26 Aug 2026)",
        "Yes if notice and ICO agree",
        "Partial if consent is INCONCLUSIVE",
        "Tax, cookies, checkout and marketing are different purposes",
    ]:
        p_run(tf, "•  " + line, size=16, color=WHITE, space_after=8)
    footer(s, 2, total)
    notes(s, "Webbkoll records one load. ICO tests one purpose at a time. Contact and lawful basis are different questions.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1", "What Webbkoll shows and key findings")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(5.9), Inches(5.0), TEAL)
    add_tb(s, Inches(0.75), Inches(1.75), Inches(5.4), Inches(0.4),
           "What Webbkoll shows", size=22, bold=True, color=DARK)
    tf = textbox(s, Inches(0.75), Inches(2.2), Inches(5.4), Inches(0.75))
    p_run(tf, "Cookies, third-party requests and server country.", size=16, space_after=6)
    p_run(tf, "Many requests does not mean many cookies.", size=16, bold=True, color=ORANGE, space_after=0)
    s.shapes.add_picture(
        str(FIG / "fig4_keycdn_lookup_klassekampen.png"),
        Inches(0.75),
        Inches(3.05),
        Inches(5.4),
        Inches(2.35),
    )
    add_rect(s, Inches(6.9), Inches(1.55), Inches(5.9), Inches(5.0), DARK)
    add_tb(s, Inches(7.15), Inches(1.75), Inches(5.4), Inches(0.4),
           "Key findings", size=22, bold=True, color=TEAL)
    tf = textbox(s, Inches(7.15), Inches(2.3), Inches(5.4), Inches(4.0))
    for line in [
        "fotball.no: 113 requests, zero third-party cookies.",
        "17 of 18 sites: zero third-party cookies. ikea.no had 2.",
        "lanekassen.no (1) and altinn.no (5): quietest e-government pages.",
        "document.no: widest country list (6 excluding Norway).",
        "News/media contacted the most. Government the fewest.",
        "babyshop.no: 45 on first scan, 101 on repeat scan.",
    ]:
        p_run(tf, "•  " + line, size=16, color=WHITE, space_after=8)
    footer(s, 3, total)
    notes(s, "Webbkoll counts contact on one load. Cookies and requests are separate measures.")

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
    add_tb(s, Inches(0.5), Inches(1.4), Inches(6), Inches(0.4), "Highest five", size=18, bold=True, color=DARK)
    add_tb(s, Inches(7.0), Inches(1.4), Inches(6), Inches(0.4), "Lowest five", size=18, bold=True, color=MID)
    y = Inches(1.78)
    for (a, b), (c, d) in zip(high, low):
        add_rect(s, Inches(0.5), y, Inches(5.9), Inches(0.82), TEAL)
        add_tb(s, Inches(0.7), y + Inches(0.06), Inches(5.5), Inches(0.32), a, size=16, bold=True, color=DARK)
        add_tb(s, Inches(0.7), y + Inches(0.38), Inches(5.5), Inches(0.32), b, size=14, color=INK)
        add_rect(s, Inches(7.0), y, Inches(5.8), Inches(0.82), MID)
        add_tb(s, Inches(7.2), y + Inches(0.06), Inches(5.4), Inches(0.32), c, size=16, bold=True, color=WHITE)
        add_tb(s, Inches(7.2), y + Inches(0.38), Inches(5.4), Inches(0.32), d, size=14, color=WHITE)
        y += Inches(0.9)
    footer(s, 4, total)
    notes(s, "fotball.no has 113 requests and zero third-party cookies. document.no has the widest country list (6).")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 1  ·  Figures 2 to 4", "Third-party requests by site and sector")
    s.shapes.add_picture(str(FIG / "fig3_requests_all18.png"), Inches(0.3), Inches(1.32), Inches(6.5), Inches(5.15))
    s.shapes.add_picture(str(FIG / "fig5_share_requests_pie.png"), Inches(6.95), Inches(1.32), Inches(6.0), Inches(2.5))
    s.shapes.add_picture(str(FIG / "fig6_requests_per_sector.png"), Inches(6.95), Inches(3.9), Inches(6.0), Inches(2.55))
    add_tb(s, Inches(0.4), Inches(6.85), Inches(12.5), Inches(0.38),
           "Table 2. News/media is the highest sector. Government is the lowest.",
           size=13, color=MUTED)
    footer(s, 5, total)
    notes(s, "fotball.no 113. lanekassen.no 1. The pie is request share, not cookies.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2", "ICO: one purpose at a time")
    tf = textbox(s, Inches(0.55), Inches(1.38), Inches(12.2), Inches(0.7))
    p_run(tf,
          "One purpose per ICO run (26 Aug 2026). Yes if notice and ICO agree; Partial if consent is INCONCLUSIVE.",
          size=16, space_after=4)
    p_run(tf, "Tax, cookies, checkout and marketing are different purposes.", size=16, space_after=0)
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
    top = Inches(2.12)
    widths = [Inches(2.8), Inches(3.4), Inches(4.8), Inches(1.5)]
    row_h = Inches(0.58)
    x = left
    for w, htxt in zip(widths, data[0]):
        add_rect(s, x, top, w, row_h, DARK)
        add_tb(s, x + Inches(0.08), top + Inches(0.14), w - Inches(0.1), Inches(0.35), htxt, size=12, bold=True, color=WHITE)
        x += w
    for i, row in enumerate(data[1:]):
        y = top + row_h * (i + 1)
        bg = TEAL if row[3] == "Partial" else (LIGHT if i % 2 else WHITE)
        x = left
        colors = [INK, INK, INK, DARK if row[3] == "Yes" else ORANGE]
        bolds = [True, False, False, True]
        for j, (w, cell) in enumerate(zip(widths, row)):
            add_rect(s, x, y, w, row_h, bg)
            add_tb(s, x + Inches(0.08), y + Inches(0.14), w - Inches(0.12), Inches(0.38), cell, size=12, bold=bolds[j], color=colors[j])
            x += w
    footer(s, 6, total)
    notes(s, "Each row is one purpose from Table 1a. Partial means consent INCONCLUSIVE.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Part 2  ·  Table 5", "Four match, two consent tests Partial")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(12.3), Inches(4.85), TEAL)
    tf = textbox(s, Inches(0.75), Inches(1.85), Inches(11.8), Inches(4.35))
    for i, line in enumerate([
        "Four core purposes match the notice: tax, paid streaming, match history, checkout.",
        "Two consent tests are Partial: Skatteetaten optional cookies and document.no Google Signals.",
        "In both cases the notice claims consent, but the ICO marks consent INCONCLUSIVE.",
        "Skatteetaten does not spell out clearly enough who processes the optional cookies and how to refuse them. "
        "document.no points users to Google ad settings; the ICO says that is not a clear, separate consent request, "
        "and Pluss terms bundle the notice.",
    ]):
        p_run(tf, line, size=20 if i < 2 else 18, bold=(i < 2), color=DARK if i != 1 else ORANGE,
              space_after=14 if i < 3 else 0)
    footer(s, 7, total)
    notes(s, "Partial is not a court finding. It means the consent wording did not pass the ICO checklist.")

    bullet_slide(
        prs, 8, "Part 2", "skatteetaten.no: two purposes",
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
        prs, 9, "Part 2", "netflix.no: paid streaming",
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
        prs, 10, "Part 2", "fotball.no: match history",
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
    add_rect(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(1.15), ORANGE)
    add_tb(s, Inches(0.7), Inches(1.7), Inches(12), Inches(0.8),
           "ICO: no basis APPROPRIATE. Consent INCONCLUSIVE. Match: Partial.",
           size=22, bold=True, color=DARK)
    tf = textbox(s, Inches(0.55), Inches(2.9), Inches(12.2), Inches(3.8))
    for line in [
        "Purpose: advertising analytics from site activity.",
        "The notice does not name Article 6. It looks like consent.",
        "ICO: the request is not clear, prominent and separate from terms.",
        "The choice sits in Google settings. Pluss terms also bundle the notice.",
    ]:
        p_run(tf, "•  " + line, size=20, space_after=12)
    footer(s, 11, total)
    notes(s, "Contract and legitimate interests do not fit this advertising purpose.")

    bullet_slide(
        prs, 12, "Part 2", "babyshop.no: checkout",
        [
            "Purpose: name, address, contact, order and payment to deliver goods.",
            "The sales terms are a purchase contract.",
            "ICO: contract APPROPRIATE. Match: Yes for checkout.",
            "The notice does not label Article 6(1)(b). Marketing is a separate purpose.",
        ],
        "Same pattern as Netflix: contract for the core service.",
        sizes=[20]*4,
    )

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, PAPER)
    header_bar(s, "Close", "What the report shows")
    add_rect(s, Inches(0.5), Inches(1.55), Inches(12.3), Inches(4.85), TEAL)
    tf = textbox(s, Inches(0.75), Inches(1.85), Inches(11.8), Inches(4.35))
    summary = [
        "We measured how much 18 sites contact others on load, and we checked whether five of them have a valid GDPR basis for one specific purpose.",
        "Many sites reach out to many others without setting cookies.",
        "Four of five ICO purposes match the notice.",
        "In two places where the site claims consent, the ICO is not satisfied with how consent is formulated.",
    ]
    for i, line in enumerate(summary):
        p_run(tf, line, size=22, color=DARK if i != 3 else ORANGE, space_after=16 if i < len(summary) - 1 else 0)
    footer(s, 13, total)
    notes(s, "Part 1 is contact. Part 2 is one purpose and one basis at a time.")

    s = prs.slides.add_slide(blank)
    add_rect(s, 0, 0, W, H, DARK)
    add_tb(s, Inches(0.7), Inches(2.4), Inches(12), Inches(1.2),
           "Questions", size=48, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_tb(s, Inches(0.7), Inches(3.8), Inches(12), Inches(1.4),
           "ACIT4280 Privacy by Design  ·  Group Assignment 1A",
           size=20, color=TEAL, align=PP_ALIGN.CENTER)
    notes(s, "")

    out = "/workspace/ACIT4280_1A_presentation.pptx"
    prs.save(out)
    print("Wrote", out, "slides", len(prs.slides))


if __name__ == "__main__":
    main()
