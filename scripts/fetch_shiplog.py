#!/usr/bin/env python3
"""
Pulls the most recent releases and commits across a user's repos via the
GitHub REST API and writes a flat, time-sorted list to data/shiplog.json.

Uses GITHUB_TOKEN if present (set automatically inside GitHub Actions) to
get a much higher rate limit; works unauthenticated too, just slower/limited.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime

USERNAME = os.environ.get("GITHUB_USERNAME", "Atif0110")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "shiplog.json")
MAX_REPOS = 8
MAX_COMMITS_PER_REPO = 5
MAX_ITEMS = 10

API = "https://api.github.com"


def api_get(path):
    req = urllib.request.Request(f"{API}{path}", headers=_headers())
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _headers():
    h = {"User-Agent": "profile-readme-bot", "Accept": "application/vnd.github+json"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def get_recent_repos():
    repos = api_get(f"/users/{USERNAME}/repos?sort=pushed&per_page={MAX_REPOS}")
    return [r for r in repos if not r.get("fork")]


def get_recent_commits(repo_name):
    try:
        commits = api_get(f"/repos/{USERNAME}/{repo_name}/commits?per_page={MAX_COMMITS_PER_REPO}")
    except Exception:
        return []
    items = []
    for c in commits:
        commit = c.get("commit", {})
        msg = (commit.get("message") or "").split("\n")[0].strip()
        if not msg:
            continue
        author = commit.get("author", {})
        items.append({
            "type": "commit",
            "repo": repo_name,
            "message": msg,
            "date": author.get("date"),
            "sha": c.get("sha", "")[:7],
        })
    return items


def get_recent_releases(repo_name):
    try:
        releases = api_get(f"/repos/{USERNAME}/{repo_name}/releases?per_page=3")
    except Exception:
        return []
    items = []
    for r in releases:
        items.append({
            "type": "release",
            "repo": repo_name,
            "message": f"released {r.get('tag_name', r.get('name',''))}",
            "date": r.get("published_at") or r.get("created_at"),
        })
    return items


def main():
    try:
        repos = get_recent_repos()
    except Exception as e:
        print(f"fetch_shiplog: failed to list repos ({e})", file=sys.stderr)
        repos = []

    items = []
    for repo in repos:
        name = repo["name"]
        items.extend(get_recent_commits(name))
        items.extend(get_recent_releases(name))

    items = [i for i in items if i.get("date")]
    items.sort(key=lambda i: i["date"], reverse=True)
    items = items[:MAX_ITEMS]

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump({"username": USERNAME, "items": items}, f, indent=2)

    print(f"wrote {len(items)} items to {OUT_PATH}")


if __name__ == "__main__":
    main()
