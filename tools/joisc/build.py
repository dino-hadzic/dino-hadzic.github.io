#!/usr/bin/env python3
"""Generator statičnih stranica JOISC arhive (prijevodi/joisc/).

Ulaz:
  tools/joisc/manifest.json   popis zadataka (godina, dan, slug, izvorni PDF-ovi)
  tools/joisc/scores.json     službene statistike rezultata po zadatku
  tools/joisc/limits.json     službena vremenska i memorijska ograničenja
  tools/joisc/slides.json     broj i dimenzije renderiranih slajdova
  tools/joisc/content/<godina>/<slug>.html   hrvatski sadržaj zadatka

Izlaz:
  prijevodi/joisc/index.html
  prijevodi/joisc/<godina>/index.html
  prijevodi/joisc/<godina>/<slug>.html            (zadatak, tabovi)
  prijevodi/joisc/<godina>/<slug>-editorial.html  (članak s analizom)

Format datoteke sadržaja: blokovi započinju retkom "@@ ime" (meta, zadatak,
rjesenje, trener, analiza). Blok meta sadrži retke "kljuc = vrijednost".
U bloku analiza posebna oznaka
  <slajdovi from="5" to="9" vrsta="koraci" naslov="...">
      <s n="5">natpis slajda 5</s> ...
  </slajdovi>
pretvara se u interaktivni klizač slajdova; <slajd n="7">natpis</slajd> je
jedan slajd. Natpisi su prijevod teksta sa slajda.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(REPO, 'prijevodi', 'joisc')
CONTENT = os.path.join(HERE, 'content')

MANIFEST = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
SCORES = json.load(open(os.path.join(HERE, 'scores.json'), encoding='utf-8'))
LIMITS = json.load(open(os.path.join(HERE, 'limits.json'), encoding='utf-8'))
SLIDES = json.load(open(os.path.join(HERE, 'slides.json'), encoding='utf-8'))

YEAR_INFO = {
    2017: ('JOI 2016/2017 Spring Camp', 'https://www.ioi-jp.org/camp/2017/2017-sp-tasks/index.html'),
    2018: ('JOI 2017/2018 Spring Camp', 'https://www.ioi-jp.org/camp/2018/2018-sp-tasks/index.html'),
    2019: ('JOI 2018/2019 Spring Camp', 'https://www.ioi-jp.org/camp/2019/2019-sp-tasks/index.html'),
    2020: ('JOI 2019/2020 Spring Camp', 'https://www.ioi-jp.org/camp/2020/2020-sp-tasks/index.html'),
    2021: ('JOI 2020/2021 Spring Camp', 'https://www.ioi-jp.org/camp/2021/2021-sp-tasks/index.html'),
    2022: ('JOI 2021/2022 Spring Camp', 'https://www.ioi-jp.org/camp/2022/2022-sp-tasks/index.html'),
    2023: ('JOI 2022/2023 Spring Camp', 'https://www.ioi-jp.org/camp/2023/2023-sp-tasks/index.html'),
    2024: ('JOI 2023/2024 Spring Camp', 'https://www2.ioi-jp.org/camp/2024/2024-sp-tasks/index.html'),
    2025: ('JOI 2024/2025 Spring Camp', 'https://www2.ioi-jp.org/camp/2025/2025-sp-tasks/index.html'),
    2026: ('JOI 2025/2026 Spring Camp', 'https://www2.ioi-jp.org/joi/2025/2026-final/'),
}

DAY_LABEL = {
    'd1': 'Dan 1', 'd2': 'Dan 2', 'd3': 'Dan 3', 'd4': 'Dan 4',
    'day1': 'Dan 1', 'day2': 'Dan 2', 'day3': 'Dan 3', 'day4': 'Dan 4',
    'contest1': 'Dan 1', 'contest2': 'Dan 2', 'contest3': 'Dan 3', 'contest4': 'Dan 4',
}

# Prosječan rezultat >= ovog praga računa se kao "najlakše" (potpuno zeleno).
GREEN_AT = 80.0


def difficulty(avg):
    """Težina u [0, 1]: 0 = najlakši (zeleno), 1 = najteži (crveno)."""
    if avg is None:
        return 0.6
    return round(max(0.0, min(1.0, 1.0 - avg / GREEN_AT)), 3)


def difficulty_label(avg):
    if avg is None:
        return 'nepoznata težina'
    t = difficulty(avg)
    if t < 0.25:
        return 'lakši'
    if t < 0.5:
        return 'srednji'
    if t < 0.75:
        return 'teži'
    return 'vrlo težak'


def parse_content(path):
    text = open(path, encoding='utf-8').read()
    blocks = {}
    current = None
    buf = []
    for line in text.split('\n'):
        m = re.match(r'^@@\s*(\w+)\s*$', line)
        if m:
            if current:
                blocks[current] = '\n'.join(buf).strip('\n')
            current = m.group(1)
            buf = []
        else:
            buf.append(line)
    if current:
        blocks[current] = '\n'.join(buf).strip('\n')
    for k in blocks:
        blocks[k] = re.sub(r'<span class="bodovi">(\d+)</span>', points_badge, blocks[k])
    meta = {}
    for line in blocks.get('meta', '').split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            meta[k.strip()] = v.strip()
    blocks['meta'] = meta
    return blocks


def esc(s):
    return html.escape(s, quote=True)


def points_word(n):
    if n % 10 == 1 and n % 100 != 11:
        return 'bod'
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return 'boda'
    return 'bodova'


def points_badge(m):
    n = int(m.group(1))
    return f'<span class="bodovi">{n} {points_word(n)}</span>'


def head(title, depth, extra_css=(), mathjax=True, coach=True, joisc_js=True):
    rel = '../' * depth
    css = ['zadatak.css', 'pozadina.css', 'trener.css', 'joisc.css'] + list(extra_css)
    parts = [
        '<!DOCTYPE html>',
        '<html lang="hr">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'    <title>{esc(title)}</title>',
    ]
    parts.append(f'    <script src="{rel}assets/js/asset-errors.js"></script>')
    if mathjax:
        parts += [
            f'    <script src="{rel}assets/js/mathjax-config.js"></script>',
            '    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js" '
            'integrity="sha384-AHAnt9ZhGeHIrydA1Kp1L7FN+2UosbF7RQg6C+9Is/a7kDpQ1684C2iH2VWil6r4" crossorigin="anonymous"',
            '        onerror="reportAssetError(\'MathJax\', \'Matematički izrazi ostat će prikazani kao izvorni LaTeX kod.\')"></script>',
        ]
    for c in css:
        parts.append(f'    <link rel="stylesheet" href="{rel}assets/css/{c}">')
    if coach:
        parts.append(f'    <script src="{rel}assets/js/coach-mode.js"></script>')
    if joisc_js:
        parts.append(f'    <script src="{rel}assets/js/joisc.js"></script>')
    parts.append('</head>')
    return '\n'.join(parts) + '\n'


def head_map(title, depth):
    rel = '../' * depth
    return '\n'.join([
        '<!DOCTYPE html>',
        '<html lang="hr">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'    <title>{esc(title)}</title>',
        f'    <link rel="stylesheet" href="{rel}assets/css/mapa.css">',
        f'    <link rel="stylesheet" href="{rel}assets/css/pozadina.css">',
        f'    <link rel="stylesheet" href="{rel}assets/css/trener.css">',
        f'    <link rel="stylesheet" href="{rel}assets/css/joisc.css">',
        f'    <script src="{rel}assets/js/coach-mode.js"></script>',
        '</head>',
    ]) + '\n'


# ---------- slajdovi ----------

SLIDES_RE = re.compile(r'<slajdovi\b([^>]*)>(.*?)</slajdovi>', re.S)
SLIDE_RE = re.compile(r'<slajd\b([^>]*)>(.*?)</slajd>', re.S)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
CAPTION_RE = re.compile(r'<s\s+n="(\d+)"\s*>(.*?)</s>', re.S)


def attrs(s):
    return dict(ATTR_RE.findall(s))


def render_slides(year, slug, a, body, n_total):
    frm = int(a.get('from', a.get('n', 1)))
    to = int(a.get('to', frm))
    vrsta = a.get('vrsta', 'slike')
    naslov = a.get('naslov', '')
    if frm < 1 or to > n_total or frm > to:
        raise ValueError(f'{year}/{slug}: raspon slajdova {frm}-{to} izvan 1-{n_total}')
    captions = {int(n): c.strip() for n, c in CAPTION_RE.findall(body)}
    rest = CAPTION_RE.sub('', body).strip()
    if rest:
        # zajednički natpis za sve slajdove bez vlastitog natpisa
        common = rest
    else:
        common = ''
    count = to - frm + 1
    oznaka = 'Koraci algoritma' if vrsta == 'koraci' else ('Slajd' if count == 1 else 'Slajdovi')
    out = [f'<div class="slajdovi" data-vrsta="{esc(vrsta)}" role="group" aria-roledescription="prikaz slajdova"'
           f' aria-label="{esc(naslov or oznaka)}">']
    out.append('    <div class="slajdovi-naslov">')
    out.append(f'        <span class="oznaka">{oznaka}</span>')
    if naslov:
        out.append(f'        <span class="naslov-slajdova">{naslov}</span>')
    src_label = f'izvorni slajdovi {frm}–{to}' if count > 1 else f'izvorni slajd {frm}'
    out.append(f'        <span class="brojac" title="{esc(src_label)}">{src_label}</span>')
    out.append('    </div>')
    out.append('    <ol class="slajd-popis">')
    for i in range(frm, to + 1):
        cap = captions.get(i, common)
        out.append('        <li class="slajd">')
        out.append('            <figure>')
        out.append(f'                <img src="slajdovi/{slug}/{i:02d}.webp" alt="Slajd {i} izvorne prezentacije rješenja" width="800">')
        out.append(f'                <figcaption><span class="broj-slajda">{i}</span>{cap}</figcaption>')
        out.append('            </figure>')
        out.append('        </li>')
    out.append('    </ol>')
    if count > 1:
        out.append('    <div class="kontrole">')
        out.append('        <button type="button" class="prethodni" aria-label="Prethodni slajd">◀</button>')
        out.append('        <input type="range" min="0" max="1" value="0" step="1" aria-label="Odabir slajda">')
        out.append('        <button type="button" class="sljedeci" aria-label="Sljedeći slajd">▶</button>')
        if vrsta == 'koraci':
            out.append('        <button type="button" class="animiraj" aria-pressed="false">▶ Animiraj</button>')
        out.append('        <span class="tipkovnica">← → tipke ili klik na sliku</span>')
        out.append('    </div>')
    out.append('</div>')
    return '\n'.join(out)


def expand_slides(text, year, slug):
    n_total = SLIDES[f'{year}/{slug}']['n']

    def rep_multi(m):
        return render_slides(year, slug, attrs(m.group(1)), m.group(2), n_total)

    def rep_single(m):
        a = attrs(m.group(1))
        a['from'] = a['to'] = a.get('n', '1')
        return render_slides(year, slug, a, m.group(2), n_total)

    text = SLIDES_RE.sub(rep_multi, text)
    text = SLIDE_RE.sub(rep_single, text)
    return text


# ---------- stranice ----------

def problem_page(year, entry, meta, blocks, score, ordinal, day_label):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_en = meta.get('engleski', '')
    avg = score['avg'] if score else None
    t = difficulty(avg)
    tags = [x.strip() for x in meta.get('oznake', '').split(',') if x.strip()]
    limits = LIMITS[str(year)][slug]
    tl = limits.get('time', '')
    ml = limits.get('mem', '')
    interactive = meta.get('tip', '')

    p = [head(f'JOISC {year} — {title_hr}', 3)]
    p.append('<body>')
    p.append('<div class="joisc-stranica">')
    p.append(f'    <p class="navigacija"><a href="index.html">← Natrag na JOISC {year}</a> · <a href="../index.html">JOISC</a> · '
             f'<a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="sadrzaj">')
    p.append('    <header class="joisc-zaglavlje">')
    p.append(f'        <p class="podnaslov">JOI Spring Camp {year} · {esc(day_label)} · zadatak {ordinal}</p>')
    p.append(f'        <h1>{esc(title_hr)}</h1>')
    if title_en:
        p.append(f'        <p class="podnaslov"><i>{esc(title_en)}</i></p>')
    p.append('        <ul class="joisc-oznake">')
    if avg is not None:
        p.append(f'            <li class="tezina" style="--tezina: {t}" title="Prosječan rezultat natjecatelja na kampu: {avg:g}/100">'
                 f'Težina: {difficulty_label(avg)} · prosjek {avg:g}/100</li>')
    if tl:
        p.append(f'            <li>Vrijeme: {esc(tl)}</li>')
    if ml:
        p.append(f'            <li>Memorija: {esc(ml)}</li>')
    if interactive:
        p.append(f'            <li>{esc(interactive)}</li>')
    for tag in tags:
        p.append(f'            <li>{esc(tag)}</li>')
    p.append('        </ul>')
    p.append('    </header>')

    p.append('    <nav class="tabovi" role="tablist" aria-label="Dijelovi zadatka">')
    p.append('        <a href="#zadatak" role="tab" class="tab-zadatak" aria-selected="true" aria-controls="zadatak" id="tab-zadatak">Zadatak</a>')
    p.append('        <a href="#rjesenje" role="tab" class="tab-rjesenje" aria-selected="false" aria-controls="rjesenje" id="tab-rjesenje">Rješenje</a>')
    p.append('        <a href="#trener" role="tab" class="tab-trener" aria-selected="false" aria-controls="trener" id="tab-trener">Trenerski mod</a>')
    p.append('    </nav>')

    # --- Zadatak
    p.append('    <section id="zadatak" class="tab-panel" role="tabpanel" aria-labelledby="tab-zadatak">')
    p.append('        <h2 class="naslov-sekcije">Zadatak</h2>')
    p.append('        <div class="zadatak">')
    p.append(blocks['zadatak'])
    p.append('        </div>')
    p.append('    </section>')

    # --- Rješenje
    p.append('    <section id="rjesenje" class="tab-panel" role="tabpanel" aria-labelledby="tab-rjesenje">')
    p.append('        <h2 class="naslov-sekcije">Rješenje</h2>')
    p.append('        <div class="rjesenje">')
    p.append('            <p class="trener-napomena">Savjet: prije čitanja rješenja prođi kroz korake u trenerskom modu.</p>')
    p.append(blocks['rjesenje'])
    p.append(f'            <a class="kartica-analize" href="{slug}-editorial.html">')
    p.append('                <span class="ikona" aria-hidden="true">📖</span>')
    p.append('                <span>Cijela analiza rješenja (editorial)'
             f'<small>Prevedena i proširena službena prezentacija ({SLIDES[f"{year}/{slug}"]["n"]} slajdova) s interaktivnim prikazom koraka.</small></span>')
    p.append('            </a>')
    p.append('        </div>')
    p.append('    </section>')

    # --- Trenerski mod
    p.append('    <section id="trener" class="tab-panel" role="tabpanel" aria-labelledby="tab-trener">')
    p.append('        <h2 class="naslov-sekcije">Trenerski mod</h2>')
    p.append('        <div class="trener-panel">')
    p.append('            <h2>TRENERSKI MOD: korak po korak</h2>')
    p.append('            <p>Vođeni tok razmišljanja: otvaraj korake redom i nakon svakog pokušaj sam nastaviti prije nego pogledaš sljedeći.</p>')
    p.append(blocks['trener'])
    p.append('        </div>')
    p.append('    </section>')

    # --- Izvor
    p.append('    <section class="izvor">')
    p.append('        <h3>Izvor</h3>')
    p.append('        <ul>')
    p.append(f'            <li><a href="{esc(entry["en_url"])}">Službeni tekst zadatka (engleski, PDF)</a></li>')
    p.append(f'            <li><a href="{esc(entry["review_url"])}">Službena prezentacija rješenja (japanski, PDF)</a></li>')
    p.append(f'            <li><a href="{esc(YEAR_INFO[year][1])}">Stranica kampa {YEAR_INFO[year][0]}</a></li>')
    p.append('        </ul>')
    p.append('    </section>')
    p.append('    </div>')
    p.append('</div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def editorial_page(year, entry, meta, blocks, score, day_label):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_en = meta.get('engleski', '')
    n = SLIDES[f'{year}/{slug}']['n']
    autor = meta.get('autor_analize', '')
    body = expand_slides(blocks['analiza'], year, slug)

    p = [head(f'JOISC {year} — {title_hr}: analiza rješenja', 3)]
    p.append('<body>')
    p.append(f'    <p class="navigacija-analize"><a href="{slug}.html">← Natrag na zadatak</a> · '
             f'<a href="index.html">JOISC {year}</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <article class="analiza">')
    p.append('        <header>')
    p.append(f'            <p class="nadnaslov">Analiza rješenja · JOI Spring Camp {year} · {esc(day_label)}</p>')
    p.append(f'            <h1>{esc(title_hr)}</h1>')
    meta_bits = []
    if title_en:
        meta_bits.append(f'<i>{esc(title_en)}</i>')
    if autor:
        meta_bits.append(f'autor službene prezentacije: {esc(autor)}')
    meta_bits.append(f'{n} izvornih slajdova')
    if score:
        meta_bits.append(f'prosječan rezultat na kampu {score["avg"]:g}/100')
    p.append(f'            <p class="meta">{" · ".join(meta_bits)}</p>')
    p.append('        </header>')
    p.append('        <div class="uvodnik">')
    p.append('            <h3>O ovom članku</h3>')
    p.append('            <p>Tekst je prijevod službene japanske prezentacije rješenja, preoblikovan u članak. '
             'Slajdovi su ugrađeni kao slike; natpis pod svakim slajdom je prijevod teksta na njemu. '
             'Dijelovi označeni kao <b>trenerska napomena</b> nisu u izvornoj prezentaciji — dodani su da popune '
             'korake koje slajdovi preskaču ili samo skiciraju.</p>')
    p.append('        </div>')
    p.append(body)
    p.append('        <footer>')
    p.append(f'            Izvor: <a href="{esc(entry["review_url"])}">službena prezentacija rješenja (PDF)</a> · '
             f'<a href="{esc(entry["en_url"])}">tekst zadatka (PDF)</a> · '
             f'<a href="{esc(YEAR_INFO[year][1])}">{esc(YEAR_INFO[year][0])}</a>. '
             'Slike slajdova pripadaju Japanskom informatičkom olimpijskom komitetu (JOI); ovdje su prikazane u obrazovne svrhe.')
    p.append('        </footer>')
    p.append('    </article>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def year_index(year, items):
    name, url = YEAR_INFO[year]
    p = [head_map(f'JOISC {year}', 3)]
    p.append('<body>')
    p.append(f'    <h1>JOI Spring Camp {year}</h1>')
    p.append('    <p><a href="../index.html">← Natrag na popis godina</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append(f'        <p>{esc(name)}: četiri natjecateljska dana, po tri zadatka dnevno. Svaki zadatak ima prevedeni tekst, '
             'sažeto rješenje, trenerski mod i zasebnu analizu (editorial) s prevedenim slajdovima.</p>')
    p.append('    </div>')
    p.append('    <div class="joisc-legenda" aria-hidden="true">')
    p.append('        <div>Boja kartice = težina po prosječnom rezultatu natjecatelja na kampu</div>')
    p.append('        <div class="traka"></div>')
    p.append('        <div class="krajevi"><span>lakši (visok prosjek)</span><span>teži (nizak prosjek)</span></div>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa joisc-mreza">')
    last_day = None
    for it in items:
        if it['day_label'] != last_day:
            p.append(f'        <div class="joisc-dan">{esc(it["day_label"])}</div>')
            last_day = it['day_label']
        avg = it['avg']
        t = difficulty(avg)
        tip = (f'Prosječan rezultat natjecatelja: {avg:g}/100 · {difficulty_label(avg)}' if avg is not None
               else 'Statistika nije dostupna')
        p.append(f'        <a href="{it["slug"]}.html" class="kucica-mape joisc-kartica" style="--tezina: {t}">')
        p.append('            <span class="strelica">➔</span>')
        p.append(f'            <span class="naslov-kucice">{esc(it["naslov"])}<small>{esc(it["engleski"])}</small></span>')
        if avg is not None:
            p.append(f'            <span class="prosjek" data-tip="{esc(tip)}" aria-label="Prosječan rezultat {avg:g} od 100">{avg:g}</span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append(f'    <p class="joisc-uvod" style="margin-top:26px"><small>Statistika je službeni prosjek bodova sudionika kampa '
             f'(<a href="{esc(url)}">izvor</a>). Zadaci nultog (probnog) dana nemaju službenu analizu pa nisu uključeni.</small></p>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def root_index(years):
    p = [head_map('JOISC — JOI Spring Camp', 2)]
    p.append('<body>')
    p.append('    <h1>JOISC — JOI Spring Camp</h1>')
    p.append('    <p><a href="../index.html">← Natrag na prijevode</a> · <a href="../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append('        <p>Japanski proljetni kamp (JOI Spring Camp) je završni krug izbora japanske ekipe za IOI. '
             'Zadaci su IOI stila s podzadacima, često s interaktivnim ili komunikacijskim formatom. '
             'Ovdje su prevedeni tekstovi zadataka, rješenja, trenerski mod i analize za godine 2017.–2026.</p>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa">')
    for y, cnt in years:
        p.append(f'        <a href="{y}/index.html" class="kucica-mape">')
        p.append('            <span class="strelica">➔</span>')
        p.append(f'            <span class="naslov-kucice">JOISC {y}</span>')
        p.append(f'            <span class="statistika"><span class="rjesivost rjesivost-4" data-tip="Broj zadataka s prijevodom i analizom">{cnt} zad.</span></span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def main():
    only = sys.argv[1:]  # opcionalno: godine koje treba (ponovno) generirati
    years = {}
    for idx, entry in enumerate(MANIFEST):
        years.setdefault(entry['year'], []).append(entry)

    built = []
    for year, entries in sorted(years.items()):
        if only and str(year) not in only:
            continue
        score_rows = SCORES.get(str(year), [])
        items = []
        os.makedirs(os.path.join(OUT, str(year)), exist_ok=True)
        day_counter = {}
        for i, entry in enumerate(entries):
            slug = entry['slug']
            path = os.path.join(CONTENT, str(year), f'{slug}.html')
            if not os.path.exists(path):
                print(f'  ! nedostaje sadržaj {year}/{slug}', file=sys.stderr)
                continue
            blocks = parse_content(path)
            for k in ('zadatak', 'rjesenje', 'trener', 'analiza'):
                if k not in blocks:
                    raise SystemExit(f'{path}: nedostaje blok @@ {k}')
            meta = blocks['meta']
            score = score_rows[i] if i < len(score_rows) else None
            day_label = DAY_LABEL[entry['day']]
            day_counter[day_label] = day_counter.get(day_label, 0) + 1
            ordinal = day_counter[day_label]
            with open(os.path.join(OUT, str(year), f'{slug}.html'), 'w', encoding='utf-8') as f:
                f.write(problem_page(year, entry, meta, blocks, score, ordinal, day_label))
            with open(os.path.join(OUT, str(year), f'{slug}-editorial.html'), 'w', encoding='utf-8') as f:
                f.write(editorial_page(year, entry, meta, blocks, score, day_label))
            items.append({
                'slug': slug,
                'naslov': meta['naslov'],
                'engleski': meta.get('engleski', ''),
                'avg': score['avg'] if score else None,
                'day_label': day_label,
            })
        if items:
            with open(os.path.join(OUT, str(year), 'index.html'), 'w', encoding='utf-8') as f:
                f.write(year_index(year, items))
        built.append((year, len(items)))
        print(f'{year}: {len(items)} zadataka')

    if not only:
        with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(root_index([(y, c) for y, c in built if c]))


if __name__ == '__main__':
    main()
