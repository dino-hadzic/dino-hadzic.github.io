#!/usr/bin/env python3
# Brute force: isprobaj sve kombinacije glasova sudaca; za svaki ishod
# skup S je moguć ako je min bodova u S >= max bodova izvan S.
import sys
from itertools import combinations, product
MOD = 998244353
data = sys.stdin.read().split()
pos = 0
t = int(data[pos]); pos += 1
out = []
for _ in range(t):
    n, m, v = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
    a = [int(x) for x in data[pos:pos + n]]; pos += n
    subsets = list(combinations(range(n), v))
    ok = set()
    for votes in product(subsets, repeat=m):
        b = a[:]
        for s in votes:
            for i in s:
                b[i] += 1
        for mask in range(1, 1 << n):
            lo = min(b[i] for i in range(n) if mask >> i & 1)
            hi = max([b[i] for i in range(n) if not mask >> i & 1], default=-1)
            if lo >= hi:
                ok.add(mask)
    out.append(str(len(ok) % MOD))
print('\n'.join(out))
