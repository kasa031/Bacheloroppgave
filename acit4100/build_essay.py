#!/usr/bin/env python3
"""Build ACIT4100 research-field essay HTML."""
from pathlib import Path

TITLE = "The Human Side of the Hook"
SUBTITLE = "A Field Guide to Research on Phishing, Social Engineering, and Digital Trust"
AUTHOR = "Karina Sætersdal Nilssen"
COURSE = "ACIT4100 · Essay · Autumn 2026"

SECTIONS = []


def add(title, level, paragraphs, style="classic"):
    SECTIONS.append((level, title, paragraphs, style))


def narrative(text):
    SECTIONS.append(("narrative", "", [text]))


add("Introduction", 1, [
    "Every year, organisations spend heavily on firewalls, filters, and multi-factor authentication. Every year, phishing remains one of the most common ways attackers enter systems. The gap between technical investment and human compromise is not a mystery to one research community: scholars who study human factors in cybersecurity. Their job is not primarily to build better malware signatures. It is to understand why cautious, literate people still click.",
    "This essay describes that field of research as it exists today: how it asks questions, how it produces knowledge, where it publishes, how it relates to law and ethics, and why it matters to society beyond the security operations centre. The focus is the research itself, not a technology product review. Where the course invites narrative style, short cut-scenes appear between sections; they illustrate how research questions emerge from ordinary digital life, not to invent new findings but to ground the reader in the world this science tries to explain.",
    "The field sits at the intersection of cybersecurity, psychology, human-computer interaction, and organisational behaviour. It is heterogeneous by design. Some studies run controlled experiments in university labs; others analyse real incident reports; still others conduct interviews with fraud victims or security awareness trainers. What unites them is a shared rejection of the idea that phishing persists because users are uniformly naive. The research field treats phishing as a problem of meaning, context, and decision under pressure.",
])

narrative("""
She refreshes her inbox between lectures. A message from \"OsloMet IT\" asks her to reset her password within the hour. She has heard the warnings about unknown senders. She has also received real IT notices before. She hovers over the link. In another building, a researcher reads survey responses describing exactly this moment—not to judge the student, but to learn what \"credible\" looks like when fear and habit collide.
""")

add("What this research field studies", 2, [
    "Human factors cybersecurity research examines how people perceive, evaluate, and respond to security threats in everyday digital environments. Phishing and social engineering are central because they exploit communication channels users already trust: email, SMS, messaging apps, and voice calls (Hadnagy, 2018; Conteh & Schmick, 2016).",
    "Typical research objects include: susceptibility to deceptive messages; effectiveness of awareness training; reporting behaviour after near misses; cognitive and emotional predictors of unsafe actions; and organisational culture around blame and disclosure (Parker & Flowerday, 2020; Chen et al., 2024). Norwegian studies by Tjostheim and Waterworth (2020, 2022) exemplify national contributions linking cognitive reflection to phishing compliance in representative samples.",
    "The field does not treat \"the user\" as a homogeneous category. Recent work emphasises lure-specific vulnerability: people may reject stranger scams yet hesitate on messages impersonating institutions, peers, or employers (Klütsch et al., 2024). That line of inquiry connects to broader debates about digital trust in high-trust societies such as Norway, where BankID, Altinn, and university IT communication create both convenience and impersonation risk (Norwegian National Security Authority [NSM], 2026; Finans Norge, 2026).",
])

add("Notable researchers, groups, and centres", 2, [
    "Human factors security research is distributed globally rather than centred in one laboratory. Influential individual researchers include Christopher Hadnagy on social engineering practice and ethics; Steven Pinker (outside security but foundational for classic style communication assigned in ACIT4100); and scholars such as Flowerday, Parker, and Tsai on phishing persuasion and organisational context.",
    "Institutional clusters include Carnegie Mellon's CyLab and usable security traditions; University of Florida's SOUPS community; European ENISA research networks; and Nordic contributions through Norwegian ICT conferences where Tjostheim and Waterworth publish representative-sample phishing studies.",
    "Industry research units (Microsoft Digital Defense, Google TAG) publish threat data that academia cites for motivation but rarely for method. Students mapping the field should distinguish corporate report series from peer-reviewed archives.",
])

add("How to read and approach scientific work in this field", 2, [
    "Course guidance emphasises skill in locating and reading scientific sources rather than producing anthropology from scratch. A practical workflow: define the field boundary (human factors + phishing); search ACM Digital Library and IEEE with terms such as \"phishing susceptibility,\" \"social engineering,\" \"usable security\"; skim abstracts for method type; read methods and limitations before discussion sections.",
    "When synthesising, note sample population (students, employees, nation), lure type (email, SMS, social), and outcome (click, report, self-report intention). Compare whether authors claim user deficit or systemic/contextual explanation—that ideological split runs through the literature and helps organise an essay thematically.",
    "Students are not required to judge statistical quality at expert level, but reporting how authors interpret their own findings is expected. Phrases such as \"the authors argue\" or \"the study suggests, within undergraduate samples\" keep interpretation honest.",
])

add("Regulatory and professional constraints in Norway", 2, [
    "Norwegian researchers must align with SIKT notification/approval for personal data on behaviour and sensitive topics (loneliness, fraud victimisation). National campaigns by Finans Norge and NSM shape public scepticism but are not research instruments—students should not confuse policy documents with empirical studies.",
    "Working life and education law intersect when organisational phishing simulations affect employees or students. Punitive simulation designs have been criticised in research literature for suppressing reporting—the regulatory environment for such programmes is organisational policy as much as national law.",
])

add("Effects of this research upon society", 2, [
    "When effective, human factors research changes training content, incident response playbooks, and public messaging. When ignored, organisations continue blaming users while impersonation of BankID, Altinn, and university IT persists (NSM, 2026; Politiet, 2024).",
    "Social effects include reduced shame when non-punitive reporting is normalised (Chen et al., 2024); potential stigmatisation if loneliness is framed as individual risk rather than structural student-life issue; and improved digital literacy when lure-specific examples replace generic \"don't click\" slogans.",
    "The research field does not operate in a vacuum: student wellbeing surveys (SHoT, 2022) and cybersecurity awareness modules rarely cross-reference each other, yet both speak to student vulnerability in digital environments. Describing that silo is part of describing the field's societal embedding.",
])

add("Style note: classic and narrative hybrid", 2, [
    "This essay applies classic style in the main exposition: direct statements, active verbs, concrete nouns, and sequential reasoning as Pinker recommends for clarifying complex ideas to a general educated reader. Narrative cut-scenes function like documentary B-roll: they do not introduce new empirical claims but situate the reader emotionally before returning to synthesis of published research.",
    "A purely narrative essay could embed all perspectives inside fiction; a purely classic essay could omit cut-scenes entirely. The hybrid used here mirrors televised documentary structure permitted by the 2026 assignment brief.",
])

add("Research methods and methodologies", 1, [
    "Methodological pluralism defines this field. No single method owns the truth about human clicking behaviour. Instead, researchers combine approaches depending on whether they need experimental control, ecological validity, or lived experience.",
])

add("Experimental and laboratory designs", 2, [
    "Controlled experiments remain common. Participants receive simulated phishing emails or messages in lab or online settings; researchers manipulate variables such as sender identity, urgency, authority cues, or grammatical quality (Tsai et al., 2021). Dependent variables include click rates, credential entry, time to decision, and self-reported suspicion.",
    "Strengths: isolation of causal factors, reproducibility, statistical power. Weaknesses: simulated attacks may not carry real consequences; participants know they are in a study, which can inflate cautious behaviour (social desirability bias). Ethics boards therefore scrutinise deceptive designs carefully.",
])

add("Surveys and scenario vignettes", 2, [
    "Large-scale surveys measure self-reported behaviour, attitudes, loneliness, scepticism, and intended responses to hypothetical scenarios (vignettes). Vignettes manipulate lure framing—stranger, institutional, social, authority—without exposing participants to live malware (Parker & Flowerday, 2020).",
    "This approach scales nationally, as Tjostheim and Waterworth demonstrated in Norway. Trade-off: intended behaviour may differ from behaviour under real loss or embarrassment.",
])

add("Mixed methods and qualitative inquiry", 2, [
    "Mixed-methods designs increasingly combine surveys with semi-structured interviews or thematic analysis (Braun & Clarke, 2006). Quantitative strands identify patterns; qualitative strands explain mechanisms—shame, credibility cues, reporting culture—that numbers alone cannot capture (Chen et al., 2024).",
    "Integration techniques include joint displays linking statistical results with anonymised quotes (Fetters et al., 2013). This reflects a maturing field that treats human factors as more than a regression table.",
])

add("Field studies and industry collaboration", 2, [
    "Some research analyses organisational phishing simulations, help-desk tickets, or anonymised incident data with industry partners. Access is negotiated under confidentiality agreements. Findings inform training design but may not be fully public.",
    "Threat intelligence reports from ENISA, Microsoft, and NSM provide macro context but rarely substitute for peer-reviewed human-subjects research (European Union Agency for Cybersecurity [ENISA], 2024).",
])

narrative("""
The lab room is quiet except for keyboard clicks. On screen, red and green bars compare click rates across two email templates. The researcher notes that version B added only one line: \"Your supervisor requested this today.\" No new exploit code. Just words. The experiment will become a conference slide; later, perhaps, a training module—if the reviewers agree the effect is real.
""")

add("Philosophy of science in the field", 1, [
    "Human factors cybersecurity research draws on multiple philosophical traditions, often implicitly rather than through explicit manifestos.",
    "Positivist and post-positivist strands dominate experimental and survey work: hypotheses, measurable variables, falsification, effect sizes. Protection Motivation Theory from health psychology migrated into security behaviour research under this logic (Rogers, 1975; Floyd et al., 2000; Bayl-Smith et al., 2024).",
    "Interpretivist and constructivist strands appear in interview-based and ethnographic work: meaning is situated; \"risk\" is co-produced by users, institutions, and attackers. A message is not objectively phishing until interpreted in context.",
    "Critical perspectives question the \"weakest link\" metaphor that locates failure inside individuals while obscuring organisational responsibility (Hadnagy, 2018). Some scholars frame phishing as a socio-technical failure: systems generate high volumes of ambiguous communication; attackers exploit trust infrastructures citizens rely on daily.",
    "The field rarely resolves these philosophies into one camp. Pragmatism wins: mixed methods prevail because the phenomenon is too messy for a single epistemology.",
])

add("History and development of the field", 1, [
    "Phishing as a research object dates to the early 2000s when mass email fraud became visible to academia and industry simultaneously. Early work catalogued technical indicators—spoofed headers, URL obfuscation—and user ignorance.",
    "The shift toward human factors accelerated as defences improved and attackers pivoted to social manipulation. Hadnagy's social engineering literature (2018) and annual industry reports documented that technical maturity did not eliminate human entry points.",
    "Human-computer interaction venues (CHI, SOUPS) began accepting phishing behaviour papers alongside usable security workshops. Psychology and consumer fraud research on loneliness and persuasion cross-pollinated with cybersecurity during the 2010s (Cacioppo & Patrick, 2008; Alves & Wilson, 2008).",
    "Norwegian contributions emerged through national ICT conferences and representative surveys (Tjostheim & Waterworth, 2020, 2022), aligning local digitalisation (BankID culture) with empirical behaviour research.",
    "Recent trajectories include AI-assisted lure generation (Halcyon, 2026; Trend Micro, 2026), loneliness and student wellbeing links (SHoT Study, 2022; Statistics Norway, 2025), and scepticism paradox framing—why general caution toward strangers coexists with institutional impersonation vulnerability.",
])

add("Publication traditions: journals and conferences", 1, [
    "Researchers in this field publish across security, HCI, and organisational journals. Notable outlets include Computers & Security, Computers in Human Behavior, Information and Computer Security, Journal of Cybersecurity, and proceedings from CHI, SOUPS, and USENIX Security workshops.",
    "Interdisciplinary acceptance varies. A vignette study may face reviewer questions from both psychologists (\"Is the scale validated?\") and security engineers (\"Where is the threat model?\"). Successful papers often include explicit threat context and reproducible instruments.",
    "Grey literature—NSM risk assessments, ENISA threat landscapes, Finans Norge fraud campaigns—shapes public discourse and student motivation but does not replace peer review for academic essays. Students learning the field must read both: reports for timeliness, journals for methodology transparency.",
])

add("Ethics, regulation, and codes of conduct", 1, [
    "Ethics is not peripheral in this field; it is structural. Deceptive experiments (simulated phishing without consent) can harm participants through shame, misplaced blame, or unintended disclosure of personal habits.",
    "Institutional review boards and national agencies (SIKT in Norway; formerly NSD) evaluate whether deception is justified, whether debriefing is adequate, and whether data minimisation is observed. Live phishing against unwitting participants is generally rejected; vignettes and announced simulations are preferred.",
    "GDPR governs storage of behavioural data. Fraud victimisation questions require content warnings. Reporting near misses in organisational studies must protect employee identity.",
    "Professional codes in cybersecurity (e.g. EC Council, (ISC)² ethics canons) emphasise lawful behaviour and public good, but academic research adds informed consent and right to withdraw. Tension arises when industry partners want identifiable incident data researchers cannot ethically provide.",
])

narrative("""
The ethics form asks: \"Will participants be deceived?\" She checks \"minimal deception—scenario vignettes only.\" The committee asks for a debrief link to svindel.no. Outside, autumn rain on the campus windows. Research here moves slowly—not because computers are slow, but because people matter.
""")

add("Relationship with society, industry, and other experts", 1, [
    "Human factors research connects to multiple publics. Industry consumes findings for awareness programmes, simulated phishing metrics, and security culture initiatives. Governments reference human behaviour in national risk assessments (NSM, 2026). Banks and finance associations run public literacy campaigns (Finans Norge, 2026).",
    "Student welfare services encounter loneliness and digital fraud as parallel student-life issues; research that bridges them must communicate carefully to avoid stigmatising vulnerable groups (Directorate of Health, 2024; SHoT Study, 2022).",
    "Relations with \"hard\" security research are complementary. Cryptographers and malware analysts ask what is technically possible; human factors researchers ask what is psychologically plausible. Incident responders supply anecdotes; academics supply sampling frames and statistics.",
    "Disagreement exists. Some practitioners dismiss academic effect sizes as irrelevant to SOC workload; some academics criticise punitive phishing simulations in workplaces. The research field documents both sides rather than enforcing unity.",
])

add("How researchers produce and synthesise knowledge", 2, [
    "Students in ACIT4100 are not expected to invent new models. The task mirrors what working researchers do in literature reviews: search databases (ACM, IEEE, Scopus, Google Scholar); trace citation chains; compare methods; note geographic and sample biases; synthesise trends.",
    "Quality signals include: pre-registration for experiments; open instruments; representative sampling; preregistered analysis plans; and replication attempts. Weak signals include: convenience samples without boundary discussion; click-rate-only metrics without context; fear-based training evaluations without coping measures.",
    "Meta-analyses on protection motivation and security behaviour aggregate decades of small studies (Floyd et al., 2000). Narrative reviews in ENISA and Microsoft reports aggregate incident trends without human-subjects detail. A well-written field essay cites both types while respecting their limits.",
])

add("Current debates within the field", 2, [
    "Active debates include: whether simulated phishing in workplaces improves behaviour or increases shame (Chen et al., 2024); whether AI-generated lures change psychology or only aesthetics (Halcyon, 2026); whether loneliness predicts fraud susceptibility equally across age groups (Wen et al., 2024; Klütsch et al., 2024); and whether general scepticism training transfers to institutional impersonation.",
    "These debates are not settled. The essay reports them as the living edge of the field—the places where new master's theses and industry pilots attach.",
])

add("Conclusion: communicating research as technologists", 1, [
    "Human factors cybersecurity research is a field where technologists learn to read humans with the same rigour they read code—through methods, ethics, history, and public consequence. It explains why phishing survives technical progress: attackers optimise for trust, urgency, and belonging, not only for software bugs.",
    "For ACIT students, understanding this field means knowing where knowledge comes from, not only what the latest awareness poster says. It means recognising journals, ethics constraints, and societal stakeholders. It means writing about research in clear classic prose, occasionally illuminated by narrative cut-scenes that remind us that behind every dataset is someone hovering over a link between lectures.",
    "The field will keep evolving as digital trust infrastructures evolve. Norway's combination of high institutional trust and measurable social disconnection among young adults makes it a relevant site for contemporary work—not because Norwegians are uniquely weak, but because the research questions about scepticism, loneliness, and credible impersonation are unusually visible here.",
    "To enter this field as a reader or future contributor is to accept a split attention: technical systems and human meaning. The research community studies that split for a living. This essay has mapped how they do it.",
])

REFERENCES = """
<p class="refs"><strong>References</strong></p>
<p class="refs hanging">Alves, L. M., &amp; Wilson, S. R. (2008). The effects of loneliness on telemarketing fraud vulnerability among older adults. <em>Journal of Elder Abuse &amp; Neglect, 20</em>(1), 63-85.</p>
<p class="refs hanging">Bayl-Smith, P., Taib, R., Yu, K., &amp; Wiggins, M. W. (2024). Response to a phishing attack. <em>Information and Computer Security</em>.</p>
<p class="refs hanging">Braun, V., &amp; Clarke, V. (2006). Using thematic analysis in psychology. <em>Qualitative Research in Psychology, 3</em>(2), 77-101.</p>
<p class="refs hanging">Cacioppo, J. T., &amp; Patrick, W. (2008). <em>Loneliness: Human nature and the need for social connection</em>. Norton.</p>
<p class="refs hanging">Chen, Y., et al. (2024). Group discussion and role-playing training on phishing reporting. <em>CHI Proceedings</em>.</p>
<p class="refs hanging">Conteh, N. Y., &amp; Schmick, P. J. (2016). Cybersecurity risk management framework. <em>Journal of Cyber Security Technology</em>.</p>
<p class="refs hanging">Directorate of Health. (2024). Loneliness and public health.</p>
<p class="refs hanging">European Union Agency for Cybersecurity. (2024). <em>ENISA threat landscape 2024</em>.</p>
<p class="refs hanging">Fetters, M. D., Curry, L. A., &amp; Creswell, J. W. (2013). Integration in mixed methods designs. <em>Journal of Mixed Methods Research, 7</em>(6), 443-453.</p>
<p class="refs hanging">Finans Norge. (2026). <em>Selvforsvar mot svindel</em>. https://www.svindel.no/</p>
<p class="refs hanging">Floyd, D. L., Prentice-Dunn, S., &amp; Rogers, R. W. (2000). Meta-analysis of protection motivation theory. <em>Journal of Applied Social Psychology, 30</em>(2), 407-429.</p>
<p class="refs hanging">Hadnagy, C. (2018). <em>Social engineering: The science of human hacking</em> (2nd ed.). Wiley.</p>
<p class="refs hanging">Halcyon. (2026). <em>AI and ransomware threat report</em>.</p>
<p class="refs hanging">Klütsch, J., et al. (2024). Friend or phisher. <em>Humanities and Social Sciences Communications, 11</em>(1).</p>
<p class="refs hanging">Norwegian National Security Authority. (2026). <em>National cyber security risk assessment</em>.</p>
<p class="refs hanging">Parker, H. J., &amp; Flowerday, S. V. (2020). Social media phishing susceptibility. <em>SA Journal of Information Management, 22</em>(1).</p>
<p class="refs hanging">Rogers, R. W. (1975). Protection motivation theory. <em>Journal of Psychology, 91</em>(1), 93-114.</p>
<p class="refs hanging">SHoT Study. (2022). Student health and wellbeing survey.</p>
<p class="refs hanging">Statistics Norway. (2025). Quality of life survey: Loneliness indicators.</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2020). Phishing susceptibility in a Norwegian sample.</p>
<p class="refs hanging">Tjostheim, I., &amp; Waterworth, J. A. (2022). Cognitive reflection and phishing.</p>
<p class="refs hanging">Trend Micro. (2026). <em>Phishing threat report</em>.</p>
<p class="refs hanging">Tsai, T. H., et al. (2021). Phishing and persuasion strategies. <em>Computers &amp; Security</em>.</p>
<p class="refs hanging">Wen, Y., et al. (2024). Loneliness and fraud susceptibility. <em>Journal of Consumer Affairs</em>.</p>
"""

CSS = """
:root { --black:#000; --ink:#1a1a1a; --dark:#333; --mid:#666; --line:#ccc; --light:#f0f0f0; --paper:#fff; --narr:#f7f3ea; }
* { box-sizing:border-box; }
body { margin:0; font-family:"Times New Roman", Times, serif; font-size:12pt; line-height:1.5; color:var(--ink); background:#e8e8e8; }
.toolbar { position:sticky; top:0; background:#111; color:#fff; padding:10px 16px; font-family:Calibri,sans-serif; font-size:14px; z-index:9; }
.toolbar a { color:#7fd; margin-right:1rem; }
.page { max-width:210mm; margin:1rem auto; background:var(--paper); padding:25mm; box-shadow:0 2px 12px rgba(0,0,0,.15); }
.cover { text-align:center; min-height:160mm; display:flex; flex-direction:column; justify-content:center; page-break-after:always; }
.cover h1 { font-size:22pt; font-weight:700; line-height:1.3; color:var(--black); margin:0 0 .5rem; }
.cover .sub { font-size:14pt; margin:.5rem 0; color:var(--dark); }
.cover .author { font-size:16pt; font-weight:700; margin-top:2rem; }
.cover .meta { font-size:12pt; color:var(--mid); margin-top:1rem; }
.criteria { font-size:11pt; color:var(--mid); margin:1rem 0; padding:.75rem; border:1px solid var(--line); }
.abstract { margin:1.5rem 0; padding:1rem; background:var(--light); border-left:3px solid var(--dark); }
h1.ch { font-size:16pt; border-bottom:2px solid var(--black); padding-bottom:.3rem; margin:2rem 0 1rem; page-break-before:always; }
h1.ch:first-of-type { page-break-before:auto; }
h2 { font-size:14pt; margin:1.2rem 0 .6rem; color:var(--black); }
p { font-size:12pt; margin:0 0 .65rem; text-align:left; }
.narrative { margin:1.2rem 0; padding:1rem 1.2rem; background:var(--narr); border-left:4px solid var(--dark); font-style:italic; }
.narrative-label { font-size:10pt; font-style:normal; font-weight:700; color:var(--mid); margin-bottom:.4rem; }
.refs { font-size:12pt; margin:0 0 .4rem; }
.hanging { padding-left:2em; text-indent:-2em; }
@media print { body{background:#fff;} .toolbar{display:none;} .page{box-shadow:none;margin:0;} }
"""

body_html = []
word_count = 0
for item in SECTIONS:
    if len(item) == 4:
        level, title, paragraphs, _style = item
    else:
        level, title, paragraphs = item
    if level == "narrative":
        body_html.append(f'<div class="narrative"><p class="narrative-label">Cut-scene (narrative style)</p><p>{paragraphs[0]}</p></div>')
        word_count += len(paragraphs[0].split())
        continue
    if level == 1:
        body_html.append(f'<h1 class="ch">{title}</h1>')
    elif level == 2:
        body_html.append(f'<h2>{title}</h2>')
    for p in paragraphs:
        body_html.append(f'<p>{p}</p>')
        word_count += len(p.split())

criteria = """
<div class="criteria"><strong>ACIT4100 2026 mapped:</strong> Research field essay (not own findings) · Methods · Philosophy of science · History · Publications · Ethics/regulation · Society/industry · Classic style + narrative cut-scenes · Synthesise existing research · APA references</div>
"""

abstract = """
<p><strong>Abstract.</strong> This essay describes the research field of human factors in cybersecurity, with emphasis on phishing, social engineering, and digital trust. Rather than evaluating a technology product or presenting original experiments, it summarises how researchers ask questions, which methods they use (experiments, surveys, vignettes, mixed methods), and how the field relates to ethics, regulation, publication traditions, and society. Classic prose carries the main argument; three narrative cut-scenes illustrate how research connects to everyday digital decisions. The field is presented as an evolving interdisciplinary domain shaped by debates on user blame, lure-specific vulnerability, and the limits of awareness training.</p>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} - ACIT4100 Essay</title>
<style>{CSS}</style>
</head>
<body>
<div class="toolbar">
  <strong>ACIT4100 Essay</strong> (~{word_count} words)
  · <a href="ACIT4100_research_field_essay.html">ACIT4100 essay</a>
  · <a href="../masterthesis/ACIT5910_phase1_essay.html">Master Phase 1</a>
  · <a href="ACIT4100_research_field_essay.pdf">PDF</a>
</div>
<div class="page">
<div class="cover">
  <p class="meta">{COURSE}</p>
  <h1>{TITLE}</h1>
  <p class="sub">{SUBTITLE}</p>
  <p class="author">{AUTHOR}</p>
  <p class="meta">OsloMet · Applied Computer and Information Technology · Cybersecurity</p>
</div>
{criteria}
<div class="abstract">{abstract}</div>
{"".join(body_html)}
{REFERENCES}
</div>
</body>
</html>"""

out_dir = Path("/workspace/acit4100")
out_dir.mkdir(exist_ok=True)
out = out_dir / "ACIT4100_research_field_essay.html"
out.write_text(html)
print(f"Body words: {word_count}")
print(f"Wrote {out}")
