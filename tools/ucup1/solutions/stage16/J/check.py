#!/usr/bin/env python3
# Checker: broj sigurnih tema jednak ocekivanom, odabir valjan (razliciti indeksi,
# ukupno vrijeme <= t) i broj sigurnih tema u odabiru tocno jednak ispisanom.
import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
q = int(inp[0]); p = 1; g = 0; e = 0
for tc in range(q):
    n, t = int(inp[p]), int(inp[p + 1]); p += 2
    a = []; b = []
    for i in range(n):
        a.append(int(inp[p])); b.append(int(inp[p + 1])); p += 2
    if g + 2 > len(got):
        print('premalo izlaza'); sys.exit(1)
    c, k = int(got[g]), int(got[g + 1]); g += 2
    if exp is not None:
        ce, ke = int(exp[e]), int(exp[e + 1]); e += 2 + ke
        if c != ce:
            print(f'test {tc}: sigurnih {c}, ocekivano {ce}'); sys.exit(1)
    if not 0 <= k <= n or g + k > len(got):
        print(f'test {tc}: nevaljan k'); sys.exit(1)
    S = [int(x) for x in got[g:g + k]]; g += k
    if any(not 1 <= x <= n for x in S) or len(set(S)) != k:
        print(f'test {tc}: nevaljani indeksi'); sys.exit(1)
    if sum(a[x - 1] for x in S) > t:
        print(f'test {tc}: premalo vremena'); sys.exit(1)
    if sum(1 for x in S if b[x - 1] <= k) != c:
        print(f'test {tc}: broj sigurnih ne odgovara'); sys.exit(1)
if g != len(got):
    print('visak izlaza'); sys.exit(1)
sys.exit(0)
