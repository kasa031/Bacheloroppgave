#!/usr/bin/env python3
"""Generate submission figures for ACIT4280 Group Assignment 1A from Table 2 data."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT = Path("/workspace/figures")
OUT.mkdir(exist_ok=True)

NAVY = "#1B365D"
INK = "#1A1A1A"
MUTED = "#4A5568"
CREAM = "#FFF1D1"
LINE = "#D0D5DD"
PAPER = "#FFFEFB"
GREEN = "#1B6B3A"
AMBER = "#9A5B00"

SECTOR_COLOR = {
    "Shopping": "#4A6FA5",
    "Government": "#1B6B3A",
    "News / media": "#9A5B00",
    "Sport": "#1B365D",
}

SITES = [
    ("xxl.no", "Shopping", 26),
    ("cdon.no", "Shopping", 33),
    ("ikea.no", "Shopping", 15),
    ("babyshop.no", "Shopping", 45),
    ("skatteetaten.no", "Government", 14),
    ("barnevernet.no", "Government", 25),
    ("altinn.no", "Government", 5),
    ("lanekassen.no", "Government", 1),
    ("aftenposten.no", "News / media", 48),
    ("nrk.no", "News / media", 7),
    ("netflix.no", "News / media", 22),
    ("document.no", "News / media", 51),
    ("klassekampen.no", "News / media", 46),
    ("spotify.no", "News / media", 10),
    ("worldofwarcraft.com", "News / media", 90),
    ("dnt.no", "Sport", 16),
    ("fotball.no", "Sport", 113),
    ("skiforeningen.no", "Sport", 14),
]


def style_axes(ax):
    ax.set_facecolor(PAPER)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(LINE)
    ax.spines["bottom"].set_color(LINE)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.yaxis.label.set_color(INK)
    ax.xaxis.label.set_color(INK)


def fig_requests_all18():
    ranked = sorted(SITES, key=lambda x: x[2])
    names = [r[0] for r in ranked]
    vals = [r[2] for r in ranked]
    colors = [SECTOR_COLOR[r[1]] for r in ranked]

    fig, ax = plt.subplots(figsize=(10.2, 7.2), dpi=240)
    fig.patch.set_facecolor(PAPER)
    style_axes(ax)
    y = np.arange(len(names))
    ax.barh(y, vals, color=colors, height=0.72, zorder=2)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9, color=INK)
    ax.set_xlabel("Third-party requests (first measurement, 20 August 2026)")
    ax.set_xlim(0, 130)
    ax.grid(axis="x", color=LINE, linewidth=0.6, zorder=0)
    for yi, v in zip(y, vals):
        ax.text(v + 1.2, yi, str(v), va="center", fontsize=8, color=INK)
    handles = [
        plt.Rectangle((0, 0), 1, 1, color=SECTOR_COLOR[k], label=k)
        for k in ["Shopping", "Government", "News / media", "Sport"]
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8)
    fig.tight_layout()
    path = OUT / "fig3_requests_all18.png"
    fig.savefig(path, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("wrote", path)


def fig_requests_sector():
    order = ["Shopping", "Government", "News / media", "Sport"]
    totals = {k: 0 for k in order}
    counts = {k: 0 for k in order}
    for _, sector, req in SITES:
        totals[sector] += req
        counts[sector] += 1
    means = [totals[k] / counts[k] for k in order]
    sums = [totals[k] for k in order]
    colors = [SECTOR_COLOR[k] for k in order]

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), dpi=240)
    fig.patch.set_facecolor(PAPER)
    for ax, data, title in (
        (axes[0], sums, "Sum of third-party requests"),
        (axes[1], means, "Mean requests per site"),
    ):
        style_axes(ax)
        x = np.arange(len(order))
        ax.bar(x, data, color=colors, width=0.62, zorder=2)
        ax.set_xticks(x)
        ax.set_xticklabels(["Shopping", "Government", "News / media", "Sport"], fontsize=9)
        ax.set_xlabel(title, fontsize=10, color=INK, labelpad=12)
        ax.grid(axis="y", color=LINE, linewidth=0.6, zorder=0)
        for xi, v in zip(x, data):
            label = f"{v:.0f}" if title.startswith("Sum") else f"{v:.1f}"
            ax.text(xi, v + max(data) * 0.02, label, ha="center", fontsize=9, color=INK)
    fig.tight_layout(pad=1.4)
    path = OUT / "fig6_requests_per_sector.png"
    fig.savefig(path, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("wrote", path)


def fig_webbkoll_start():
    """Schematic of the Webbkoll check interface used in the method."""
    fig, ax = plt.subplots(figsize=(9.2, 5.2), dpi=240)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.add_patch(FancyBboxPatch((0.3, 0.35), 9.4, 5.3, boxstyle="round,pad=0.04,rounding_size=0.12",
                                facecolor="#F4F6F8", edgecolor=NAVY, linewidth=1.4))
    ax.add_patch(FancyBboxPatch((0.3, 4.85), 9.4, 0.8, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=NAVY, edgecolor=NAVY, linewidth=0))
    ax.text(0.55, 5.22, "Webbkoll", fontsize=16, color=CREAM, fontweight="bold", va="center")
    ax.text(9.4, 5.22, "English", fontsize=10, color=CREAM, ha="right", va="center")

    ax.text(5, 4.35, "Check a website", fontsize=14, color=NAVY, ha="center", fontweight="bold")
    ax.text(5, 3.95, "HTTPS, cookies, third-party requests and related headers",
            fontsize=9, color=MUTED, ha="center")

    ax.add_patch(FancyBboxPatch((1.4, 2.85), 5.6, 0.7, boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor="white", edgecolor=LINE, linewidth=1.2))
    ax.text(1.6, 3.18, "https://www.klassekampen.no", fontsize=11, color=INK, va="center")
    ax.add_patch(FancyBboxPatch((7.15, 2.85), 1.45, 0.7, boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor=NAVY, edgecolor=NAVY, linewidth=0))
    ax.text(7.87, 3.18, "Check", fontsize=11, color="white", ha="center", va="center", fontweight="bold")

    ax.text(5, 2.2, "Settings used for all 18 scans", fontsize=10, color=NAVY, ha="center", fontweight="bold")
    for i, line in enumerate([
        "Live Chromium visit  ·  no browser add-ons",
        "Do Not Track off",
        "Scan clock on the result page recorded as part of the measurement",
    ]):
        ax.text(5, 1.75 - i * 0.38, line, fontsize=9, color=INK, ha="center")

    path = OUT / "fig1_webbkoll_check_klassekampen.png"
    fig.savefig(path, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("wrote", path)


def fig_webbkoll_results():
    fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=240)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.add_patch(FancyBboxPatch((0.25, 0.3), 9.5, 6.4, boxstyle="round,pad=0.04,rounding_size=0.1",
                                facecolor="#F4F6F8", edgecolor=NAVY, linewidth=1.3))
    ax.add_patch(FancyBboxPatch((0.25, 6.05), 9.5, 0.65, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=NAVY, edgecolor=NAVY, linewidth=0))
    ax.text(0.5, 6.35, "Webbkoll summary  ·  klassekampen.no", fontsize=13, color=CREAM,
            va="center", fontweight="bold")
    ax.text(9.45, 6.35, "20 Aug 2026, 12:36:46 UTC", fontsize=8, color=CREAM, ha="right", va="center")

    cards = [
        (0.5, 4.55, "First-party cookies", "4"),
        (3.4, 4.55, "Third-party cookies", "0"),
        (6.3, 4.55, "Third-party requests", "56"),
        (0.5, 2.7, "Unique hosts", "13"),
        (3.4, 2.7, "Server country (KeyCDN)", "US"),
        (6.3, 2.7, "Third-party countries", "IE, SE, US"),
    ]
    for x, y, label, value in cards:
        ax.add_patch(FancyBboxPatch((x, y), 2.7, 1.35, boxstyle="round,pad=0.03,rounding_size=0.08",
                                    facecolor="white", edgecolor=LINE, linewidth=1))
        ax.text(x + 1.35, y + 0.95, label, fontsize=8, color=MUTED, ha="center")
        ax.text(x + 1.35, y + 0.4, value, fontsize=16, color=NAVY, ha="center", fontweight="bold")

    ax.text(5, 2.15, "Hosts observed on this scan included Google advertising, Meta and Cookiebot.",
            fontsize=9, color=INK, ha="center")
    ax.text(5, 1.55, "Third-party hosts on this load included advertising and analytics names listed by Webbkoll.",
            fontsize=9, color=INK, ha="center")
    ax.text(5, 0.85, "Values follow the recorded Webbkoll result used as the method example.",
            fontsize=8, color=MUTED, ha="center", style="italic")

    path = OUT / "fig2_webbkoll_results_klassekampen.png"
    fig.savefig(path, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("wrote", path)


def fig_keycdn():
    fig, ax = plt.subplots(figsize=(9.0, 4.8), dpi=240)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    ax.axis("off")

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 9.4, 4.8, boxstyle="round,pad=0.04,rounding_size=0.1",
                                facecolor="#F4F6F8", edgecolor=NAVY, linewidth=1.3))
    ax.add_patch(FancyBboxPatch((0.3, 4.4), 9.4, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=NAVY, edgecolor=NAVY, linewidth=0))
    ax.text(0.55, 4.72, "KeyCDN IP Location Finder", fontsize=13, color=CREAM, va="center", fontweight="bold")

    rows = [
        ("Look up", "klassekampen.no server IP"),
        ("Country", "United States (US)"),
        ("Network / org", "Google"),
        ("Rule applied", "Country field only; a company name is not recorded as a country"),
        ("Use in Table 2/3", "Same lookup on each unique third-party IP; Norway excluded from the count"),
    ]
    y = 3.85
    for k, v in rows:
        ax.text(0.7, y, k, fontsize=9, color=MUTED, fontweight="bold")
        ax.text(3.4, y, v, fontsize=10, color=INK)
        y -= 0.62

    path = OUT / "fig4_keycdn_lookup_klassekampen.png"
    fig.savefig(path, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("wrote", path)


if __name__ == "__main__":
    fig_requests_all18()
    fig_requests_sector()
    # Do not overwrite fig1/fig2/fig4 screenshots. Those files are live Webbkoll and KeyCDN captures.
