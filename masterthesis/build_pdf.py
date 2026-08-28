#!/usr/bin/env python3
"""Export HTML drafts to PDF using Headless Chrome (same engine as Phase I)."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHROME = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")

PDF_TARGETS = [
    "ACIT5910_phase1_essay.html",
    "ACIT5920_phase2_draft.html",
    "ACIT5930_phase3_draft.html",
]


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    if not CHROME:
        raise RuntimeError("Chrome/Chromium not found for PDF export")
    url = html_path.resolve().as_uri()
    pdf_path.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory(prefix="masterthesis-chrome-") as tmp:
        cmd = (
            f"timeout 120 {CHROME} --headless=new --disable-gpu --no-sandbox "
            f'--user-data-dir="{tmp}" --run-all-compositor-stages-before-draw '
            f'--print-to-pdf="{pdf_path.resolve()}" --no-pdf-header-footer "{url}"'
        )
        result = subprocess.run(cmd, shell=True)
        # Chrome often writes the PDF then hangs; timeout 124 is OK if output exists.
        if result.returncode not in (0, 124):
            raise RuntimeError(f"Chrome PDF export failed (exit {result.returncode})")
    if not pdf_path.exists() or pdf_path.stat().st_size < 1024:
        raise RuntimeError(f"No PDF produced for {html_path.name}")


def main() -> int:
    for name in PDF_TARGETS:
        html = ROOT / name
        if not html.exists():
            print(f"Skip missing {html.name}")
            continue
        pdf = html.with_suffix(".pdf")
        html_to_pdf(html, pdf)
        print(f"PDF: {pdf.name} ({pdf.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
