# Brute force: DFS po svim stazama (svaki brid najviše jednom) od (1,1) do (n,n); ispisuje samo l.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    edges = []
    for kind in range(3):
        for i in range(1, n):
            for j in range(1, i + 1):
                w = int(data[p]); p += 1
                if kind == 0: edges.append(((i, j), (i + 1, j), w))
                elif kind == 1: edges.append(((i, j), (i + 1, j + 1), w))
                else: edges.append(((i + 1, j), (i + 1, j + 1), w))
    adj = {}
    for idx, (a, b, w) in enumerate(edges):
        adj.setdefault(a, []).append((idx, b, w)); adj.setdefault(b, []).append((idx, a, w))
    used = [False] * len(edges)
    best = [0]
    def dfs(u, l):
        if u == (n, n): best[0] = max(best[0], l)
        for idx, v, w in adj[u]:
            if not used[idx]:
                used[idx] = True; dfs(v, l + w); used[idx] = False
    dfs((1, 1), 0)
    out.append(str(best[0]))
print('\n'.join(out))
