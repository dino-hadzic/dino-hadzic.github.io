"""Jednokratni uvoz ručno pisanih stranica (Stage 1, 2, 4–8, 10) u content/stageN.py,
kako bi se i te etape generirale iz gen.py. Naputci i trenerski koraci uzimaju se iz
content/retro_stageN.py.  Pokretanje: python3 import_legacy.py 1 2 4 5 6 7 8 10
"""
import importlib
import os
import re
import sys
from collections import Counter

import gen

HERE = os.path.dirname(os.path.abspath(__file__))


def lit(s):
    s = s.strip('\n')
    assert "'''" not in s and not s.endswith('\\'), s[:80]
    return "r'''\n" + s + "\n'''"


def parse_page(path):
    html = open(path).read()
    title = re.search(r'<title>([A-Z])\. (.*?)</title>', html)
    letter, ptitle = title.group(1), title.group(2)
    z = re.search(r'    <div class="zadatak">\n        <h1>ZADATAK (\w): (.*?)</h1>\n        (<p><i>(.*?)</i> — The 1st Universal Cup, '
                  r'(.*?) \((.*?)\)\. Vremensko ograničenje: (.*?), memorijsko ograničenje: (.*?)\.</p>)\n(.*?)\n    </div>\n', html, re.S)
    assert z, path
    assert z.group(1) == letter, path
    title_hr, stage_name, source_name, tl, ml, statement = z.group(4), z.group(5), z.group(6), z.group(7), z.group(8), z.group(9)
    statement = re.sub(r'^ {8}', '', statement, flags=re.M)
    s = re.search(r'            <div class="rjesenje">\n'
                  r'                <p class="trener-napomena">.*?</p>\n(.*?)\n            </div>\n        </div>\n    </details>\n', html, re.S)
    assert s, path
    solution = re.sub(r'^ {16}', '', s.group(1), flags=re.M)
    src = re.search(r'    <div class="izvor">\n        <h3>Izvor</h3>\n(.*?)\n    </div>\n', html, re.S)
    source = re.sub(r'^ {8}', '', src.group(1), flags=re.M)
    return {
        'letter': letter, 'title': ptitle, 'title_hr': title_hr, 'slug': os.path.basename(path)[:-5],
        'tl': tl, 'ml': ml, 'statement': statement, 'solution': solution, 'source': source,
        'stage_name': stage_name, 'source_name': source_name,
    }


def run(stage_no):
    d = os.path.join(gen.REPO, 'prijevodi', 'ucup', '1st', f'stage{stage_no}')
    extra = importlib.import_module(f'content.retro_stage{stage_no}').EXTRA
    pages = [parse_page(os.path.join(d, n)) for n in sorted(os.listdir(d)) if n.endswith('.html') and n != 'index.html']
    stage_name = Counter(p['stage_name'] for p in pages).most_common(1)[0][0]
    source_name = Counter(p['source_name'] for p in pages).most_common(1)[0][0]
    source_html = Counter(p['source'] for p in pages).most_common(1)[0][0]
    for p in pages:
        assert p['stage_name'] == stage_name, (p['slug'], p['stage_name'])
        assert p['source_name'] == source_name, (p['slug'], p['source_name'])
    out = ['"""1st Universal Cup – %s. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i' % stage_name,
           'trenerski koraci iz nekadašnjeg retro_stage%s.py."""' % stage_no, '',
           'STAGE = {', f'    \'no\': {stage_no},', f'    \'name\': {stage_name!r},', f'    \'source_name\': {source_name!r},',
           '    \'source_html\': ' + lit(source_html) + ',', '}', '', 'PROBLEMS = [']
    for p in pages:
        e = extra[p['slug'] + '.html']
        out.append('{')
        for k in ('letter', 'title', 'title_hr', 'slug', 'tl', 'ml'):
            out.append(f'    {k!r}: {p[k]!r},')
        out.append("    'statement': " + lit(p['statement']) + ',')
        out.append("    'hints': [")
        for h in e['hints']:
            out.append('        ' + lit(h) + ',')
        out.append('    ],')
        out.append("    'coach': [")
        for t, b in e['coach']:
            out.append(f'        ({t!r},')
            out.append('         ' + lit(b) + '),')
        out.append('    ],')
        out.append("    'solution': " + lit(p['solution']) + ',')
        if p['source'] != source_html:
            out.append("    'source': " + lit(p['source']) + ',')
        out.append('},')
    out.append(']')
    path = os.path.join(HERE, 'content', f'stage{stage_no}.py')
    with open(path, 'w') as f:
        f.write('\n'.join(out) + '\n')
    print(f'stage{stage_no}: {len(pages)} problems -> {os.path.relpath(path, HERE)}')


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    for a in sys.argv[1:]:
        run(a)
