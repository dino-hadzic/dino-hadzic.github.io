# Brute force: za n <= 4 dodatno prolazi sve permutacije bridova K_n i pokrece Kruskala;
# za vece n koristi egzaktni DP po multiskupu velicina komponenti (svaki prihvaceni
# brid je uniformno slucajan par vrhova iz razlicitih komponenti; sve komponente
# moraju ostati staze, tj. brid spaja krajeve).  Sve u racionalnim brojevima.
import sys, itertools
from fractions import Fraction
from functools import lru_cache

def perm_prob(n):
    E = [(i, j) for i in range(n) for j in range(i + 1, n)]
    tot = good = 0
    for perm in itertools.permutations(E):
        par = list(range(n)); deg = [0] * n
        def f(x):
            while par[x] != x: x = par[x]
            return x
        for u, v in perm:
            a, b = f(u), f(v)
            if a != b:
                par[a] = b; deg[u] += 1; deg[v] += 1
        tot += 1; good += all(d <= 2 for d in deg)
    return Fraction(good, tot)

def process_prob(n):
    @lru_cache(None)
    def f(state):
        if len(state) == 1: return Fraction(1)
        total = (n * n - sum(s * s for s in state)) // 2
        res = Fraction(0)
        k = len(state)
        for i in range(k):
            for j in range(i + 1, k):
                ei = 1 if state[i] == 1 else 2
                ej = 1 if state[j] == 1 else 2
                nxt = list(state); si, sj = nxt[i], nxt[j]
                del nxt[j]; del nxt[i]; nxt.append(si + sj)
                res += Fraction(ei * ej, total) * f(tuple(sorted(nxt)))
        return res
    return f(tuple([1] * n))

N, P = map(int, sys.stdin.read().split())
for n in range(2, N + 1):
    q = process_prob(n)
    if n <= 4:
        assert q == perm_prob(n)
    print(q.numerator * pow(q.denominator, -1, P) % P)
