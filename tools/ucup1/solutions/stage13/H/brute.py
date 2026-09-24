# Brute force: svi binarni nizovi duljine <= n, prebroji razlicite podnizove skupom, sortiraj leksikografski.
import sys
from itertools import product

def podnizovi(s):
    seen = {""}
    for ch in s:
        seen |= {t + ch for t in seen}
    return len(seen) - 1

def blokovi(s):
    b = []
    for ch in s:
        if b and b[-1][0] == ch:
            b[-1][1] += 1
        else:
            b.append([ch, 1])
    return b

data = sys.stdin.read().split()
t = int(data[0]); pos = 1
out = []
for _ in range(t):
    n, k = int(data[pos]), int(data[pos + 1]); pos += 2
    valid = []
    for L in range(1, n + 1):
        for tup in product("01", repeat=L):
            s = "".join(tup)
            if podnizovi(s) == n:
                valid.append(s)
    valid.sort()
    if len(valid) < k:
        out.append("-1")
    else:
        b = blokovi(valid[k - 1])
        out.append(f"{len(b)} {b[0][0]}")
        out.append(" ".join(str(x[1]) for x in b))
print("\n".join(out))
