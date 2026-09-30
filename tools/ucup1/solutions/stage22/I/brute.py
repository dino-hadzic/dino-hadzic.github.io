# Brute force: točno računanje očekivanja razlomcima (Fraction) po definiciji
# E(n) = 1 + (1/k) sum_d E(n(d+1)), rješavanjem za E(n) zbog znamenke 0, pa modulo p.
import sys
from fractions import Fraction
from functools import lru_cache
sys.setrecursionlimit(10000)
MOD = 998244353

def solve(n0, N):
    @lru_cache(maxsize=None)
    def E(n):
        if n > N:
            return Fraction(0)
        s = str(n); k = len(s)
        zeros = s.count('0')
        tot = Fraction(0)
        for ch in s:
            d = int(ch)
            if d:
                tot += E(n * (d + 1))
        # E = 1 + (zeros*E + tot)/k
        return (k + tot) / (k - zeros)
    v = E(n0)
    return v.numerator % MOD * pow(v.denominator % MOD, MOD - 2, MOD) % MOD

data = sys.stdin.read().split()
T = int(data[0])
out = []
for i in range(T):
    n, N = int(data[1 + 2 * i]), int(data[2 + 2 * i])
    out.append(str(solve(n, N)))
print('\n'.join(out))
