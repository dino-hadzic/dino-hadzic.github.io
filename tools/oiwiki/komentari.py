#!/usr/bin/env python3
"""Prevodi komentare u src/code/{hr,en} prema rječniku komentari.json ({"kineski": ["hrvatski", "english"]}).
Zamjena je doslovna (podniz), pa se kôd ne mijenja. Na kraju ispisuje retke u kojima je ostalo kineskih znakova.

    python3 tools/oiwiki/komentari.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CJK = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def main():
    rjecnik = json.loads((HERE / "komentari.json").read_text(encoding="utf8"))
    ostalo = 0
    for i, lang in enumerate(("hr", "en")):
        for f in sorted((HERE / "src" / "code" / lang).rglob("*")):
            if not f.is_file():
                continue
            s = f.read_text(encoding="utf8")
            for zh, prijevodi in sorted(rjecnik.items(), key=lambda kv: -len(kv[0])):
                s = s.replace(zh, prijevodi[i])
            f.write_text(s, encoding="utf8")
            for n, line in enumerate(s.splitlines(), 1):
                if CJK.search(line):
                    print(f"{lang}: {f.relative_to(HERE / 'src' / 'code' / lang)}:{n}: {line.strip()}")
                    ostalo += 1
    print(f"preostalo redaka s kineskim znakovima: {ostalo}")


if __name__ == "__main__":
    main()
