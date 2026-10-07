#!/usr/bin/env python3
"""Popravak kotvi nakon spajanja serija prijevoda: poveznice ``../x.md#kineska-kotva`` na stranice koje su u
međuvremenu prevedene pretvara u kotvu prevedenog naslova (po rednom broju naslova – struktura je 1:1).

    python3 tools/oiwiki/kotve.py /put/do/OI-wiki        # ispisuje i mijenja
    python3 tools/oiwiki/kotve.py /put/do/OI-wiki --check  # samo ispisuje
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from pymdownx.slugs import slugify

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
slug = slugify(case="lower")
LINK = re.compile(r"\((((?:\.{1,2}/)*[^)#\s:]*?)\.md)#([^)\s]+)\)")
INLINE = re.compile(r"`[^`]*`|\$[^$]*\$|\*\*|\*|__|_")


def headings(text: str) -> list[str]:
    out, fence = [], None
    for line in text.splitlines():
        m = re.match(r"^(\s*)(```+|~~~+)", line)
        if m:
            if fence is None:
                fence = m.group(2)[0]
            elif line.strip().startswith(fence * 3):
                fence = None
            continue
        if fence is None and (m := re.match(r"^(#{2,6})\s+(.+?)\s*#*\s*$", line)):
            out.append(m.group(2))
    return out


def anchor_of(title: str) -> str:
    plain = INLINE.sub(lambda m: m.group(0).strip("`$") if m.group(0)[0] in "`$" else "", title)
    plain = re.sub(r"\{[^}]*\}\s*$", "", plain)  # attr_list
    return slug(plain, "-")


def main():
    klon = Path(sys.argv[1])
    check = "--check" in sys.argv
    changed = problems = 0
    for lang in ("hr", "en"):
        for f in sorted((SRC / lang).rglob("*.md")):
            key = str(f.relative_to(SRC / lang))[:-3]
            text = f.read_text(encoding="utf8")

            def fix(m):
                nonlocal changed, problems
                rel, anchor = m.group(1), m.group(3)
                target = (Path(key).parent / rel).as_posix()
                target = Path(target).as_posix()
                target = re.sub(r"^(\.\./)+", "", Path("/" + target).resolve().as_posix().lstrip("/"))[:-3]
                tf = SRC / lang / (target + ".md")
                if not tf.exists():
                    return m.group(0)
                tr = [anchor_of(h) for h in headings(tf.read_text(encoding="utf8"))]
                if anchor in tr:
                    return m.group(0)
                zhf = klon / "docs" / (target + ".md")
                zh = [anchor_of(h) for h in headings(zhf.read_text(encoding="utf8"))] if zhf.exists() else []
                a = unquote(anchor)
                if a in zh and len(zh) == len(tr):
                    new = tr[zh.index(a)]
                    print(f"{lang}/{key}: {rel}#{anchor} -> #{new}")
                    changed += 1
                    return f"({rel}#{new})"
                problems += 1
                print(f"?? {lang}/{key}: {rel}#{anchor} (zh={len(zh)} naslova, prijevod={len(tr)}, nađeno={a in zh})")
                return m.group(0)

            new = LINK.sub(fix, text)
            if new != text and not check:
                f.write_text(new, encoding="utf8")
    print(f"promijenjeno {changed}, neriješeno {problems}")


if __name__ == "__main__":
    main()
