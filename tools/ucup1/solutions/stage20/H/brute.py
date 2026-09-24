# Brute force: nabrojimo sva glasanja (svaki ne-korijen bira jednog od svojih strogih predaka)
# i zabiljezimo tko je bio jedini pobjednik.
import sys, itertools
data = sys.stdin.read().split(); T = int(data[0]); p = 1
for _ in range(T):
    n = int(data[p]); p += 1
    par = [0, 0] + [int(x) for x in data[p:p+n-1]]; p += n - 1
    anc = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        u = par[v]
        while u:
            anc[v].append(u); u = par[u]
    can = [False] * (n + 1)
    for choice in itertools.product(*[anc[v] for v in range(2, n + 1)]):
        cnt = [0] * (n + 1)
        for c in choice: cnt[c] += 1
        mx = max(cnt)
        if cnt.count(mx) == 1: can[cnt.index(mx)] = True
    print("".join('1' if can[v] else '0' for v in range(1, n + 1)))
