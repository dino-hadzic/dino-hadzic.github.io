"""Skini najkraće AC predaje s qoj.ac za zadane zadatke (samo čitanje, ništa se ne predaje).

Usage: python3 fetch_ac.py <qoj_problem_id> [...]     ili    python3 fetch_ac.py --stage 3 9
Sprema u subs/<pid>/<sid>.<ext> + subs/<pid>/meta.json. Pretpostavlja da je Chrome (CDP :29229) već prijavljen.
"""
import html as htmllib
import json
import os
import re
import sys
import time

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SUBS = os.path.join(HERE, 'subs')
STATS = os.path.join(HERE, '..', 'content', 'stats.json')
PER_PROBLEM = 6      # koliko predaja skinuti
LIST_PAGES = 3       # koliko stranica popisa pregledati (20 po stranici)
DELAY = 4

EXT = {'C++': 'cpp', 'C': 'c', 'Python': 'py', 'Java': 'java', 'Rust': 'rs', 'Kotlin': 'kt', 'Pascal': 'pas'}


def size_bytes(s):
    m = re.match(r'([\d.]+)\s*(b|kb|mb)', s.lower())
    if not m:
        return 10 ** 9
    v = float(m.group(1))
    return int(v * {'b': 1, 'kb': 1024, 'mb': 1024 ** 2}[m.group(2)])


def goto(pg, url):
    pg.goto(url, wait_until='domcontentloaded', timeout=60000)
    for _ in range(40):
        if 'Just a moment' not in pg.title():
            break
        time.sleep(1)
    time.sleep(DELAY)
    h = pg.content()
    if 'Too many requests' in h:
        print('  rate limited, sleeping 120 s')
        time.sleep(120)
        return goto(pg, url)
    if pg.url.rstrip('/').endswith('/login'):
        raise SystemExit('not logged in')
    return h


def list_ac(pg, pid):
    rows = []
    for page in range(1, LIST_PAGES + 1):
        h = goto(pg, f'https://qoj.ac/submissions?problem_id={pid}&min_score=100&max_score=100&page={page}')
        for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', h, re.S):
            sm = re.search(r'href="/submission/(\d+)"', tr)
            if not sm:
                continue
            cells = [re.sub(r'\s+', ' ', htmllib.unescape(re.sub(r'<[^>]+>', ' ', c))).strip()
                     for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
            if len(cells) < 8 or 'AC' not in cells[3]:
                continue
            rows.append({'sid': int(sm.group(1)), 'who': cells[2], 'time': cells[4], 'mem': cells[5],
                         'lang': cells[6], 'size': cells[7], 'bytes': size_bytes(cells[7])})
        if 'page=%d' % (page + 1) not in h:
            break
    seen, out = set(), []
    for r in rows:
        if r['sid'] not in seen:
            seen.add(r['sid'])
            out.append(r)
    return out


def get_code(pg, sid):
    h = goto(pg, f'https://qoj.ac/submission/{sid}')
    m = re.search(r'<pre class="sh_sourceCode">(.*?)</pre>', h, re.S)
    if not m:
        return None   # kod skriven (privatna predaja)
    return htmllib.unescape(re.sub(r'<[^>]+>', '', m.group(1)))


def fetch_problem(pg, pid):
    d = os.path.join(SUBS, str(pid))
    os.makedirs(d, exist_ok=True)
    meta_path = os.path.join(d, 'meta.json')
    if os.path.exists(meta_path):
        print(pid, 'already fetched')
        return
    rows = list_ac(pg, pid)
    # prednost: C++ i kraći kod (obično najčitljiviji), ali uzmi i jednu najbržu
    cpp = sorted([r for r in rows if r['lang'].startswith('C++')], key=lambda r: r['bytes'])
    fastest = sorted(rows, key=lambda r: int(re.sub(r'\D', '', r['time']) or 10 ** 9))
    order = fastest[:1] + cpp + [r for r in rows if r not in cpp]
    pick, hidden = [], 0
    for r in order:
        if r in pick:
            continue
        if len(pick) >= PER_PROBLEM:
            break
        code = get_code(pg, r['sid'])
        if code is None:
            hidden += 1
            continue
        ext = next((e for k, e in EXT.items() if r['lang'].startswith(k)), 'txt')
        open(os.path.join(d, f'{r["sid"]}.{ext}'), 'w').write(code)
        r['file'] = f'{r["sid"]}.{ext}'
        pick.append(r)
    json.dump({'pid': pid, 'total_ac_seen': len(rows), 'hidden_code': hidden, 'picked': pick},
              open(meta_path, 'w'), indent=1, ensure_ascii=False)
    print(pid, f'{len(rows)} AC seen, saved {len(pick)}, hidden {hidden}', flush=True)


def main(argv):
    pids = []
    if argv and argv[0] == '--stage':
        stats = json.load(open(STATS))
        for s in argv[1:]:
            pids += [e['qoj'] for e in stats[s].values()]
    else:
        pids = [int(a) for a in argv]
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp('http://localhost:29229')
        pg = b.contexts[0].new_page()
        for pid in pids:
            fetch_problem(pg, pid)
        pg.close()


if __name__ == '__main__':
    main(sys.argv[1:])
