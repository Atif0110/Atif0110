#!/usr/bin/env python3
"""
Renders data/shiplog.json into a terminal-window-styled SVG that looks like
`git log --oneline --all`, newest first. Pure stdlib.
"""

import json
import os
from datetime import datetime, timezone

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "shiplog.json")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "shiplog.svg")

BG = "#0d1117"
BORDER = "#30363d"
TEXT = "#8b949e"
TEXT_BRIGHT = "#c9d1d9"
GREEN = "#39d353"
REPO_COLOR = "#7ee787"

ROW_H = 26
TOP_PAD = 40
BOTTOM_PAD = 30
WIDTH = 760


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load_data():
    if not os.path.exists(DATA_PATH):
        return {"username": "", "items": []}
    with open(DATA_PATH) as f:
        return json.load(f)


def fmt_date(iso):
    try:
        d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return d.strftime("%b %-d")
    except Exception:
        return ""


def render(payload):
    items = payload.get("items", [])
    username = payload.get("username", "")
    height = TOP_PAD + max(len(items), 1) * ROW_H + BOTTOM_PAD
    now_label = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    rows = []
    for i, item in enumerate(items):
        y = TOP_PAD + i * ROW_H + 18
        marker = "&#9650;" if item["type"] == "release" else "&#8226;"
        marker_color = GREEN if item["type"] == "release" else TEXT
        date_str = fmt_date(item.get("date", ""))
        repo = esc(item.get("repo", ""))
        msg = esc(item.get("message", ""))
        weight = "font-weight:600;" if item["type"] == "release" else ""
        delay = round(i * 0.05, 3)

        rows.append(f'''
  <g class="row" style="animation-delay:{delay}s">
    <text x="20" y="{y}" class="marker" fill="{marker_color}">{marker}</text>
    <text x="40" y="{y}" class="date">{date_str}</text>
    <text x="96" y="{y}" class="repo">{repo}</text>
    <text x="260" y="{y}" class="msg" style="{weight}">{msg}</text>
  </g>''')

    if not items:
        rows.append(f'<text x="20" y="{TOP_PAD + 18}" class="date">no recent activity found</text>')

    svg = f'''<svg width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}"
     xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <style>
    .row {{ opacity: 0; animation: fadein 0.35s ease-out forwards; }}
    @keyframes fadein {{ to {{ opacity: 1; }} }}
    .dim {{ fill: {TEXT}; font-size: 11px; }}
    .date {{ fill: {TEXT}; font-size: 12px; }}
    .repo {{ fill: {REPO_COLOR}; font-size: 12px; }}
    .msg {{ fill: {TEXT_BRIGHT}; font-size: 12px; }}
    .marker {{ font-size: 11px; }}
    .prompt {{ fill: {GREEN}; }}
    @media (prefers-reduced-motion: reduce) {{
      .row {{ animation: none; opacity: 1; }}
    }}
  </style>

  <rect x="0" y="0" width="{WIDTH}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <circle cx="18" cy="16" r="5" fill="#ff5f56"/>
  <circle cx="34" cy="16" r="5" fill="#ffbd2e"/>
  <circle cx="50" cy="16" r="5" fill="#27c93f"/>
  <text x="66" y="20" class="dim"><tspan class="prompt">{esc(username)}@github</tspan> ~ $ git log --oneline --all</text>
  <text x="{WIDTH - 12}" y="20" class="dim" text-anchor="end">updated {now_label}</text>

  {''.join(rows)}

  <text x="20" y="{height - 12}" class="dim">releases and commits, newest first, refreshed daily by a workflow in this repo</text>
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
