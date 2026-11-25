"""Generator stranica za prijevode Ynoi zadataka (lxl-ova serija zadataka iz struktura podataka; zadaci na qoj.ac).

Sadržaj: content/<natjecanje>/<slug>.html s blokovima @@ meta, @@ zadatak, @@ editorial
(isti format i komponente kao JOISC/RMI — vidi tools/joisc/EDITORIAL.md i tools/ynoi/EDITORIAL.md).
Izlaz: prijevodi/ynoi/<natjecanje>/<slug>.html, <slug>-editorial.html, index.html.
Pokretanje: python3 tools/ynoi/build.py [natjecanje ...]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools', 'joisc'))
import build as joisc  # noqa: E402  (komponente, head(), provjera SVG-a ...)

OUT = os.path.join(REPO, 'prijevodi', 'ynoi')
CONTENT = os.path.join(HERE, 'content')
MANIFEST = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
esc = joisc.esc


def head_map(title, depth):
    h = joisc.head_map(title, depth)
    return '\n'.join(l for l in h.split('\n') if 'trener.css' not in l and 'coach-mode.js' not in l)


def qoj_url(entry):
    return f'https://qoj.ac/problem/{entry["qoj"]}'


def problem_page(contest, entry, meta, blocks):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_orig = meta.get('izvornik', '')
    tags = [x.strip() for x in meta.get('oznake', '').split(',') if x.strip()]
    cname = contest['naziv']

    p = [joisc.head(f'{cname} — {title_hr}', 3, coach=False)]
    p.append('<body>')
    p.append('<div class="joisc-stranica">')
    p.append(f'    <p class="navigacija"><a href="index.html">← Natrag na {esc(cname)}</a> · <a href="../index.html">Ynoi</a> · '
             f'<a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="sadrzaj">')
    p.append('    <header class="joisc-zaglavlje">')
    p.append(f'        <p class="podnaslov">{esc(cname)} · QOJ #{entry["qoj"]}</p>')
    p.append(f'        <h1>{esc(title_hr)}</h1>')
    if title_orig and title_orig != title_hr:
        p.append(f'        <p class="podnaslov"><i>{esc(title_orig)}</i></p>')
    p.append('        <ul class="joisc-oznake">')
    if entry.get('tl'):
        p.append(f'            <li>Vrijeme: {esc(entry["tl"])}</li>')
    if entry.get('ml'):
        p.append(f'            <li>Memorija: {esc(entry["ml"])}</li>')
    if entry.get('tip'):
        p.append(f'            <li>{esc(entry["tip"])}</li>')
    for tag in tags:
        p.append(f'            <li>{esc(tag)}</li>')
    p.append('        </ul>')
    p.append('    </header>')
    p.append('    <nav class="tabovi" aria-label="Dijelovi zadatka">')
    p.append('        <a href="#zadatak" class="tab-zadatak" aria-current="page">Zadatak</a>')
    p.append(f'        <a href="{slug}-editorial.html" class="tab-rjesenje">Rješenje (editorial) →</a>')
    p.append('    </nav>')
    p.append('    <section id="zadatak" class="tab-panel" role="tabpanel" aria-labelledby="tab-zadatak">')
    p.append('        <h2 class="naslov-sekcije">Zadatak</h2>')
    p.append('        <div class="zadatak">')
    p.append(joisc.expand_components(blocks['zadatak'], f'ynoi {contest["id"]}/{slug} zadatak'))
    p.append('        </div>')
    p.append('    </section>')
    p.append('    <section class="izvor">')
    p.append('        <h3>Izvor</h3>')
    p.append('        <ul>')
    p.append(f'            <li><a href="{esc(qoj_url(entry))}">Zadatak na QOJ-u (qoj.ac/problem/{entry["qoj"]})</a></li>')
    if entry.get('izvor'):
        p.append(f'            <li>{esc(entry["izvor"])}</li>')
    p.append('        </ul>')
    p.append('    </section>')
    p.append('    </div>')
    p.append('</div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def editorial_page(contest, entry, meta, blocks):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_orig = meta.get('izvornik', '')
    izvori = meta.get('izvori', '')
    cname = contest['naziv']
    body = joisc.expand_components(blocks['editorial'], f'ynoi {contest["id"]}/{slug}')

    p = [joisc.head(f'{cname} — {title_hr}: analiza rješenja', 3, coach=False)]
    p.append('<body>')
    p.append(f'    <p class="navigacija-analize"><a href="{slug}.html">← Natrag na zadatak</a> · '
             f'<a href="index.html">{esc(cname)}</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <article class="analiza">')
    p.append('        <header>')
    p.append(f'            <p class="nadnaslov">Analiza rješenja · {esc(cname)} · QOJ #{entry["qoj"]}</p>')
    p.append(f'            <h1>{esc(title_hr)}</h1>')
    if title_orig and title_orig != title_hr:
        p.append(f'            <p class="meta"><i>{esc(title_orig)}</i></p>')
    p.append('        </header>')
    p.append('        <div class="uvodnik">')
    p.append('            <h3>O ovom članku</h3>')
    p.append('            <p>Za Ynoi zadatke na QOJ-u nema službenog pisanog editoriala, pa je ova analiza autorska'
             + (f' (izvori: {izvori})' if izvori else '') + '. '
             'Opisano rješenje je implementirano i provjereno usporedbom s izravnim (brute-force) rješenjem na nasumičnim testovima. '
             'Gumb <span class="info-gumb-primjer" aria-hidden="true">i</span> otvara karticu s dodatnim objašnjenjem pojma.</p>')
    p.append('        </div>')
    p.append(body)
    p.append('        <footer>')
    p.append(f'            Izvor: <a href="{esc(qoj_url(entry))}">zadatak na QOJ-u</a>. '
             'Tekst zadatka preveden je prema tekstu na QOJ-u; analiza je autorska.')
    p.append('        </footer>')
    p.append('    </article>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def contest_index(contest, items):
    cname = contest['naziv']
    p = [head_map(cname, 3)]
    p.append('<body>')
    p.append(f'    <h1>{esc(cname)}</h1>')
    p.append('    <p><a href="../index.html">← Natrag na popis natjecanja</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append('        <p>Svaki zadatak ima prevedeni tekst i zasebnu analizu rješenja (editorial).</p>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa joisc-mreza">')
    for it in items:
        p.append(f'        <a href="{it["slug"]}.html" class="kucica-mape joisc-kartica">')
        p.append('            <span class="strelica">➔</span>')
        small = f'<small>{esc(it["izvornik"])}</small>' if it['izvornik'] and it['izvornik'] != it['naslov'] else ''
        p.append(f'            <span class="naslov-kucice">{esc(it["naslov"])}{small}</span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def root_index(contests):
    p = [head_map('Ynoi', 2)]
    p.append('<body>')
    p.append('    <h1>Ynoi</h1>')
    p.append('    <p><a href="../index.html">← Natrag na prijevode</a> · <a href="../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append('        <p>Ynoi je serija vrlo teških zadataka iz struktura podataka (autor: lxl / nzhtl1477), poznata po '
             'sqrt-dekompoziciji, offline tehnikama i strogim vremenskim ograničenjima. „Godine” natjecanja su izmišljene oznake serije. '
             'Ovdje je izbor najbolje ocijenjenih zadataka s <a href="https://qoj.ac/problems?search=Ynoi">QOJ-a</a>: '
             'prevedeni tekstovi i analize rješenja.</p>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa">')
    for c, cnt in contests:
        p.append(f'        <a href="{c["id"]}/index.html" class="kucica-mape">')
        p.append('            <span class="strelica">➔</span>')
        p.append(f'            <span class="naslov-kucice">{esc(c["naziv"])}</span>')
        p.append(f'            <span class="statistika"><span class="rjesivost rjesivost-4" data-tip="Broj zadataka s prijevodom i analizom">{cnt} zad.</span></span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def main():
    only = sys.argv[1:]
    built = []
    for contest in MANIFEST:
        cid = contest['id']
        if only and cid not in only:
            continue
        items = []
        for entry in contest['zadaci']:
            slug = entry['slug']
            path = os.path.join(CONTENT, cid, f'{slug}.html')
            if not os.path.exists(path):
                print(f'  ! nedostaje sadržaj {cid}/{slug}', file=sys.stderr)
                continue
            blocks = joisc.parse_content(path)
            for k in ('meta', 'zadatak', 'editorial'):
                if k not in blocks:
                    raise SystemExit(f'{path}: nedostaje blok @@ {k}')
            meta = blocks['meta']
            os.makedirs(os.path.join(OUT, cid), exist_ok=True)
            with open(os.path.join(OUT, cid, f'{slug}.html'), 'w', encoding='utf-8') as f:
                f.write(problem_page(contest, entry, meta, blocks))
            with open(os.path.join(OUT, cid, f'{slug}-editorial.html'), 'w', encoding='utf-8') as f:
                f.write(editorial_page(contest, entry, meta, blocks))
            items.append({'slug': slug, 'naslov': meta['naslov'], 'izvornik': meta.get('izvornik', '')})
        if items:
            with open(os.path.join(OUT, cid, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(contest_index(contest, items))
        built.append((contest, len(items)))
        print(f'{contest["naziv"]}: {len(items)} zadataka')
    if not only:
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(root_index([(c, n) for c, n in built if n]))


if __name__ == '__main__':
    main()
