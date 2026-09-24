# Sve permutacije cudovista (n <= 8), provjera valjanosti i izravna simulacija HP-a.
import sys, itertools
data = sys.stdin.read().split(); pos = 0
n, m = int(data[pos]), int(data[pos + 1]); pos += 2
a = [0] * (n + 1); b = [0] * (n + 1)
for v in range(2, n + 1):
    a[v], b[v] = int(data[pos]), int(data[pos + 1]); pos += 2
ulaz = [set() for _ in range(n + 1)]
for _ in range(m):
    u, v = int(data[pos]), int(data[pos + 1]); pos += 2
    ulaz[v].add(u)
best = None
for perm in itertools.permutations(range(2, n + 1)):
    porazeni = {1}; ok = True; cur = 0; need = 0
    for v in perm:
        if not (ulaz[v] & porazeni): ok = False; break
        need = max(need, a[v] - cur); cur += b[v] - a[v]; porazeni.add(v)
    if ok and (best is None or need < best): best = need
print(best)
