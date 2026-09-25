# Iscrpno: svi podskupovi velicine k (n <= 9), najmanji nagib kao razlomak, maksimum.
import sys
from itertools import combinations
from fractions import Fraction
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
pts = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n)]
best = None
for comb in combinations(range(n), k):
    mn = None
    for a in range(k):
        for b in range(a + 1, k):
            i, j = comb[a], comb[b]
            s = Fraction(pts[j][1] - pts[i][1], pts[j][0] - pts[i][0])
            if mn is None or s < mn:
                mn = s
    if best is None or mn > best:
        best = mn
print('%.12f' % float(best))
