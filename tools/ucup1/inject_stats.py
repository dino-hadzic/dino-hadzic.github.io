"""Ubaci/obnovi statistiku (rješivost + QOJ ocjena) i oznaku "!" na karticama svih stage indexa.

Idempotentno: postojeći <span class="statistika"> i stara oznaka "!" se zamjenjuju.
Usage: python3 inject_stats.py            (svi stageovi 1-22)
       python3 inject_stats.py 8 10
"""
import os
import re
import sys

from cards import render_no_editorial_badge, render_stage_stats, render_stats

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
UCUP = os.path.join(REPO, 'prijevodi', 'ucup', '1st')

CARD_RE = re.compile(r'( *)<a href="([^"]+)" class="kucica-mape">\n(.*?)\n\s*</a>\n', re.S)
STATS_RE = re.compile(r'\s*<span class="statistika">.*?</span></span>\n?', re.S)
BADGE_RE = re.compile(r'\s*<span class="oznaka-nema-rjesenja"[^>]*>!</span>\n?', re.S)
LETTER_RE = re.compile(r'<span class="naslov-kucice">([A-Z]{1,2})\. ')
STAGE_HREF_RE = re.compile(r'^stage(\d+)/index\.html$')


def rewrite(stage_no, html):
    def card(m):
        pad, href, inner = m.group(1), m.group(2), m.group(3)
        has_badge = bool(BADGE_RE.search(inner))
        inner = STATS_RE.sub('\n', inner)
        inner = BADGE_RE.sub('\n', inner).rstrip('\n')
        lm = LETTER_RE.search(inner)
        letter = lm.group(1) if lm else None
        tail = ''
        if letter:
            tail += render_stats(stage_no, letter, indent=pad + '    ')
        if has_badge:
            tail += render_no_editorial_badge(indent=pad + '    ')
        return f'{pad}<a href="{href}" class="kucica-mape">\n{inner}\n{tail}{pad}</a>\n'

    return CARD_RE.sub(card, html)


def rewrite_root(html):
    """Kartice stageova na početnoj stranici UCupa: ocjena stagea + postojeća oznaka "!" (s vlastitim tekstom)."""
    def card(m):
        pad, href, inner = m.group(1), m.group(2), m.group(3)
        sm = STAGE_HREF_RE.match(href)
        if not sm:
            return m.group(0)
        bm = BADGE_RE.search(inner)
        badge = bm.group(0).strip('\n') + '\n' if bm else ''
        inner = STATS_RE.sub('\n', inner)
        inner = BADGE_RE.sub('\n', inner).rstrip('\n')
        tail = render_stage_stats(int(sm.group(1)), indent=pad + '    ') + badge
        return f'{pad}<a href="{href}" class="kucica-mape">\n{inner}\n{tail}{pad}</a>\n'

    return CARD_RE.sub(card, html)


def main_root():
    path = os.path.join(UCUP, 'index.html')
    html = open(path, encoding='utf-8').read()
    new = rewrite_root(html)
    if new != html:
        open(path, 'w', encoding='utf-8').write(new)
    print('root:', new.count('aria-label="Ocjena stagea'), 'stage cards with rating')


def main(stages):
    for s in stages:
        path = os.path.join(UCUP, f'stage{s}', 'index.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        if 'kucica-mape' not in html:
            continue
        new = rewrite(s, html)
        n = new.count('class="statistika"')
        if new != html:
            open(path, 'w', encoding='utf-8').write(new)
        print(f'stage{s}: {n} cards with stats')


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or range(1, 23))
    if len(sys.argv) == 1:
        main_root()
