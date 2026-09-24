"""Zajednički HTML za desnu stranu kartice zadatka: statistika (rješivost + QOJ ocjena) i oznaka "!".

Koriste ga gen.py (novogenerirani stageovi) i inject_stats.py (postojeći index.html).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
STATS_PATH = os.path.join(HERE, 'content', 'stats.json')
STAGE_STATS_PATH = os.path.join(HERE, 'content', 'stage_stats.json')

_stats = None
_stage_stats = None


def stats():
    global _stats
    if _stats is None:
        _stats = json.load(open(STATS_PATH)) if os.path.exists(STATS_PATH) else {}
    return _stats


def stage_stats():
    global _stage_stats
    if _stage_stats is None:
        _stage_stats = json.load(open(STAGE_STATS_PATH)) if os.path.exists(STAGE_STATS_PATH) else {}
    return _stage_stats


# gornja granica udjela (u %) -> razred boje, od najteže do najlakše
RATE_CLASSES = [(2, 'rjesivost-1'), (10, 'rjesivost-2'), (25, 'rjesivost-3'), (50, 'rjesivost-4'), (101, 'rjesivost-5')]


def rate_class(pct):
    for limit, cls in RATE_CLASSES:
        if pct < limit:
            return cls
    return RATE_CLASSES[-1][1]


def fmt_pct(solved, teams):
    pct = 100.0 * solved / teams if teams else 0.0
    if 0 < pct < 1:
        return pct, '<1%'
    return pct, f'{round(pct)}%'


def fmt_score(z):
    if z > 0:
        return 'ocjena-plus', f'+{z}'
    if z < 0:
        return 'ocjena-minus', f'\u2212{-z}'
    return 'ocjena-nula', '0'


def render_stats(stage_no, letter, indent='            '):
    e = stats().get(str(stage_no), {}).get(letter)
    if not e or 'solved' not in e:
        return ''
    # nazivnik: timovi s barem jednim slanjem na natjecanju (ne svi prijavljeni timovi)
    denom = e.get('participated', e['teams'])
    pct, pct_txt = fmt_pct(e['solved'], denom)
    parts = [
        f'<span class="rjesivost {rate_class(pct)}" '
        f'data-tip="Riješilo {e["solved"]} od {denom} timova s barem jednim slanjem ({pct:.1f}%)" '
        f'aria-label="Rješivost {pct_txt}">{pct_txt}</span>'
    ]
    if 'zan' in e:
        cls, txt = fmt_score(e['zan'])
        parts.append(
            f'<span class="ocjena {cls}" '
            f'data-tip="QOJ ocjena zadatka: {txt} (palac gore \u2212 palac dolje)" '
            f'aria-label="Ocjena {txt}">{txt}</span>'
        )
    return f'{indent}<span class="statistika">' + ''.join(parts) + '</span>\n'


def render_stage_stats(stage_no, indent='            '):
    """Ocjena cijelog stagea (palac gore − palac dolje) za kartice stageova na početnoj stranici UCupa."""
    e = stage_stats().get(str(stage_no))
    if not e or 'zan' not in e:
        return ''
    cls, txt = fmt_score(e['zan'])
    return (f'{indent}<span class="statistika">'
            f'<span class="ocjena {cls}" '
            f'data-tip="QOJ ocjena stagea: {txt} (palac gore \u2212 palac dolje)" '
            f'aria-label="Ocjena stagea {txt}">{txt}</span></span>\n')


NO_EDITORIAL_TIP = 'Službeno rješenje (editorial) za ovaj UCup zadatak nije objavljeno'


def render_no_editorial_badge(indent='            ', tip=NO_EDITORIAL_TIP):
    return (f'{indent}<span class="oznaka-nema-rjesenja" data-tip="{tip}" '
            f'role="img" aria-label="{tip}">!</span>\n')
