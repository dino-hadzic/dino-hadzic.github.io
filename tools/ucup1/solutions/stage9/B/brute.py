# Brute force: za svaki brid ga ukloni, nadi komponente i zbroji najcesce vrijednosti.
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); p += 2
    a = [int(x) for x in data[p:p+n]]; p += n
    E = []
    for i in range(m):
        E.append((int(data[p]) - 1, int(data[p+1]) - 1)); p += 2
    res = []
    for skip in range(m):
        par = list(range(n))
        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        for i, (u, v) in enumerate(E):
            if i != skip: par[find(u)] = find(v)
        comps = {}
        for v in range(n):
            comps.setdefault(find(v), []).append(a[v])
        tot = 0
        for vals in comps.values():
            tot += max(vals.count(x) for x in set(vals))
        res.append(tot)
    out.append(' '.join(map(str, res)))
print('\n'.join(out))
