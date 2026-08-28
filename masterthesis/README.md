# Master Thesis - Phase I (read-only view)

Private viewing copies for Karina. Not part of the GitHub Pages app on `main`.

## Reference style

Body text uses the same layout as `master_thesis_phase1.pdf` (Times New Roman 12 pt, 1.5 line spacing, 16 pt chapter headings). Reference lists follow APA 7 (Kildekompasset) with hanging indent. LaTeX source uses `biblatex` with `style=apa`.

## Build

```bash
python3 build_essay.py      # ACIT5910 Phase 1 HTML
python3 build_phase2.py     # ACIT5920 Phase 2 HTML
python3 build_phase3.py     # ACIT5930 Phase 3 HTML
python3 build_pdf.py        # Export phase HTML to PDF (Headless Chrome)
```

## Read in browser

- **ACIT5910 Phase 1 essay (HTML):** [ACIT5910_phase1_essay.html](./ACIT5910_phase1_essay.html)
- **ACIT5910 Phase 1 essay (PDF):** [ACIT5910_phase1_essay.pdf](./ACIT5910_phase1_essay.pdf)
- **ACIT5920 Phase 2 draft (HTML):** [ACIT5920_phase2_draft.html](./ACIT5920_phase2_draft.html)
- **ACIT5920 Phase 2 draft (PDF):** [ACIT5920_phase2_draft.pdf](./ACIT5920_phase2_draft.pdf)
- **ACIT5930 Phase 3 draft (HTML):** [ACIT5930_phase3_draft.html](./ACIT5930_phase3_draft.html)
- **ACIT5930 Phase 3 draft (PDF):** [ACIT5930_phase3_draft.pdf](./ACIT5930_phase3_draft.pdf)
- **Newest Phase I (HTML):** [index.html](./index.html)
- **Newest Phase I (PDF):** [master_thesis_phase1.pdf](./master_thesis_phase1.pdf)
- **Original draft v0.8 (HTML):** [master_thesis_draft_v08.html](./master_thesis_draft_v08.html)
- **Original draft v0.8 (PDF):** [master_thesis_draft_v08.pdf](./master_thesis_draft_v08.pdf)

## LaTeX source

Files in `source/` (main.tex, mybib.bib, etc.)

## CDN links (after push)

Replace `BRANCH` with `cursor/masterthesis-view-d899`:

- ACIT5910 essay HTML: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5910_phase1_essay.html`
- ACIT5910 essay PDF: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5910_phase1_essay.pdf`
- ACIT5920 Phase 2 HTML: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5920_phase2_draft.html`
- ACIT5920 Phase 2 PDF: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5920_phase2_draft.pdf`
- ACIT5930 Phase 3 HTML: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5930_phase3_draft.html`
- ACIT5930 Phase 3 PDF: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/ACIT5930_phase3_draft.pdf`
- jsDelivr HTML: `https://cdn.jsdelivr.net/gh/kasa031/Bacheloroppgave@BRANCH/masterthesis/index.html`
- GitHub raw PDF: `https://raw.githubusercontent.com/kasa031/Bacheloroppgave/BRANCH/masterthesis/master_thesis_phase1.pdf`
