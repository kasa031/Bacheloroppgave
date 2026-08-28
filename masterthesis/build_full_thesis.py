#!/usr/bin/env python3
"""Build one long master thesis HTML from original Phase I text + Phase 2 + Phase 3."""
from __future__ import annotations

import re
from pathlib import Path

import build_phase2
import build_phase3
from apa_style import APA_FULL_CSS, REFERENCES, full_thesis_cover, render_chapter

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT / "master_thesis_original_phase1.html"
OUT_HTML = ROOT / "master_thesis_full.html"

SKIP_PHASE1_CHAPTERS = {
    "Planned Results",
    "Research Plan and Timeline",
    "Summary and Preliminary Conclusions",
    "Planned Discussion",
}


def extract_phase1_body(html: str) -> str:
    """Keep original Phase I chapters through Methodology (original prose)."""
    page_match = re.search(r'<div class="page">(.*)</div></div>\s*</body>', html, re.DOTALL)
    if not page_match:
        raise ValueError("Could not find .page content in original HTML")
    body = page_match.group(1)
    body = re.sub(r'<div class="cover-page">.*?</div>', "", body, count=1, flags=re.DOTALL)
    body = re.sub(r"<p>dept=.*?</p>\s*<p>program=.*?</p>\s*<p>option=.*?</p>", "", body, flags=re.DOTALL)

    parts = []
    for match in re.finditer(
        r'<section class="chapter"><h1>([^<]+)</h1>(.*?)</section>',
        body,
        re.DOTALL,
    ):
        title = match.group(1).strip()
        if title in SKIP_PHASE1_CHAPTERS:
            break
        parts.append(f'<section class="chapter"><h1>{title}</h1>{match.group(2)}</section>')
    return "".join(parts)


def count_words(html: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html)
    return len(text.split())


def build_html() -> str:
    original = ORIGINAL.read_text(encoding="utf-8")
    phase1 = extract_phase1_body(original)

    p2 = build_phase2.SECTIONS
    p3 = build_phase3.SECTIONS

    body = f"""
{full_thesis_cover()}
<div class="draft-banner"><strong>Working full thesis draft.</strong> Based on <a href="master_thesis_original_phase1.html">original Phase I</a> (unchanged copy) with Phase 2 survey and Phase 3 interview strands appended. APA 7 (Kildekompasset). Replace all [INSERT] before submission.</div>
{phase1}
<section class="chapter"><h1>Survey Methodology (Phase 2)</h1>
{render_chapter(p2, "Methodology")}
</section>
<section class="chapter"><h1>Results: Quantitative Findings</h1>
{render_chapter(p2, "Results")}
</section>
<section class="chapter"><h1>Interview Methodology (Phase 3)</h1>
{render_chapter(p3, "Interview methodology")}
</section>
<section class="chapter"><h1>Results: Qualitative Themes</h1>
{render_chapter(p3, "Qualitative results")}
</section>
<section class="chapter"><h1>Integrated Findings</h1>
{render_chapter(p3, "Integrated findings")}
</section>
<section class="chapter"><h1>Discussion</h1>
{render_chapter(p3, "Discussion")}
</section>
<section class="chapter"><h1>Conclusion</h1>
{render_chapter(p3, "Conclusion")}
</section>
<section class="chapter"><h1>Appendices</h1>
<h2>Survey and ethics (Phase 2)</h2>
{render_chapter(p2, "Appendices")}
<h2>Interview materials (Phase 3)</h2>
{render_chapter(p3, "Appendices")}
</section>
{REFERENCES}
"""
    words = count_words(body)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Beyond the Weakest Link - Full Master Thesis Draft</title>
<style>{APA_FULL_CSS}</style>
</head>
<body>
<div class="toolbar">
  <strong>Masteroppgave · full utkast (APA 7)</strong> (~{words} words)
  · <a href="master_thesis_original_phase1.html">Original Phase I (kopi)</a>
  · <a href="master_thesis_phase1.pdf">Phase I PDF</a>
  · <a href="master_thesis_full.pdf">Full PDF</a>
</div>
<div class="page">
{body}
</div>
</body>
</html>"""


def main() -> None:
    html = build_html()
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML} (~{count_words(html)} words)")


if __name__ == "__main__":
    main()
