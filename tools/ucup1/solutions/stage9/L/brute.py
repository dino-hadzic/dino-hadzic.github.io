# Brute force: nabroji sve skupove od m bridova na n vrhova i provjeri je li graf podgraf ciklusa
# (svi stupnjevi <= 2 i nema ciklusa, osim ako je to jedan Hamiltonov ciklus).
import sys, itertools
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
MOD = 10**9 + 7
for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); p += 2
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    cnt = 0
    if m <= len(edges):
        for sub in itertools.combinations(edges, m):
            deg = [0] * n
            par = list(range(n))
            def find(x):
                while par[x] != x:
                    par[x] = par[par[x]]; x = par[x]
                return x
            ok = True; cyc = 0
            for u, v in sub:
                deg[u] += 1; deg[v] += 1
                a, b = find(u), find(v)
                if a == b: cyc += 1
                else: par[a] = b
            if max(deg + [0]) > 2: ok = False
            if cyc > 1: ok = False
            if cyc == 1 and m != n: ok = False   # ciklus mora biti Hamiltonov
            if ok: cnt += 1
    out.append(str(cnt % MOD))
print('\n'.join(out))
