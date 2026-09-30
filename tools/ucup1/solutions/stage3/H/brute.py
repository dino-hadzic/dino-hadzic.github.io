# Brute force: sve jednostavne staze 1 -> n, biramo najkracu, a medu njima onu sa
# leksikografski najvecim silazno sortiranim nizom duljina bridova.
import sys
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, m = int(d[p]), int(d[p+1]); p += 2
    adj = {v: [] for v in range(1, n + 1)}
    for _ in range(m):
        u, v, w = int(d[p]), int(d[p+1]), int(d[p+2]); p += 3
        adj[u].append((v, w)); adj[v].append((u, w))
    best = None
    def rec(v, path, ws, total):
        global best
        if v == n:
            key = (-total, sorted(ws, reverse=True))
            if best is None or key > best[0]: best = (key, list(path))
            return
        for w, c in adj[v]:
            if w not in path:
                path.append(w); ws.append(c); rec(w, path, ws, total + c); path.pop(); ws.pop()
    rec(1, [1], [], 0)
    out.append(str(len(best[1]))); out.append(' '.join(map(str, best[1])))
print('\n'.join(out))
