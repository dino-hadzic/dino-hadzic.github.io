# Checker: k mora biti jednak očekivanom (brute force) ili, bez očekivanog izlaza, donjoj granici
# |T \ T*| (Kruskal koji preferira bridove početnog stabla); svaka zamjena mora ukloniti brid
# stabla i dodati brid izvan stabla tako da rezultat ostane razapinjuće stablo; konačno stablo
# mora imati težinu MST-a.
import sys

inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
data = open(inp).read().split()
n, m = int(data[0]), int(data[1])
E = [(int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(m)]

class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
    def f(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def u(self, a, b):
        a, b = self.f(a), self.f(b)
        if a == b:
            return False
        self.p[a] = b
        return True

def je_stablo(S):
    if len(S) != n - 1:
        return False
    d = DSU(n)
    return all(d.u(E[e][0], E[e][1]) for e in S)

# MST težina i donja granica
red = sorted(range(m), key=lambda e: (E[e][2], 0 if e < n - 1 else 1))
d = DSU(n); mst_w = 0; u_mst = set()
for e in red:
    if d.u(E[e][0], E[e][1]):
        mst_w += E[e][2]; u_mst.add(e)
donja = sum(1 for e in range(n - 1) if e not in u_mst)

g = open(got).read().split()
if not g:
    print("prazan izlaz"); sys.exit(1)
k = int(g[0])
if exp != '-':
    k_exp = int(open(exp).read().split()[0])
    if k != k_exp:
        print("k = %d, očekivano %d" % (k, k_exp)); sys.exit(1)
elif k != donja:
    print("k = %d, donja granica %d" % (k, donja)); sys.exit(1)
if len(g) != 1 + 2 * k:
    print("krivi broj brojeva u izlazu"); sys.exit(1)
S = set(range(n - 1))
for i in range(k):
    a, b = int(g[1 + 2 * i]) - 1, int(g[2 + 2 * i]) - 1
    if not (0 <= a < m and 0 <= b < m) or a not in S or b in S:
        print("zamjena %d: nevaljani indeksi %d %d" % (i + 1, a + 1, b + 1)); sys.exit(1)
    S.remove(a); S.add(b)
    if not je_stablo(S):
        print("zamjena %d: rezultat nije razapinjuće stablo" % (i + 1)); sys.exit(1)
if sum(E[e][2] for e in S) != mst_w:
    print("konačno stablo nije minimalno"); sys.exit(1)
sys.exit(0)
