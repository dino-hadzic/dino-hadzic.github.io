#!/usr/bin/env python3
# Brute force: prodi svih n^k rasporeda prijatelja i za svaki nadi grad
# s najmanjim zbrojem udaljenosti (najmanji indeks pri izjednacenju).
import sys, itertools
n, k = map(int, sys.stdin.read().split())
MOD = 998244353
total = 0
for tup in itertools.product(range(1, n + 1), repeat=k):
    best = min(range(1, n + 1), key=lambda v: (sum(abs(v - a) for a in tup), v))
    total += best
print(total % MOD)
