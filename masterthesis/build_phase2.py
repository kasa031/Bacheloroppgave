#!/usr/bin/env python3
"""Build ACIT5920 Phase 2 draft HTML."""
from pathlib import Path
from apa_style import APA_BANNER, APA_CSS, REFERENCES, abstract_html, cover_html

TITLE = "Beyond the Weakest Link: The Skepticism Paradox"
SUBTITLE = "Why Phishing Works Despite Rising Skepticism"
COURSE = "ACIT5920 Master's Thesis, Phase 2 (draft)"

SECTIONS = []


def add(title, level, paragraphs):
    SECTIONS.append((level, title, paragraphs))


def table(html):
    SECTIONS.append(("table", "", [html]))


add("Introduction and continuity from Phase 1", 1, [
    "This document is a draft submission for ACIT5920 (Phase 2) of the master thesis Beyond the Weakest Link: The Skepticism Paradox. Phase 1 (ACIT5910) established the research problem, literature review, theoretical framework, and preliminary methodology. Phase 2 advances the project by finalising the survey instrument, documenting ethics and data collection procedures, and presenting preliminary quantitative analysis from pilot testing and main survey collection.",
    "The central research question remains: How can phishing remain effective despite rising scepticism, and which emotional, cognitive, and contextual factors make individuals especially vulnerable beyond the weakest-link explanation? Four hypotheses (H1-H4) guide empirical testing through scenario vignettes, loneliness measures, general scepticism items, situational pressure scales, and security culture indicators.",
    "Phase 2 deliverables per the ACIT handbook and project plan include: (1) a finalised survey instrument after pilot; (2) SIKT ethics approval and documented consent procedures; (3) collection and cleaning of the main survey dataset (target N = 120-180); and (4) preliminary quantitative analysis with a draft Results chapter. Interviews and integrated mixed-methods analysis are planned for Phase 3 (ACIT5930).",
    "This draft is structured for WISEflow submission as Etternavn_Fornavn_studentnummer_ACIT5920. Placeholders marked [INSERT] indicate fields to complete when pilot or main data are available. The draft follows handbook chapter structure: Introduction, condensed theory, Methodology, Results, Preliminary Discussion, and Appendices.",
])

add("Theoretical framework recap", 1, [
    "The scepticism paradox holds that general caution toward strangers and vulnerability to socially or institutionally credible lures can coexist (Klütsch et al., 2024; Parker & Flowerday, 2020). Loneliness is treated as subjective social disconnection that may increase salience of belonging-framed lures (Cacioppo & Patrick, 2008). Protection Motivation Theory (PMT) informs analysis of verification habits and non-punitive security culture as coping appraisal factors (Rogers, 1975; Bayl-Smith et al., 2024).",
])

add("Hypotheses", 2, [
    "H1: Higher loneliness is associated with higher self-reported phishing susceptibility, especially for socially framed lures (S2, S6).",
    "H2: Higher general scepticism reduces susceptibility for stranger-framed lures (S1) but not for institutionally or emotionally relevant lures (S2-S6); a loneliness x lure-type interaction is expected for social/belonging vignettes.",
    "H3: Situational pressure (urgency, authority, stress) partially mediates the relationship between loneliness and unsafe intended behaviour.",
    "H4: Participants with stronger verification habits and supportive, non-punitive security culture report lower susceptibility across vignettes (PMT coping appraisal).",
])

add("Methodology", 1, [])

add("Research design", 2, [
    "The study uses an exploratory sequential mixed-methods design (Braun & Clarke, 2006). Phase 2 implements the quantitative strand: a cross-sectional online survey with scenario vignettes and validated/adapted scales. Phase 3 will add semi-structured interviews and integrate findings. The quantitative phase precedes interviews so that interview sampling can target variation in loneliness scores and vignette responses.",
    "The design prioritises ethical safety: vignettes present hypothetical messages; no live deceptive phishing is deployed against participants. Intended behaviour is measured on a fixed ordinal scale rather than actual clicks on malicious links.",
    "Within-subject comparison across six vignettes increases statistical power relative to between-subject designs and mirrors the real-world condition in which the same individual receives multiple lure types over time. Each participant acts as their own control for general scepticism and loneliness, while lure framing varies systematically.",
    "The quantitative phase answers whether self-reported traits and contexts predict intended unsafe behaviour across lure types. It does not measure actual victimisation rates or organisational incident data; those would require different methods and permissions beyond this thesis scope.",
])

add("Conceptual model and variables", 2, [
    "Figure 1 (conceptual, from Phase 1) maps the scepticism paradox for empirical testing. Independent variables: loneliness (continuous), general online scepticism (continuous), situational pressure (continuous/mediator). Within-subject factor: lure type (six vignettes). Dependent variable: intended unsafe behaviour (click immediately vs verify/ignore/report). Moderators/mediators for H3-H4: situational pressure, verification habits, security culture.",
    "Control variables reduce confounding: age, role (student/staff), prior phishing training exposure, self-rated digital literacy. Optional cognitive reflection item enables comparison with Tjostheim and Waterworth (2020, 2022) Norwegian samples.",
    "The model treats phishing susceptibility as lure-specific rather than trait-only. A respondent may score high on scepticism and low on loneliness yet still select \"click\" on S3 if institutional authority cues dominate—a pattern that would support H2 and contradict uniform weakest-link assumptions.",
])

add("Pilot study", 2, [
    "Before main data collection, a pilot with 10-15 students and staff at OsloMet tested instrument clarity, completion time, and floor/ceiling effects. Pilot criteria: median completion under 12 minutes; no item with more than 5% missing; vignette instructions understood without assistance; loneliness and scepticism items show sufficient variance.",
    "Pilot revisions expected: shorten redundant items, clarify Norwegian/English terminology for institutional lures (BankID, Altinn, IT-support), and adjust vignette ordering to reduce carry-over effects. Pilot data are excluded from main hypothesis tests but inform instrument finalisation documented in Appendix A.",
    "[INSERT: Pilot N, completion time median, items revised, date conducted]",
])

add("Population, sampling, and recruitment", 2, [
    "Population: adults aged 18+ in Norwegian higher education with regular digital communication for study or work. Target sample: 120-180 complete survey responses (power adequate for moderation analysis with continuous predictors; see analysis plan).",
    "Inclusion: student or employee at a Norwegian university or university college; uses email or messaging for study/work weekly; reads Norwegian or English.",
    "Exclusion: under 18; no regular digital communication; completed the survey previously (duplicate IP/cookie check).",
    "Recruitment channels: OsloMet student email lists (with faculty approval), student organisation social media, LinkedIn (higher-education Norway), and snowball sharing with privacy-preserving invitation text. No personal phishing data are collected; recruitment materials state the academic purpose and SIKT approval reference.",
    "[INSERT: Recruitment start/end dates, institutions reached, response rate]",
])

add("Survey platform and procedure", 2, [
    "The survey is hosted on an institution-approved platform (e.g. Nettskjema/Digital Survey Services via OsloMet). Participants access via anonymous link or QR code. Flow: information sheet, informed consent checkbox, demographics, loneliness and scepticism scales, situational pressure and culture items, vignettes S1-S6 in randomised order (to control order effects), verification habits, open-text items, debrief with fraud reporting resources (Finans Norge, NSM Nettvett).",
    "Estimated duration: 10-12 minutes. No compensation planned unless approved by supervisor and SIKT. Participants may withdraw until submission; partial responses are deleted on withdrawal request.",
    "Randomisation of vignette order uses built-in survey logic to reduce priming effects: if S1 (stranger) always appeared first, subsequent institutional lures might appear more credible by contrast. Counterbalancing checks whether order affects mean unsafe intention.",
    "Mobile compatibility is required because many students complete surveys on phones—the same device used for smishing targets. Layout is single-column with minimum 12 pt equivalent text.",
])

add("Instruments and operationalisation", 2, [
    "Loneliness (3-6 items): adapted from established short forms aligned with SSB loneliness indicators (Statistics Norway, 2025). Example stem: \"How often do you feel that you lack companionship?\" (1 = never to 5 = always). Mean score forms continuous predictor; higher = greater subjective loneliness.",
    "General online scepticism (4-6 items): distrust of unknown senders, unexpected links, unsolicited attachments. Example: \"I am cautious about clicking links from people I do not know.\" (1 = strongly disagree to 5 = strongly agree).",
    "Situational pressure (4 items): perceived urgency, authority, stress, time pressure during survey completion as proxy for decision context.",
    "Verification habits (4 items): frequency of checking sender via separate channel, inspecting URL, consulting peers, delaying response when unsure.",
    "Security culture (4 items): perceived blame after mistakes, comfort reporting near misses, quality of institutional security communication (Bayl-Smith et al., 2024; Chen et al., 2024).",
    "Controls: age, gender (optional), role (student/staff), study level, prior phishing training, self-rated digital literacy, cognitive reflection short item (optional, compare Tjostheim & Waterworth, 2020).",
    "Full item list: Appendix A.",
])

add("Scenario vignettes (S1-S6)", 2, [
    "Six vignettes manipulate lure framing. Each presents a short message in Norwegian context. Response scale per vignette: 1 = Would click/open immediately; 2 = Would verify via separate channel first; 3 = Would ignore; 4 = Would report as suspicious. Primary dependent variable: unsafe intention (1 vs 2-4) and ordinal susceptibility score.",
    "S1 Stranger: SMS from unknown number claiming prize win, link to \"claim reward.\"",
    "S2 Social: Message appearing to be from a fellow student inviting you to a private study group WhatsApp link before exam.",
    "S3 Institutional: Email styled as OsloMet IT support requesting immediate password reset via link due to \"security incident.\"",
    "S4 Authority: Email appearing from exam office demanding fee payment within 2 hours to avoid registration hold.",
    "S5 Opportunity: LinkedIn-style message offering exclusive internship interview slot; link to \"confirm availability\" within 24 hours.",
    "S6 Belonging: Invitation to a \"student wellbeing circle\" video call for people \"who often feel left out,\" with warm tone and signup link.",
    "Full vignette texts: Appendix B. Alt-text and plain-language summaries included for accessibility (handbook WCAG requirement).",
])

add("Ethics and data management", 2, [
    "Ethics application submitted to SIKT (Norwegian Agency for Shared Services in Education and Research) before main collection. [INSERT: SIKT reference number, approval date]. Informed consent covers anonymised storage, thesis use, and optional contact for Phase 3 interviews.",
    "GDPR compliance: data stored encrypted on OsloMet-approved systems; access limited to researcher and supervisor; retention per SIKT approval; deletion after archive period. No names, email addresses, or IP addresses stored with response data. Fraud victimisation questions are optional and preceded by content warning.",
    "Debrief provides links to Finans Norge (svindel.no), NSM Nettvett, and student welfare services. Participants experiencing distress may contact SiO or equivalent.",
    "The study avoids deception about study purpose: participants know they are evaluating hypothetical messages for a thesis on phishing and loneliness. This differs from unannounced simulated phishing in organisations, which raises separate ethical issues (Chen et al., 2024). Transparency may increase social desirability bias toward \"verify\" responses; this is acknowledged as a limitation.",
])

add("Data cleaning and quality checks", 2, [
    "Exclusion rules: completion time under 3 minutes (insufficient engagement); straight-lining on all Likert items; duplicate responses. Missing data: preregistered maximum 20% missing on scale items; multiple imputation not planned for main analysis given ordinal outcomes; listwise deletion for primary regression models with sensitivity analysis.",
    "Coding: vignette unsafe = 1 if response is \"click immediately\"; scepticism and loneliness as continuous; lure type as within-subject factor (six levels) in repeated-measures framework.",
])

add("Analysis plan", 2, [
    "Software: R or SPSS. Descriptive statistics for all variables and vignette response distributions. Reliability: Cronbach's alpha for multi-item scales (target alpha > .70).",
    "H1: Mixed-effects or repeated-measures logistic regression with loneliness predicting unsafe intention; interaction term loneliness x lure type; focus on S2 and S6 vs S1.",
    "H2: General scepticism x lure type interaction; contrast stranger (S1) vs institutional/social lures.",
    "H3: Mediation analysis (PROCESS or structural equation) with situational pressure as mediator between loneliness and unsafe intention.",
    "H4: Verification habits and security culture as moderators or predictors of safer responses (verify/report vs click).",
    "Controls in all models: age, role, prior training, digital literacy. Subgroup exploratory analysis: age bands 18-24 vs 25+ given Wen et al. (2024).",
    "Assumptions: check multicollinearity (VIF), residual patterns for linear components; sensitivity analysis with alternative cut-offs for unsafe behaviour.",
    "[INSERT: R/SPSS script reference in appendix when analysis complete]",
    "Sample size rationale: N = 120-180 provides adequate power for medium-sized interaction effects in logistic mixed models with six repeated measures per participant. A conservative rule of thumb requires 15-20 observations per predictor in multivariate models; the upper target (N = 180) allows listwise deletion without falling below power thresholds.",
    "Multiple comparison correction: Benjamini-Hochberg FDR applied across primary hypothesis tests (H1-H4) to control false discovery rate while retaining power relative to Bonferroni.",
])

add("Validity, reliability, and limitations", 2, [
    "Construct validity: vignettes reviewed by supervisor and pilot participants for face validity in Norwegian HE context. Self-report susceptibility may differ from behaviour; vignettes approximate decision intention under hypothetical conditions (common in phishing research; Parker & Flowerday, 2020).",
    "External validity: convenience sample may overrepresent digitally literate students; findings generalise cautiously beyond higher education.",
    "Limitations stated in Phase 2: cross-sectional design; self-report bias; no causal claims; loneliness measured subjectively; English/Norwegian bilingual items may affect subsets.",
])

add("Results", 1, [])

add("Sample and descriptives", 2, [
    "This section presents preliminary quantitative results from the Phase 2 survey. [INSERT when main collection complete: final N, demographics table, recruitment summary.] Table 1 shows the planned descriptive output structure.",
])

table("""
<table class="data">
<caption><strong>Table 1.</strong> Sample characteristics (main survey). [INSERT data]</caption>
<thead><tr><th>Variable</th><th>n</th><th>% or M (SD)</th></tr></thead>
<tbody>
<tr><td>Total valid responses</td><td>[ ]</td><td>100%</td></tr>
<tr><td>Students</td><td>[ ]</td><td>[ ]%</td></tr>
<tr><td>Staff</td><td>[ ]</td><td>[ ]%</td></tr>
<tr><td>Age 18-24</td><td>[ ]</td><td>[ ]%</td></tr>
<tr><td>Age 25-34</td><td>[ ]</td><td>[ ]%</td></tr>
<tr><td>Prior phishing training (yes)</td><td>[ ]</td><td>[ ]%</td></tr>
<tr><td>Loneliness scale mean</td><td colspan="2">[ ] ([ ])</td></tr>
<tr><td>General scepticism mean</td><td colspan="2">[ ] ([ ])</td></tr>
</tbody>
</table>
""")

add("Vignette response patterns", 2, [
    "Figure 1 (planned) displays the percentage selecting \"click immediately\" per vignette. Based on Phase 1 literature, stranger-framed S1 is expected to show lower unsafe intention among high-scepticism respondents, while S3 (institutional) and S6 (belonging) may show higher unsafe intention regardless of general scepticism—consistent with the scepticism paradox.",
    "[INSERT: Figure 1 bar chart S1-S6 unsafe intention percentages]",
])

table("""
<table class="data">
<caption><strong>Table 2.</strong> Intended unsafe behaviour by vignette (click immediately). [INSERT data]</caption>
<thead><tr><th>Vignette</th><th>Lure type</th><th>Click %</th><th>Verify %</th><th>Ignore %</th><th>Report %</th></tr></thead>
<tbody>
<tr><td>S1</td><td>Stranger</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>S2</td><td>Social</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>S3</td><td>Institutional</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>S4</td><td>Authority</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>S5</td><td>Opportunity</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>S6</td><td>Belonging</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
</tbody>
</table>
""")

add("Hypothesis testing (preliminary)", 2, [
    "H1 (loneliness and social lures): [INSERT: regression coefficient, OR, p-value, interaction loneliness x S2/S6]. Expected direction: positive association between loneliness and unsafe intention for S2 and S6; weaker or null for S1.",
    "H2 (scepticism x lure type): [INSERT: interaction term results]. Expected: scepticism negatively associated with S1 unsafe intention; non-significant or weaker for S3 and S6.",
    "H3 (mediation): [INSERT: indirect effect estimate, CI]. Expected: partial mediation by situational pressure.",
    "H4 (coping appraisal): [INSERT: verification habits and culture predictors]. Expected: higher verify/report rates among those with strong verification habits and non-punitive culture perceptions.",
])

table("""
<table class="data">
<caption><strong>Table 3.</strong> Summary of hypothesis tests. [INSERT statistics]</caption>
<thead><tr><th>Hypothesis</th><th>Model</th><th>Key statistic</th><th>p</th><th>Supported?</th></tr></thead>
<tbody>
<tr><td>H1</td><td>Loneliness x lure (S2,S6)</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>H2</td><td>Scepticism x lure type</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>H3</td><td>Mediation (pressure)</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
<tr><td>H4</td><td>Verification + culture</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
</tbody>
</table>
""")

add("Open-text preliminary themes", 2, [
    "Two open items asked about near misses and what makes messages feel credible. Phase 2 coding is descriptive until Phase 3 thematic analysis. Preliminary codebook: (1) institutional branding; (2) time pressure; (3) social inclusion; (4) shame about almost clicking; (5) knowledge-behaviour gap.",
    "[INSERT: 2-3 anonymised quote excerpts illustrative of scepticism paradox]",
])

add("Preliminary discussion", 1, [])

add("Interpretation through the scepticism paradox", 2, [
    "Phase 2 results will be interpreted against the scepticism paradox: if H2 is supported, general scepticism protects primarily against stranger-framed lures, not institutional or belonging frames. That pattern would challenge weakest-link training that treats scepticism as uniformly protective.",
    "If H1 is supported among higher-education adults, loneliness research and cybersecurity practice should intersect more deliberately—without pathologising students, but recognising that socially meaningful lures exploit unmet connection needs (SHoT Study, 2022).",
    "If H4 is supported, organisational responsibility for non-punitive reporting and verify-by-default routines is empirically justified alongside individual traits (Chen et al., 2024).",
])

add("Implications for Phase 3", 2, [
    "Interview sampling in Phase 3 will stratify by loneliness tertiles and vignette response profiles (high vs low susceptibility on S3/S6). Interview guide topics: credibility cues, emotional state, reporting culture experiences. Integration will use joint displays linking Table 2 patterns with qualitative mechanisms.",
    "[INSERT: Planned interview N, recruitment from survey opt-in]",
])

add("Limitations and next steps", 2, [
    "Phase 2 remains cross-sectional and self-report based. Causal language is avoided. Main limitations: sample representativeness, hypothetical vignettes vs live behaviour, single time point.",
    "Next steps before Phase 3 submission: complete main survey analysis; finalise Figure 1 and Table 3; obtain supervisor feedback; begin SIKT-approved interview recruitment; update abstract with confirmed findings.",
    "Timeline alignment: Autumn 2026 Phase 1 approved; pilot and SIKT application; Spring 2027 main survey; Autumn 2027 interviews; Spring 2028 final thesis. Phase 2 submission target follows ACIT5920 Canvas deadline for Autumn semester.",
])

add("Relation to Phase 1 and thesis continuity", 2, [
    "Phase 1 established the scepticism paradox theoretically and reviewed evidence that weakest-link training is insufficient. Phase 2 operationalises that theory into measurable constructs and vignettes grounded in Norwegian higher-education contexts (BankID culture, OsloMet IT communication patterns, student loneliness data from SHoT 2022).",
    "No contradiction is expected between phases: if results fail to support H1 or H2, the thesis will revise the paradox or its boundary conditions rather than ignore null findings. Phase 2 therefore includes explicit hypothesis summary tables and pre-registered analysis steps to support transparent reporting.",
    "Writing from Phase 1 Introduction and Literature Review will be condensed in the final thesis; Phase 2 Methodology and Results chapters will replace the Phase 1 \"planned\" placeholders in master_thesis_phase1.pdf.",
])

add("Practical relevance (preliminary)", 2, [
    "Even before final results, the Phase 2 instrument can inform OsloMet awareness materials: vignettes S3 and S6 can be adapted (with ethics approval) into training examples that address institutional and belonging lures rather than only stranger scams.",
    "If H4 trends appear in descriptive data, student administration and IT security may collaborate on non-punitive reporting messaging during exam periods—when S4 authority lures are most plausible.",
    "Findings will be shared with supervisor and, if approved, summarised for student welfare and IT security stakeholders without exposing individual responses.",
])

add("Appendices", 1, [])

add("Appendix A: Survey items (draft)", 2, [
    "L1. I lack companionship. [1-5] | L2. I feel left out. [1-5] | L3. I feel isolated from others. [1-5]",
    "SK1. I am cautious about links from unknown senders. [1-5] | SK2. Unexpected attachments make me suspicious. [1-5] | SK3. I trust messages from official institutions without checking. [reverse, 1-5]",
    "VH1. I verify unexpected requests via a separate channel. [1-5] | VH2. I check URL before clicking. [1-5]",
    "SC1. My institution treats phishing mistakes punitively. [reverse] | SC2. I would feel comfortable reporting a near miss.",
    "Open: Describe a time you almost clicked a suspicious message. What made it credible?",
])

add("Appendix B: Vignette texts (full draft)", 2, [
    "S1 (Stranger): \"Gratulerer! Du har vunnet 10 000 kr i varelotteriet. Klikk her for a hente premien innen 24 timer: [link]\"",
    "S2 (Social): \"Hei! Det er [fornavn] fra DATA2000-gruppen. Vi har lage en WhatsApp-gruppe til eksamen - bli med her sa deler vi oppsummeringer: [link]\"",
    "S3 (Institutional): \"OsloMet IT: Av sikkerhetsgrunner ma du tilbakestille passordet ditt innen i kveld. Klikk her: [link]. Unnlatelse kan medfore sperret konto.\"",
    "S4 (Authority): \"Eksamenskontoret: Utestaende eksamensgebyr ma betales innen 2 timer for a unnga studiestopp. Betal her: [link]\"",
    "S5 (Opportunity): \"Hei, jeg representerer [selskap]. Vi har et eksklusivt internship-intervju til deg - bekreft tidspunkt innen 24t: [link]\"",
    "S6 (Belonging): \"Hei, vi inviterer deg til en liten online gruppe for studenter som ofte foler seg alene. Ingen drommer, bare stotte. Bli med her: [link]\"",
])

add("Appendix C: Consent and debrief (outline)", 2, [
    "Consent key points: voluntary participation; anonymised data; thesis and academic publication use; right to withdraw; contact researcher/supervisor; SIKT approval reference.",
    "Debrief: study purpose (scepticism paradox); no real credentials collected; resources - svindel.no, nettvett.no, SiO/student welfare.",
])

add("Appendix D: Recruitment invitation (draft text)", 2, [
    "Subject: Invitation to research survey - digital security and social connection (10 min)",
    "Body: You are invited to participate in an anonymous OsloMet master thesis survey on phishing awareness and social connection among students and staff. The study uses hypothetical message scenarios—not real phishing. Approved by SIKT [reference]. Link: [URL]. Contact: [researcher email].",
])

add("Appendix E: Phase 2 checklist for WISEflow submission", 2, [
    "1. Replace all [INSERT] placeholders with final data. 2. Confirm SIKT approval number on consent page. 3. Run plagiarism check (Ouriginal). 4. Filename: Etternavn_Fornavn_studentnummer_ACIT5920. 5. Append survey PDF export as ACIT5920_Appx if required. 6. Verify figure alt-text. 7. Supervisor sign-off obtained.",
])

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

abstract = abstract_html(
    "This Phase 2 draft (ACIT5920) documents the quantitative strand of a mixed-methods study on the scepticism paradox: why phishing remains effective despite rising general scepticism toward strangers in Norway. Building on Phase 1, the draft presents finalised survey methodology, scenario vignettes (S1-S6), SIKT ethics procedures, data cleaning rules, and statistical analysis plans for hypotheses H1-H4. The Results chapter provides structured tables and figures with [INSERT] placeholders for main survey data. Phase 3 will add interviews and integrated analysis.",
    "phishing, scepticism paradox, methodology, survey, vignettes, loneliness, ACIT5920",
)

draft_banner = """
<div class="draft-banner"><strong>Draft status:</strong> Replace all [INSERT] fields after pilot and main survey collection. Do not submit fabricated statistics.</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} - ACIT5920 Phase 2 Draft</title>
<style>{APA_CSS}</style>
</head>
<body>
<div class="toolbar">
  <strong>ACIT5920 Phase 2 draft</strong> (~{word_count} words)
  · <a href="ACIT5910_phase1_essay.html">Phase 1</a>
  · <a href="ACIT5920_phase2_draft.pdf">PDF</a>
</div>
<div class="page">
{cover_html(TITLE, SUBTITLE, COURSE)}
{APA_BANNER}
{draft_banner}
{abstract}
{"".join(body_html)}
{REFERENCES}
</div>
</body>
</html>"""

out = Path("/workspace/masterthesis/ACIT5920_phase2_draft.html")
out.write_text(html)
print(f"Body words: {word_count}")
print(f"Wrote {out}")
