# Checker: izlaz mora biti permutacija 1..n koja poštuje ovisnosti; ako postoji očekivani izlaz
# (optimalni redoslijed iz brute forcea), očekivani trošak dobivenog redoslijeda mora biti unutar
# 1e-6 (apsolutno ili relativno) od optimalnog.
import sys
from fractions import Fraction

inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
data = open(inp).read().split()
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

g = list(map(int, open(got).read().split()))
if sorted(g) != list(range(1, n + 1)):
    print("izlaz nije permutacija 1..n"); sys.exit(1)
pos = {x: i for i, x in enumerate(g)}
for x in range(1, n + 1):
    if d[x] and pos[d[x]] > pos[x]:
        print("test %d izveden prije svoje ovisnosti %d" % (x, d[x])); sys.exit(1)
if exp != '-':
    e = list(map(int, open(exp).read().split()))
    Eo, Eg = trosak(e), trosak(g)
    if abs(Eg - Eo) > Fraction(1, 10 ** 6) * max(1, abs(Eo)):
        print("trošak %.9f, optimalno %.9f" % (float(Eg), float(Eo))); sys.exit(1)
sys.exit(0)
