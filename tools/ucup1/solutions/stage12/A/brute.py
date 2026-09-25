import sys
from itertools import product

def main():
    data = sys.stdin.read().split()
    n = int(data[0]); a = [0] + [int(x) for x in data[1:1 + n]]
    g = [[] for _ in range(n + 1)]
    p = 1 + n
    for _ in range(n - 1):
        u, v = int(data[p]), int(data[p + 1]); p += 2
        g[u].append(v); g[v].append(u)
    par = [0] * (n + 1); par[1] = -1
    order = [1]
    for v in order:
        for u in g[v]:
            if u != par[v]:
                par[u] = v; order.append(u)
    leaves = [v for v in range(2, n + 1) if len(g[v]) == 1]
    paths = []
    for x in leaves:
        s = set(); v = x
        while v != -1:
            s.add(v); v = par[v]
        paths.append(s)
    best = 0
    for mask in product([0, 1], repeat=len(leaves)):
        col = a[:]
        for i, m in enumerate(mask):
            if m:
                for v in paths[i]:
                    col[v] ^= 1
        best = max(best, sum(col[1:]))
    print(best)

main()
