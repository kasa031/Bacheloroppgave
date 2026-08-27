#!/usr/bin/env python3
"""Build PDF versions of master thesis documents."""

import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace")
CHROME = "/usr/bin/google-chrome"
PROFILE = "/tmp/chrome-master-pdf"


def build_pdf(html: Path, pdf: Path) -> None:
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={PROFILE}",
        "--force-device-scale-factor=1",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf}",
        f"file://{html}",
    ]
    subprocess.run(cmd, check=True, timeout=90)


def main():
    targets = [
        (ROOT / "master_thesis_phishing_proposal.html", ROOT / "master_thesis_phishing_proposal.pdf"),
        (ROOT / "master_thesis_draft.html", ROOT / "master_thesis_draft.pdf"),
    ]
    if len(sys.argv) > 1:
        name = sys.argv[1]
        targets = [(ROOT / f"{name}.html", ROOT / f"{name}.pdf")]
    for html, pdf in targets:
        if not html.exists():
            raise SystemExit(f"Missing {html}")
        build_pdf(html, pdf)
        print("Wrote", pdf, "bytes", pdf.stat().st_size)


if __name__ == "__main__":
    main()
