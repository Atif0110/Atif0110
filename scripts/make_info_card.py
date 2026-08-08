#!/usr/bin/env python3
"""
Generates a static terminal-window SVG info card (the `whoami` style block).
No API calls, edit the FIELDS list below when your facts change and rerun.
Pure stdlib.
"""

import os
from datetime import datetime, timezone

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "infocard.svg")

USERNAME = "Atif0110"

# (label, value, is_highlighted)
FIELDS = [
    ("user", "Mohd Atif ~ Lucknow, India", False),
    ("", "", None),  # blank spacer row
    ("role", "Data Scientist", False),
    ("focus", "forecasting systems, LLM production services, agent reliability", False),
    ("shipping", "Churn Engine, Power Market Forecaster, Urban Dashboard", False),
    ("", "", None),
    ("stack", "Python, FastAPI, SQL, XGBoost, scikit learn", False),
    ("llms", "OpenAI, Anthropic, Groq, LangChain, RAG", False),
    ("cloud", "Docker, AWS, Render, Streamlit Cloud", False),
    ("", "", None),
    ("results", "20 to 35% forecast lift, 15% margin gain, 95% accuracy", False),
    ("", "", None),
    ("status", "Building production ML systems full time", "highlight"),
    ("links", "atif0110.github.io/Portfolio", False),
]

BG = "#0d1117"
BORDER = "#30363d"
LABEL_COLOR = "#7ee787"
VALUE_COLOR = "#c9d1d9"
DIM = "#8b949e"
GREEN = "#39d353"
HIGHLIGHT = "#ffa657"

ROW_H = 22
LABEL_COL_W = 90
LEFT_PAD = 24
TOP_PAD = 44
BOTTOM_PAD = 20
WIDTH = 480


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    height = TOP_PAD + len(FIELDS) * ROW_H + BOTTOM_PAD

    rows = []
    for i, (label, value, highlight) in enumerate(FIELDS):
        y = TOP_PAD + i * ROW_H + 14
        if not label and not value:
            continue
        color = HIGHLIGHT if highlight else VALUE_COLOR
        rows.append(
            f'<text x="{LEFT_PAD}" y="{y}" font-size="12" fill="{LABEL_COLOR}">{esc(label)}</text>'
            f'<text x="{LEFT_PAD + LABEL_COL_W}" y="{y}" font-size="12" fill="{DIM}">:</text>'
            f'<text x="{LEFT_PAD + LABEL_COL_W + 14}" y="{y}" font-size="12" fill="{color}">{esc(value)}</text>'
        )

    svg = f'''<svg width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}"
     xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect x="0" y="0" width="{WIDTH}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <circle cx="18" cy="16" r="5" fill="#ff5f56"/>
  <circle cx="34" cy="16" r="5" fill="#ffbd2e"/>
  <circle cx="50" cy="16" r="5" fill="#27c93f"/>
  <text x="66" y="20" font-size="11" fill="{DIM}"><tspan fill="{GREEN}">{esc(USERNAME)}@github</tspan> ~ $ whoami</text>

  {''.join(rows)}
</svg>'''

    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
