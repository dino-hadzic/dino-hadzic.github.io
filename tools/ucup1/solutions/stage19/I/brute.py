# Brute force: za n = 1, 2, ..., isqrt(x) izračunaj n^f(n) (Python veliki brojevi) i usporedi s x.
# Za n >= 2 je f(n) >= 2 pa n^f(n) >= n^2, dakle n <= isqrt(x) je dovoljno.
import sys
from math import isqrt

def f(n):
    d = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            d += 1 if i * i == n else 2
        i += 1
    return d

x = int(sys.stdin.read().split()[0])
ans = -1
for n in range(1, isqrt(x) + 1):
    if n ** f(n) == x:
        ans = n
        break
print(ans)
