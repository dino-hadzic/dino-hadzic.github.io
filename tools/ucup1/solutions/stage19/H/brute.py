# Brute force (egzaktno, razlomci): Markovljev lanac po svim podskupovima preostalih.
# P(p drugi | S) računamo neovisno o kantama: sum_q int f_p(x) (1-F_q(x)) prod_{r!=p,q} F_r(x) dx,
# po jediničnim intervalima gdje su sve F_r linearne (množenje polinoma s razlomcima).
import sys
from fractions import Fraction
from functools import lru_cache

n, k = map(int, sys.stdin.read().split())

def poly_mul(a, b):
    res = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            res[i + j] += x * y
    return res

def poly_int01(a):
    return sum(c / (i + 1) for i, c in enumerate(a))

def F_poly(r, b):
    # F_r(x) za x = b + u, u u [0,1)
    if b + 1 <= r:
        return [Fraction(0)]
    if b >= r + k:
        return [Fraction(1)]
    return [Fraction(b - r, k), Fraction(1, k)]

@lru_cache(maxsize=None)
def second_probs(S):
    S = list(S)
    res = {}
    for p in S:
        tot = Fraction(0)
        for q in S:
            if q == p:
                continue
            for b in range(p, p + k):
                poly = [Fraction(1, k)]
                fq = F_poly(q, b)
                one_minus = [Fraction(1) - fq[0]] + [-c for c in fq[1:]]
                poly = poly_mul(poly, one_minus)
                for r in S:
                    if r == p or r == q:
                        continue
                    poly = poly_mul(poly, F_poly(r, b))
                tot += poly_int01(poly)
        res[p] = tot
    return res

E = [Fraction(0)] * (n + 1)
dist = {tuple(range(1, n + 1)): Fraction(1)}
for size in range(n, 1, -1):
    nxt = {}
    for S, pr in dist.items():
        probs = second_probs(S)
        for p in S:
            q = probs[p]
            if q == 0:
                continue
            E[p] += pr * q * size
            T = tuple(x for x in S if x != p)
            nxt[T] = nxt.get(T, Fraction(0)) + pr * q
    dist = nxt
for S, pr in dist.items():
    E[S[0]] += pr
for i in range(1, n + 1):
    print("%.9f" % float(E[i]))
