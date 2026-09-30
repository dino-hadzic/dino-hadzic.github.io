# Brute force: iscrpno po podskupovima puteva; put = skup bridova (preko roditelja u ukorijenjenom stablu).
import sys
from itertools import combinations
data = sys.stdin.read().split()
n, m, k = int(data[0]), int(data[1]), int(data[2]); p = 3
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = int(data[p]), int(data[p + 1]); p += 2
    adj[x].append(y); adj[y].append(x)
par = [0] * (n + 1); dep = [0] * (n + 1)
order = [1]; seen = {1}
for v in order:
    for w in adj[v]:
        if w not in seen:
            seen.add(w); par[w] = v; dep[w] = dep[v] + 1; order.append(w)
def edges(a, b):
    s = set()
    while a != b:
        if dep[a] < dep[b]: a, b = b, a
        s.add(a); a = par[a]          # brid (a, par[a]) označen djetetom a
    return s
paths = []
for _ in range(m):
    a, b, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    paths.append((edges(a, b), w))
best = 0
for r in range(1, m + 1):
    for sub in combinations(range(m), r):
        used = set(); ok = True; tot = 0
        for i in sub:
            e, w = paths[i]
            if used & e: ok = False; break
            used |= e; tot += w
        if ok: best = max(best, tot)
print(best)
