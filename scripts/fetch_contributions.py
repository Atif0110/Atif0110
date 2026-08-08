#!/usr/bin/env python3
"""
Scrapes the public GitHub contribution calendar for a user (no token needed)
and writes it to data/contributions.json.

GitHub renders the calendar as a server-side HTML fragment at:
    https://github.com/users/<username>/contributions
Each day is a <td> with class "ContributionCalendar-day",
a data-date attribute, and a data-level attribute (0-4 intensity).
"""

import json
import os
import re
import sys
import urllib.request

USERNAME = os.environ.get("GITHUB_USERNAME", "Atif0110")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")

CALENDAR_URL = f"https://github.com/users/{USERNAME}/contributions"

DAY_RE = re.compile(
    r'data-date="(?P<date>\d{4}-\d{2}-\d{2})"[^>]*'
    r'(?:id="[^"]*")?[^>]*'
    r'data-level="(?P<level>\d)"'
)
# GitHub's markup order for attributes has shifted before; fall back to a
# more permissive scan if the primary regex finds nothing.
FALLBACK_RE = re.compile(
    r'<td[^>]*data-date="(?P<date>\d{4}-\d{2}-\d{2})"[^>]*>.*?'
    r'data-level="(?P<level>\d)"',
    re.DOTALL,
)


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "profile-readme-bot"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_days(html: str):
    days = []
    matches = list(DAY_RE.finditer(html))
    if not matches:
        matches = list(FALLBACK_RE.finditer(html))
    for m in matches:
        days.append({"date": m.group("date"), "level": int(m.group("level"))})
    days.sort(key=lambda d: d["date"])
    return days


def compute_streaks(days):
    """Longest streak ending on the most recent day, and best streak overall."""
    best = cur = 0
    current_streak = 0
    for i, d in enumerate(days):
        if d["level"] > 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    # trailing streak (from the end backwards) counts as "current"
    for d in reversed(days):
        if d["level"] > 0:
            current_streak += 1
        else:
            break
    return current_streak, best


def main():
    try:
        html = fetch_html(CALENDAR_URL)
        days = parse_days(html)
        if not days:
            raise ValueError("no contribution cells parsed, GitHub markup may have changed")
    except Exception as e:
        print(f"fetch_contributions: failed to fetch/parse ({e}), writing empty fallback", file=sys.stderr)
        days = []

    total = sum(d["level"] > 0 for d in days)  # count of active days, refined below
    # Better: sum actual contribution counts if we can find them; level is 0-4 bucket only.
    # We keep it simple and report active days + streaks; the renderer can adapt.
    current_streak, best_streak = compute_streaks(days)

    payload = {
        "username": USERNAME,
        "days": days,
        "active_days_last_year": total,
        "current_streak": current_streak,
        "best_streak": best_streak,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"wrote {len(days)} days to {OUT_PATH}")


if __name__ == "__main__":
    main()
