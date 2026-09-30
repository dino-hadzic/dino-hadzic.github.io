# Brute force: za svaki d oznacimo vidikovce i provjerimo put svakog lista do korijena.
import sys
sys.setrecursionlimit(10000)
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n = int(d[p]); p += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = int(d[p]), int(d[p+1]); p += 2
        adj[a].append(b); adj[b].append(a)
    par = [0] * (n + 1); order = [1]; par[1] = -1
    for v in order:
        for w in adj[v]:
            if w != par[v]: par[w] = v; order.append(w)
    sz = [1] * (n + 1)
    for v in reversed(order):
        if v != 1: sz[par[v]] += sz[v]
    leaves = [v for v in range(2, n + 1) if len(adj[v]) == 1]
    res = []
    for dd in range(1, n + 1):
        ok = True
        for l in leaves:
            v = l; hit = False
            while v != -1:
                if sz[v] == dd: hit = True; break
                v = par[v]
            if not hit: ok = False; break
        if ok: res.append(dd)
    out.append(str(len(res))); out.append(' '.join(map(str, res)))
print('\n'.join(out))
