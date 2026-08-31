#!/usr/bin/env python3
"""Generate src/data/zadaci.json: a curated, difficulty-sorted problem set per chapter.

Data sources (all fetched live, so no link is invented):
  * CSES problem set index      https://cses.fi/problemset/
  * Codeforces API              https://codeforces.com/api/problemset.problems
  * AtCoder Problems datasets   https://kenkoooo.com/atcoder/resources/problems.json
                                https://kenkoooo.com/atcoder/resources/problem-models.json

Every emitted problem is checked against the fetched catalogue (name and id), so a
problem that does not exist upstream cannot end up in the output. `verify_zadaci.py`
additionally pings the generated URLs.

Difficulty used for sorting:
  * Codeforces -> official problem rating
  * AtCoder    -> estimated difficulty from AtCoder Problems (clamped to >= 400)
  * CSES       -> estimate: per-topic base + position inside the CSES topic list
                  (CSES lists tasks of a topic roughly from easiest to hardest)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from collections import defaultdict

CSES_URL = "https://cses.fi/problemset/"
CF_URL = "https://codeforces.com/api/problemset.problems"
AC_PROBLEMS_URL = "https://kenkoooo.com/atcoder/resources/problems.json"
AC_MODELS_URL = "https://kenkoooo.com/atcoder/resources/problem-models.json"
UA = {"User-Agent": "zadaci-builder/1.0 (dino-hadzic.github.io book)"}
FIELDS = ("name", "url", "source", "code", "difficulty")

# Estimated difficulty (Codeforces-rating scale) of the first task of each CSES topic
# and the step added per following task in that topic.
CSES_BASE = {
    "Introductory Problems": (800, 25),
    "Sorting and Searching": (1000, 25),
    "Dynamic Programming": (1150, 35),
    "Graph Algorithms": (1200, 30),
    "Range Queries": (1300, 35),
    "Tree Algorithms": (1400, 45),
    "Mathematics": (1300, 25),
    "String Algorithms": (1600, 40),
    "Geometry": (1600, 40),
    "Advanced Techniques": (1900, 25),
    "Sliding Window Problems": (1500, 40),
    "Bitwise Operations": (1500, 50),
    "Construction Problems": (1600, 50),
    "Advanced Graph Problems": (2000, 25),
    "Counting Problems": (1800, 30),
    "Interactive Problems": (1600, 50),
    "Additional Problems I": (1900, 20),
    "Additional Problems II": (2100, 20),
}

# AtCoder Problems has no difficulty estimate for the educational contests, so the
# difficulty of those tasks (used only for ordering) is estimated here.
AC_FALLBACK = {
    "dp_a": 800, "dp_b": 900, "dp_c": 1000, "dp_d": 1200, "dp_e": 1400,
    "dp_f": 1400, "dp_g": 1300, "dp_h": 1200, "dp_i": 1500, "dp_j": 2000,
    "dp_k": 1400, "dp_l": 1700, "dp_m": 1700, "dp_o": 2100, "dp_p": 1300,
    "dp_u": 2100, "dp_v": 2400, "dp_y": 2100,
    "practice2_a": 1200, "practice2_b": 1300, "practice2_d": 1900,
    "practice2_e": 2300, "practice2_g": 1700, "practice2_h": 2100,
    "practice2_i": 2200, "practice2_l": 2300,
}

# Per chapter: CSES task ids, Codeforces tag/rating windows, AtCoder task ids.
CHAPTERS: dict[str, dict] = {
    "chapter01": {
        "cses": [1068, 1083, 1069, 1094, 1071, 1072, 1092, 1617, 1618, 1754, 1755, 2431],
        "cf": [{"tags": ["implementation", "math"], "range": (800, 1300), "count": 6}],
        "atcoder": [],
    },
    "chapter02": {
        "cses": [1643, 1644, 1085, 1074, 1141, 1660],
        "cf": [
            {"tags": ["dp", "brute force"], "range": (800, 1300), "count": 5},
            {"tags": ["dp", "greedy"], "range": (1400, 1900), "count": 4},
        ],
        "atcoder": [],
    },
    "chapter03": {
        "cses": [1621, 1084, 1090, 1091, 1619, 1629, 1640, 1620, 1632, 1163],
        "cf": [
            {"tags": ["sortings"], "range": (800, 1300), "count": 4},
            {"tags": ["binary search"], "range": (1400, 2100), "count": 6},
        ],
        "atcoder": ["abc146_c", "abc192_d"],
    },
    "chapter04": {
        "cses": [2183, 2216, 1073, 1164, 1749, 1734, 1144],
        "cf": [
            {"tags": ["data structures"], "range": (800, 1400), "count": 4},
            {"tags": ["data structures"], "range": (1500, 2200), "count": 6},
        ],
        "atcoder": ["practice2_b", "abc170_e"],
    },
    "chapter05": {
        "cses": [1622, 1623, 1624, 3419, 1628, 2136],
        "cf": [
            {"tags": ["brute force"], "range": (800, 1400), "count": 5},
            {"tags": ["bitmasks", "brute force"], "range": (1500, 2000), "count": 4, "all": True},
            {"tags": ["meet-in-the-middle"], "range": (2000, 2600), "count": 3},
        ],
        "atcoder": ["abc167_c", "abc182_c"],
    },
    "chapter06": {
        "cses": [1090, 1091, 1629, 1074, 1631, 1630, 1084, 1112],
        "cf": [
            {"tags": ["greedy"], "range": (800, 1300), "count": 5},
            {"tags": ["greedy"], "range": (1400, 2000), "count": 5},
        ],
        "atcoder": ["abc121_c", "abc137_d"],
    },
    "chapter07": {
        "cses": [1633, 1634, 1636, 1637, 1638, 1158, 1639, 3403, 1745, 1097, 1093],
        "cf": [
            {"tags": ["dp"], "range": (900, 1400), "count": 3},
            {"tags": ["dp"], "range": (1500, 2100), "count": 4},
        ],
        "atcoder": ["dp_a", "dp_c", "dp_d", "dp_e", "dp_f", "dp_h", "dp_i"],
    },
    "chapter08": {
        "cses": [1660, 1662, 1661, 1645, 3220, 3221, 3222, 1076, 1077],
        "cf": [
            {"tags": ["two pointers"], "range": (900, 1400), "count": 4},
            {"tags": ["two pointers", "data structures"], "range": (1500, 2100), "count": 5, "all": True},
        ],
        "atcoder": ["abc130_d", "arc098_b"],
    },
    "chapter09": {
        "cses": [1646, 1647, 1648, 1649, 1650, 1651, 1652, 1143, 1144, 2166, 2206, 1190, 1734],
        "cf": [
            {"tags": ["data structures"], "range": (1300, 1800), "count": 4},
            {"tags": ["data structures"], "range": (1900, 2400), "count": 4},
        ],
        "atcoder": ["practice2_b", "abc185_f", "abc231_f"],
    },
    "chapter10": {
        "cses": [1146, 1655, 3191, 3211, 1654, 1653, 2181],
        "cf": [
            {"tags": ["bitmasks"], "range": (800, 1400), "count": 4},
            {"tags": ["bitmasks"], "range": (1500, 2200), "count": 6},
        ],
        "atcoder": ["dp_o", "dp_u", "abc142_d"],
    },
    "chapter11": {
        "cses": [1192, 1193, 1666, 1667, 1668, 1669, 1194],
        "cf": [
            {"tags": ["graphs", "dfs and similar"], "range": (800, 1400), "count": 6, "all": True},
            {"tags": ["graphs"], "range": (1500, 1900), "count": 4},
        ],
        "atcoder": ["abc168_d", "abc211_d"],
    },
    "chapter12": {
        "cses": [1192, 1193, 1666, 1667, 1668, 1669, 1194, 1678, 1202, 2076],
        "cf": [
            {"tags": ["dfs and similar"], "range": (900, 1500), "count": 5},
            {"tags": ["dfs and similar", "graphs"], "range": (1600, 2200), "count": 5, "all": True},
        ],
        "atcoder": ["abc088_d", "abc151_d"],
    },
    "chapter13": {
        "cses": [1671, 1672, 1673, 1195, 1196, 1197, 1202, 3303, 1203],
        "cf": [
            {"tags": ["shortest paths"], "range": (1300, 1900), "count": 5},
            {"tags": ["shortest paths"], "range": (2000, 2500), "count": 4},
        ],
        "atcoder": ["abc143_e", "abc073_d", "abc192_e"],
    },
    "chapter14": {
        "cses": [1674, 1130, 1131, 1132, 1133, 1136, 1137, 1138, 1139, 2079],
        "cf": [
            {"tags": ["trees"], "range": (1200, 1700), "count": 5},
            {"tags": ["trees", "dp"], "range": (1800, 2300), "count": 5, "all": True},
        ],
        "atcoder": ["dp_v", "abc220_f"],
    },
    "chapter15": {
        "cses": [1675, 1676, 1682, 1683, 1677, 3111, 3407, 3408],
        "cf": [
            {"tags": ["dsu"], "range": (1200, 1700), "count": 5},
            {"tags": ["dsu", "graphs"], "range": (1800, 2300), "count": 5, "all": True},
        ],
        "atcoder": ["practice2_a", "abc214_d"],
    },
    "chapter16": {
        "cses": [1679, 1680, 1681, 1750, 1160, 1751, 1678, 1756, 1757],
        "cf": [
            {"tags": ["graphs", "dp"], "range": (1300, 1800), "count": 4, "all": True},
            {"tags": ["graphs", "dfs and similar"], "range": (1900, 2400), "count": 4, "all": True},
        ],
        "atcoder": ["dp_g", "abc223_d", "abc245_f"],
    },
    "chapter17": {
        "cses": [1682, 1683, 1686, 1684, 2177, 2179, 1703, 1705],
        # Codeforces has no tag for strong connectivity, so these are picked by hand.
        "cf_ids": ["427C", "999E", "949C", "228E", "776D"],
        "cf": [
            {"tags": ["2-sat"], "range": (1900, 2700), "count": 4},
        ],
        "atcoder": ["practice2_g", "practice2_h"],
    },
    "chapter18": {
        "cses": [1687, 1688, 1135, 1136, 1137, 1138, 2134, 1139, 2080, 2143],
        "cf": [
            {"tags": ["trees", "data structures"], "range": (1500, 2000), "count": 5, "all": True},
            {"tags": ["trees", "data structures"], "range": (2100, 2600), "count": 4, "all": True},
        ],
        "atcoder": ["abc209_d", "abc267_f"],
    },
    "chapter19": {
        "cses": [1691, 1693, 1692, 1690, 1689, 2078, 3358],
        # Codeforces has no tag for Euler/Hamilton paths, so these are picked by hand.
        "cf_ids": ["508D", "723E", "1361C", "209C", "429E", "21D"],
        "cf": [
            {"tags": ["graphs", "bitmasks"], "range": (2200, 2700), "count": 2, "all": True},
        ],
        "atcoder": ["abc054_c", "abc190_e"],
    },
    "chapter20": {
        "cses": [1694, 1695, 1696, 1711, 2121, 2129, 2130],
        "cf": [
            {"tags": ["flows"], "range": (1700, 2300), "count": 5},
            {"tags": ["graph matchings", "flows"], "range": (2400, 2900), "count": 4},
        ],
        "atcoder": ["practice2_d", "practice2_e"],
    },
    "chapter21": {
        "cses": [1095, 1712, 1713, 1081, 1082, 2182, 2185, 2417, 3396, 2164, 3154],
        "cf": [
            {"tags": ["number theory"], "range": (900, 1500), "count": 4},
            {"tags": ["number theory"], "range": (1600, 2300), "count": 5},
        ],
        "atcoder": ["abc177_e", "abc206_e"],
    },
    "chapter22": {
        "cses": [1079, 1715, 1716, 1717, 2064, 2187, 2209, 2210, 1080, 2229, 1078, 1075],
        "cf": [
            {"tags": ["combinatorics"], "range": (1200, 1800), "count": 5},
            {"tags": ["combinatorics"], "range": (1900, 2500), "count": 4},
        ],
        "atcoder": ["abc132_d", "abc202_d"],
    },
    "chapter23": {
        "cses": [1722, 1096, 1723, 1724, 3154, 3357],
        "cf": [
            {"tags": ["matrices"], "range": (1400, 2000), "count": 5},
            {"tags": ["matrices", "dp"], "range": (2100, 2600), "count": 4, "all": True},
        ],
        "atcoder": ["abc199_f", "abc236_g"],
    },
    "chapter24": {
        "cses": [1725, 1726, 1727, 1728, 2419],
        "cf": [
            {"tags": ["probabilities"], "range": (1300, 1900), "count": 6},
            {"tags": ["probabilities", "dp"], "range": (2000, 2500), "count": 5, "all": True},
        ],
        "atcoder": ["dp_j", "abc194_d", "abc280_e"],
    },
    "chapter25": {
        "cses": [1729, 1730, 1098, 1099, 2207, 2208],
        "cf": [
            {"tags": ["games"], "range": (900, 1600), "count": 6},
            {"tags": ["games"], "range": (1700, 2400), "count": 5},
        ],
        "atcoder": ["dp_k", "dp_l", "abc195_d"],
    },
    "chapter26": {
        "cses": [1731, 1753, 1732, 1733, 1110, 1111, 3138, 1112, 2102, 2103, 2105, 2106, 2107],
        "cf": [
            {"tags": ["strings"], "range": (1200, 1800), "count": 4},
            {"tags": ["hashing", "string suffix structures"], "range": (1900, 2500), "count": 4},
        ],
        "atcoder": ["abc141_e", "practice2_i", "abc257_g"],
    },
    "chapter27": {
        "cses": [2136, 2138, 2143, 2101, 2133, 2111, 2112, 2113, 1653],
        "cf": [
            {"tags": ["data structures"], "range": (1900, 2400), "count": 5},
            {"tags": ["data structures", "divide and conquer"], "range": (2500, 3000), "count": 4, "all": True},
        ],
        "atcoder": ["abc238_g", "abc242_g"],
    },
    "chapter28": {
        "cses": [1651, 1652, 1735, 1736, 1737, 1739, 3163, 3226, 3356, 2416, 1664, 1741],
        "cf": [
            {"tags": ["data structures"], "range": (1700, 2200), "count": 4},
            {"tags": ["data structures", "trees"], "range": (2300, 2800), "count": 4, "all": True},
        ],
        "atcoder": ["abc153_f", "practice2_l"],
    },
    "chapter29": {
        "cses": [2189, 2191, 2192, 2193, 2190, 2194, 2195, 3410, 1742],
        "cf": [
            {"tags": ["geometry"], "range": (1000, 1700), "count": 5},
            {"tags": ["geometry"], "range": (1800, 2400), "count": 5},
        ],
        "atcoder": ["abc207_d", "abc250_f"],
    },
    "chapter30": {
        "cses": [2190, 2194, 2195, 1740, 1741, 3427, 3429],
        "cf": [
            {"tags": ["geometry", "sortings"], "range": (1400, 2000), "count": 5, "all": True},
            {"tags": ["geometry", "data structures"], "range": (2100, 2700), "count": 5, "all": True},
        ],
        "atcoder": ["abc228_d", "abc266_f"],
    },
}


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def load_cses() -> dict[int, dict]:
    html = fetch(CSES_URL).decode("utf-8", "replace")
    tasks: dict[int, dict] = {}
    topic = None
    index = 0
    for match in re.finditer(r'<h2>(.*?)</h2>|task/(\d+)">(.*?)</a>', html):
        if match.group(1):
            topic = re.sub(r"<[^>]+>", "", match.group(1)).strip()
            index = 0
            continue
        base, step = CSES_BASE.get(topic, (1500, 30))
        task_id = int(match.group(2))
        tasks.setdefault(
            task_id,
            {
                "name": re.sub(r"<[^>]+>", "", match.group(3)).strip(),
                "url": f"https://cses.fi/problemset/task/{task_id}",
                "source": "CSES",
                "code": f"CSES {task_id}",
                "difficulty": base + step * index,
                "topic": topic,
            },
        )
        index += 1
    return tasks


def load_codeforces() -> list[dict]:
    payload = json.loads(fetch(CF_URL))
    if payload.get("status") != "OK":
        raise RuntimeError("Codeforces API returned an error")
    result = payload["result"]
    solved = {
        (stat["contestId"], stat["index"]): stat["solvedCount"]
        for stat in result["problemStatistics"]
        if "contestId" in stat
    }
    problems = []
    for problem in result["problems"]:
        if problem.get("type") != "PROGRAMMING" or "rating" not in problem:
            continue
        contest_id, index = problem.get("contestId"), problem["index"]
        if contest_id is None:
            continue
        problems.append(
            {
                "name": problem["name"],
                "url": f"https://codeforces.com/problemset/problem/{contest_id}/{index}",
                "source": "Codeforces",
                "code": f"Codeforces {contest_id}{index}",
                "difficulty": problem["rating"],
                "tags": problem["tags"],
                "solved": solved.get((contest_id, index), 0),
            }
        )
    return problems


def load_atcoder() -> dict[str, dict]:
    problems = json.loads(fetch(AC_PROBLEMS_URL))
    models = json.loads(fetch(AC_MODELS_URL))
    catalogue = {}
    for problem in problems:
        difficulty = models.get(problem["id"], {}).get("difficulty")
        if difficulty is not None:
            difficulty = min(3500, max(400, int(difficulty)))
        else:
            difficulty = AC_FALLBACK.get(problem["id"])
        # AtCoder Problems sometimes reports a mirror contest; the original contest is
        # always the task id without its trailing letter, and that URL is the canonical one.
        if "_" not in problem["id"]:
            continue
        contest = problem["id"].rsplit("_", 1)[0]
        label = {"dp": "AtCoder DP", "practice2": "AtCoder Library Practice"}.get(
            contest, f"AtCoder {contest.upper()}"
        )
        letter = problem["id"].rsplit("_", 1)[1].upper()
        catalogue[problem["id"]] = {
            "name": re.sub(r"^[A-Z0-9]{1,3}\.\s*", "", problem["title"]).strip(),
            "url": f"https://atcoder.jp/contests/{contest}/tasks/{problem['id']}",
            "source": "AtCoder",
            "code": f"{label} {letter}",
            "difficulty": difficulty,
        }
    return catalogue


def pick_codeforces(problems: list[dict], spec: dict, used: set[str]) -> list[dict]:
    """One problem per rating step inside the window: the most-solved one with matching tags.

    A tag matches when the problem carries any of the given tags, or all of them when the
    spec sets "all" (used where a single Codeforces tag is too broad for the chapter topic).
    """
    low, high = spec["range"]
    tags = set(spec["tags"])
    buckets: dict[int, list[dict]] = defaultdict(list)
    for problem in problems:
        if problem["url"] in used or not (low <= problem["difficulty"] <= high):
            continue
        problem_tags = set(problem["tags"])
        matches = tags <= problem_tags if spec.get("all") else bool(tags & problem_tags)
        if not matches:
            continue
        buckets[problem["difficulty"]].append(problem)
    chosen = []
    for rating in sorted(buckets):
        best = max(buckets[rating], key=lambda p: (p["solved"], p["url"]))
        chosen.append(best)
    # spread the picks evenly over the rating window
    if len(chosen) > spec["count"]:
        step = len(chosen) / spec["count"]
        chosen = [chosen[int(i * step)] for i in range(spec["count"])]
    for problem in chosen:
        used.add(problem["url"])
    return chosen


def build() -> dict[str, list[dict]]:
    cses = load_cses()
    codeforces = load_codeforces()
    atcoder = load_atcoder()

    by_key = {}
    for problem in codeforces:
        match = re.fullmatch(r"https://codeforces\.com/problemset/problem/(\d+)/(\w+)", problem["url"])
        if match:
            by_key[(int(match.group(1)), match.group(2))] = problem

    output: dict[str, list[dict]] = {}
    for slug, spec in CHAPTERS.items():
        picked: list[dict] = []
        used: set[str] = set()

        for task_id in spec["cses"]:
            task = cses.get(task_id)
            if task is None:
                raise SystemExit(f"{slug}: CSES task {task_id} is not in the CSES problem set")
            if task["url"] in used:
                continue
            used.add(task["url"])
            picked.append({k: task[k] for k in FIELDS})

        for task_id in spec["atcoder"]:
            task = atcoder.get(task_id)
            if task is None:
                raise SystemExit(f"{slug}: AtCoder task {task_id} does not exist")
            if task["difficulty"] is None:
                raise SystemExit(f"{slug}: AtCoder task {task_id} has no difficulty estimate")
            if task["url"] in used:
                continue
            used.add(task["url"])
            picked.append({k: task[k] for k in FIELDS})

        for code in spec.get("cf_ids", []):
            match = re.fullmatch(r"(\d+)([A-Z]\d?)", code)
            if match is None:
                raise SystemExit(f"{slug}: malformed Codeforces id {code}")
            key = (int(match.group(1)), match.group(2))
            problem = by_key.get(key)
            if problem is None:
                raise SystemExit(f"{slug}: Codeforces problem {code} does not exist or has no rating")
            if problem["url"] in used:
                continue
            used.add(problem["url"])
            picked.append({k: problem[k] for k in FIELDS})

        for cf_spec in spec["cf"]:
            for problem in pick_codeforces(codeforces, cf_spec, used):
                picked.append({k: problem[k] for k in FIELDS})

        picked.sort(key=lambda p: (p["difficulty"], p["name"]))
        if not 10 <= len(picked) <= 25:
            raise SystemExit(f"{slug}: {len(picked)} problems, expected between 10 and 25")
        output[slug] = picked
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        default=os.path.join(os.path.dirname(__file__), "..", "src", "data", "zadaci.json"),
    )
    args = parser.parse_args()
    data = build()
    with open(os.path.abspath(args.out), "w") as handle:
        json.dump(data, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    total = sum(len(v) for v in data.values())
    print(f"zadaci: {len(data)} chapters, {total} problems")


if __name__ == "__main__":
    main()
