#!/usr/bin/env python3
"""Build ACIT5930 Phase 3 draft HTML - final thesis strand."""
from pathlib import Path

TITLE = "Beyond the Weakest Link: The Skepticism Paradox"
SUBTITLE = "Why Phishing Works Despite Rising Skepticism"
AUTHOR = "Karina [Surname]"
COURSE = "ACIT5930 Master's Thesis, Phase 3 (final draft)"

SECTIONS = []


def add(title, level, paragraphs):
    SECTIONS.append((level, title, paragraphs))


def table(html):
    SECTIONS.append(("table", "", [html]))


add("Introduction and thesis arc", 1, [
    "This document is a draft for ACIT5930 (Phase 3), the final phase of the master thesis Beyond the Weakest Link: The Skepticism Paradox. Phase 1 (ACIT5910) established theory and literature; Phase 2 (ACIT5920) collected and analysed survey data. Phase 3 completes the mixed-methods design through semi-structured interviews, reflexive thematic analysis, integration with quantitative findings, and final discussion, conclusions, and recommendations.",
    "The main research question remains: How can phishing remain effective despite rising scepticism, and which emotional, cognitive, and contextual factors make individuals especially vulnerable beyond the weakest-link explanation? Phase 3 answers the \"how\" and \"why\" behind statistical patterns by examining lived experience: what makes messages feel credible, when knowledge fails to produce safe action, and how reporting culture shapes disclosure of near misses.",
    "Final submission follows WISEflow naming: Etternavn_Fornavn_studentnummer_ACIT5930, with appendices as ACIT5930_Appx. Sluttinnlevering deadline per handbook: 19 May. Oral defence: approximately 30 minutes presentation plus 30 minutes discussion.",
    "This draft focuses on Phase 3 deliverables. The complete thesis merges condensed Phase 1 chapters (Introduction, Literature Review, Theoretical Framework) with Phase 2 Methodology and Survey Results, plus the new content below. Placeholders marked [INSERT] must be replaced with real interview and integration data before submission.",
])

add("Recap of quantitative findings (from Phase 2)", 2, [
    "[INSERT: Brief summary of Phase 2 N, key vignette patterns, H1-H4 outcomes. Example structure: \"Survey N = [ ]. Unsafe intention highest for S[ ] and S[ ]; general scepticism predicted S1 responses but not S3/S6 (H2 [supported/partial/not supported]).\"]",
    "Quantitative results provide the structural skeleton for integration. Interviews explain mechanisms: why institutional lures bypass scepticism, how loneliness surfaces in credibility judgements, and whether shame prevents reporting despite awareness.",
])

add("Interview methodology", 1, [])

add("Design and sampling", 2, [
    "Phase 3 implements the qualitative strand of the exploratory sequential mixed-methods design (Braun & Clarke, 2006). Interviews follow survey completion so that sampling can target variation identified in Phase 2.",
    "Target sample: 12-18 semi-structured interviews. Purposive sampling from survey opt-in pool, stratified by: (1) loneliness score tertile (high/medium/low); (2) vignette profile (high susceptibility on S3 or S6 vs low); (3) role (student vs staff). Aim for diversity in gender and age where possible without compromising anonymity.",
    "Inclusion: completed Phase 2 survey; consented to follow-up contact; aged 18+; comfortable interviewing in Norwegian or English.",
    "Exclusion: insufficient language proficiency; inability to consent; duplicate participation.",
    "[INSERT: Final interview N, recruitment period, opt-in rate from survey]",
])

add("Interview guide and procedure", 2, [
    "Interviews use a semi-structured guide (Appendix A) with core topics: experiences with suspicious messages; credibility cues; emotional context (loneliness, stress, exam periods); knowledge-behaviour gaps; training and reporting culture; reactions to vignettes S3 and S6 if not discussed spontaneously.",
    "Format: video or audio call (Teams/Zoom) or in-person at OsloMet, 45-60 minutes. Recorded with consent; transcribed verbatim (or intelligent verbatim) by researcher; pseudonyms assigned (P1-P18).",
    "Opening: reconfirm consent, explain confidentiality, emphasise no wrong answers. Warm-up: general digital communication habits. Core blocks: (1) near-miss narratives; (2) institutional vs stranger messages; (3) loneliness and social connection (sensitive - allow skip); (4) organisational support and shame; (5) debrief and member-check offer.",
    "Member checking: summary sent to willing participants for factual correction (not veto over interpretation).",
])

add("Qualitative analysis approach", 2, [
    "Analysis follows reflexive thematic analysis (Braun & Clarke, 2006; Braun & Clarke, 2021). Six phases: familiarisation with transcripts; initial coding; theme search; theme review; theme definition and naming; report writing.",
    "Coding software: NVivo, Taguette, or manual coding in Word/Excel. Initial codes generated inductively from data and deductively from the scepticism paradox framework (lure-specific credibility, knowledge-behaviour gap, shame/reporting, institutional trust).",
    "Reflexivity journal maintained: researcher assumptions about weakest-link narrative, loneliness stigma, and cybersecurity culture documented to reduce unexamined bias.",
    "Trustworthiness: thick description of quotes; audit trail of codebook revisions; negative case analysis (interviews contradicting H1/H2); peer debrief with supervisor.",
])

add("Integration with survey data", 2, [
    "Mixed-methods integration uses a joint display approach (Fetters et al., 2013): rows represent themes; columns link to survey statistics (e.g. S6 click rate among high-loneliness tertile). Integration questions: Do interviews explain quantitative interaction effects? Do qualitative cases illustrate outliers?",
    "Triangulation protocol: convergence (qual + quant agree), expansion (qual adds mechanism), discordance (qual challenges quant - reported transparently).",
    "[INSERT: Reference to integration table in Results chapter]",
])

add("Ethics (interview strand)", 2, [
    "Interview strand covered under SIKT approval from Phase 2 [INSERT: reference]. Separate interview consent form. Transcripts stored encrypted; identifiers removed; audio deleted after verified transcription per retention schedule.",
    "Sensitive topics: fraud victimisation, loneliness, shame. Participants may skip questions, pause, or withdraw. Contact information for SiO/student welfare provided before and after interview.",
])

add("Qualitative results", 1, [])

add("Overview of sample", 2, [
    "[INSERT: Table of pseudonyms, role, loneliness tertile, vignette profile, interview duration. No identifying details.]",
])

add("Theme 1: Lure-specific credibility", 2, [
    "Expected theme: participants distinguish stranger scams from institutional or social messages. Stranger lures described as \"obvious\" or \"ridiculous\"; institutional lures (BankID, IT, exam office) described as \"could be real\" even by sceptical participants.",
    "[INSERT: 2-4 anonymised quotes supporting Theme 1]",
    "Relation to H2: if supported, quotes should show general scepticism coexisting with institutional trust - the scepticism paradox in participants' own words.",
])

add("Theme 2: Emotional context and loneliness", 2, [
    "Expected theme: belonging and social lures gain credibility during lonely or stressful periods (exam season, relocation, remote study). Not all high-loneliness scorers endorse this; negative cases noted.",
    "[INSERT: 2-4 quotes. Handle with care - avoid implying loneliness causes gullibility.]",
    "Relation to H1: qualitative depth on when S2/S6 feel tempting despite awareness training.",
])

add("Theme 3: Knowledge-behaviour gap", 2, [
    "Expected theme: participants articulate correct advice (\"check sender,\" \"use separate channel\") yet describe moments of almost clicking due to urgency, multitasking, or emotional pull.",
    "[INSERT: quotes on gap between knowing and doing]",
    "Relation to sub-question 3 from Phase 1 and situational pressure mediation (H3).",
])

add("Theme 4: Shame, blame, and reporting culture", 2, [
    "Expected theme: near misses hidden when culture feels punitive; supportive reporting linked to willingness to ask for help. Aligns with PMT coping appraisal (H4) and Chen et al. (2024).",
    "[INSERT: quotes on reporting comfort or fear of blame]",
])

add("Theme 5: Training gaps", 2, [
    "Expected theme: awareness materials focus on stranger scams; participants request examples of social and institutional impersonation relevant to student life.",
    "[INSERT: quotes on training relevance]",
    "Practical implication for OsloMet and comparable institutions.",
])

table("""
<table class="data">
<caption><strong>Table 1.</strong> Thematic overview and link to hypotheses. [INSERT/refine after coding]</caption>
<thead><tr><th>Theme</th><th>Brief description</th><th>Linked hypothesis</th><th>Example quote ID</th></tr></thead>
<tbody>
<tr><td>1. Lure-specific credibility</td><td>Institutional/social lures feel more credible than stranger scams</td><td>H2</td><td>[P?]</td></tr>
<tr><td>2. Emotional context</td><td>Loneliness/stress increases openness to belonging lures</td><td>H1, H3</td><td>[P?]</td></tr>
<tr><td>3. Knowledge-behaviour gap</td><td>Rules known but not applied under pressure</td><td>H3</td><td>[P?]</td></tr>
<tr><td>4. Reporting culture</td><td>Shame suppresses disclosure; support enables reporting</td><td>H4</td><td>[P?]</td></tr>
<tr><td>5. Training gaps</td><td>Generic training; need lure-specific examples</td><td>Practical</td><td>[P?]</td></tr>
</tbody>
</table>
""")

add("Integrated findings", 1, [])

add("Joint display: quantitative patterns and qualitative mechanisms", 2, [
    "This section integrates Phase 2 and Phase 3 findings. [INSERT: Narrative weaving survey statistics with interview excerpts.]",
    "Example integration structure (to complete with real data): If survey shows higher S6 unsafe intention in high-loneliness tertile, interviews should illustrate mechanisms (e.g. desire for connection during isolated exam period). If H2 interaction is significant, interviews should show participants who \"never click stranger links\" but hesitated on IT reset emails.",
])

table("""
<table class="data">
<caption><strong>Table 2.</strong> Integration matrix (joint display). [INSERT data]</caption>
<thead><tr><th>Survey finding</th><th>Related theme</th><th>Illustrative quote</th><th>Integration type</th></tr></thead>
<tbody>
<tr><td>[e.g. S6 click % high in lonely tertile]</td><td>Theme 2</td><td>"[quote]"</td><td>Convergence</td></tr>
<tr><td>[e.g. S1 vs S3 scepticism interaction]</td><td>Theme 1</td><td>"[quote]"</td><td>Expansion</td></tr>
<tr><td>[discordant case if any]</td><td>[theme]</td><td>"[quote]"</td><td>Discordance</td></tr>
</tbody>
</table>
""")

add("Answering the research questions", 2, [
    "Main RQ: [INSERT synthesized answer drawing on quant + qual]",
    "Sub-Q1 (loneliness, scepticism, susceptibility): [INSERT]",
    "Sub-Q2 (emotional/situational factors): [INSERT]",
    "Sub-Q3 (knowledge-behaviour gap): [INSERT]",
    "Sub-Q4 (protective factors): [INSERT]",
])

add("Discussion", 1, [])

add("The scepticism paradox revisited", 2, [
    "The discussion interprets integrated findings through the scepticism paradox lens. If convergent evidence shows lure-specific protection, the weakest-link narrative is insufficient as both training model and incident explanation (Hadnagy, 2018).",
    "Norwegian high-trust digital context (BankID, Altinn, OsloMet IT) creates predictable impersonation surfaces. General stranger-scepticism, promoted in public campaigns (Finans Norge, 2026; NSM, 2026), may not transfer to domains where trust is functional and necessary.",
    "[INSERT: Interpretation of whether paradox is supported, partially supported, or requires revision based on actual findings]",
])

add("Theoretical contributions", 2, [
    "The thesis contributes: (1) a named paradox tested with mixed methods in Norwegian higher education; (2) integration of loneliness research with human-factors cybersecurity; (3) extension of PMT toward coping appraisal and reporting culture when threats are not initially recognised as such (Rogers, 1975; Bayl-Smith et al., 2024).",
    "Comparison with Tjostheim and Waterworth (2020, 2022): cognitive reflection remains relevant; this thesis adds emotional and social framing, especially for institutional lures not tested in prior Norwegian samples.",
])

add("Practical recommendations", 2, [
    "Recommendation 1 - Lure-specific training: Replace generic \"don't click unknown links\" with scenario-based modules covering IT impersonation, exam/fee authority lures, and social/belonging messages (Finans Norge, 2026; Nettvett.no & NSM, n.d.).",
    "Recommendation 2 - Non-punitive reporting: Near-miss reporting channels with explicit no-blame policy; align with Chen et al. (2024) support-seeking training rather than fear-only simulations.",
    "Recommendation 3 - Student welfare integration: Coordinate security communications with student loneliness initiatives (SHoT Study, 2022; OsloMet, 2024) without stigmatising lonely students as \"high risk.\"",
    "Recommendation 4 - Verify-by-default routines: Separate-channel verification for unexpected IT, fee, or BankID requests; institutional templates showing how legitimate messages appear.",
    "Recommendation 5 - High-risk periods: Targeted reminders during exam periods, tax season, and onboarding when authority and stress lures peak.",
    "[INSERT: Tailor recommendations to supported/unsupported hypotheses]",
])

add("Limitations", 2, [
    "Methodological: self-report survey; hypothetical vignettes; convenience sample; cross-sectional design; single country; higher-education focus.",
    "Qualitative: researcher interpretation; social desirability in interviews; opt-in bias among interviewees willing to discuss fraud and loneliness.",
    "Integration: quant and qual samples overlap partially but not all interviewees need represent survey median.",
    "Generalisation: findings apply cautiously to Norwegian HE adults, not all populations or live phishing behaviour.",
])

add("Future research", 2, [
    "Longitudinal study tracking loneliness and near misses over an academic year.",
    "Intervention study comparing lure-specific emotional-aware training vs standard modules.",
    "Cross-Nordic comparison of institutional trust and phishing susceptibility.",
    "Organisational ethnography of reporting culture in university IT and student admin units.",
])

add("Conclusion", 1, [
    "Phishing persists not primarily because users lack scepticism, but because scepticism is lure-specific and human needs are exploitable. The weakest-link metaphor obscures how credible impersonation targets belonging, authority, and institutional trust - domains that function normally in Norwegian digital life.",
    "This thesis introduced and tested the scepticism paradox through mixed methods: survey vignettes, loneliness and scepticism scales, and interviews on credibility, shame, and reporting. [INSERT: One-sentence summary of key empirical outcome.]",
    "The practical takeaway for OsloMet and comparable institutions: security is socio-technical. Safer outcomes require lure-specific awareness, non-punitive learning from near misses, and recognition that emotionally meaningful lures can bypass the same scepticism that protects against obvious stranger fraud.",
    "Phase 3 completes the ACIT long thesis arc. Final steps before defence: merge chapters into single WISEflow document; Ouriginal plagiarism check; figure/table lists; supervisor approval; oral presentation preparation.",
])

add("Oral defence preparation (notes)", 2, [
    "Presentation structure (~30 min): (1) problem and paradox; (2) methods overview; (3) key results quant + qual; (4) integrated finding example; (5) recommendations; (6) limitations.",
    "[INSERT: 3-5 core slides storyline after results known]",
])

add("Appendices", 1, [])

add("Appendix A: Interview guide (draft)", 2, [
    "1. Walk me through a time you received a message you thought might be fraudulent. What did you notice first?",
    "2. What makes a message feel trustworthy or suspicious?",
    "3. How do you handle unexpected emails from IT, exam office, or BankID/Altinn?",
    "4. Have you ever almost clicked something you later realised was suspicious? What was happening in your life then?",
    "5. Do feelings of loneliness or stress affect how you respond to messages? (Optional skip)",
    "6. What training have you had? What was missing?",
    "7. If you made a mistake, would you report it? Why or why not?",
    "8. Anything else about digital fraud and student/work life?",
])

add("Appendix B: Codebook template", 2, [
    "Code | Definition | Example excerpt | Theme",
    "institutional_trust | Message perceived as official/expected | \"It looked like OsloMet IT\" | Theme 1",
    "stranger_dismissal | Quick rejection of unknown sender | \"Obviously fake lottery\" | Theme 1",
    "belonging_pull | Social inclusion motive | \"I wanted to join the group\" | Theme 2",
    "exam_pressure | Urgency during exams/deadlines | \"Had three deadlines that week\" | Theme 2/3",
    "know_but_click | Articulates rules yet nearly acted | \"I knew I should check\" | Theme 3",
    "shame_silence | Would not report due to embarrassment | \"I'd feel stupid\" | Theme 4",
    "supportive_report | Would report if culture supportive | \"Better to tell IT\" | Theme 4",
])

add("Appendix C: Interview consent (outline)", 2, [
    "Recording consent; pseudonym use; secure storage; right to withdraw; SIKT reference; welfare contacts.",
])

add("Appendix D: Final thesis chapter merge checklist", 2, [
    "1. Preface and abstract (updated with results). 2. Ch 1-2 from Phase 1 (edited). 3. Ch 3 Methodology (Phase 2 survey + Phase 3 interviews). 4. Ch 4 Results (survey + themes + integration). 5. Ch 5 Discussion. 6. Ch 6 Conclusion. 7. References merged. 8. Appendices: survey, vignettes, interview guide, ethics. 9. List of figures/tables. 10. WISEflow ACIT5930 + Appx zip.",
])

add("Appendix E: WISEflow submission checklist", 2, [
    "Filename Etternavn_Fornavn_studentnummer_ACIT5930; Ouriginal check; all [INSERT] removed; SIKT docs in Appx; figure alt-text; page numbers; 19 May deadline.",
])

REFERENCES = """
<p class="refs"><strong>References</strong></p>
<p class="refs hanging">Bayl-Smith, P., Taib, R., Yu, K., &amp; Wiggins, M. W. (2024). Response to a phishing attack. <em>Information and Computer Security</em>.</p>
<p class="refs hanging">Braun, V., &amp; Clarke, V. (2006). Using thematic analysis in psychology. <em>Qualitative Research in Psychology, 3</em>(2), 77-101.</p>
<p class="refs hanging">Braun, V., &amp; Clarke, V. (2021). One size fits all? What counts as quality practice in (reflexive) thematic analysis? <em>Qualitative Research in Psychology, 18</em>(3), 328-352.</p>
<p class="refs hanging">Cacioppo, J. T., &amp; Patrick, W. (2008). <em>Loneliness: Human nature and the need for social connection</em>. Norton.</p>
<p class="refs hanging">Chen, Y., et al. (2024). Group discussion and role-playing training on phishing reporting. <em>CHI Proceedings</em>.</p>
<p class="refs hanging">Fetters, M. D., Curry, L. A., &amp; Creswell, J. W. (2013). Achieving integration in mixed methods designs. <em>Journal of Mixed Methods Research, 7</em>(6), 443-453.</p>
<p class="refs hanging">Finans Norge. (2026). <em>Selvforsvar mot svindel</em>. https://www.svindel.no/</p>
<p class="refs hanging">Hadnagy, C. (2018). <em>Social engineering: The science of human hacking</em> (2nd ed.). Wiley.</p>
<p class="refs hanging">Klütsch, J., et al. (2024). Friend or phisher. <em>Humanities and Social Sciences Communications, 11</em>(1).</p>
<p class="refs hanging">Norwegian National Security Authority. (2026). <em>National cyber security risk assessment</em>.</p>
<p class="refs hanging">OsloMet. (2024). Student social connection initiatives.</p>
<p class="refs hanging">Rogers, R. W. (1975). Protection motivation theory. <em>Journal of Psychology, 91</em>(1), 93-114.</p>
<p class="refs hanging">SHoT Study. (2022). Student health and wellbeing survey.</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2020). Phishing susceptibility in a Norwegian sample.</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2022). Cognitive reflection and phishing.</p>
"""

CSS = """
:root { --black:#000; --ink:#1a1a1a; --dark:#333; --mid:#666; --line:#ccc; --light:#f0f0f0; --paper:#fff; }
* { box-sizing:border-box; }
body { margin:0; font-family:"Times New Roman", Times, serif; font-size:12pt; line-height:1.5; color:var(--ink); background:#e8e8e8; }
.toolbar { position:sticky; top:0; background:#111; color:#fff; padding:10px 16px; font-family:Calibri,sans-serif; font-size:14px; z-index:9; }
.toolbar a { color:#7fd; margin-right:1rem; }
.page { max-width:210mm; margin:1rem auto; background:var(--paper); padding:25mm; box-shadow:0 2px 12px rgba(0,0,0,.15); }
.cover { text-align:center; min-height:180mm; display:flex; flex-direction:column; justify-content:center; page-break-after:always; }
.cover h1 { font-size:22pt; font-weight:700; line-height:1.3; color:var(--black); margin:0 0 .5rem; }
.cover .sub { font-size:14pt; margin:.5rem 0; color:var(--dark); }
.cover .author { font-size:16pt; font-weight:700; margin-top:2rem; }
.cover .meta { font-size:12pt; color:var(--mid); margin-top:1rem; }
.draft-banner { background:#fff3cd; border:1px solid #856404; color:#533f03; padding:.75rem; margin:1rem 0; font-size:11pt; }
.abstract { margin:1.5rem 0; padding:1rem; background:var(--light); border-left:3px solid var(--dark); page-break-after:always; }
h1.ch { font-size:16pt; border-bottom:2px solid var(--black); padding-bottom:.3rem; margin:2rem 0 1rem; page-break-before:always; }
h1.ch:first-of-type { page-break-before:auto; }
h2 { font-size:14pt; margin:1.2rem 0 .6rem; color:var(--black); }
p { font-size:12pt; margin:0 0 .65rem; text-align:left; }
.criteria { font-size:11pt; color:var(--mid); margin:1rem 0; padding:.75rem; border:1px solid var(--line); }
table.data { width:100%; border-collapse:collapse; margin:1rem 0; font-size:11pt; }
table.data th, table.data td { border:1px solid var(--line); padding:6px 8px; text-align:left; }
table.data caption { caption-side:top; text-align:left; font-weight:700; margin-bottom:.5rem; }
.refs { font-size:12pt; margin:0 0 .4rem; }
.hanging { padding-left:2em; text-indent:-2em; }
@media print { body{background:#fff;} .toolbar{display:none;} .page{box-shadow:none;margin:0;} }
"""

body_html = []
word_count = 0
for level, title, paragraphs in SECTIONS:
    if level == 1:
        body_html.append(f'<h1 class="ch">{title}</h1>')
    elif level == 2:
        body_html.append(f'<h2>{title}</h2>')
    elif level == "table":
        body_html.append(paragraphs[0])
        continue
    for p in paragraphs:
        body_html.append(f'<p>{p}</p>')
        word_count += len(p.split())

abstract = """
<p><strong>Abstract.</strong> This Phase 3 draft (ACIT5930) completes the mixed-methods master thesis on the scepticism paradox in Norwegian higher education. Building on Phase 1 theory and Phase 2 survey analysis, Phase 3 presents semi-structured interview methodology (N = 12-18 planned), reflexive thematic analysis, integration with quantitative findings via joint displays, and final discussion, conclusions, and recommendations. Five thematic areas are anticipated: lure-specific credibility, emotional context and loneliness, knowledge-behaviour gaps, shame and reporting culture, and training limitations. The discussion revisits the weakest-link narrative, extends Protection Motivation Theory toward coping appraisal, and proposes lure-specific training, non-punitive reporting, and student welfare integration for OsloMet and comparable institutions. [INSERT: Final abstract results sentence after data collection.] Keywords: phishing, scepticism paradox, thematic analysis, mixed methods, loneliness, Norway.</p>
"""

criteria = """
<div class="criteria"><strong>ACIT5930 Phase 3 draft mapped:</strong> Interview methodology · Qualitative results (themes) · Integration with Phase 2 · Discussion · Conclusion · Recommendations · Oral defence notes · Appendices · Sluttinnlevering 19 May · Times New Roman 12 pt</div>
<div class="draft-banner"><strong>Final phase draft:</strong> Replace all [INSERT] fields after interviews and integration. Merge with Phase 1-2 into single WISEflow document for ACIT5930. No fabricated quotes.</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} - ACIT5930 Phase 3 Draft</title>
<style>{CSS}</style>
</head>
<body>
<div class="toolbar">
  <strong>ACIT5930 Phase 3 Draft</strong> (~{word_count} words body)
  · <a href="ACIT5920_phase2_draft.html">Phase 2</a>
  · <a href="ACIT5910_phase1_essay.html">Phase 1</a>
  · <a href="index.html">Phase I PDF view</a>
  · <a href="ACIT5930_phase3_draft.pdf">PDF</a>
</div>
<div class="page">
<div class="cover">
  <p class="meta">{COURSE}</p>
  <h1>{TITLE}<br>{SUBTITLE}</h1>
  <p class="sub">A Mixed-Methods Study of Loneliness, Social Engineering, and Digital Trust in Norway</p>
  <p class="author">{AUTHOR}</p>
  <p class="meta">OsloMet · Department of Computer Science · Cybersecurity · Final submission draft</p>
</div>
{criteria}
<div class="abstract">{abstract}</div>
{"".join(body_html)}
{REFERENCES}
</div>
</body>
</html>"""

out = Path("/workspace/masterthesis/ACIT5930_phase3_draft.html")
out.write_text(html)
print(f"Body words: {word_count}")
print(f"Wrote {out}")
