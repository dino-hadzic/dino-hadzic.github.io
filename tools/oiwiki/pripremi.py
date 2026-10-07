#!/usr/bin/env python3
"""Priprema izvornika za prevođenje: za zadane stranice (npr. basic/quick-sort) kopira kôd koji
stranica uključuje u src/code/hr i src/code/en (nepromijenjen – komentare treba prevesti ručno) te
slike u src/images, i ispisuje retke s kineskim komentarima koje treba prevesti.

    python3 tools/oiwiki/pripremi.py /put/do/OI-wiki basic/quick-sort basic/merge-sort
"""
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
CJK = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def main():
    klon = Path(sys.argv[1])
    for key in sys.argv[2:]:
        md = (klon / "docs" / (key + ".md")).read_text(encoding="utf8")
        for inc in re.findall(r'--8<-- "([^":]+)', md):
            for lang in ("hr", "en"):
                dest = SRC / "code" / lang / inc
                dest.parent.mkdir(parents=True, exist_ok=True)
                if not dest.exists():
                    shutil.copy2(klon / inc, dest)
            for i, line in enumerate((klon / inc).read_text(encoding="utf8").splitlines(), 1):
                if CJK.search(line):
                    print(f"{inc}:{i}: {line.strip()}")
        for img in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", md):
            if img.startswith("http"):
                continue
            rel = Path(key).parent / img
            dest = SRC / "images" / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(klon / "docs" / rel, dest)
        inline = [l.strip() for l in md.splitlines() if CJK.search(l) and re.match(r"\s{4,}.*(//|#)", l)]
        print(f"== {key}: {len(md)} B, komentari u ugrađenom kodu: {len(inline)}")


if __name__ == "__main__":
    main()
