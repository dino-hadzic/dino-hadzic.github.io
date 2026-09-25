# Brute force: za n <= 6 nabroji sve nizove nad abecedom {1..n}, izracunaj p iz definicije i za svaki p
# zapamti leksikografski najmanji niz.
import sys, itertools
from functools import lru_cache
def pvec(s):
    n = len(s); res = []
    for j in range(1, n + 1):
        best = min(range(j), key=lambda x: s[x:j])
        res.append(best + 1)
    return tuple(res)
@lru_cache(None)
def table(n):
    d = {}
    for s in itertools.product(range(1, n + 1), repeat=n):
        pv = pvec(s)
        if pv not in d or s < d[pv]: d[pv] = s
    return d
data = sys.stdin.read().split(); ptr = 0
T = int(data[ptr]); ptr += 1
outs = []
for _ in range(T):
    n = int(data[ptr]); ptr += 1
    pv = tuple(int(x) for x in data[ptr:ptr + n]); ptr += n
    d = table(n)
    outs.append(' '.join(map(str, d[pv])) if pv in d else '-1')
print('\n'.join(outs))
