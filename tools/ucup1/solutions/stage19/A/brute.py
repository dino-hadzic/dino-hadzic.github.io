# Brute force preko igre: F(k, d) = najveci broj spojeva koji se sigurno razlikuje s k mjesta u d dana.
# Jednog dana alergen reagira na nekom podskupu S mjesta (mjesta iz S vise nisu upotrebljiva),
# pa je F(k, d) = sum_{j} C(k, j) * F(k - j, d - 1),  F(k, 0) = 1.  Za velike d koristi Python velike brojeve
# i zatvorenu formulu (d+1)^k (samo kao provjera prelijevanja u sol.cpp).
import sys
from functools import lru_cache
from math import comb

@lru_cache(maxsize=None)
def F(k, d):
    if d == 0:
        return 1
    return sum(comb(k, j) * F(k - j, d - 1) for j in range(k + 1))

data = sys.stdin.read().split()
t = int(data[0]); i = 1
out = []
for _ in range(t):
    n, d = int(data[i]), int(data[i + 1]); i += 2
    k = 0
    if d <= 12:
        while F(k, d) < n:
            k += 1
    else:
        while (d + 1) ** k < n:
            k += 1
    out.append(str(k))
print('\n'.join(out))
