#!/usr/bin/env python3
"""Structural comparison between English source .tex and Croatian translation.

Checks that only prose changed: environment counts, math delimiters, label/ref/
cite/index/key counts, and equality of lstlisting code (comments excluded, since
they are translated too).
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ENV_BEGIN = re.compile(r"\\begin\{([^}]*)\}")
ENV_END = re.compile(r"\\end\{([^}]*)\}")
LST = re.compile(r"\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}", re.S)
COMMANDS = ["label", "ref", "cite", "index", "key", "includegraphics", "footnote"]
ENGLISH_HINTS = [" the ", " is ", " we ", " of the ", " with "]


TIKZ = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.S)
COMMENT = re.compile(r"(?m)^\s*%.*$")
EMPH = re.compile(r"\\emph\{[^{}]*\}")
CODE_COMMENT = re.compile(r"(?m)\s*//.*$")


def strip_code(text: str) -> str:
    """Drop content where English words are expected (code, figures, titles)."""
    return EMPH.sub("", COMMENT.sub("", TIKZ.sub("", LST.sub("", text))))


def listing_code(body: str) -> str:
    """Listing body without comments, which are translated in the Croatian text."""
    return CODE_COMMENT.sub("", body)


def stats(text: str) -> dict[str, object]:
    return {
        "begin": Counter(ENV_BEGIN.findall(text)),
        "end": Counter(ENV_END.findall(text)),
        "dollars": text.count("$"),
        "cmds": {c: len(re.findall(r"\\" + c + r"\{", text)) for c in COMMANDS},
        "nodes": text.count("\\node"),
        "listings": [listing_code(m.strip("\n")) for m in LST.findall(text)],
    }


def compare(src: Path, dst: Path) -> list[str]:
    a, b = stats(src.read_text()), stats(dst.read_text())
    problems: list[str] = []
    for kind in ("begin", "end"):
        ca, cb = a[kind], b[kind]
        for name in sorted(set(ca) | set(cb)):
            if ca[name] != cb[name]:
                problems.append(f"{kind}{{{name}}}: en={ca[name]} hr={cb[name]}")
    if a["dollars"] != b["dollars"]:
        problems.append(f"$ count: en={a['dollars']} hr={b['dollars']}")
    for cmd, n in a["cmds"].items():
        if n != b["cmds"][cmd]:
            problems.append(f"\\{cmd}{{: en={n} hr={b['cmds'][cmd]}")
    if a["nodes"] != b["nodes"]:
        problems.append(f"\\node: en={a['nodes']} hr={b['nodes']}")
    if len(a["listings"]) != len(b["listings"]):
        problems.append(f"lstlisting blocks: en={len(a['listings'])} hr={len(b['listings'])}")
    else:
        for i, (la, lb) in enumerate(zip(a["listings"], b["listings"]), 1):
            if la != lb:
                problems.append(f"lstlisting #{i} code differs")
    prose = strip_code(dst.read_text())
    hits = sorted({h.strip() for h in ENGLISH_HINTS if h in prose})
    if hits:
        problems.append("possible untranslated English (words: " + ", ".join(hits) + ")")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir")
    parser.add_argument("hr_dir")
    args = parser.parse_args()
    src_dir, hr_dir = Path(args.src_dir), Path(args.hr_dir)
    failed = 0
    for src in sorted(src_dir.glob("*.tex")):
        if src.name in {"book.tex", "list.tex"}:
            continue
        dst = hr_dir / src.name
        if not dst.exists():
            print(f"{src.name}: MISSING translation")
            failed += 1
            continue
        problems = compare(src, dst)
        if problems:
            failed += 1
            print(f"{src.name}: {len(problems)} problem(s)")
            for p in problems:
                print(f"    - {p}")
        else:
            print(f"{src.name}: ok")
    print(f"\n{failed} file(s) with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
