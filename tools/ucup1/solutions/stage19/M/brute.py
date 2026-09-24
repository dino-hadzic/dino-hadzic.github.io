# Brute force (n <= 7): za zadanu konfiguraciju isprobaj sve derangemente (svaki gleda točno
# jednog, svakoga gleda točno jedan), provjeri vidljivost segmenta i zbroji okrete.
# Premještanje (1000) se isplati samo ako bez njega nema rješenja (i tada najviše jedno):
# za svaki dron isprobaj skup kandidatskih pozicija (na zraci nekog drona, na zraci unazad
# od nekog cilja, presjeci takvih zraka, te "generička" točka), egzaktno razlomcima.
import sys
from fractions import Fraction
from itertools import permutations

data = sys.stdin.read().split()
n = int(data[0])
P0 = [tuple(Fraction(int(data[1 + 6 * i + k])) for k in range(3)) for i in range(n)]
D = [tuple(Fraction(int(data[4 + 6 * i + k])) for k in range(3)) for i in range(n)]

def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def mul(a, t): return tuple(x * t for x in a)
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def zero(a): return all(x == 0 for x in a)

def cijena_konfiguracije(P):
    m = len(P)
    # vidljivost i "koga trenutno gleda"
    vid = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j: continue
            d = sub(P[j], P[i])
            ok = True
            for k in range(m):
                if k == i or k == j: continue
                e = sub(P[k], P[i])
                if zero(cross(d, e)) and 0 < dot(e, d) < dot(d, d):
                    ok = False; break
            vid[i][j] = ok
    gleda = [-1] * m
    for i in range(m):
        best = None
        for j in range(m):
            if i == j: continue
            d = sub(P[j], P[i])
            if zero(cross(d, D[i])) and dot(d, D[i]) > 0:
                t = dot(d, d)
                if best is None or t < best[0]: best = (t, j)
        if best: gleda[i] = best[1]
    najbolje = None
    for perm in permutations(range(m)):
        if any(perm[i] == i or not vid[i][perm[i]] for i in range(m)): continue
        c = sum(1 for i in range(m) if gleda[i] != perm[i])
        if najbolje is None or c < najbolje: najbolje = c
    return najbolje

def zauzeto(P, X):
    return any(X == p for p in P)

if n == 1:
    print(-1); sys.exit()
odg = cijena_konfiguracije(P0)
if odg is None:
    for m in range(n):
        ostali = [i for i in range(n) if i != m]
        kand = []
        for w in ostali:
            for s in (1, 2, Fraction(1, 3)):
                kand.append(add(P0[w], mul(D[w], s)))
        for t_ in ostali:
            for s in (1, 2, Fraction(1, 3)):
                kand.append(sub(P0[t_], mul(D[m], s)))
        for w in ostali:
            for t_ in ostali:
                A, u = P0[t_], mul(D[m], -1); B, wv = P0[w], D[w]
                nrm = cross(u, wv)
                if zero(nrm): continue
                Dd = sub(B, A)
                if dot(Dd, nrm) != 0: continue
                t = Fraction(dot(cross(Dd, wv), nrm), dot(nrm, nrm))
                if t > 0: kand.append(add(A, mul(u, t)))
        kand.append((Fraction(1234567, 7), Fraction(-7654321, 11), Fraction(9999991, 13)))
        vidjeno = set()
        for X in kand:
            if X in vidjeno or zauzeto([P0[i] for i in ostali], X): continue
            vidjeno.add(X)
            P = list(P0); P[m] = X
            c = cijena_konfiguracije(P)
            if c is not None:
                c += 1000
                if odg is None or c < odg: odg = c
print(odg if odg is not None else -1)
