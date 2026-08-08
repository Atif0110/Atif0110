#!/usr/bin/env python3
"""
Renders data/contributions.json into a terminal-window-styled SVG heatmap.
Pure stdlib, no dependencies. Animation is a simple CSS fade-in staggered
per cell, done with inline <style> + nth-child delays so it plays once on
load and respects prefers-reduced-motion.
"""

import json
import os
from datetime import date, datetime, timedelta, timezone

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "contribheatmap.svg")

CELL = 11
GAP = 3
LEFT_PAD = 32
TOP_PAD = 40
BOTTOM_PAD = 34

LEVEL_COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

BG = "#0d1117"
BORDER = "#30363d"
TEXT = "#8b949e"
TEXT_BRIGHT = "#c9d1d9"
GREEN = "#39d353"


def load_data():
    if not os.path.exists(DATA_PATH):
        return {"days": [], "current_streak": 0, "best_streak": 0}
    with open(DATA_PATH) as f:
        return json.load(f)


def build_grid(days):
    """Bucket days into week columns, Sun-start, matching GitHub's layout."""
    if not days:
        return [], []
    parsed = [(datetime.strptime(d["date"], "%Y-%m-%d").date(), d["level"]) for d in days]
    parsed.sort(key=lambda x: x[0])
    start = parsed[0][0]
    start -= timedelta(days=(start.weekday() + 1) % 7)  # back up to Sunday

    by_date = {d: lvl for d, lvl in parsed}
    end = parsed[-1][0]

    weeks = []
    cur = start
    week = []
    while cur <= end:
        week.append((cur, by_date.get(cur, -1)))  # -1 = no data / outside range
        if cur.weekday() == 5:  # Saturday closes the week
            weeks.append(week)
            week = []
        cur += timedelta(days=1)
    if week:
        weeks.append(week)

    month_labels = []
    last_month = None
    for i, wk in enumerate(weeks):
        m = wk[0][0].strftime("%b")
        if m != last_month:
            month_labels.append((i, m))
            last_month = m

    return weeks, month_labels


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(payload):
    weeks, months = build_grid(payload.get("days", []))
    n_weeks = max(len(weeks), 1)
    n_rows = 7

    width = LEFT_PAD + n_weeks * (CELL + GAP) + 24
    height = TOP_PAD + n_rows * (CELL + GAP) + BOTTOM_PAD
    width = max(width, 560)

    active_days = payload.get("active_days_last_year", 0)
    total_contribs = payload.get("total_contributions")
    streak = payload.get("current_streak", 0)
    best = payload.get("best_streak", 0)
    username = payload.get("username", "")

    cells_svg = []
    idx = 0
    for wi, wk in enumerate(weeks):
        for di, (d, lvl) in enumerate(wk):
            x = LEFT_PAD + wi * (CELL + GAP)
            y = TOP_PAD + di * (CELL + GAP)
            color = LEVEL_COLORS[0] if lvl < 0 else LEVEL_COLORS[min(lvl, 4)]
            delay = round(idx * 0.0025, 4)
            cells_svg.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{color}" class="cell" style="animation-delay:{delay}s">'
                f'<title>{esc(d.isoformat())}</title></rect>'
            )
            idx += 1

    month_svg = []
    for wi, label in months:
        x = LEFT_PAD + wi * (CELL + GAP)
        month_svg.append(f'<text x="{x}" y="20" class="axis">{label}</text>')

    day_labels = [("Mon", 1), ("Wed", 3), ("Fri", 5)]
    day_svg = []
    for label, row in day_labels:
        y = TOP_PAD + row * (CELL + GAP) + CELL - 2
        day_svg.append(f'<text x="8" y="{y}" class="axis">{label}</text>')

    footer_bits = [f"{active_days} active days in the last year"]
    if streak:
        footer_bits.append(f"streak {streak}d")
    if best:
        footer_bits.append(f"best {best}d")
    footer = " &#183; ".join(footer_bits)

    now_label = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    legend_x = width - 150
    legend_swatches = "".join(
        f'<rect x="{legend_x + 34 + i * 13}" y="{height - 16}" width="10" height="10" rx="2" fill="{c}"/>'
        for i, c in enumerate(LEVEL_COLORS)
    )

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}"
     xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <style>
    .cell {{ opacity: 0; animation: fadein 0.4s ease-out forwards; }}
    @keyframes fadein {{ to {{ opacity: 1; }} }}
    .axis {{ fill: {TEXT}; font-size: 10px; }}
    .title {{ fill: {TEXT_BRIGHT}; font-size: 13px; }}
    .dim {{ fill: {TEXT}; font-size: 11px; }}
    .prompt {{ fill: {GREEN}; }}
    @media (prefers-reduced-motion: reduce) {{
      .cell {{ animation: none; opacity: 1; }}
    }}
  </style>

  <rect x="0" y="0" width="{width}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <circle cx="18" cy="16" r="5" fill="#ff5f56"/>
  <circle cx="34" cy="16" r="5" fill="#ffbd2e"/>
  <circle cx="50" cy="16" r="5" fill="#27c93f"/>
  <text x="66" y="20" class="dim"><tspan class="prompt">{esc(username)}@github</tspan> ~ $ ./contributions.sh</text>
  <text x="{width - 12}" y="20" class="dim" text-anchor="end">updated {now_label}</text>

  {''.join(month_svg)}
  {''.join(day_svg)}
  {''.join(cells_svg)}

  <text x="{LEFT_PAD}" y="{height - 12}" class="dim">{footer}</text>
  <text x="{legend_x}" y="{height - 12}" class="dim">Less</text>
  {legend_swatches}
  <text x="{legend_x + 34 + len(LEVEL_COLORS) * 13 + 6}" y="{height - 12}" class="dim">More</text>
</svg>'''
    return svg


def main():
    payload = load_data()
    svg = render(payload)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
