# Brute force: točna distribucija procesa (razlomci) nad svim stanjima, bez ikakvih pretpostavki.
import sys
from fractions import Fraction
MOD = 998244353
n, d, r = map(int, sys.stdin.read().split())
dist = {tuple([1] * n): Fraction(1)}
for step in range(d):
    tot = n + step
    nd = {}
    for st, pr in dist.items():
        for i in range(n):
            ns = list(st); ns[i] += 1; ns = tuple(ns)
            nd[ns] = nd.get(ns, 0) + pr * Fraction(st[i], tot)
    dist = nd
E = Fraction(0)
for st, pr in dist.items():
    E += pr * sum(sorted(st, reverse=True)[:r])
print(E.numerator % MOD * pow(E.denominator % MOD, MOD - 2, MOD) % MOD)
