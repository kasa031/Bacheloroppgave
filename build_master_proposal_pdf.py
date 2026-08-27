#!/usr/bin/env python3
"""Build PDF from master thesis proposal HTML."""

import subprocess
from pathlib import Path

ROOT = Path("/workspace")
HTML = ROOT / "master_thesis_phishing_proposal.html"
PDF = ROOT / "master_thesis_phishing_proposal.pdf"
CHROME = "/usr/bin/google-chrome"


def main():
    if not HTML.exists():
        raise SystemExit(f"Missing {HTML}")
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir=/tmp/chrome-master-pdf",
        "--force-device-scale-factor=1",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF}",
        f"file://{HTML}",
    ]
    subprocess.run(cmd, check=True, timeout=60)
    print("Wrote", PDF, "bytes", PDF.stat().st_size)


if __name__ == "__main__":
    main()
