"""Generator statičkih HTML stranica za prijevode 1st Universal Cup-a.

Podaci o zadacima žive u content/stageNN.py (STAGE, PROBLEMS); ovaj modul ih
pretvara u HTML u repozitoriju. Pokretanje:  python3 gen.py 11 12 ...

Polja zadatka (uz obvezna letter/title/title_hr/slug/tl/ml/statement):
  solution  – sažeto rješenje (HTML) ili None ako rješenje ne postoji
  hints     – popis naputaka (HTML), svaki u vlastitom spoileru
  coach     – trenerski način: popis (pitanje, odgovor) – retorička pitanja koja vode do ideje
  tips      – opći savjeti/prečaci (HTML <li> sadržaj) prikazani na kraju trenerskog načina
  detailed  – detaljno rješenje (HTML), vidljivo samo uz uključen prekidač "Detaljno rješenje"
  verified  – kratak opis lokalne provjere koda (uzorci, stress test protiv brute forcea)
  code      – (neobvezno) put do C++ rješenja; zadano solutions/stageN/<slovo>/sol.cpp
Polja stagea: no_editorial (nema službenog editoriala), community (rješenja izvedena iz AC predaja).
"""
import html as htmllib
import importlib
import os
import re
import sys

from cards import render_no_editorial_badge, render_stats

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
SOLUTIONS = os.path.join(HERE, 'solutions')
ROOT = '../../../../'

MATHJAX = (
    '    <!-- UKLJUČIVANJE LATEX-A (MATHJAX) -->\n'
    f'    <script src="{ROOT}assets/js/asset-errors.js"></script>\n'
    f'    <script src="{ROOT}assets/js/mathjax-config.js"></script>\n'
    '    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js" '
    'integrity="sha384-AHAnt9ZhGeHIrydA1Kp1L7FN+2UosbF7RQg6C+9Is/a7kDpQ1684C2iH2VWil6r4" crossorigin="anonymous"\n'
    '        onerror="reportAssetError(\'MathJax\', \'Matematički izrazi ostat će prikazani kao izvorni LaTeX kod.\')"></script>\n'
)

HEAD_TAIL = (
    f'    <link rel="stylesheet" href="{ROOT}assets/css/zadatak.css">\n'
    f'    <link rel="stylesheet" href="{ROOT}assets/css/pozadina.css">\n'
    f'    <link rel="stylesheet" href="{ROOT}assets/css/trener.css">\n'
    f'    <script src="{ROOT}assets/js/coach-mode.js"></script>\n'
    f'    <script src="{ROOT}assets/js/detailed-mode.js"></script>\n'
)

COACH_INTRO = (
    'Vođeni tok razmišljanja: otvaraj korake redom i nakon svakog pokušaj sam nastaviti '
    'prije nego pogledaš sljedeći.'
)

LOGIC_INTRO = (
    'Logički put do rješenja: svaki je korak pitanje koje bi si iskusan natjecatelj postavio. '
    'Pokušaj na njega odgovoriti sam, pa tek onda otvori odgovor i usporedi – cilj je uvježbati '
    'način razmišljanja, a ne zapamtiti rješenje.'
)

COMMUNITY_NOTE = (
    'Organizatori za ovaj stage nisu objavili službeni editorial. Rješenje u nastavku izvedeno je '
    'iz analize prihvaćenih predaja na QOJ-u i vlastitog rješavanja, a priloženi kod lokalno je '
    'testiran (uzorci + stress test), no nije službeno rješenje autora zadatka.'
)

NO_DETAILED_NOTE = 'Detaljno rješenje za ovaj zadatak još nije napisano; prikazano je sažeto rješenje.'


def indent(html, n):
    pad = ' ' * n
    lines = html.strip('\n').rstrip().split('\n')
    lines[0] = lines[0].lstrip()
    rest = [l for l in lines[1:] if l.strip()]
    if rest:
        m = min(len(l) - len(l.lstrip()) for l in rest)
        lines = [lines[0]] + [l[m:] if l.strip() else '' for l in lines[1:]]
    return '\n'.join(pad + line if line.strip() else '' for line in lines)


def render_hints(hints):
    if not hints:
        return ''
    out = ['    <section class="naputci">', '        <h2>NAPUTCI</h2>']
    for i, h in enumerate(hints, 1):
        out.append('        <details class="spoiler naputak">')
        out.append(f'            <summary>Naputak {i}<span class="spoiler-napomena">klikni za prikaz</span></summary>')
        out.append('            <div class="spoiler-sadrzaj">')
        out.append(indent(h, 16))
        out.append('            </div>')
        out.append('        </details>')
    out.append('    </section>')
    return '\n'.join(out) + '\n'


def render_coach(coach, tips=()):
    if not coach:
        return ''
    if tips:
        out = ['    <section class="trener">', '        <h2>TRENERSKI NAČIN: logički put do rješenja</h2>',
               f'        <p>{LOGIC_INTRO}</p>', '        <ol class="koraci">']
    else:
        out = ['    <section class="trener">', '        <h2>TRENERSKI NAČIN: korak po korak</h2>',
               f'        <p>{COACH_INTRO}</p>', '        <ol class="koraci">']
    for title, body in coach:
        out.append('            <li>')
        out.append('                <details class="spoiler korak">')
        out.append(f'                    <summary>{title}</summary>')
        out.append('                    <div class="spoiler-sadrzaj">')
        out.append(indent(body, 24))
        out.append('                    </div>')
        out.append('                </details>')
        out.append('            </li>')
    out.append('        </ol>')
    if tips:
        out.append('        <div class="savjeti">')
        out.append('            <h3>Opći savjeti i prečaci</h3>')
        out.append('            <ul>')
        for t in tips:
            out.append(f'                <li>{t.strip()}</li>')
        out.append('            </ul>')
        out.append('        </div>')
    out.append('    </section>')
    return '\n'.join(out) + '\n'


NO_EDITORIAL = ('    <div class="nema-rjesenja">\n'
                '        <h2>RJEŠENJE</h2>\n'
                '        <p>Za ovaj zadatak službeno rješenje nije objavljeno (u službenom je materijalu označeno kao '
                '<em>TBD</em>), pa prijevod rješenja nije dostupan. Naputci i koraci trenerskog načina, ako postoje, '
                'temelje se samo na tekstu zadatka.</p>\n'
                '    </div>\n')


NO_EDITORIAL_STAGE = ('    <div class="nema-rjesenja">\n'
                      '        <h2>RJEŠENJE</h2>\n'
                      '        <p>Organizatori za ovaj stage nisu objavili službena rješenja (editorial), pa je za sada '
                      'dostupan samo prijevod teksta zadatka. Rješenje će biti dodano naknadno.</p>\n'
                      '    </div>\n')


def code_path(stage, p):
    if p.get('code'):
        return os.path.join(SOLUTIONS, p['code'])
    return os.path.join(SOLUTIONS, f'stage{stage["no"]}', p['letter'], 'sol.cpp')


def render_code(path):
    with open(path) as f:
        src = f.read().rstrip('\n') + '\n'
    return ['                <details class="spoiler kod-spoiler">',
            '                    <summary>KOD (C++)<span class="spoiler-napomena">klikni za prikaz izvornog koda</span></summary>',
            '                    <div class="spoiler-sadrzaj">',
            '<pre><code class="language-cpp">' + htmllib.escape(src, quote=False) + '</code></pre>',
            '                    </div>',
            '                </details>']


def render_solution(stage, p):
    solution = p['solution']
    if solution is None:
        return NO_EDITORIAL_STAGE if stage.get('no_editorial') else NO_EDITORIAL
    detailed = p.get('detailed')
    out = ['    <details class="spoiler rjesenje-spoiler">',
           '        <summary>RJEŠENJE<span class="spoiler-napomena">klikni za prikaz cijelog rješenja</span></summary>',
           '        <div class="spoiler-sadrzaj">',
           '            <div class="rjesenje">',
           '                <p class="trener-napomena">Savjet: prije čitanja rješenja prođi kroz korake trenerskog načina iznad.</p>']
    if stage.get('community'):
        out.append(f'                <p class="zajednica-napomena"><em>{COMMUNITY_NOTE}</em></p>')
    if detailed:
        out += ['                <div class="rjesenje-sazeto ima-detaljno">',
                indent(solution, 20),
                '                </div>',
                '                <div class="rjesenje-detaljno">',
                '                    <h2>DETALJNO RJEŠENJE</h2>',
                indent(detailed, 20)]
        if p.get('verified'):
            out.append(f'                    <p class="provjera"><strong>Provjera koda:</strong> {p["verified"].strip()}</p>')
        out += [line if line.startswith('<pre>') else '    ' + line for line in render_code(code_path(stage, p))]
        out.append('                </div>')
    else:
        out += ['                <div class="rjesenje-sazeto">',
                f'                    <p class="detaljno-napomena">{NO_DETAILED_NOTE}</p>',
                indent(solution, 20),
                '                </div>']
    out += ['            </div>',
            '        </div>',
            '    </details>']
    return '\n'.join(out) + '\n'


def render_body(stage, nav_html, statement_html, p, source_html):
    parts = [nav_html]
    if statement_html:
        parts += ['', statement_html]
    parts += ['', '    <hr>', '']
    for block in (render_hints(p.get('hints', [])), render_coach(p.get('coach', []), p.get('tips', [])),
                  render_solution(stage, p),
                  '    <div class="izvor">\n        <h3>Izvor</h3>\n' + indent(source_html, 8) + '\n    </div>\n'):
        if block:
            parts.append(block)
    return '\n'.join(parts)


def render_problem(stage, p):
    title = f"{p['letter']}. {p['title']}"
    head = (
        '<!DOCTYPE html>\n<html lang="hr">\n<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'    <title>{title}</title>\n\n' + MATHJAX + HEAD_TAIL + '</head>\n\n<body>\n'
    )
    nav = (f'    <!-- NAVIGACIJA -->\n    <p><a href="index.html">← Natrag na popis zadataka</a> · '
           f'<a href="{ROOT}index.html">Početna</a></p>')
    intro = (f"<p><i>{p['title_hr']}</i> — The 1st Universal Cup, {stage['name']} ({stage['source_name']}). "
             f"Vremensko ograničenje: {p['tl']}, memorijsko ograničenje: {p['ml']}.</p>")
    statement = ('    <div class="zadatak">\n'
                 f"        <h1>ZADATAK {p['letter']}: {p['title']}</h1>\n"
                 f'        {intro}\n' + indent(p['statement'], 8) + '\n    </div>')
    source = p.get('source') or stage['source_html']
    body = render_body(stage, nav, statement, p, source)
    return head + body + '\n</body>\n</html>\n'


def render_index(stage, problems):
    cards = []
    for p in problems:
        badge = render_no_editorial_badge() if p['solution'] is None else ''
        cards.append(
            f'        <a href="{p["slug"]}.html" class="kucica-mape">\n'
            '            <span class="strelica">➔</span>\n'
            f'            <span class="naslov-kucice">{p["letter"]}. {p["title"]}</span>\n'
            + render_stats(stage['no'], p['letter']) + badge +
            '        </a>\n')
    return (
        '<!DOCTYPE html>\n<html lang="hr">\n<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'    <title>1st Universal Cup — {stage["name"]}</title>\n'
        f'    <link rel="stylesheet" href="{ROOT}assets/css/mapa.css">\n'
        f'    <link rel="stylesheet" href="{ROOT}assets/css/pozadina.css">\n'
        f'    <link rel="stylesheet" href="{ROOT}assets/css/trener.css">\n'
        f'    <script src="{ROOT}assets/js/coach-mode.js"></script>\n'
        f'    <script src="{ROOT}assets/js/detailed-mode.js"></script>\n'
        '</head>\n<body>\n\n'
        f'    <h1>{stage["name"]}</h1>\n\n'
        '    <p><a href="../index.html">← Natrag</a></p>\n\n'
        '    <div class="mreza-mapa">\n\n' + '\n'.join(cards) + '\n    </div>\n\n</body>\n</html>\n'
    )


def check_problem(stage, p):
    problems = []
    for key in ('letter', 'title', 'title_hr', 'slug', 'tl', 'ml', 'statement'):
        if not p.get(key):
            problems.append(f'missing {key}')
    if 'solution' not in p:
        problems.append('missing solution key')
    has_solution = p.get('solution') is not None
    if has_solution and len(p.get('hints', [])) < 2:
        problems.append('fewer than 2 hints')
    if has_solution and len(p.get('coach', [])) < 3:
        problems.append('fewer than 3 coach steps')
    if p.get('detailed'):
        if not p.get('solution'):
            problems.append('detailed without solution')
        if not os.path.exists(code_path(stage, p)):
            problems.append('missing code file ' + os.path.relpath(code_path(stage, p), HERE))
        if not p.get('verified'):
            problems.append('missing verified')
        if not p.get('tips'):
            problems.append('missing tips')
        if len(p['detailed']) < 2 * len(p['solution']):
            problems.append('detailed is not substantially longer than solution')
    if p.get('tips'):
        for t, b in p.get('coach', []):
            if not t.rstrip().endswith('?'):
                problems.append(f'coach step is not a question: {t[:40]}')
        if len(p.get('coach', [])) < 3:
            problems.append('fewer than 3 coach steps')
    for name, html in [('statement', p.get('statement', '')), ('solution', p.get('solution') or ''),
                       ('detailed', p.get('detailed') or '')] + \
            [(f'hint{i}', h) for i, h in enumerate(p.get('hints', []))] + \
            [(f'tip{i}', h) for i, h in enumerate(p.get('tips', []))] + \
            [(f'coach{i}', b) for i, (t, b) in enumerate(p.get('coach', []))]:
        for tag in ('p', 'ul', 'ol', 'li', 'pre', 'div'):
            if html.count(f'<{tag}>') + html.count(f'<{tag} ') != html.count(f'</{tag}>'):
                problems.append(f'{name}: unbalanced <{tag}>')
        if html.count('$') % 2 == 1:
            problems.append(f'{name}: odd number of $')
    return problems


def build(stage_no):
    mod = importlib.import_module(f'content.stage{stage_no}')
    stage, problems = mod.STAGE, mod.PROBLEMS
    outdir = os.path.join(REPO, 'prijevodi', 'ucup', '1st', f'stage{stage_no}')
    os.makedirs(outdir, exist_ok=True)
    ok = True
    for p in problems:
        errs = check_problem(stage, p)
        if errs:
            ok = False
            print(f'stage{stage_no} {p["letter"]}: ' + '; '.join(errs))
    for p in problems:
        with open(os.path.join(outdir, p['slug'] + '.html'), 'w') as f:
            f.write(render_problem(stage, p))
    with open(os.path.join(outdir, 'index.html'), 'w') as f:
        f.write(render_index(stage, problems))
    print(f'stage{stage_no}: wrote {len(problems)} problems' + ('' if ok else '  (WITH WARNINGS)'))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for arg in sys.argv[1:]:
        build(arg)
