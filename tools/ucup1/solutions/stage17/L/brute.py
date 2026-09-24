# Iscrpno: sve dodjele ±1 prostim brojevima do n (n <= 30).
import sys
from itertools import product
data = sys.stdin.read().split()
T = int(data[0]); p = 1
out = []
for _ in range(T):
    n, k = int(data[p]), int(data[p + 1]); p += 2
    primes = [x for x in range(2, n + 1) if all(x % d for d in range(2, x))]
    found = None
    for signs in product((1, -1), repeat=len(primes)):
        fp = dict(zip(primes, signs))
        f = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            d = next(q for q in primes if i % q == 0)
            f[i] = fp[d] * f[i // d]
        if sum(f[1:]) == k:
            found = f[1:]
            break
    out.append("-1" if found is None else " ".join(map(str, found)))
print("\n".join(out))
