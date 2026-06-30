"""Update verified public Google Scholar metrics without failing the workflow.

The script writes metrics only when the expected Mesfin Genie profile and all
three headline values are present. If Google Scholar blocks the request or the
page structure changes, the existing JSON file is left untouched and the
script exits successfully.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import html
import json
import re
import sys
import urllib.error
import urllib.request

PROFILE_URL = "https://scholar.google.com/citations?user=v2SXM_kAAAAJ&hl=en"
OUTPUT_PATH = (
    Path(__file__).resolve().parents[1] / "assets" / "scholar-metrics.json"
)


def _clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def _extract_metrics(page: str) -> tuple[int, int, int]:
    lowered = page.lower()
    if "unusual traffic" in lowered or "not a robot" in lowered:
        raise RuntimeError("Google Scholar blocked the automated request")

    name_match = re.search(
        r'id=["\']gsc_prf_in["\'][^>]*>(.*?)</',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    profile_name = _clean_text(name_match.group(1)) if name_match else ""
    if "mesfin" not in profile_name.lower() or "genie" not in profile_name.lower():
        raise RuntimeError("The expected Google Scholar profile was not verified")

    cells = re.findall(
        r'<td[^>]*class=["\']gsc_rsb_std["\'][^>]*>(.*?)</td>',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    numbers: list[int] = []
    for cell in cells:
        text = _clean_text(cell)
        if re.fullmatch(r"[0-9][0-9,]*", text):
            numbers.append(int(text.replace(",", "")))

    # Scholar normally provides two columns for each metric:
    # all-time and since-year. We use the all-time values at positions 0, 2, 4.
    if len(numbers) < 5:
        raise RuntimeError("The Google Scholar metrics table was incomplete")

    citations, h_index, i10_index = numbers[0], numbers[2], numbers[4]
    if citations < 0 or h_index < 0 or i10_index < 0:
        raise RuntimeError("Invalid metric values were returned")

    return citations, h_index, i10_index


def main() -> int:
    request = urllib.request.Request(
        PROFILE_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/149.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            page = response.read().decode("utf-8", errors="replace")
        citations, h_index, i10_index = _extract_metrics(page)
    except (urllib.error.URLError, TimeoutError, RuntimeError, ValueError) as exc:
        print(f"Google Scholar metrics were not updated: {exc}")
        print("The existing verified metrics file was left unchanged.")
        return 0

    data = {
        "status": "verified",
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "source": PROFILE_URL,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    new_content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    old_content = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""

    if new_content == old_content:
        print("Verified Google Scholar metrics are unchanged.")
        return 0

    OUTPUT_PATH.write_text(new_content, encoding="utf-8")
    print("Verified Google Scholar metrics were updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
