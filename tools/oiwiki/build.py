#!/usr/bin/env python3
"""Gradi oiwiki/ – hrvatski i engleski prijevod OI Wikija (https://github.com/OI-wiki/OI-wiki).

Ulaz (tools/oiwiki/src):
  hr/<put>.md, en/<put>.md      prevedeni Markdown; isti <put> kao docs/<put>.md u izvorniku,
                                 s frontmatterom  ---\\ntitle: ...\\n---
  code/<jezik>/docs/<put do koda>  kôd koji se uključuje s  --8<-- "docs/..."  (u izvorniku se
                                 smiju prevesti SAMO komentari; build to i provjerava)
  images/<odjeljak>/<slika>      slike, kopiraju se u oiwiki/<odjeljak>/images/

Izlaz: oiwiki/<put>.html – jedna stranica sadrži oba jezika, gumb prebacuje (assets/js/oiwiki.js).

    python3 tools/oiwiki/build.py            # gradi i provjerava
    python3 tools/oiwiki/build.py --check    # samo provjerava (bez pisanja)
"""
from __future__ import annotations

import html
import json
import os
import posixpath
import re
import shutil
import sys
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter
from pymdownx.slugs import slugify

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SRC = HERE / "src"
OUT = ROOT / "oiwiki"
NAV = json.loads((HERE / "nav.json").read_text(encoding="utf8"))
LANGS = ("hr", "en")

UPSTREAM_REPO = "https://github.com/OI-wiki/OI-wiki"
UPSTREAM_SITE = "https://oi-wiki.org/"

UI = {
    "hr": {
        "home": "Početna",
        "wiki": "OI Wiki (prijevod)",
        "nadnaslov": "OI Wiki · prijevod",
        "izvor": 'Prijevod stranice <a href="{blob}" rel="noopener">{file}</a> iz repozitorija '
                 '<a href="{repo}" rel="noopener">OI-wiki/OI-wiki</a> (izvornik je na kineskom, stanje od {date}). '
                 'Tekst je pod licencom <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.hr" rel="noopener">CC BY-SA 4.0</a>; '
                 'kôd je nepromijenjen osim komentara.',
        "original_page": "Izvornik na GitHubu",
        "untranslated_title": "Još nije prevedeno – otvara izvornu (kinesku) stranicu na oi-wiki.org",
        "prev": "Prethodna",
        "next": "Sljedeća",
        "sadrzaj": "Sadržaj",
        "index_intro": "Prevedeno je {n} od {total} stranica. Neprevedene poveznice vode na izvorni OI Wiki (kineski) i označene su ovako: ",
        "untranslated_badge": "izvornik",
        "lang_label": "Jezik",
    },
    "en": {
        "home": "Home",
        "wiki": "OI Wiki (translation)",
        "nadnaslov": "OI Wiki · translation",
        "izvor": 'Translation of <a href="{blob}" rel="noopener">{file}</a> from the '
                 '<a href="{repo}" rel="noopener">OI-wiki/OI-wiki</a> repository (the original is in Chinese, as of {date}). '
                 'Text is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener">CC BY-SA 4.0</a>; '
                 'code is unchanged except for comments.',
        "original_page": "Original on GitHub",
        "untranslated_title": "Not translated yet – opens the original (Chinese) page on oi-wiki.org",
        "prev": "Previous",
        "next": "Next",
        "sadrzaj": "Contents",
        "index_intro": "{n} of {total} pages have been translated. Links to untranslated pages go to the original OI Wiki (Chinese) and are marked like this: ",
        "untranslated_badge": "original",
        "lang_label": "Language",
    },
}

EXT = [
    "admonition", "attr_list", "def_list", "footnotes", "md_in_html", "tables", "toc",
    "pymdownx.arithmatex", "pymdownx.details", "pymdownx.highlight", "pymdownx.inlinehilite",
    "pymdownx.snippets", "pymdownx.superfences", "pymdownx.tabbed", "pymdownx.tasklist",
    "pymdownx.tilde", "pymdownx.mark", "pymdownx.caret",
]

problemi: list[str] = []


def greska(msg: str) -> None:
    problemi.append(msg)
    print("GREŠKA:", msg, file=sys.stderr)


def frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        text = text[m.end():]
    return meta, text


def md_instance(lang: str) -> markdown.Markdown:
    return markdown.Markdown(
        extensions=EXT,
        extension_configs={
            "toc": {"slugify": slugify(case="lower"), "permalink": False, "toc_depth": "2-3"},
            "pymdownx.arithmatex": {"generic": True},
            "pymdownx.highlight": {"css_class": "highlight", "guess_lang": False},
            "pymdownx.snippets": {"base_path": [str(SRC / "code" / lang)], "check_paths": True},
            "pymdownx.superfences": {"custom_fences": []},
            "pymdownx.tabbed": {"alternate_style": True},
            "pymdownx.tasklist": {"custom_checkbox": True},
        },
    )


def rel(from_key: str, to_path: str) -> str:
    d = posixpath.dirname(from_key)
    return posixpath.relpath(to_path, d) if d else to_path


def root_prefix(key: str) -> str:
    return "../" * (key.count("/") + 1)


def upstream_url(key: str) -> str:
    if key == "index":
        return UPSTREAM_SITE
    if key.endswith("/index"):
        return UPSTREAM_SITE + key[: -len("index")]
    return UPSTREAM_SITE + key + "/"


def strip_comments(code: str, suffix: str) -> str:
    if suffix in (".py", ".sh"):
        code = re.sub(r"(?m)#.*$", "", code)
    else:
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.S)
        code = re.sub(r"(?m)//.*$", "", code)
    return "\n".join(l.rstrip() for l in code.splitlines() if l.strip())


def provjeri_kod() -> None:
    """HR i EN inačice koda moraju biti jednake kad se maknu komentari; ako postoji klon izvornika
    (OIWIKI_UPSTREAM), uspoređuje i s njim."""
    upstream = os.environ.get("OIWIKI_UPSTREAM")
    hr_dir, en_dir = SRC / "code" / "hr", SRC / "code" / "en"
    for f in sorted(hr_dir.rglob("*")):
        if not f.is_file():
            continue
        r = f.relative_to(hr_dir)
        e = en_dir / r
        if not e.exists():
            greska(f"kôd {r} nema englesku inačicu")
            continue
        a, b = strip_comments(f.read_text(encoding="utf8"), f.suffix), strip_comments(e.read_text(encoding="utf8"), f.suffix)
        if a != b:
            greska(f"kôd {r}: hr i en inačice se razlikuju izvan komentara")
        if upstream:
            u = Path(upstream) / r
            if not u.exists():
                greska(f"kôd {r}: nema ga u izvorniku {u}")
            elif strip_comments(u.read_text(encoding="utf8"), f.suffix) != a:
                greska(f"kôd {r}: razlikuje se od izvornika izvan komentara")
    for f in sorted(en_dir.rglob("*")):
        if f.is_file() and not (hr_dir / f.relative_to(en_dir)).exists():
            greska(f"kôd {f.relative_to(en_dir)} nema hrvatsku inačicu")


class Page:
    def __init__(self, key: str):
        self.key = key
        self.title: dict[str, str] = {}
        self.body: dict[str, str] = {}
        self.ids: dict[str, set[str]] = {}
        self.toc: dict[str, str] = {}
        self.links: list[tuple[str, str, str]] = []  # (lang, target_key, anchor)
        self.headings: dict[str, int] = {}


def render(page: Page) -> None:
    for lang in LANGS:
        src = SRC / lang / (page.key + ".md")
        if not src.exists():
            greska(f"{page.key}: nema {lang} prijevoda ({src.relative_to(ROOT)})")
            continue
        meta, text = frontmatter(src.read_text(encoding="utf8"))
        if "title" not in meta:
            greska(f"{src.relative_to(ROOT)}: nedostaje 'title' u frontmatteru")
        page.title[lang] = meta.get("title", page.key)
        md = md_instance(lang)
        try:
            body = md.convert(text)
        except Exception as e:  # npr. snippet koji ne postoji
            greska(f"{src.relative_to(ROOT)}: {e}")
            body = ""
        page.headings[lang] = len(re.findall(r"<h[2-6]\b", body))
        page.ids[lang] = set(re.findall(r'\bid="([^"]+)"', body))
        page.toc[lang] = md.toc if md.toc_tokens else ""
        if lang != "hr":
            body = prefix_ids(body, lang)
            page.toc[lang] = prefix_ids(page.toc[lang], lang)
        page.body[lang] = body
    if len(page.headings) == 2 and page.headings["hr"] != page.headings["en"]:
        print(f"UPOZORENJE: {page.key}: broj naslova hr={page.headings['hr']} en={page.headings['en']}", file=sys.stderr)


def prefix_ids(body: str, lang: str) -> str:
    body = re.sub(r'\b(id|for|name)="([^"]+)"', lambda m: f'{m.group(1)}="{lang}-{m.group(2)}"', body)
    body = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{lang}-{m.group(1)}"', body)
    return body


def rewrite_links(page: Page, pages: dict[str, Page], lang: str) -> str:
    def zamjena(m):
        attrs, href = m.group(1), m.group(2)
        if href.startswith("#"):
            anchor = href[1:]
            if lang != "hr" and anchor.startswith(f"{lang}-"):
                anchor = anchor[len(lang) + 1:]
            if anchor and anchor not in page.ids.get(lang, set()):
                greska(f"{page.key} ({lang}): poveznica na nepostojeću kotvu #{anchor} na istoj stranici")
            return m.group(0)
        if re.match(r"^(https?:|mailto:|javascript:)", href):
            return m.group(0)
        path, _, anchor = href.partition("#")
        if path.endswith(".md"):
            target = posixpath.normpath(posixpath.join(posixpath.dirname(page.key), path[:-3]))
            if target in pages:
                if anchor and anchor not in pages[target].ids.get(lang, set()):
                    greska(f"{page.key} ({lang}): poveznica na nepostojeću kotvu {path}#{anchor}")
                new = rel(page.key, target + ".html")
                if anchor:
                    new += "#" + (anchor if lang == "hr" else f"{lang}-{anchor}")
                return f'<a{attrs}href="{new}"'
            new = upstream_url(target) + (f"#{anchor}" if anchor else "")
            t = html.escape(UI[lang]["untranslated_title"])
            return f'<a{attrs}href="{new}" class="oiwiki-izvornik" title="{t}" rel="noopener"'
        if path and not path.startswith("/"):
            if not (OUT / posixpath.dirname(page.key) / path).exists() and not (SRC / "images" / posixpath.normpath(posixpath.join(posixpath.dirname(page.key), path))).exists():
                greska(f"{page.key} ({lang}): poveznica na nepostojeću datoteku {href}")
        return m.group(0)

    body = re.sub(r'<a([^>]*?)href="([^"]+)"', zamjena, page.body[lang])

    def slika(m):
        attrs, src2 = m.group(1), m.group(2)
        if re.match(r"^(https?:|data:)", src2):
            return m.group(0)
        p = posixpath.normpath(posixpath.join(posixpath.dirname(page.key), src2))
        if not (SRC / "images" / p).exists():
            greska(f"{page.key} ({lang}): slika {src2} ne postoji u tools/oiwiki/src/images/{p}")
        return m.group(0)

    body = re.sub(r'<img([^>]*?)src="([^"]+)"', slika, body)
    return body


def section_of(key: str):
    for s in NAV["sections"]:
        for i, p in enumerate(s["pages"]):
            if p["path"] == key:
                return s, i
    return None, -1


def head(title: str, pref: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="hr" data-jezik="hr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <script>(function(){{try{{var j=localStorage.getItem('oiwiki-jezik');if(j==='en'||j==='hr'){{document.documentElement.setAttribute('data-jezik',j);document.documentElement.lang=j;}}}}catch(e){{}}}})();</script>
    <script src="{pref}assets/js/asset-errors.js"></script>
    <script src="{pref}assets/js/mathjax-config.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js" integrity="sha384-AHAnt9ZhGeHIrydA1Kp1L7FN+2UosbF7RQg6C+9Is/a7kDpQ1684C2iH2VWil6r4" crossorigin="anonymous"
        onerror="reportAssetError('MathJax', 'Matematički izrazi ostat će prikazani kao izvorni LaTeX kod.')"></script>
    <link rel="stylesheet" href="{pref}assets/css/zadatak.css">
    <link rel="stylesheet" href="{pref}assets/css/pozadina.css">
    <script defer src="{pref}assets/js/pozadina.js"></script>
    <link rel="stylesheet" href="{pref}assets/css/joisc.css">
    <link rel="stylesheet" href="{pref}assets/css/oiwiki-pygments.css">
    <link rel="stylesheet" href="{pref}assets/css/oiwiki.css">
    <script defer src="{pref}assets/js/oiwiki.js"></script>
</head>
<body>
"""


def bilingual(hr: str, en: str, tag: str = "span") -> str:
    return f'<{tag} class="jezik jezik-hr" lang="hr">{hr}</{tag}><{tag} class="jezik jezik-en" lang="en">{en}</{tag}>'


def toggle() -> str:
    return ('<span class="oiwiki-prebaci" role="group" aria-label="Jezik / Language">'
            '<button type="button" data-jezik="hr" lang="hr" aria-pressed="true">Hrvatski</button>'
            '<button type="button" data-jezik="en" lang="en" aria-pressed="false">English</button></span>')


def page_html(page: Page, pages: dict[str, Page]) -> str:
    pref = root_prefix(page.key)
    section, idx = section_of(page.key)
    blob = f"{UPSTREAM_REPO}/blob/{NAV['upstream_commit']}/docs/{page.key}.md"
    file = f"docs/{page.key}.md"
    izvor = {l: UI[l]["izvor"].format(blob=blob, file=file, repo=UPSTREAM_REPO, date=NAV["upstream_date"]) for l in LANGS}
    nad = {l: UI[l]["nadnaslov"] + (f" · {section[l]}" if section else "") for l in LANGS}

    prev_link = next_link = ""
    if section:
        translated = [p["path"] for p in section["pages"] if p["path"] in pages]
        j = translated.index(page.key)
        if j > 0:
            k = translated[j - 1]
            prev_link = f'<a class="prethodna" href="{rel(page.key, k + ".html")}">← ' + bilingual(html.escape(pages[k].title["hr"]), html.escape(pages[k].title["en"])) + "</a>"
        if j + 1 < len(translated):
            k = translated[j + 1]
            next_link = f'<a class="sljedeca" href="{rel(page.key, k + ".html")}">' + bilingual(html.escape(pages[k].title["hr"]), html.escape(pages[k].title["en"])) + " →</a>"

    out = [head(f"OI Wiki – {page.title['hr']}", pref)]
    out.append(f'    <p class="navigacija-analize"><a href="{pref}oiwiki/index.html">← ' + bilingual(UI["hr"]["wiki"], UI["en"]["wiki"]) +
               f'</a> · <a href="{pref}index.html">' + bilingual(UI["hr"]["home"], UI["en"]["home"]) + "</a>" + toggle() + "</p>\n")
    out.append('    <article class="analiza oiwiki">\n        <header>\n')
    out.append(f'            <p class="nadnaslov">{bilingual(html.escape(nad["hr"]), html.escape(nad["en"]))}</p>\n')
    out.append(f'            <h1>{bilingual(html.escape(page.title["hr"]), html.escape(page.title["en"]))}</h1>\n')
    out.append(f'            <p class="meta oiwiki-izvor">{bilingual(izvor["hr"], izvor["en"])}</p>\n')
    out.append(f'            <p class="oiwiki-github"><a href="{blob}" rel="noopener">{bilingual(UI["hr"]["original_page"], UI["en"]["original_page"])}</a></p>\n')
    out.append("        </header>\n")
    for lang in LANGS:
        body = rewrite_links(page, pages, lang)
        toc = ""
        if page.toc.get(lang) and page.headings.get(lang, 0) >= 3:
            toc = f'<details class="oiwiki-sadrzaj"><summary>{UI[lang]["sadrzaj"]}</summary>{page.toc[lang]}</details>\n'
        out.append(f'        <div class="jezik jezik-{lang} oiwiki-tekst" lang="{lang}">\n{toc}{body}\n        </div>\n')
    if prev_link or next_link:
        out.append(f'        <nav class="oiwiki-susjedi">{prev_link}<span></span>{next_link}</nav>\n')
    out.append("    </article>\n</body>\n</html>\n")
    return "".join(out)


def index_html(pages: dict[str, Page]) -> str:
    page = pages["index"]
    total = sum(len(s["pages"]) for s in NAV["sections"])
    out = [page_html(page, pages)]
    # umetni popis odjeljaka prije zatvaranja članka
    lists = []
    for lang in LANGS:
        items = []
        for s in NAV["sections"]:
            lis = []
            for p in s["pages"]:
                if p["path"] in pages:
                    lis.append(f'<li><a href="{rel("index", p["path"] + ".html")}">{html.escape(pages[p["path"]].title[lang])}</a></li>')
                else:
                    t = html.escape(UI[lang]["untranslated_title"])
                    lis.append(f'<li class="neprevedeno"><a href="{upstream_url(p["path"])}" class="oiwiki-izvornik" title="{t}" rel="noopener">{html.escape(p["zh"] or p["path"])}</a></li>')
            n = sum(1 for p in s["pages"] if p["path"] in pages)
            items.append(f'<details class="oiwiki-odjeljak"{" open" if n else ""}><summary>{html.escape(s[lang])} <small>{n}/{len(s["pages"])}</small></summary><ol>{"".join(lis)}</ol></details>')
        intro = UI[lang]["index_intro"].format(n=len(pages), total=total)
        badge = f'<span class="oiwiki-izvornik-primjer">{UI[lang]["untranslated_badge"]}</span>'
        lists.append(f'        <section class="jezik jezik-{lang} oiwiki-popis" lang="{lang}"><h2 id="{"" if lang == "hr" else lang + "-"}popis">{UI[lang]["sadrzaj"]}</h2><p>{intro}{badge}</p>{"".join(items)}</section>\n')
    s = out[0]
    marker = '        <nav class="oiwiki-susjedi">' if '<nav class="oiwiki-susjedi">' in s else "    </article>\n"
    return s.replace(marker, "".join(lists) + marker, 1)


def write(path: Path, text: str, check_only: bool) -> None:
    if check_only:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf8")


def main() -> int:
    check_only = "--check" in sys.argv
    keys = sorted(str(p.relative_to(SRC / "hr"))[:-3] for p in (SRC / "hr").rglob("*.md"))
    for p in (SRC / "en").rglob("*.md"):
        if str(p.relative_to(SRC / "en"))[:-3] not in keys:
            greska(f"{p.relative_to(ROOT)}: postoji samo engleska inačica")
    pages = {k: Page(k) for k in keys}
    for k in keys:
        if section_of(k)[0] is None and k != "index":
            greska(f"{k}: nije u nav.json (nema u izvornom mkdocs.yml)")
    provjeri_kod()
    for page in pages.values():
        render(page)
    if "index" not in pages:
        greska("nedostaje index.md (početna stranica OI Wikija)")
        return 1
    if not check_only and OUT.exists():
        shutil.rmtree(OUT)
    for page in pages.values():
        if page.key == "index":
            continue
        write(OUT / (page.key + ".html"), page_html(page, pages), check_only)
    write(OUT / "index.html", index_html(pages), check_only)
    if not check_only:
        for f in (SRC / "images").rglob("*"):
            if f.is_file():
                dest = OUT / f.relative_to(SRC / "images")
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)
        css = ROOT / "assets" / "css" / "oiwiki-pygments.css"
        css.write_text("/* generira tools/oiwiki/build.py (Pygments) */\n" + HtmlFormatter(style="friendly").get_style_defs(".highlight") + "\n", encoding="utf8")
    print(f"{len(pages)} stranica, {len(problemi)} grešaka")
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
