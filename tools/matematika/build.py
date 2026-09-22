#!/usr/bin/env python3
"""Generator statičnih stranica kurikuluma Matematika (Matematika/).

Ulaz:
  tools/matematika/manifest.json                     oblasti i redoslijed lekcija
  tools/matematika/content/<oblast>/<slug>.html      sadržaj lekcije

Izlaz:
  Matematika/index.html                              kartice svih lekcija
  Matematika/<oblast>/<slug>.html                    stranica lekcije

Format datoteke sadržaja: blokovi započinju retkom "@@ ime":
  meta      retci "kljuc = vrijednost" (naslov, podnaslov, oznake)
  ciljevi   <li> stavke "U ovoj lekciji"
  teorija   teorijski dio
  primjeri  riješeni primjeri
  zadaci    zadaci za vježbu (rješenja skrivena)
  sazetak   (opcionalno) kratki sažetak lekcije
  literatura (opcionalno) <li> stavke za daljnje čitanje

Kratice koje se pretvaraju u HTML (ne smiju biti ugniježđene jedna u drugu):
  <definicija naslov="...">...</definicija>
  <teorem naslov="...">...</teorem>   (i <lema>, <propozicija>, <korolar>)
  <dokaz>...</dokaz>
  <napomena>...</napomena>                    trenerska napomena
  <primjer izvor="...">tekst<rjesenje>...</rjesenje></primjer>
  <zadatak izvor="..." tezina="1|2|3|4">tekst[<naputak>...</naputak>]<rjesenje>...</rjesenje></zadatak>
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(REPO, 'Matematika')
CONTENT = os.path.join(HERE, 'content')

MANIFEST = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))

# Razine težine po rednom broju lekcije (1–12); --tezina ide linearno od 0 do 1.
RAZINE = [
    (3, 'Osnove', 'školska i županijska razina'),
    (5, 'Državno', 'državno natjecanje, HMO kvalifikacije'),
    (7, 'JBMO / MEMO', 'juniorska balkanska i srednjoeuropska olimpijada'),
    (9, 'ISL 1–2', 'lakši zadaci IMO shortliste (npr. A1–A2, N1–N2)'),
    (11, 'ISL 3–4', 'srednji zadaci IMO shortliste (npr. A3–A4, G3–G4)'),
    (12, 'ISL 4–5', 'teži zadaci IMO shortliste (npr. A4–A5, C5, N4–N5)'),
]

TEZINA_ZADATKA = {'1': 'lakši', '2': 'srednji', '3': 'teži', '4': 'najteži'}


def razina(i):
    for granica, kratko, opis in RAZINE:
        if i <= granica:
            return kratko, opis
    return RAZINE[-1][1], RAZINE[-1][2]


def tezina(i, n):
    return round((i - 1) / max(1, n - 1), 3)


def esc(s):
    return html.escape(s, quote=True)


# ---------- parsiranje sadržaja ----------

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
    meta = {}
    for line in blocks.get('meta', '').split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            meta[k.strip()] = v.strip()
    blocks['meta'] = meta
    return blocks


ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


def attrs(s):
    return dict(ATTR_RE.findall(s))


class Counter:
    def __init__(self):
        self.n = {}

    def next(self, key):
        self.n[key] = self.n.get(key, 0) + 1
        return self.n[key]


TVRDNJA_RE = re.compile(r'<(teorem|lema|propozicija|korolar)\b([^>]*)>(.*?)</\1>', re.S)
DEFINICIJA_RE = re.compile(r'<definicija\b([^>]*)>(.*?)</definicija>', re.S)
DOKAZ_RE = re.compile(r'<dokaz\b[^>]*>(.*?)</dokaz>', re.S)
NAPOMENA_RE = re.compile(r'<napomena\b[^>]*>(.*?)</napomena>', re.S)
PRIMJER_RE = re.compile(r'<primjer\b([^>]*)>(.*?)</primjer>', re.S)
ZADATAK_RE = re.compile(r'<zadatak\b([^>]*)>(.*?)</zadatak>', re.S)
RJESENJE_RE = re.compile(r'<rjesenje\b[^>]*>(.*?)</rjesenje>', re.S)
NAPUTAK_RE = re.compile(r'<naputak\b[^>]*>(.*?)</naputak>', re.S)

VRSTA_NAZIV = {'teorem': 'Teorem', 'lema': 'Lema', 'propozicija': 'Propozicija', 'korolar': 'Korolar'}


def wrap_paragraph(body):
    """Tijelo kratice bez blok-elemenata omotaj u <p> da razmaci budu ujednačeni."""
    body = body.strip()
    if not re.match(r'^<(p|ul|ol|div|table|h\d|pre)\b', body):
        body = f'<p>{body}</p>'
    return body


def expand_theory(text, counter):
    def tvrdnja(m):
        vrsta, a, body = m.group(1), attrs(m.group(2)), m.group(3)
        n = counter.next('tvrdnja')
        naslov = a.get('naslov', '')
        label = f'{VRSTA_NAZIV[vrsta]} {n}' + (f' ({naslov})' if naslov else '') + '.'
        body = body.strip()
        if body.startswith('<p>'):
            body = body.replace('<p>', f'<p><strong>{esc(label)}</strong> ', 1)
        else:
            body = f'<p><strong>{esc(label)}</strong> {body}</p>'
        return f'<div class="tvrdnja">\n{body}\n</div>'

    def definicija(m):
        a, body = attrs(m.group(1)), m.group(2)
        naslov = a.get('naslov', 'Definicija')
        return f'<div class="pojam">\n<h4>{esc(naslov)}</h4>\n{wrap_paragraph(body)}\n</div>'

    def dokaz(m):
        body = m.group(1).strip()
        if body.startswith('<p>'):
            body = body.replace('<p>', '<p><em>Dokaz.</em> ', 1)
        else:
            body = f'<p><em>Dokaz.</em> {body}</p>'
        # kraj dokaza: kvadratić na kraju zadnjeg odlomka
        idx = body.rfind('</p>')
        if idx != -1:
            body = body[:idx] + ' <span class="qed" aria-hidden="true">∎</span></p>' + body[idx + 4:]
        return f'<div class="dokaz">\n{body}\n</div>'

    def napomena(m):
        return f'<div class="trener-umetak">\n{wrap_paragraph(m.group(1))}\n</div>'

    text = TVRDNJA_RE.sub(tvrdnja, text)
    text = DEFINICIJA_RE.sub(definicija, text)
    text = DOKAZ_RE.sub(dokaz, text)
    text = NAPOMENA_RE.sub(napomena, text)
    return text


def split_solution(body, path, what):
    m = RJESENJE_RE.search(body)
    if not m:
        raise SystemExit(f'{path}: {what} nema <rjesenje>')
    statement = (body[:m.start()] + body[m.end():]).strip()
    return statement, m.group(1).strip()


def expand_examples(text, path, counter):
    def primjer(m):
        a, body = attrs(m.group(1)), m.group(2)
        n = counter.next('primjer')
        izvor = a.get('izvor', '')
        statement, solution = split_solution(body, path, f'primjer {n}')
        p = ['<section class="primjer">']
        p.append(f'<h3>Primjer {n}' + (f' <span class="izvor-oznaka">{esc(izvor)}</span>' if izvor else '') + '</h3>')
        p.append('<div class="zadatak">')
        p.append(wrap_paragraph(statement))
        p.append('</div>')
        p.append('<div class="rjesenje">')
        p.append('<h4>Rješenje</h4>')
        p.append(expand_theory(solution, counter))
        p.append('</div>')
        p.append('</section>')
        return '\n'.join(p)

    return PRIMJER_RE.sub(primjer, text)


def expand_problems(text, path, counter):
    def zadatak(m):
        a, body = attrs(m.group(1)), m.group(2)
        n = counter.next('zadatak')
        izvor = a.get('izvor', '')
        tez = a.get('tezina', '')
        hint = None
        hm = NAPUTAK_RE.search(body)
        if hm:
            hint = hm.group(1).strip()
            body = body[:hm.start()] + body[hm.end():]
        statement, solution = split_solution(body, path, f'zadatak {n}')
        p = ['<section class="vjezba">']
        head = f'<h3>Zadatak {n}'
        if tez in TEZINA_ZADATKA:
            head += f' <span class="tezina-zadatka tezina-{tez}" title="Procijenjena težina unutar lekcije">{TEZINA_ZADATKA[tez]}</span>'
        if izvor:
            head += f' <span class="izvor-oznaka">{esc(izvor)}</span>'
        head += '</h3>'
        p.append(head)
        p.append('<div class="zadatak">')
        p.append(wrap_paragraph(statement))
        p.append('</div>')
        if hint:
            p.append('<details class="spoiler naputak">')
            p.append('<summary>Naputak<span class="spoiler-napomena">klikni za prikaz</span></summary>')
            p.append(f'<div class="spoiler-sadrzaj">\n{wrap_paragraph(hint)}\n</div>')
            p.append('</details>')
        p.append('<details class="spoiler rjesenje-spoiler">')
        p.append('<summary>Rješenje<span class="spoiler-napomena">klikni za prikaz</span></summary>')
        p.append('<div class="spoiler-sadrzaj">')
        p.append('<div class="rjesenje">')
        p.append(expand_theory(solution, counter))
        p.append('</div>')
        p.append('</div>')
        p.append('</details>')
        p.append('</section>')
        return '\n'.join(p)

    return ZADATAK_RE.sub(zadatak, text)


# ---------- provjere ----------

VOID = {'br', 'hr', 'img', 'meta', 'link', 'input'}


class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs_):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs_):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f'redak {self.getpos()[0]}: zatvarajući </{tag}> bez otvarajućeg')
            return
        top, line = self.stack.pop()
        if top != tag:
            self.errors.append(f'redak {self.getpos()[0]}: </{tag}> zatvara <{top}> (otvoren u retku {line})')


def check_html(text, path):
    checker = TagChecker()
    checker.feed(text)
    checker.close()
    errors = list(checker.errors)
    for tag, line in checker.stack:
        errors.append(f'redak {line}: <{tag}> nikad zatvoren')
    if errors:
        raise SystemExit(f'{path}: HTML nije dobro oblikovan:\n  ' + '\n  '.join(errors[:10]))


MATH_RE = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


def check_math(text, path):
    """Neparan broj $ ili znak < / > unutar formule (razbija HTML) su greške."""
    stripped = re.sub(r'<pre\b.*?</pre>', '', text, flags=re.S)
    stripped = re.sub(r'<code\b.*?</code>', '', stripped, flags=re.S)
    stripped = stripped.replace('\\$', '')
    if stripped.count('$') % 2:
        raise SystemExit(f'{path}: neparan broj znakova $ (formula nije zatvorena)')
    for m in MATH_RE.finditer(stripped):
        f = m.group(1) or m.group(2)
        if '<' in f or '>' in f:
            raise SystemExit(f'{path}: unutar formule koristi \\lt, \\gt umjesto < i >: {f[:60]!r}')
        if '\n\n' in f:
            raise SystemExit(f'{path}: prazan redak unutar formule: {f[:60]!r}')
    for tag in ('teorem', 'lema', 'propozicija', 'korolar', 'definicija', 'dokaz', 'napomena',
                'primjer', 'zadatak', 'rjesenje', 'naputak'):
        if re.search(rf'<{tag}\b', text):
            raise SystemExit(f'{path}: kratica <{tag}> nije pretvorena (vjerojatno ugniježđena ili neispravna)')


# ---------- stranice ----------

def head(title, depth, mapa=False):
    rel = '../' * depth
    parts = [
        '<!DOCTYPE html>',
        '<html lang="hr">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'    <title>{esc(title)}</title>',
    ]
    parts += [
        f'    <script src="{rel}assets/js/asset-errors.js"></script>',
        f'    <script src="{rel}assets/js/mathjax-config.js"></script>',
    ]
    if not mapa:
        parts.append(f'    <script src="{rel}assets/js/matematika.js"></script>')
    parts += [
        '    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js" '
        'integrity="sha384-AHAnt9ZhGeHIrydA1Kp1L7FN+2UosbF7RQg6C+9Is/a7kDpQ1684C2iH2VWil6r4" crossorigin="anonymous"',
        '        onerror="reportAssetError(\'MathJax\', \'Matematički izrazi ostat će prikazani kao izvorni LaTeX kod.\')"></script>',
    ]
    if mapa:
        parts += [
            f'    <link rel="stylesheet" href="{rel}assets/css/mapa.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/pozadina.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/joisc.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/matematika.css">',
        ]
    else:
        parts += [
            f'    <link rel="stylesheet" href="{rel}assets/css/zadatak.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/pozadina.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/trener.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/joisc.css">',
            f'    <link rel="stylesheet" href="{rel}assets/css/matematika.css">',
        ]
    parts.append('</head>')
    return '\n'.join(parts) + '\n'


def lesson_card(oblast, item, n, indent='        '):
    i = item['i']
    t = tezina(i, n)
    kratko, opis = razina(i)
    tip = f'Lekcija {i} od {n} · razina: {kratko} ({opis})'
    p = [f'{indent}<a href="{oblast["slug"]}/{item["slug"]}.html" class="kucica-mape joisc-kartica" style="--tezina: {t}">']
    p.append(f'{indent}    <span class="strelica">➔</span>')
    sub = f'<small>{esc(item["podnaslov"])}</small>' if item['podnaslov'] else ''
    p.append(f'{indent}    <span class="naslov-kucice"><span class="broj-lekcije">{oblast["kod"]}{i}</span> {esc(item["naslov"])}{sub}</span>')
    p.append(f'{indent}    <span class="prosjek razina" data-tip="{esc(tip)}" aria-label="{esc(tip)}">{esc(kratko)}</span>')
    p.append(f'{indent}</a>')
    return '\n'.join(p)


def root_index(oblasti):
    total = sum(len(o['items']) for o in oblasti)
    p = [head('Matematika — olimpijski kurikulum', 1, mapa=True)]
    p.append('<body>')
    p.append('    <h1>Matematika</h1>')
    p.append('    <p><a href="../index.html">← Natrag na početnu</a></p>')
    p.append('    <div class="joisc-uvod">')
    p.append(f'        <p>Kurikulum za natjecateljsku matematiku u {total} lekcije, po {len(oblasti[0]["items"])} u svakoj od četiri oblasti. '
             'Lekcije unutar oblasti idu linearno po težini: od školskih osnova preko državnog natjecanja i JBMO/MEMO razine '
             'do zadataka IMO shortliste (razine A4–A5, C5, G4–G5, N4–N5).</p>')
    p.append('        <p>Svaka lekcija je zasebna kartica s teorijom i dokazima, riješenim primjerima korak po korak i zadacima za vježbu '
             'sa skrivenim rješenjima (klikni na <b>Rješenje</b>). Preporučeni redoslijed: prolazi četiri oblasti usporedno, '
             'lekciju po lekciju (A1, C1, G1, N1, pa A2, …).</p>')
    p.append('    </div>')
    p.append('    <nav class="matematika-oblasti" aria-label="Oblasti">')
    for o in oblasti:
        p.append(f'        <a href="#{o["slug"]}">{esc(o["naslov"])}</a>')
    p.append('    </nav>')
    p.append('    <div class="joisc-legenda" aria-hidden="true">')
    p.append('        <div>Boja kartice = razina lekcije unutar oblasti</div>')
    p.append('        <div class="traka"></div>')
    p.append('        <div class="krajevi"><span>osnove</span><span>IMO shortlist</span></div>')
    p.append('    </div>')
    p.append('    <div class="mreza-mapa joisc-mreza">')
    for o in oblasti:
        n = len(o['items'])
        p.append(f'        <div class="joisc-dan matematika-oblast" id="{o["slug"]}">{esc(o["naslov"])}</div>')
        p.append(f'        <p class="matematika-opis">{esc(o["opis"])}</p>')
        for item in o['items']:
            p.append(lesson_card(o, item, n))
    p.append('    </div>')
    p.append('</body>')
    p.append('</html>')
    return '\n'.join(p) + '\n'


def nav_link(oblast, item, cls, label):
    if item is None:
        return f'<span class="lekcija-nav-prazno {cls}"></span>'
    return (f'<a class="{cls}" href="{item["slug"]}.html"><small>{esc(label)}</small>'
            f'{oblast["kod"]}{item["i"]} · {esc(item["naslov"])}</a>')


def lesson_page(oblast, item, prev_item, next_item, n, blocks, path):
    meta = blocks['meta']
    i = item['i']
    t = tezina(i, n)
    kratko, opis = razina(i)
    tags = [x.strip() for x in meta.get('oznake', '').split(',') if x.strip()]
    counter = Counter()

    teorija = expand_theory(blocks['teorija'], counter)
    primjeri = expand_examples(blocks['primjeri'], path, counter)
    primjeri = expand_theory(primjeri, counter)
    zadaci = expand_problems(blocks['zadaci'], path, counter)
    zadaci = expand_theory(zadaci, counter)

    p = [head(f'Matematika — {oblast["naslov"]} {i}: {meta["naslov"]}', 2)]
    p.append('<body>')
    p.append('    <p class="navigacija-analize"><a href="../index.html">← Natrag na Matematiku</a> · '
             f'<a href="../index.html#{oblast["slug"]}">{esc(oblast["naslov"])}</a> · <a href="../../index.html">Početna</a></p>')
    p.append('    <article class="analiza lekcija">')
    p.append('        <header>')
    p.append(f'            <p class="nadnaslov">Matematika · {esc(oblast["naslov"])} · lekcija {i} od {n}</p>')
    p.append(f'            <h1><span class="broj-lekcije">{oblast["kod"]}{i}</span> {esc(meta["naslov"])}</h1>')
    if meta.get('podnaslov'):
        p.append(f'            <p class="meta">{esc(meta["podnaslov"])}</p>')
    p.append('            <ul class="joisc-oznake">')
    p.append(f'                <li class="tezina" style="--tezina: {t}" title="{esc(opis)}">Razina: {esc(kratko)}</li>')
    for tag in tags:
        p.append(f'                <li>{esc(tag)}</li>')
    p.append('            </ul>')
    p.append('        </header>')
    if blocks.get('ciljevi'):
        p.append('        <div class="uvodnik">')
        p.append('            <h3>U ovoj lekciji</h3>')
        p.append('            <ul>')
        p.append(blocks['ciljevi'])
        p.append('            </ul>')
        p.append('        </div>')
    p.append('        <nav class="lekcija-sadrzaj" aria-label="Dijelovi lekcije">')
    p.append('            <a href="#teorija">Teorija</a><a href="#primjeri">Riješeni primjeri</a><a href="#zadaci">Zadaci za vježbu</a>')
    p.append('        </nav>')
    p.append('        <h2 id="teorija">Teorija</h2>')
    p.append(teorija)
    p.append('        <h2 id="primjeri">Riješeni primjeri</h2>')
    p.append(primjeri)
    p.append('        <h2 id="zadaci">Zadaci za vježbu</h2>')
    p.append('        <p class="zadaci-napomena">Prvo pokušaj sam; rješenje otvori tek nakon ozbiljnog pokušaja. '
             'Oznaka težine je relativna unutar lekcije.</p>')
    p.append(zadaci)
    if blocks.get('sazetak'):
        p.append('        <div class="rezime">')
        p.append('            <h2>Sažetak</h2>')
        p.append(blocks['sazetak'])
        p.append('        </div>')
    if blocks.get('literatura'):
        p.append('        <section class="literatura">')
        p.append('            <h3>Za daljnje čitanje</h3>')
        p.append('            <ul>')
        p.append(blocks['literatura'])
        p.append('            </ul>')
        p.append('        </section>')
    p.append('        <footer>')
    p.append('            <nav class="lekcija-nav" aria-label="Susjedne lekcije">')
    p.append('                ' + nav_link(oblast, prev_item, 'prethodna', '← Prethodna lekcija'))
    p.append('                ' + nav_link(oblast, next_item, 'sljedeca', 'Sljedeća lekcija →'))
    p.append('            </nav>')
    p.append('        </footer>')
    p.append('    </article>')
    p.append('</body>')
    p.append('</html>')
    page = '\n'.join(p) + '\n'
    check_math(page, path)
    check_html(page, path)
    return page


def main():
    only = set(sys.argv[1:])  # opcionalno: oblasti koje treba (ponovno) generirati
    oblasti = []
    missing = 0
    for o in MANIFEST['oblasti']:
        items = []
        n = len(o['lekcije'])
        for i, slug in enumerate(o['lekcije'], start=1):
            path = os.path.join(CONTENT, o['slug'], f'{slug}.html')
            if not os.path.exists(path):
                print(f'  ! nedostaje sadržaj {o["slug"]}/{slug}', file=sys.stderr)
                missing += 1
                continue
            blocks = parse_content(path)
            for k in ('teorija', 'primjeri', 'zadaci'):
                if k not in blocks:
                    raise SystemExit(f'{path}: nedostaje blok @@ {k}')
            if 'naslov' not in blocks['meta']:
                raise SystemExit(f'{path}: meta nema naslov')
            items.append({
                'i': i,
                'slug': slug,
                'naslov': blocks['meta']['naslov'],
                'podnaslov': blocks['meta'].get('podnaslov', ''),
                'blocks': blocks,
                'path': path,
            })
        oblasti.append({**o, 'items': items})

    for o in oblasti:
        if only and o['slug'] not in only:
            continue
        n = len(o['lekcije'])
        os.makedirs(os.path.join(OUT, o['slug']), exist_ok=True)
        for idx, item in enumerate(o['items']):
            prev_item = o['items'][idx - 1] if idx > 0 else None
            next_item = o['items'][idx + 1] if idx + 1 < len(o['items']) else None
            page = lesson_page(o, item, prev_item, next_item, n, item['blocks'], item['path'])
            with open(os.path.join(OUT, o['slug'], f'{item["slug"]}.html'), 'w', encoding='utf-8') as f:
                f.write(page)
        print(f'{o["naslov"]}: {len(o["items"])} lekcija')

    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(root_index(oblasti))
    if missing:
        print(f'  ! {missing} lekcija bez sadržaja', file=sys.stderr)


if __name__ == '__main__':
    main()
