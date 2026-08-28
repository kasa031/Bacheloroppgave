"""Shared styling for master thesis HTML builds.

APA 7 (Kildekompasset) reference list. Full-thesis template uses double spacing;
phase drafts keep the readable Phase I chapter scale (16 pt headings).
"""

AUTHOR = "Karina Sætersdal Nilssen"
INSTITUTION = "Oslo Metropolitan University"
DEPARTMENT = "Department of Computer Science"
PROGRAM = "Applied Computer and Information Technology (ACIT) · Cybersecurity"

# No visible banner - keeps the clean Phase I look in browser and PDF.
APA_BANNER = ""

REFERENCES = """
<h1 class="ch refs-heading">References</h1>
<p class="refs hanging">Alves, L. M., &amp; Wilson, S. R. (2008). The effects of loneliness on telemarketing fraud vulnerability among older adults. <em>Journal of Elder Abuse &amp; Neglect, 20</em>(1), 63–85. https://doi.org/10.1080/08946560801973137</p>
<p class="refs hanging">Bayl-Smith, P., Taib, R., Yu, K., &amp; Wiggins, M. W. (2024). Response to a phishing attack: Persuasion and protection motivation in an organizational context. <em>Information and Computer Security</em>.</p>
<p class="refs hanging">Braun, V., &amp; Clarke, V. (2006). Using thematic analysis in psychology. <em>Qualitative Research in Psychology, 3</em>(2), 77–101. https://doi.org/10.1191/1478088706qp063oa</p>
<p class="refs hanging">Braun, V., &amp; Clarke, V. (2021). One size fits all? What counts as quality practice in (reflexive) thematic analysis? <em>Qualitative Research in Psychology, 18</em>(3), 328–352. https://doi.org/10.1080/14780887.2020.1769238</p>
<p class="refs hanging">Cacioppo, J. T., &amp; Patrick, W. (2008). <em>Loneliness: Human nature and the need for social connection</em>. W. W. Norton &amp; Company.</p>
<p class="refs hanging">Chen, Y. (2024). <em>The effects of group discussion and role-playing training on self-efficacy, support-seeking, and reporting phishing emails</em> [Conference presentation]. CHI Conference on Human Factors in Computing Systems. https://doi.org/10.1145/3613904</p>
<p class="refs hanging">Conteh, N. Y., &amp; Schmick, P. J. (2020). Cybersecurity risks, vulnerabilities, and countermeasures to prevent social engineering attacks. In <em>Cyber security and threats: Concepts, methodologies, tools, and applications</em> (pp. 1–27). IGI Global. https://doi.org/10.4018/978-1-7998-6504-9.ch002</p>
<p class="refs hanging">Cybersecurity and Infrastructure Security Agency. (n.d.). <em>Phishing guidance</em>. https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks</p>
<p class="refs hanging">Directorate of Health. (2024). <em>Social isolation and loneliness: Strategy for prevention and reduction</em>. https://www.helsedirektoratet.no</p>
<p class="refs hanging">European Union Agency for Cybersecurity. (2024). <em>ENISA threat landscape 2024</em>. https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024</p>
<p class="refs hanging">Fetters, M. D., Curry, L. A., &amp; Creswell, J. W. (2013). Achieving integration in mixed methods designs—principles and practices. <em>Health Services Research, 48</em>(6), 2134–2156. https://doi.org/10.1111/1475-6773.12117</p>
<p class="refs hanging">Finans Norge. (2026). <em>Selvforsvar mot svindel</em>. https://www.svindel.no</p>
<p class="refs hanging">Floyd, D. L., Prentice-Dunn, S., &amp; Rogers, R. W. (2000). A meta-analysis of research on protection motivation theory. <em>Journal of Applied Social Psychology, 30</em>(2), 407–429. https://doi.org/10.1111/j.1559-1816.2000.tb02323.x</p>
<p class="refs hanging">Frauenstein, E. D., &amp; Flowerday, S. V. (2020). Susceptibility to phishing on social network sites: A personality information processing model. <em>Computers &amp; Security, 94</em>, Article 101862. https://doi.org/10.1016/j.cose.2020.101862</p>
<p class="refs hanging">Hadnagy, C. (2018). <em>Social engineering: The science of human hacking</em> (2nd ed.). Wiley.</p>
<p class="refs hanging">Halcyon. (2026). <em>AI and ransomware threat report</em>. https://www.halcyon.ai</p>
<p class="refs hanging">Khrono &amp; Norwegian Student Organisation. (2024). <em>Student loneliness survey</em>. https://www.khrono.no</p>
<p class="refs hanging">Kildekompasset. (n.d.). <em>APA 7th edition</em>. https://kildekompasset.no/referansestiler/apa-7</p>
<p class="refs hanging">Klütsch, J., Schwab, J., Boffel, C., Zimmermann, V., &amp; Schlittmeier, S. J. (2024). Friend or phisher? How known senders and fear of missing out affect young adults' phishing susceptibility on social media. <em>Humanities and Social Sciences Communications, 11</em>(1), Article 145. https://doi.org/10.1057/s41599-024-03412-8</p>
<p class="refs hanging">Microsoft. (2024). <em>Digital defense report 2024</em>. https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report</p>
<p class="refs hanging">Nettvett.no &amp; Norwegian National Security Authority. (n.d.). <em>Phishing guidance</em>. https://www.nettvett.no</p>
<p class="refs hanging">Norwegian Communications Authority. (n.d.). <em>Digital fraud reports</em>. https://www.nkom.no</p>
<p class="refs hanging">Norwegian National Security Authority. (2026). <em>National cyber security risk assessment 2026</em>. https://www.nsm.no</p>
<p class="refs hanging">Norwegian Police. (2024). <em>Report online fraud</em>. https://www.politiet.no/rad/nettsvindel</p>
<p class="refs hanging">OsloMet. (2024). <em>Student social connection initiatives</em>. https://www.oslomet.no</p>
<p class="refs hanging">Parker, H. J., &amp; Flowerday, S. V. (2020). Contributing factors to increased susceptibility to social media phishing attacks. <em>South African Journal of Information Management, 22</em>(1), a1176. https://doi.org/10.4102/sajim.v22i1.1176</p>
<p class="refs hanging">Przybylski, A. K., Murayama, K., DeHaan, C. R., &amp; Gladwell, V. (2013). Motivational, emotional, and behavioral correlates of fear of missing out. <em>Computers in Human Behavior, 29</em>(4), 1841–1848. https://doi.org/10.1016/j.chb.2013.02.014</p>
<p class="refs hanging">Rogers, R. W. (1975). A protection motivation theory of fear appeals and attitude change. <em>Journal of Psychology, 91</em>(1), 93–114. https://doi.org/10.1080/00223980.1975.9915803</p>
<p class="refs hanging">SHoT Study. (2022). <em>Student health and wellbeing survey (SHoT2022)</em>. https://shot.no</p>
<p class="refs hanging">Statistics Norway. (2025). <em>How many people feel lonely in Norway? Quality of life survey</em>. https://www.ssb.no/sosiale-forhold-og-kriminalitet/levekar/statistikk/livskvalitet</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2020). Phishing susceptibility in a Norwegian sample. In <em>Proceedings of Norsk IKT-konferanse for forskning og utdanning</em>.</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2022). Cognitive reflection and phishing susceptibility. In <em>Proceedings of Norsk IKT-konferanse for forskning og utdanning</em>.</p>
<p class="refs hanging">Trend Micro. (2026). <em>Phishing threat report 2026</em>. https://www.trendmicro.com</p>
<p class="refs hanging">Tsai, H.-Y. (2021). Phishing and persuasion strategies. <em>Computers &amp; Security</em>.</p>
<p class="refs hanging">Wen, J., Yang, H., Zhang, Q., &amp; Shao, J. (2022). Mechanisms linking loneliness and fraud victimization. <em>Journal of Elder Abuse &amp; Neglect</em>.</p>
<p class="refs hanging">Wen, J., Yang, H., Zhang, Q., &amp; Shao, J. (2024). Loneliness could lead to risk of fraud victimization for middle-aged and older adults. <em>Journal of Elder Abuse &amp; Neglect</em>. https://doi.org/10.1080/08946566.2024.2404040</p>
<p class="refs hanging">World Health Organization. (2023). <em>Social connection and health</em>. https://www.who.int</p>
<p class="refs note">Referanselisten er formatert etter APA 7th edition (Kildekompasset). Kontroller DOI-er og forfatterlister i Zotero før endelig innlevering.</p>
"""

APA_CSS = """
:root { --black:#000; --ink:#1a1a1a; --dark:#333; --mid:#666; --line:#ccc; --light:#f0f0f0; --paper:#fff; }
* { box-sizing:border-box; }
body { margin:0; font-family:"Times New Roman", Times, serif; font-size:12pt; line-height:1.5; color:var(--ink); background:#e8e8e8; }
.toolbar { position:sticky; top:0; background:#111; color:#fff; padding:10px 16px; font-family:Calibri,sans-serif; font-size:14px; z-index:9; line-height:1.4; }
.toolbar a { color:#7fd; margin-right:1rem; }
.page { max-width:210mm; margin:1rem auto; background:var(--paper); padding:25mm; box-shadow:0 2px 12px rgba(0,0,0,.15); }
.cover-page { min-height:200mm; display:flex; flex-direction:column; justify-content:center; text-align:center; page-break-after:always; }
.cover-title { font-size:22pt; font-weight:700; line-height:1.3; color:var(--black); margin:0; }
.cover-sub { font-size:14pt; margin-top:1rem; color:var(--dark); }
.cover-author { font-size:16pt; font-weight:700; margin-top:2rem; }
.cover-meta { font-size:12pt; color:var(--mid); margin-top:1rem; }
h1.ch, .chapter h1 { font-size:16pt; font-weight:700; border-bottom:2px solid var(--black); padding-bottom:.3rem; margin:2rem 0 1rem; page-break-before:always; }
h1.ch:first-of-type { page-break-before:auto; }
h1.refs-heading { page-break-before:always; }
h2 { font-size:14pt; font-weight:700; margin:1.2rem 0 .6rem; color:var(--black); }
h3 { font-size:12pt; font-weight:700; margin:1rem 0 .4rem; }
p, li { font-size:12pt; margin:0 0 .65rem; text-align:left; }
ul, ol, dl { margin:.4rem 0 .8rem; padding-left:1.4rem; }
blockquote.quote { margin:.8rem 0; padding:.8rem 1rem; background:var(--light); border-left:3px solid var(--dark); }
.draft-banner { background:#fff3cd; border:1px solid #856404; color:#533f03; padding:.75rem; margin:1rem 0; font-size:11pt; line-height:1.5; }
table.data { width:100%; border-collapse:collapse; margin:1rem 0; font-size:11pt; line-height:1.4; }
table.data th, table.data td { border:1px solid var(--line); padding:6px 8px; text-align:left; }
table.data caption { caption-side:top; text-align:left; font-weight:700; margin-bottom:.5rem; }
.refs { font-size:12pt; margin:0 0 .5rem; }
.hanging { padding-left:0.5in; text-indent:-0.5in; margin-left:0; }
.refs.note { font-size:10pt; color:var(--mid); margin-top:1rem; font-style:italic; }
dt { font-weight:700; margin-top:.5rem; }
dd { margin:0 0 .5rem 1rem; }
@media print { body{background:#fff;} .toolbar{display:none;} .page{box-shadow:none;margin:0;max-width:none;} }
"""

# APA 7 full thesis: Kildekompasset double spacing + original chapter typography.
APA_FULL_CSS = """
:root { --black:#000; --ink:#1a1a1a; --dark:#333; --mid:#666; --line:#ccc; --light:#f0f0f0; --paper:#fff; }
* { box-sizing:border-box; }
body { margin:0; font-family:"Times New Roman", Times, serif; font-size:12pt; line-height:2; color:var(--ink); background:#e8e8e8; }
.toolbar { position:sticky; top:0; background:#111; color:#fff; padding:10px 16px; font-family:Calibri,sans-serif; font-size:14px; z-index:9; line-height:1.4; }
.toolbar a { color:#7fd; margin-right:1rem; }
.page { max-width:210mm; margin:1rem auto; background:var(--paper); padding:25mm; box-shadow:0 2px 12px rgba(0,0,0,.15); }
.cover-page { min-height:200mm; display:flex; flex-direction:column; justify-content:center; text-align:center; page-break-after:always; line-height:2; }
.cover-title { font-size:22pt; font-weight:700; line-height:1.3; color:var(--black); margin:0; }
.cover-sub { font-size:14pt; margin-top:1rem; color:var(--dark); font-style:italic; }
.cover-author { font-size:12pt; font-weight:400; margin-top:2rem; }
.cover-affil { font-size:12pt; color:var(--dark); margin:.15rem 0; }
.cover-meta { font-size:12pt; color:var(--mid); margin-top:1rem; }
h1.ch, .chapter h1 { font-size:16pt; font-weight:700; border-bottom:2px solid var(--black); padding-bottom:.3rem; margin:2rem 0 1rem; page-break-before:always; text-align:left; }
h1.ch:first-of-type, .chapter:first-of-type h1 { page-break-before:auto; }
h1.refs-heading { page-break-before:always; border-bottom:none; text-align:center; }
h2 { font-size:14pt; font-weight:700; margin:1.2rem 0 .6rem; color:var(--black); }
h3 { font-size:12pt; font-weight:700; margin:1rem 0 .4rem; }
p, li { font-size:12pt; margin:0 0 .65rem; text-align:left; text-indent:0.5in; }
h1 + p, h2 + p, h3 + p, .chapter h1 + p, .cover-page p, blockquote p, li, dt, dd, table.data, .draft-banner, .refs, .note { text-indent:0; }
ul, ol, dl { margin:.4rem 0 .8rem; padding-left:1.4rem; }
blockquote.quote { margin:.8rem 0; padding:.8rem 1rem; background:var(--light); border-left:3px solid var(--dark); text-indent:0; }
.cite { color:var(--mid); font-size:11pt; }
.draft-banner { background:#fff3cd; border:1px solid #856404; color:#533f03; padding:.75rem; margin:1rem 0; font-size:11pt; line-height:1.5; }
table.data { width:100%; border-collapse:collapse; margin:1rem 0; font-size:11pt; line-height:1.4; }
table.data th, table.data td { border:1px solid var(--line); padding:6px 8px; text-align:left; }
table.data caption { caption-side:top; text-align:left; font-weight:700; margin-bottom:.5rem; }
.refs { font-size:12pt; margin:0 0 .5rem; }
.hanging { padding-left:0.5in; text-indent:-0.5in; margin-left:0; }
.refs.note { font-size:10pt; color:var(--mid); margin-top:1rem; font-style:italic; }
dt { font-weight:700; margin-top:.5rem; }
dd { margin:0 0 .5rem 1rem; }
@media print { body{background:#fff;} .toolbar{display:none;} .page{box-shadow:none;margin:0;max-width:none;} }
"""


def render_chapter(sections, chapter_title, demote_h1=False):
    """Render one level-1 chapter block (excludes the chapter h1 heading)."""
    parts = []
    in_chapter = False
    for level, title, paragraphs in sections:
        if level == 1:
            if title == chapter_title:
                in_chapter = True
                continue
            if in_chapter:
                break
        if not in_chapter:
            continue
        if level == 2:
            parts.append(f"<h2>{title}</h2>")
        elif level == "table":
            parts.append(paragraphs[0])
            continue
        for p in paragraphs:
            parts.append(f"<p>{p}</p>")
    return "".join(parts)


def render_sections(sections, skip_h1=None, demote_h1=False):
    """Render structured sections to HTML."""
    skip = skip_h1 or set()
    parts = []
    for level, title, paragraphs in sections:
        if level == 1 and title in skip:
            continue
        if level == 1:
            tag = "h2" if demote_h1 else "h1"
            cls = ' class="ch"' if tag == "h1" else ""
            parts.append(f"<{tag}{cls}>{title}</{tag}>")
        elif level == 2:
            parts.append(f"<h2>{title}</h2>")
        elif level == "table":
            parts.append(paragraphs[0])
            continue
        for p in paragraphs:
            parts.append(f"<p>{p}</p>")
    return "".join(parts)


def full_thesis_cover():
    return f"""
<div class="cover-page">
  <h1 class="cover-title">Beyond the Weakest Link: The Skepticism Paradox<br>Why Phishing Works Despite Rising Skepticism</h1>
  <p class="cover-sub">A Mixed-Methods Study of Loneliness, Social Engineering, and Digital Trust in Norway</p>
  <p class="cover-author">{AUTHOR}</p>
  <p class="cover-affil">{INSTITUTION}</p>
  <p class="cover-affil">{DEPARTMENT}</p>
  <p class="cover-meta">{PROGRAM}</p>
  <p class="cover-meta">Master's Thesis · ACIT5910–5930 · APA 7 (Kildekompasset)</p>
</div>
"""


def cover_html(title, subtitle, course_meta):
    return f"""
<div class="cover-page">
  <h1 class="cover-title">{title}<br>{subtitle}</h1>
  <p class="cover-sub">A Mixed-Methods Study of Loneliness, Social Engineering, and Digital Trust in Norway</p>
  <p class="cover-author">{AUTHOR}</p>
  <p class="cover-meta">{course_meta} · OsloMet · Cybersecurity</p>
</div>
"""


def abstract_html(text, keywords):
    return f"""
<section class="chapter"><h1>Abstract</h1>
<p>{text}</p>
<p><strong>Keywords:</strong> {keywords}</p>
</section>
"""
