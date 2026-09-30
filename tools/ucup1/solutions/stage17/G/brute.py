# Brute force: definicija zadatka bez ikakvih pretpostavki o strukturi.
# Duljina niza = najdulji put + 1, broj slova = broj izvora. Isprobamo sve
# kanonske nizove (slova po redoslijedu prvog pojavljivanja) u leksikografskom
# poretku, izgradimo DAG podnizova i provjerimo izomorfizam s ulaznim grafom
# (WL-profinjavanje boja + backtracking). Prvi pogodak je odgovor.
import sys
from itertools import product

sys.setrecursionlimit(10000)


def substr_dag(s):
    subs = set(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
    idx = {t: i for i, t in enumerate(sorted(subs, key=lambda t: (len(t), t)))}
    edges = set()
    for t in subs:
        if len(t) > 1:
            edges.add((idx[t[:-1]], idx[t]))
            edges.add((idx[t[1:]], idx[t]))
    return len(subs), edges


def colors(n, edges):
    pred = [[] for _ in range(n)]
    succ = [[] for _ in range(n)]
    for u, v in edges:
        succ[u].append(v)
        pred[v].append(u)
    col = [0] * n
    for _ in range(n + 1):
        sig = [(col[v], tuple(sorted(col[p] for p in pred[v])), tuple(sorted(col[q] for q in succ[v]))) for v in range(n)]
        uniq = {x: i for i, x in enumerate(sorted(set(sig)))}
        new = [uniq[x] for x in sig]
        if new == col:
            break
        col = new
    return col, pred, succ


def isomorphic(n, e1, e2):
    if len(e1) != len(e2):
        return False
    c1, p1, s1 = colors(n, e1)
    c2, p2, s2 = colors(n, e2)
    if sorted(c1) != sorted(c2):
        return False
    by_col = {}
    for v in range(n):
        by_col.setdefault(c2[v], []).append(v)
    order = sorted(range(n), key=lambda v: (len(p1[v]), c1[v]))  # po slojevima
    mp = [-1] * n
    used = [False] * n
    e2set = e2

    def bt(i):
        if i == n:
            return True
        u = order[i]
        for v in by_col[c1[u]]:
            if used[v]:
                continue
            ok = True
            for p in p1[u]:
                if mp[p] >= 0 and (mp[p], v) not in e2set:
                    ok = False
                    break
            if ok:
                for q in s1[u]:
                    if mp[q] >= 0 and (v, mp[q]) not in e2set:
                        ok = False
                        break
            if ok:
                mp[u] = v
                used[v] = True
                if bt(i + 1):
                    return True
                mp[u] = -1
                used[v] = False
        return False

    return bt(0)


def canonical_strings(L, k):
    # svi nizovi duljine L s točno k slova, slova po redoslijedu prvog pojavljivanja, leksikografski
    def rec(pref, mx):
        if len(pref) == L:
            if mx + 1 == k:
                yield ''.join(pref)
            return
        for c in range(min(mx + 2, k)):
            pref.append(chr(97 + c))
            yield from rec(pref, max(mx, c))
            pref.pop()
    yield from rec([], -1)


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    T = int(data[pos]); pos += 1
    out = []
    for _ in range(T):
        n, m = int(data[pos]), int(data[pos + 1]); pos += 2
        edges = set()
        for _ in range(m):
            u, v = int(data[pos]) - 1, int(data[pos + 1]) - 1; pos += 2
            edges.add((u, v))
        indeg = [0] * n
        succ = [[] for _ in range(n)]
        for u, v in edges:
            indeg[v] += 1
            succ[u].append(v)
        # duljina = najdulji put + 1 (topološki)
        dist = [0] * n
        order = [v for v in range(n) if indeg[v] == 0]
        k = len(order)
        rem = indeg[:]
        i = 0
        while i < len(order):
            u = order[i]; i += 1
            for v in succ[u]:
                dist[v] = max(dist[v], dist[u] + 1)
                rem[v] -= 1
                if rem[v] == 0:
                    order.append(v)
        L = max(dist) + 1
        ans = None
        for s in canonical_strings(L, k):
            cnt, e2 = substr_dag(s)
            if cnt != n or len(e2) != m:
                continue
            if isomorphic(n, edges, e2):
                ans = s
                break
        assert ans is not None
        out.append(ans)
    print('\n'.join(out))


main()
