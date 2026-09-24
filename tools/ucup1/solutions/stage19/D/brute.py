# Brute force: sve permutacije (n <= 7) koje poštuju ovisnosti, očekivani trošak egzaktno
# razlomcima; ispisuje optimalni redoslijed.
import sys
from fractions import Fraction
from itertools import permutations

data = sys.stdin.read().split()
n = int(data[0])
c, p, d = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    c[i] = int(data[3 * i - 2]); p[i] = Fraction(data[3 * i - 1]); d[i] = int(data[3 * i])

def trosak(perm):
    E = Fraction(0); C = 0; P = Fraction(1)
    for x in perm:
        C += c[x]
        E += C * P * (1 - p[x])
        P *= p[x]
    return E

best = None; best_perm = None
for perm in permutations(range(1, n + 1)):
    pos = {x: i for i, x in enumerate(perm)}
    if any(d[x] and pos[d[x]] > pos[x] for x in perm):
        continue
    E = trosak(perm)
    if best is None or E < best:
        best, best_perm = E, perm
print("\n".join(map(str, best_perm)))
