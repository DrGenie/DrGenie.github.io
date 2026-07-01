#!/usr/bin/env python3
"""
Update assets/scholar-metrics.json with real Google Scholar metrics.

Why this design
---------------
Google Scholar has no public API and blocks GitHub-hosted runners with HTTP 403,
so scraping it directly from CI does not work reliably. This script uses SerpAPI's
Google Scholar Author API, which reads the same public profile through a service
that is not blocked. SerpAPI has a free tier that is more than enough for one
lookup per day.

Safety rules
------------
1. No fabrication: only values actually returned by SerpAPI are written.
2. Fail-safe: on any error, or if no API key is set, the existing file is left
   unchanged and the script exits 0 so the site build is never blocked.
3. Never overwrite good values with blanks.

Setup (one time)
----------------
1. Create a free key at https://serpapi.com (Dashboard -> Api Key).
2. In GitHub: Settings -> Secrets and variables -> Actions -> New repository
   secret, name it SERPAPI_KEY, paste the key.
The daily workflow does the rest.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date, timezone, datetime
from pathlib import Path

AUTHOR_ID = "v2SXM_kAAAAJ"
OUT = Path(__file__).resolve().parents[1] / "assets" / "scholar-metrics.json"
SOURCE = f"https://scholar.google.com/citations?user={AUTHOR_ID}&hl=en"


def load_existing() -> dict:
    try:
        return json.loads(OUT.read_text(encoding="utf-8"))
    except Exception:
        return {}


def fetch_from_serpapi(key: str) -> dict:
    params = urllib.parse.urlencode(
        {"engine": "google_scholar_author", "author_id": AUTHOR_ID, "api_key": key, "hl": "en"}
    )
    url = f"https://serpapi.com/search.json?{params}"
    with urllib.request.urlopen(url, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    table = data.get("cited_by", {}).get("table", [])
    out = {}
    for row in table:
        if "citations" in row:
            out["citations"] = row["citations"].get("all")
        elif "h_index" in row:
            out["h_index"] = row["h_index"].get("all")
        elif "i10_index" in row:
            out["i10_index"] = row["i10_index"].get("all")
    return out


def main() -> int:
    existing = load_existing()
    key = os.environ.get("SERPAPI_KEY", "").strip()
    if not key:
        print("[scholar] SERPAPI_KEY not set; leaving metrics unchanged.", file=sys.stderr)
        return 0
    try:
        metrics = fetch_from_serpapi(key)
    except Exception as e:
        print(f"[scholar] fetch failed, keeping existing values: {e}", file=sys.stderr)
        return 0

    if not metrics.get("citations"):
        print("[scholar] no citation count returned; keeping existing values.", file=sys.stderr)
        return 0

    result = dict(existing)
    result.update(metrics)
    result["updated"] = date.today().isoformat()
    result["source"] = SOURCE
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"[scholar] updated {datetime.now(timezone.utc).isoformat()}: {metrics}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
