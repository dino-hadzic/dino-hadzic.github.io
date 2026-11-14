"""Generator stranica za prijevode RMI-a (Romanian Master of Informatics).

Sadržaj: content/<godina>/<slug>.html s blokovima @@ meta, @@ zadatak, @@ editorial
(isti format i komponente kao JOISC: <info>, <dodatak>, <skica>, <okviri> — vidi tools/joisc/EDITORIAL.md
i tools/rmi/EDITORIAL.md). Izlaz: prijevodi/rmi/<godina>/<slug>.html, <slug>-editorial.html, index.html.
Pokretanje: python3 tools/rmi/build.py [godina]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools', 'joisc'))
import build as joisc  # noqa: E402  (komponente, head(), provjera SVG-a ...)

OUT = os.path.join(REPO, 'prijevodi', 'rmi')
CONTENT = os.path.join(HERE, 'content')
MANIFEST = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
esc = joisc.esc

YEAR_INFO = {
    2025: ('RMI 2025 (Bukurešt, 26.–30. studenoga 2025.)', 'https://rmi.lbi.ro/rmi_2025/'),
}
DAY_LABEL = {'d1': 'Dan 1', 'd2': 'Dan 2'}


def qoj_url(entry):
    return f'https://qoj.ac/contest/{entry["contest"]}/problem/{entry["qoj"]}'


def points_list(entry):
    b = entry['bodovi']
    return ', '.join(f'{x}' for x in b) + f' (ukupno {sum(b)})'


def problem_page(year, entry, meta, blocks, ordinal, day_label):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_en = meta.get('engleski', '')
    tags = [x.strip() for x in meta.get('oznake', '').split(',') if x.strip()]

    p = [joisc.head(f'RMI {year} — {title_hr}', 3)]
    p.append('<body>')
    p.append('<div class="joisc-stranica">')
    p.append(f'    <p class="navigacija"><a href="index.html">← Natrag na RMI {year}</a> · <a href="../index.html">RMI</a> · '
             f'<a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="sadrzaj">')
    p.append('    <header class="joisc-zaglavlje">')
    p.append(f'        <p class="podnaslov">Romanian Master of Informatics {year} · {esc(day_label)} · zadatak {ordinal}</p>')
    p.append(f'        <h1>{esc(title_hr)}</h1>')
    if title_en:
        p.append(f'        <p class="podnaslov"><i>{esc(title_en)}</i></p>')
    p.append('        <ul class="joisc-oznake">')
    if entry.get('tl'):
        p.append(f'            <li>Vrijeme: {esc(entry["tl"])}</li>')
    if entry.get('ml'):
        p.append(f'            <li>Memorija: {esc(entry["ml"])}</li>')
    if entry.get('tip'):
        p.append(f'            <li>{esc(entry["tip"])}</li>')
    p.append(f'            <li title="Bodovi po podzadacima">Podzadaci: {esc(points_list(entry))}</li>')
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
    p.append(joisc.expand_components(blocks['zadatak'], f'rmi {year}/{slug} zadatak'))
    p.append('        </div>')
    p.append('    </section>')
    p.append('    <section class="izvor">')
    p.append('        <h3>Izvor</h3>')
    p.append('        <ul>')
    p.append(f'            <li><a href="{esc(entry["paket"])}">Službeni paket zadatka (tekst, testovi, službena rješenja; ZIP)</a></li>')
    p.append(f'            <li><a href="{esc(qoj_url(entry))}">Zadatak na QOJ-u (qoj.ac)</a></li>')
    p.append(f'            <li><a href="{esc(YEAR_INFO[year][1])}">Službena stranica natjecanja — {esc(YEAR_INFO[year][0])}</a></li>')
    p.append('        </ul>')
    p.append('    </section>')
    p.append('    </div>')
    p.append('</div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def editorial_page(year, entry, meta, blocks, day_label):
    slug = entry['slug']
    title_hr = meta['naslov']
    title_en = meta.get('engleski', '')
    izvori = meta.get('izvori', '')
    body = joisc.expand_components(blocks['editorial'], f'rmi {year}/{slug}')

    p = [joisc.head(f'RMI {year} — {title_hr}: analiza rješenja', 3)]
    p.append('<body>')
    p.append(f'    <p class="navigacija-analize"><a href="{slug}.html">← Natrag na zadatak</a> · '
             f'<a href="index.html">RMI {year}</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <article class="analiza">')
    p.append('        <header>')
    p.append(f'            <p class="nadnaslov">Analiza rješenja · Romanian Master of Informatics {year} · {esc(day_label)}</p>')
    p.append(f'            <h1>{esc(title_hr)}</h1>')
    meta_bits = []
    if title_en:
        meta_bits.append(f'<i>{esc(title_en)}</i>')
    meta_bits.append(f'podzadaci: {esc(points_list(entry))}')
    p.append(f'            <p class="meta">{" · ".join(meta_bits)}</p>')
    p.append('        </header>')
    p.append('        <div class="uvodnik">')
    p.append('            <h3>O ovom članku</h3>')
    p.append('            <p>RMI ne objavljuje pisani editorial, pa je ova analiza napisana prema službenim rješenjima iz paketa zadatka '
             'i prema prihvaćenim (AC) rješenjima natjecatelja na QOJ-u' + (f' ({izvori})' if izvori else '') + '. '
             'Svaki opisani pristup implementiran je i provjeren na službenim testovima. Rješenje je izloženo podzadatak po podzadatak. '
             'Gumb <span class="info-gumb-primjer" aria-hidden="true">i</span> otvara karticu s dodatnim objašnjenjem pojma.</p>')
    p.append('        </div>')
    p.append(body)
    p.append('        <footer>')
    p.append(f'            Izvor: <a href="{esc(entry["paket"])}">službeni paket zadatka (ZIP)</a> · '
             f'<a href="{esc(qoj_url(entry))}">zadatak na QOJ-u</a> · '
             f'<a href="{esc(YEAR_INFO[year][1])}">{esc(YEAR_INFO[year][0])}</a>. '
             'Tekst zadatka i skice prevedeni su prema službenom engleskom tekstu; analiza je autorska, izvedena iz službenih i prihvaćenih rješenja.')
    p.append('        </footer>')
    p.append('    </article>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def year_index(year, items):
    name, url = YEAR_INFO[year]
    p = [joisc.head_map(f'RMI {year}', 3)]
    p.append('<body>')
    p.append(f'    <h1>Romanian Master of Informatics {year}</h1>')
    p.append('    <p><a href="../index.html">← Natrag na popis godina</a> · <a href="../../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append(f'        <p>{esc(name)}: dva natjecateljska dana, po tri zadatka dnevno. Svaki zadatak ima prevedeni tekst i '
             'zasebnu analizu rješenja (editorial) podzadatak po podzadatak, napisanu prema službenim i prihvaćenim rješenjima.</p>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa joisc-mreza">')
    last_day = None
    for it in items:
        if it['day_label'] != last_day:
            p.append(f'        <div class="joisc-dan">{esc(it["day_label"])}</div>')
            last_day = it['day_label']
        p.append(f'        <a href="{it["slug"]}.html" class="kucica-mape joisc-kartica">')
        p.append('            <span class="strelica">➔</span>')
        p.append(f'            <span class="naslov-kucice">{esc(it["naslov"])}<small>{esc(it["engleski"])}</small></span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append(f'    <p class="joisc-uvod" style="margin-top:26px"><small>Službena stranica: <a href="{esc(url)}">{esc(url)}</a>.</small></p>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def root_index(years):
    p = [joisc.head_map('RMI — Romanian Master of Informatics', 2)]
    p.append('<body>')
    p.append('    <h1>RMI — Romanian Master of Informatics</h1>')
    p.append('    <p><a href="../index.html">← Natrag na prijevode</a> · <a href="../../index.html">Početna</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append('        <p>Romanian Master of Informatics je međunarodno pozivno natjecanje za srednjoškolce koje se održava u Bukureštu, '
             'u organizaciji Nacionalnog koledža za informatiku „Tudor Vianu”. Zadaci su IOI stila s podzadacima, često s '
             'interaktivnim formatom. Ovdje su prevedeni tekstovi zadataka i analize rješenja.</p>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa">')
    for y, cnt in years:
        p.append(f'        <a href="{y}/index.html" class="kucica-mape">')
        p.append('            <span class="strelica">➔</span>')
        p.append(f'            <span class="naslov-kucice">RMI {y}</span>')
        p.append(f'            <span class="statistika"><span class="rjesivost rjesivost-4" data-tip="Broj zadataka s prijevodom i analizom">{cnt} zad.</span></span>')
        p.append('        </a>')
    p.append('    </div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def main():
    only = sys.argv[1:]
    years = {}
    for entry in MANIFEST:
        years.setdefault(entry['year'], []).append(entry)
    built = []
    for year, entries in sorted(years.items()):
        if only and str(year) not in only:
            continue
        os.makedirs(os.path.join(OUT, str(year)), exist_ok=True)
        items = []
        day_counter = {}
        for entry in entries:
            slug = entry['slug']
            path = os.path.join(CONTENT, str(year), f'{slug}.html')
            if not os.path.exists(path):
                print(f'  ! nedostaje sadržaj {year}/{slug}', file=sys.stderr)
                continue
            blocks = joisc.parse_content(path)
            for k in ('meta', 'zadatak', 'editorial'):
                if k not in blocks:
                    raise SystemExit(f'{path}: nedostaje blok @@ {k}')
            meta = blocks['meta']
            day_label = DAY_LABEL[entry['day']]
            day_counter[day_label] = day_counter.get(day_label, 0) + 1
            with open(os.path.join(OUT, str(year), f'{slug}.html'), 'w', encoding='utf-8') as f:
                f.write(problem_page(year, entry, meta, blocks, day_counter[day_label], day_label))
            with open(os.path.join(OUT, str(year), f'{slug}-editorial.html'), 'w', encoding='utf-8') as f:
                f.write(editorial_page(year, entry, meta, blocks, day_label))
            items.append({'slug': slug, 'naslov': meta['naslov'], 'engleski': meta.get('engleski', ''), 'day_label': day_label})
        if items:
            with open(os.path.join(OUT, str(year), 'index.html'), 'w', encoding='utf-8') as f:
                f.write(year_index(year, items))
        built.append((year, len(items)))
        print(f'RMI {year}: {len(items)} zadataka')
    if not only:
        with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(root_index([(y, c) for y, c in built if c]))


if __name__ == '__main__':
    main()
