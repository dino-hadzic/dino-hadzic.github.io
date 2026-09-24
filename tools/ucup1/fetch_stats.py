"""Dohvat statistike UCup 1 zadataka.

- contest.ucup.ac/contest/<id>/standings  -> broj timova koji su riješili zadatak / broj timova s barem
  jednim slanjem ("participated"); "teams" je ukupan broj timova na ljestvici (i bez slanja)
- contest.ucup.ac/contest/<id>           -> neto ocjena cijelog stagea (data-type="C"), u content/stage_stats.json
- contest.ucup.ac/contest/<cid>/problem/<id> -> neto ocjena (palac gore - palac dolje), tzv. "zan";
  ista vrijednost kao na qoj.ac/problem/<id> (zajednička baza), ali bez Cloudflarea i rate limita

Rezultat: content/stats.json  { "<stage>": { "<slovo>": {qoj, solved, teams, zan} } }
Usage: python3 fetch_stats.py [standings|zan|contest|all] [stage ...]
"""
import json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'content', 'stats.json')
OUT_STAGE = os.path.join(HERE, 'content', 'stage_stats.json')

# stage -> contest id na contest.ucup.ac (isti id vrijedi i za qoj.ac/contest)
CONTESTS = {
    1: 1096, 2: 1099, 3: 1103, 4: 1106, 5: 1111, 6: 1124, 7: 1129, 8: 1070,
    9: 1187, 10: 1195, 11: 1197, 12: 1207, 13: 1212, 14: 1214, 15: 1221,
    16: 1223, 17: 1244, 18: 1245, 19: 1248, 20: 1259, 21: 1277, 22: 1287,
}

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/133.0 Safari/537.36'


def load():
    if os.path.exists(OUT):
        return json.load(open(OUT))
    return {}


def save(stats):
    json.dump(stats, open(OUT, 'w'), indent=1, ensure_ascii=False, sort_keys=True)


def js_var(html, name):
    m = re.search(r'^' + name + r'=(.*);$', html, re.M)
    return json.loads(m.group(1))


def fetch_standings(stats):
    for stage, cid in CONTESTS.items():
        url = f'https://contest.ucup.ac/contest/{cid}/standings'
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        html = urllib.request.urlopen(req, timeout=60).read().decode()
        problems = js_var(html, 'problems')
        letters = js_var(html, 'problems_id')
        standings = js_var(html, 'standings')
        score = js_var(html, 'score')
        teams = [row[2][0] for row in standings]
        solved = [0] * len(problems)
        attempted = [0] * len(problems)
        participated = 0
        for t in teams:
            sc = score.get(t) or {}
            if isinstance(sc, list) or not sc:
                continue
            participated += 1
            for idx, rec in sc.items():
                attempted[int(idx)] += 1
                if rec[0] == 100:
                    solved[int(idx)] += 1
        st = stats.setdefault(str(stage), {})
        for i, (pid, letter) in enumerate(zip(problems, letters)):
            e = st.setdefault(letter, {})
            e.update({'qoj': pid, 'solved': solved[i], 'attempted': attempted[i],
                      'teams': len(teams), 'participated': participated})
        print(f'stage {stage:2d} (contest {cid}): {len(teams)} teams, {participated} with submissions, '
              + ' '.join(f'{l}={s}' for l, s in zip(letters, solved)))
        save(stats)
        time.sleep(1)


def fetch_zan(stats, only=None):
    """Neto ocjena (palac gore - palac dolje). qoj.ac i contest.ucup.ac dijele bazu zadataka pa je
    data-cnt isti; ucup nema Cloudflare ni strogi rate limit, zato se čita odande."""
    for stage in sorted(stats, key=int):
        if only and int(stage) not in only:
            continue
        cid = CONTESTS[int(stage)]
        for letter, e in stats[stage].items():
            if 'zan' in e:
                continue
            url = f'https://contest.ucup.ac/contest/{cid}/problem/{e["qoj"]}'
            for attempt in range(5):
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': UA})
                    html = urllib.request.urlopen(req, timeout=60).read().decode()
                    if 'Too many requests' in html:
                        print('  rate limited, waiting 120 s')
                        time.sleep(120)
                        continue
                    m = re.search(r'uoj-click-zan-block[^>]*data-type="P"[^>]*data-cnt="(-?\d+)"', html)
                    if m:
                        e['zan'] = int(m.group(1))
                        break
                    print('  no zan on', url)
                    time.sleep(10)
                except Exception as ex:
                    print('  ERR', url, ex)
                    time.sleep(10)
            print(f'stage {stage} {letter} qoj {e["qoj"]}: zan={e.get("zan")}')
            save(stats)
            time.sleep(1.5)


def fetch_contest_zan():
    """Neto ocjena cijelog stagea (contest), isti zan-blok kao za zadatke, data-type=\"C\"."""
    out = json.load(open(OUT_STAGE)) if os.path.exists(OUT_STAGE) else {}
    for stage, cid in CONTESTS.items():
        url = f'https://contest.ucup.ac/contest/{cid}'
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        html = urllib.request.urlopen(req, timeout=60).read().decode()
        m = re.search(r'data-id="%d" data-type="C" data-val="-?\d+" data-cnt="(-?\d+)"' % cid, html)
        if not m:
            print(f'stage {stage}: no contest zan on {url}')
            continue
        out[str(stage)] = {'contest': cid, 'zan': int(m.group(1))}
        print(f'stage {stage:2d} (contest {cid}): zan={m.group(1)}')
        time.sleep(1)
    json.dump(out, open(OUT_STAGE, 'w'), indent=1, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    stats = load()
    if what in ('standings', 'all'):
        fetch_standings(stats)
    if what in ('zan', 'all'):
        fetch_zan(stats, [int(a) for a in sys.argv[2:]])
    if what in ('contest', 'all'):
        fetch_contest_zan()
    save(stats)
