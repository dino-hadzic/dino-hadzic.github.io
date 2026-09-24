# Brute force: svi m^n nizovi, prebroji palindromne podsegmente, zadrzi minimalne, sortiraj leksikografski.
import sys
from itertools import product
n, m, k = map(int, sys.stdin.read().split())
def pal(a):
    c = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            t = a[i:j + 1]
            if t == t[::-1]:
                c += 1
    return c
best = None; opt = []
for a in product(range(1, m + 1), repeat=n):
    c = pal(a)
    if best is None or c < best:
        best = c; opt = []
    if c == best:
        opt.append(a)
opt.sort()
if k > len(opt):
    print(-1)
else:
    print(*opt[k - 1])
