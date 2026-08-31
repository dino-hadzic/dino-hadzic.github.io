#!/usr/bin/env python3
"""Check every link in src/data/zadaci.json.

CSES and AtCoder task pages are fetched and must answer 200. Codeforces blocks
automated requests to problem pages (403 for any non-browser client), so its links
are verified against the official API (problemset.problems) instead: the contest id,
problem index and problem name must all match.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

CF_URL = "https://codeforces.com/api/problemset.problems"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) zadaci-verifier/1.0"}


def status(url: str) -> int:
    request = urllib.request.Request(url, headers=UA)
    code = 0
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.status
        except urllib.error.HTTPError as error:
            code = error.code
            if code not in (429, 503):
                return code
        except Exception:  # network hiccup
            code = 0
        time.sleep(3 * (attempt + 1))
    return code


def codeforces_catalogue() -> dict[tuple[str, str], str]:
    request = urllib.request.Request(CF_URL, headers=UA)
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = json.loads(response.read())
    return {
        (str(p["contestId"]), p["index"]): p["name"]
        for p in payload["result"]["problems"]
        if p.get("contestId")
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        default=os.path.join(os.path.dirname(__file__), "..", "src", "data", "zadaci.json"),
    )
    args = parser.parse_args()
    data = json.load(open(os.path.abspath(args.data)))

    problems = [(slug, p) for slug, items in data.items() for p in items]
    failures: list[str] = []

    for slug, items in data.items():
        if not 10 <= len(items) <= 25:
            failures.append(f"{slug}: {len(items)} problems (expected 10-25)")
        difficulties = [p["difficulty"] for p in items]
        if difficulties != sorted(difficulties):
            failures.append(f"{slug}: problems are not sorted by difficulty")
        urls = [p["url"] for p in items]
        if len(set(urls)) != len(urls):
            failures.append(f"{slug}: duplicate links")

    catalogue = codeforces_catalogue()
    for slug, problem in problems:
        if problem["source"] != "Codeforces":
            continue
        match = re.fullmatch(r"https://codeforces\.com/problemset/problem/(\d+)/(\w+)", problem["url"])
        if not match:
            failures.append(f"{slug}: malformed Codeforces link {problem['url']}")
            continue
        name = catalogue.get((match.group(1), match.group(2)))
        if name is None:
            failures.append(f"{slug}: {problem['url']} is not in the Codeforces problem set")
        elif name != problem["name"]:
            failures.append(f"{slug}: {problem['url']} is '{name}', not '{problem['name']}'")

    fetched = [(slug, p) for slug, p in problems if p["source"] != "Codeforces"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        codes = list(pool.map(lambda item: status(item[1]["url"]), fetched))
    for (slug, problem), code in zip(fetched, codes):
        if code != 200:
            failures.append(f"{slug}: {problem['url']} returned HTTP {code}")

    print(f"checked {len(problems)} problems in {len(data)} chapters")
    for failure in failures:
        print("FAIL", failure)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
