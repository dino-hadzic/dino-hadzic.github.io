# Iscrpno: sve kombinacije k izbacenih pozicija u [l, r], gcd ostatka.
import sys
from itertools import combinations
from math import gcd
data = sys.stdin.read().split(); p = 0
n, q = int(data[0]), int(data[1]); p = 2
a = [0] + [int(x) for x in data[p:p + n]]; p += n
out = []
for _ in range(q):
    l, r, k = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    best = 0
    for rem in combinations(range(l, r + 1), k):
        g = 0
        for i in range(l, r + 1):
            if i not in rem:
                g = gcd(g, a[i])
        best = max(best, g)
    out.append(best)
print('\n'.join(map(str, out)))
