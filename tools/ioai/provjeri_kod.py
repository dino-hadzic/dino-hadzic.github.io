#!/usr/bin/env python3
"""Pokreće sve <kod jezik="python"> blokove lekcija IOAI i uspoređuje ispis s <izlaz>.

Pokretanje:  python3 tools/ioai/provjeri_kod.py [--ispisi] [content/<oblast>/<slug>.html ...]
  bez argumenata: sve lekcije iz manifesta
  --ispisi:       umjesto usporedbe ispiši stvarni ispis svakog bloka (za lijepljenje u <izlaz>)
  --upisi:        prazne <izlaz></izlaz> blokove popuni stvarnim ispisom (datoteka se prepisuje)

Pravila:
  * blokovi jedne lekcije izvršavaju se redom u ISTOM procesu (kao ćelije bilježnice),
    u privremenoj mapi, s MPLBACKEND=Agg; vremensko ograničenje je 15 min po lekciji
  * <kod jezik="python" pokreni="ne"> se preskače (npr. pip install, pseudokod, kod za GPU)
  * <izlaz> koji slijedi odmah iza bloka je očekivani ispis tog bloka (usporedba bez
    završnih razmaka u retku); <izlaz provjera="ne"> se ne uspoređuje (nedeterministički ispis)
"""
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
KOD_RE = re.compile(r'<kod\b([^>]*)>\n?(.*?)</kod>(\s*<izlaz\b([^>]*)>\n?(.*?)</izlaz>)?', re.S)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
MARK = '\n@@BLOK@@\n'


def attrs(s):
    return dict(ATTR_RE.findall(s))


def blocks(path):
    text = open(path, encoding='utf-8').read()
    out = []
    for m in KOD_RE.finditer(text):
        a = attrs(m.group(1))
        if a.get('jezik', 'python') != 'python' or a.get('pokreni') == 'ne':
            continue
        line = text.count('\n', 0, m.start()) + 1
        izlaz = m.group(5)
        provjera = m.group(3) is not None and attrs(m.group(4) or '').get('provjera') != 'ne'
        out.append((line, m.group(2).rstrip('\n'), (izlaz or '').rstrip(), provjera))
    return out


def norm(s):
    return '\n'.join(l.rstrip() for l in s.strip('\n').split('\n'))


def upisi(path, bl, parts):
    """Prazne <izlaz> blokove zamijeni stvarnim ispisom pripadnog bloka koda."""
    text = open(path, encoding='utf-8').read()
    out, pos, k, n = [], 0, 0, 0
    for m in KOD_RE.finditer(text):
        a = attrs(m.group(1))
        if a.get('jezik', 'python') != 'python' or a.get('pokreni') == 'ne':
            continue
        if m.group(3) is not None and not m.group(5).strip() and k < len(parts):
            got = norm(parts[k])
            out.append(text[pos:m.start(3)])
            out.append('\n<izlaz>\n' + html_escape_free(got) + '\n</izlaz>')
            pos = m.end(3)
            n += 1
        k += 1
    out.append(text[pos:])
    open(path, 'w', encoding='utf-8').write(''.join(out))
    print(f'{path}: upisano {n} ispisa')


def html_escape_free(s):
    # <izlaz> je sirovi tekst; generator ga escapea, pa ovdje ništa ne mijenjamo
    return s


def run(path, ispisi, upisi_=False):
    bl = blocks(path)
    if not bl:
        print(f'{path}: nema koda')
        return True
    script = []
    for line, src, _, _ in bl:
        script.append(f'print({MARK!r}, end="")\n' + src + '\n')
    with tempfile.TemporaryDirectory() as tmp:
        sp = os.path.join(tmp, 'lekcija.py')
        open(sp, 'w', encoding='utf-8').write(''.join(script))
        env = dict(os.environ, MPLBACKEND='Agg', PYTHONHASHSEED='0', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
        try:
            r = subprocess.run([sys.executable, sp], cwd=tmp, env=env, capture_output=True, text=True, timeout=900)
        except subprocess.TimeoutExpired:
            print(f'{path}: KOD PREDUGO TRAJE (>15 min)')
            return False
    parts = r.stdout.split(MARK)[1:]
    ok = r.returncode == 0
    if not ok:
        print(f'{path}: GREŠKA pri izvršavanju (blok {len(parts)} od {len(bl)}, redak {bl[min(len(parts), len(bl)) - 1][0]}):')
        print('  ' + r.stderr.strip().replace('\n', '\n  ')[-3000:])
    if upisi_ and ok:
        upisi(path, bl, parts)
        return True
    for k, (line, src, izlaz, provjera) in enumerate(bl):
        got = norm(parts[k]) if k < len(parts) else ''
        if ispisi:
            print(f'--- {path} blok {k + 1} (redak {line}) ---')
            print(got)
            continue
        if k >= len(parts):
            break
        if provjera and norm(izlaz) != got:
            ok = False
            print(f'{path}: ISPIS SE RAZLIKUJE, blok {k + 1} (redak {line})')
            print('  očekivano:\n    ' + norm(izlaz).replace('\n', '\n    '))
            print('  dobiveno:\n    ' + got.replace('\n', '\n    '))
    if ok and not ispisi:
        print(f'{path}: {len(bl)} blokova OK')
    return ok


def main():
    argv = sys.argv[1:]
    ispisi = '--ispisi' in argv
    upisi_ = '--upisi' in argv
    files = [a for a in argv if not a.startswith('--')]
    if not files:
        for o in MANIFEST['oblasti']:
            for slug in o['lekcije']:
                p = os.path.join(HERE, 'content', o['slug'], f'{slug}.html')
                if os.path.exists(p):
                    files.append(p)
    ok = True
    for f in files:
        ok = run(f, ispisi, upisi_) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
