#!/usr/bin/env python3
"""Convert the (Croatian) LaTeX sources of the book into HTML fragments + JSON metadata.

tikzpicture figures are rendered to SVG with latex + dvisvgm (one latex run per file),
math is kept as raw TeX and rendered with KaTeX at Astro build time.

Usage: python3 tex2html.py <src-tex-dir> [--out-data DIR] [--out-fig DIR] [--no-figures]
"""

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

TOK_OPEN = "\x00"
TOK_CLOSE = "\x01"

PARTS = {
    1: "Osnovne tehnike",
    11: "Algoritmi na grafovima",
    21: "Napredne teme",
}

FIG_PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[table]{xcolor}
\usepackage{tikz}
\usepackage{array}
\usepackage{multicol}
\usepackage{pifont}
\usepackage{ifthen}
\usepackage{skak}
\usepackage[scaled=0.95]{inconsolata}
\usetikzlibrary{patterns,snakes}
\newcommand{\key}[1]{\textbf{#1}}
\usepackage[active,tightpage]{preview}
\PreviewEnvironment{tikzpicture}
\begin{document}
"""


class Store:
    """Holds already-converted HTML fragments behind opaque tokens."""

    def __init__(self):
        self.items = []

    def add(self, html_fragment):
        self.items.append(html_fragment)
        return f"{TOK_OPEN}{len(self.items) - 1}{TOK_CLOSE}"

    def expand(self, text, depth=0):
        if depth > 40:
            return text
        def sub(m):
            return self.expand(self.items[int(m.group(1))], depth + 1)
        return re.sub(TOK_OPEN + r"(\d+)" + TOK_CLOSE, sub, text)


def strip_comments(text):
    out = []
    for line in text.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        if m:
            line = line[: m.start()]
            if not line.strip():
                continue
        out.append(line)
    return "\n".join(out)


def find_env(text, name, start=0):
    """Return (start, body_start, body_end, end) of the next \\begin{name}...\\end{name}."""
    b = re.compile(r"\\begin\{" + name + r"\}")
    e = re.compile(r"\\end\{" + name + r"\}")
    m = b.search(text, start)
    if not m:
        return None
    depth = 1
    pos = m.end()
    while depth:
        nb = b.search(text, pos)
        ne = e.search(text, pos)
        if not ne:
            return None
        if nb and nb.start() < ne.start():
            depth += 1
            pos = nb.end()
        else:
            depth -= 1
            pos = ne.end()
            last = ne
    return m.start(), m.end(), last.start(), last.end()


def match_brace(text, i):
    """text[i] == '{' -> index just after the matching '}'."""
    assert text[i] == "{"
    depth = 0
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced braces")


def take_arg(text, i):
    """Read one {...} argument starting at i (skipping whitespace). Returns (content, next_i)."""
    while i < len(text) and text[i] in " \n\t":
        i += 1
    if i >= len(text) or text[i] != "{":
        return None, i
    end = match_brace(text, i)
    return text[i + 1 : end - 1], end


class Converter:
    def __init__(self, src_dir, fig_dir, slug):
        self.src_dir = src_dir
        self.fig_dir = fig_dir
        self.slug = slug
        self.store = Store()
        self.figures = []        # tex source of each tikzpicture
        self.defs = []           # \def lines in order, for the figure document
        self.footnotes = []
        self.sections = []
        self.title = None
        self.math_errors = 0

    # ---------- protection passes ----------

    def protect_listings(self, text):
        out = []
        pos = 0
        while True:
            found = find_env(text, "lstlisting", pos)
            if not found:
                out.append(text[pos:])
                break
            s, bs, be, e = found
            out.append(text[pos:s])
            code = text[bs:be]
            code = code.strip("\n")
            out.append(self.store.add(
                '<pre class="code"><code>' + html.escape(code) + "</code></pre>"
            ))
            pos = e
        return "".join(out)

    def protect_figures(self, text):
        out = []
        pos = 0
        while True:
            found = find_env(text, "tikzpicture", pos)
            if not found:
                out.append(text[pos:])
                break
            s, bs, be, e = found
            out.append(text[pos:s])
            src = text[s:e]
            # \newcommand definitions preceding this figure belong to the figure document
            idx = len(self.figures)
            self.figures.append(src)
            name = f"{self.slug}-{idx + 1}.svg"
            out.append(self.store.add(
                f'<img class="figure" src="/fig/{name}" alt="Slika {idx + 1}" loading="lazy" />'
            ))
            pos = e
        return "".join(out)

    def collect_defs(self, text):
        """Turn \\newcommand definitions (used only by figures) into \\def and drop them."""
        out = []
        pos = 0
        pat = re.compile(r"\\newcommand\s*\{?\\([A-Za-z]+)\}?\s*(\[(\d+)\])?\s*")
        while True:
            m = pat.search(text, pos)
            if not m:
                out.append(text[pos:])
                break
            out.append(text[pos : m.start()])
            body, nxt = take_arg(text, m.end())
            if body is None:
                out.append(text[m.start() : m.end()])
                pos = m.end()
                continue
            nargs = int(m.group(3) or 0)
            params = "".join(f"#{i + 1}" for i in range(nargs))
            self.defs.append((m.start(), f"\\def\\{m.group(1)}{params}{{{body}}}"))
            pos = nxt
        return "".join(out)

    def protect_math(self, text):
        # display: \[ ... \], equation*, $$ ... $$
        def disp(inner):
            return self.store.add(
                '<span class="math-display" data-tex="'
                + html.escape(inner.strip(), quote=True)
                + '"></span>'
            )

        while True:
            found = find_env(text, r"equation\*", 0)
            if not found:
                break
            s, bs, be, e = found
            text = text[:s] + disp(text[bs:be]) + text[e:]

        text = re.sub(r"\\\[(.+?)\\\]", lambda m: disp(m.group(1)), text, flags=re.S)
        text = re.sub(r"\$\$(.+?)\$\$", lambda m: disp(m.group(1)), text, flags=re.S)

        # inline math
        out = []
        i = 0
        while i < len(text):
            c = text[i]
            if c == "\\" and i + 1 < len(text):
                out.append(text[i : i + 2])
                i += 2
                continue
            if c == "$":
                j = i + 1
                while j < len(text):
                    if text[j] == "\\":
                        j += 2
                        continue
                    if text[j] == "$":
                        break
                    j += 1
                inner = text[i + 1 : j]
                out.append(self.store.add(
                    '<span class="math-inline" data-tex="'
                    + html.escape(inner, quote=True)
                    + '"></span>'
                ))
                i = j + 1
                continue
            out.append(c)
            i += 1
        return "".join(out)

    # ---------- structure ----------

    def convert_tabular(self, text):
        while True:
            found = find_env(text, "tabular", 0)
            if not found:
                break
            s, bs, be, e = found
            body = text[bs:be]
            # column spec right after \begin{tabular}
            spec_end = bs
            if body.lstrip().startswith("{") or body.lstrip().startswith("["):
                stripped = len(body) - len(body.lstrip())
                k = bs + stripped
                if text[k] == "[":
                    k = text.index("]", k) + 1
                    while text[k] in " \n":
                        k += 1
                spec_end = match_brace(text, k)
                body = text[spec_end:be]
            rows_html = []
            body = body.replace("\\hline", "")
            for raw_row in re.split(r"\\\\", body):
                if not raw_row.strip():
                    continue
                cells = re.split(r"(?<!\\)&", raw_row)
                tds = "".join(
                    "<td>" + self.inline(c.strip()) + "</td>" for c in cells
                )
                rows_html.append("<tr>" + tds + "</tr>")
            table = (
                '<div class="table-wrap"><table><tbody>'
                + "".join(rows_html)
                + "</tbody></table></div>"
            )
            text = text[:s] + self.store.add(table) + text[e:]
        return text

    def convert_lists(self, text):
        for env, tag in (("itemize", "ul"), ("enumerate", "ol"), ("description", "ul")):
            while True:
                found = find_env(text, env, 0)
                if not found:
                    break
                s, bs, be, e = found
                body = text[bs:be]
                items = re.split(r"\\item\b", body)[1:]
                lis = []
                for it in items:
                    it = it.strip()
                    if it.startswith("["):
                        k = it.index("]")
                        lead = self.inline(it[1:k])
                        it = it[k + 1 :]
                        lis.append(f"<li><strong>{lead}</strong> " + self.paragraphs(it, bare=True) + "</li>")
                    else:
                        lis.append("<li>" + self.paragraphs(it, bare=True) + "</li>")
                text = text[:s] + self.store.add(
                    f"<{tag}>" + "".join(lis) + f"</{tag}>"
                ) + text[e:]
        return text

    def convert_wrappers(self, text):
        for env, cls in (
            ("center", "center"),
            ("framed", "framed"),
            ("samepage", None),
            ("multicols", "cols"),
            ("flushright", "flushright"),
            ("split", None),
        ):
            while True:
                found = find_env(text, env, 0)
                if not found:
                    break
                s, bs, be, e = found
                body = text[bs:be]
                if env == "multicols":
                    body, _ = re.subn(r"^\s*\{\d+\}", "", body)
                inner = self.paragraphs(body, bare=(cls is None))
                wrapped = inner if cls is None else f'<div class="{cls}">{inner}</div>'
                text = text[:s] + self.store.add(wrapped) + text[e:]
        return text

    def convert_headings(self, text):
        def slugify(t):
            plain = re.sub(TOK_OPEN + r"\d+" + TOK_CLOSE, "", t)
            plain = re.sub(r"[^\w\s-]", "", plain, flags=re.U).strip().lower()
            plain = re.sub(r"\s+", "-", plain)
            tr = str.maketrans("čćžšđ", "cczsd")
            return plain.translate(tr) or "odjeljak"

        out = []
        pos = 0
        pat = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\s*")
        used = set()
        while True:
            m = pat.search(text, pos)
            if not m:
                out.append(text[pos:])
                break
            out.append(text[pos : m.start()])
            arg, nxt = take_arg(text, m.end())
            if arg is None:
                out.append(m.group(0))
                pos = m.end()
                continue
            kind = m.group(1)
            inner = self.inline(arg)
            if kind == "chapter":
                self.title = inner
                out.append(self.store.add(f"<h1>{inner}</h1>"))
            else:
                level = {"section": 2, "subsection": 3, "subsubsection": 4}[kind]
                sid = slugify(arg)
                n = 2
                base = sid
                while sid in used:
                    sid = f"{base}-{n}"
                    n += 1
                used.add(sid)
                self.sections.append({"id": sid, "title": inner, "level": level})
                out.append(self.store.add(
                    f'<h{level} id="{sid}">{inner}</h{level}>'
                ))
            pos = nxt
        return "".join(out)

    # ---------- inline ----------

    SIMPLE = {
        "key": ("<strong>", "</strong>"),
        "textbf": ("<strong>", "</strong>"),
        "emph": ("<em>", "</em>"),
        "textit": ("<em>", "</em>"),
        "texttt": ("<code>", "</code>"),
        "underline": ("<u>", "</u>"),
        "textrm": ("", ""),
        "text": ("", ""),
        "mbox": ("", ""),
        "small": ("", ""),
        "footnotesize": ("", ""),
    }

    DROP_ARG = ("index", "label", "markboth", "addcontentsline", "phantomsection",
                "hspace", "vspace", "hspace*", "vspace*", "setcounter", "pagenumbering")
    DROP_BARE = ("noindent", "small", "footnotesize", "normalsize", "large", "centering",
                 "cleardoublepage", "phantomsection", "newpage", "medskip", "bigskip",
                 "smallskip", "par", "sffamily", "ttfamily", "raggedright")

    def inline(self, text):
        text = self.replace_commands(text)
        text = self.escape_text(text)
        return text.strip()

    def replace_commands(self, text):
        # footnotes
        while True:
            m = re.search(r"\\footnote\s*", text)
            if not m:
                break
            arg, nxt = take_arg(text, m.end())
            if arg is None:
                text = text[: m.start()] + text[m.end() :]
                continue
            self.footnotes.append(self.inline(arg))
            n = len(self.footnotes)
            tok = self.store.add(
                f'<sup class="fn"><a href="#fn-{n}" id="fnref-{n}">{n}</a></sup>'
            )
            text = text[: m.start()] + tok + text[nxt:]

        # \cite{a,b}
        def cite(m):
            keys = [k.strip() for k in m.group(1).split(",")]
            links = ", ".join(
                f'<a href="/literatura/#ref-{k}">{k}</a>' for k in keys
            )
            return self.store.add(f"[{links}]")

        text = re.sub(r"\\cite\{([^}]*)\}", cite, text)
        text = re.sub(r"\\url\{([^}]*)\}",
                      lambda m: self.store.add(
                          f'<a href="{html.escape(m.group(1), quote=True)}">{html.escape(m.group(1))}</a>'),
                      text)

        for name in self.DROP_ARG:
            while True:
                m = re.search(r"\\" + re.escape(name) + r"\s*(?=[{\[])", text)
                if not m:
                    break
                i = m.end()
                if text[i] == "[":
                    i = text.index("]", i) + 1
                arg, nxt = take_arg(text, i)
                text = text[: m.start()] + text[(nxt if arg is not None else i) :]

        # commands with one argument -> tags
        pat = re.compile(r"\\(" + "|".join(self.SIMPLE) + r")\s*(?=\{)")
        while True:
            m = pat.search(text)
            if not m:
                break
            arg, nxt = take_arg(text, m.end())
            open_t, close_t = self.SIMPLE[m.group(1)]
            inner = self.inline(arg)
            text = text[: m.start()] + self.store.add(
                open_t + self.store.add(inner) + close_t
            ) + text[nxt:]

        for name in self.DROP_BARE:
            text = re.sub(r"\\" + name + r"\b\s*", "", text)

        return text

    ESCAPES = {
        r"\%": "%", r"\&": "&amp;", r"\_": "_", r"\#": "#", r"\$": "$",
        r"\{": "{", r"\}": "}", r"\ ": " ",
        r"\textasciitilde": "~", r"\textbackslash": "\\",
        r"\ldots": "…", r"\dots": "…", r"\dag": "†",
        r"\LaTeX": "LaTeX", r"\TeX": "TeX", r"\today": "",
    }

    def escape_text(self, text):
        text = text.replace("``", "\u201e").replace("''", "\u201c")
        text = text.replace("\\\\", "<br />")
        text = html.escape(text, quote=False)
        # html.escape mangled the escape sequences' ampersands; work on the escaped text
        for k, v in self.ESCAPES.items():
            text = text.replace(html.escape(k, quote=False), v)
        text = text.replace("&lt;br /&gt;", "<br />")
        text = text.replace("~", "\u00a0")
        text = re.sub(r"\\[a-zA-Z]+\s*", "", text)  # any leftover bare command
        return text

    def paragraphs(self, text, bare=False):
        chunks = re.split(r"\n\s*\n", text)
        out = []
        for chunk in chunks:
            body = self.inline(chunk)
            if not body or body.isspace():
                continue
            only_token = re.fullmatch(TOK_OPEN + r"\d+" + TOK_CLOSE, body.strip())
            if bare or only_token:
                out.append(body)
            else:
                out.append("<p>" + body + "</p>")
        return "\n".join(out)

    # ---------- figures ----------

    def render_figures(self):
        if not self.figures:
            return 0
        defs = "\n".join(d for _, d in self.defs)
        doc = FIG_PREAMBLE
        # definitions must precede the figures that use them, in source order
        parts = []
        for idx, fig in enumerate(self.figures):
            parts.append(fig)
        doc += defs + "\n" + "\n\n".join(parts) + "\n\\end{document}\n"
        tmp = tempfile.mkdtemp(prefix="fig-")
        tex_path = os.path.join(tmp, "f.tex")
        with open(tex_path, "w") as f:
            f.write(doc)
        r = subprocess.run(
            ["latex", "-interaction=nonstopmode", "-halt-on-error", "f.tex"],
            cwd=tmp, capture_output=True, text=True,
        )
        if not os.path.exists(os.path.join(tmp, "f.dvi")):
            sys.stderr.write(f"[{self.slug}] latex FAILED\n" + r.stdout[-3000:] + "\n")
            return -1
        os.makedirs(self.fig_dir, exist_ok=True)
        out_pat = "%f-%p.svg"
        r2 = subprocess.run(
            ["dvisvgm", "--font-format=woff", "--exact", "--optimize",
             "--bbox=preview", "--page=1-", "-o", out_pat, "f.dvi"],
            cwd=tmp, capture_output=True, text=True,
        )
        # dvisvgm zero-pads %p to the width of the highest page number
        pages = {}
        for fn in os.listdir(tmp):
            m = re.fullmatch(r"f-(\d+)\.svg", fn)
            if m:
                pages[int(m.group(1))] = os.path.join(tmp, fn)
        made = 0
        for idx in range(len(self.figures)):
            src = pages.get(idx + 1, "")
            if not src or not os.path.exists(src):
                sys.stderr.write(f"[{self.slug}] missing svg page {idx + 1}\n{r2.stderr[-1500:]}\n")
                continue
            shutil.copyfile(src, os.path.join(self.fig_dir, f"{self.slug}-{idx + 1}.svg"))
            made += 1
        shutil.rmtree(tmp, ignore_errors=True)
        return made

    # ---------- main ----------

    def convert(self, text):
        text = strip_comments(text)
        text = self.protect_listings(text)
        text = self.collect_defs(text)
        text = self.protect_figures(text)
        text = self.protect_math(text)
        text = self.convert_tabular(text)
        text = self.convert_lists(text)
        text = self.convert_headings(text)
        text = self.convert_wrappers(text)
        body = self.paragraphs(text)
        if self.footnotes:
            items = "".join(
                f'<li id="fn-{i + 1}">{f} <a href="#fnref-{i + 1}">↩</a></li>'
                for i, f in enumerate(self.footnotes)
            )
            body += f'\n<section class="footnotes"><ol>{items}</ol></section>'
        return self.store.expand(body)


def convert_bibliography(path, store_dir):
    with open(path) as f:
        text = strip_comments(f.read())
    found = find_env(text, "thebibliography", 0)
    body = text[found[1] : found[2]] if found else text
    body = re.sub(r"^\s*\{[^}]*\}", "", body)
    entries = []
    for chunk in re.split(r"\\bibitem", body)[1:]:
        arg, nxt = take_arg(chunk, 0)
        conv = Converter(os.path.dirname(path), store_dir, "lit")
        entries.append({"key": arg, "html": conv.convert(chunk[nxt:]).replace("<p>", "").replace("</p>", "")})
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out-data", default="src/data")
    ap.add_argument("--out-fig", default="public/fig")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--only", default=None, help="comma separated slugs, e.g. chapter01")
    args = ap.parse_args()

    os.makedirs(args.out_data, exist_ok=True)
    files = sorted(
        f for f in os.listdir(args.src)
        if re.fullmatch(r"(chapter\d\d|preface)\.tex", f)
    )
    if args.only:
        keep = set(args.only.split(","))
        files = [f for f in files if f[:-4] in keep]

    index = []
    part = None
    for fname in files:
        slug = fname[:-4]
        with open(os.path.join(args.src, fname)) as f:
            text = f.read()
        conv = Converter(args.src, args.out_fig, slug)
        body = conv.convert(text)
        n_fig = 0 if args.no_figures else conv.render_figures()
        m = re.fullmatch(r"chapter(\d\d)", slug)
        number = int(m.group(1)) if m else None
        if number in PARTS:
            part = PARTS[number]
        data = {
            "slug": slug,
            "number": number,
            "title": conv.title or "Predgovor",
            "part": part if number else None,
            "sections": conv.sections,
            "html": body,
        }
        with open(os.path.join(args.out_data, f"{slug}.json"), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        index.append({k: data[k] for k in ("slug", "number", "title", "part", "sections")})
        print(f"{slug}: {len(body)} bytes html, {len(conv.figures)} figures -> {n_fig} svg, "
              f"{len(conv.sections)} sections, title={data['title'][:50]!r}")

    lit_path = os.path.join(args.src, "list.tex")
    if os.path.exists(lit_path):
        entries = convert_bibliography(lit_path, args.out_fig)
        with open(os.path.join(args.out_data, "literatura.json"), "w") as f:
            json.dump(entries, f, ensure_ascii=False, indent=1)
        print(f"literatura: {len(entries)} entries")

    with open(os.path.join(args.out_data, "index.json"), "w") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
