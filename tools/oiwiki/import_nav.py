#!/usr/bin/env python3
"""Iz mkdocs.yml izvornog OI Wikija izvlači navigaciju (redoslijed stranica i kineske naslove)
i sprema je u nav.json. Pokreće se ručno kad se želi osvježiti struktura:

    python3 tools/oiwiki/import_nav.py /put/do/klona/OI-wiki
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent

# Prijevodi naslova glavnih odjeljaka (hr, en); kineski naslov dolazi iz mkdocs.yml.
ODJELJCI = {
    "简介": ("Uvod", "Introduction"),
    "比赛相关": ("Natjecanja", "Contests"),
    "工具软件": ("Alati", "Tools"),
    "语言基础": ("Programski jezici", "Programming languages"),
    "算法基础": ("Osnove algoritama", "Algorithm basics"),
    "搜索": ("Pretraživanje", "Search"),
    "动态规划": ("Dinamičko programiranje", "Dynamic programming"),
    "字符串": ("Stringovi", "Strings"),
    "数学": ("Matematika", "Mathematics"),
    "数据结构": ("Strukture podataka", "Data structures"),
    "图论": ("Teorija grafova", "Graph theory"),
    "计算几何": ("Računska geometrija", "Computational geometry"),
    "杂项": ("Razno", "Miscellaneous"),
    "专题": ("Posebne teme", "Special topics"),
}


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("!", lambda loader, suffix, node: None)
Loader.add_multi_constructor("tag:yaml.org,2002:python", lambda loader, suffix, node: None)


def stranice(cvor, out):
    if isinstance(cvor, str):
        out.append({"path": re.sub(r"\.md$", "", cvor), "zh": ""})
    elif isinstance(cvor, list):
        for x in cvor:
            stranice(x, out)
    elif isinstance(cvor, dict):
        for naslov, v in cvor.items():
            if isinstance(v, str):
                out.append({"path": re.sub(r"\.md$", "", v), "zh": naslov})
            else:
                stranice(v, out)


def main():
    klon = Path(sys.argv[1])
    cfg = yaml.load((klon / "mkdocs.yml").read_text(encoding="utf8"), Loader=Loader)
    commit = subprocess.run(["git", "-C", str(klon), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    datum = subprocess.run(["git", "-C", str(klon), "log", "-1", "--format=%cs"], capture_output=True, text=True, check=True).stdout.strip()
    odjeljci = []
    for top in cfg["nav"]:
        (zh, sadrzaj), = top.items()
        hr, en = ODJELJCI[zh]
        lst = []
        stranice(sadrzaj, lst)
        odjeljci.append({"zh": zh, "hr": hr, "en": en, "pages": lst})
    nav = {"upstream_commit": commit, "upstream_date": datum, "sections": odjeljci}
    (HERE / "nav.json").write_text(json.dumps(nav, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    print(f"{sum(len(s['pages']) for s in odjeljci)} stranica, commit {commit[:10]} ({datum})")


if __name__ == "__main__":
    main()
