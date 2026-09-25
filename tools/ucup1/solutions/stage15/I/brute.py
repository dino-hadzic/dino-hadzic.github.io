# Iscrpno: svi podskupovi bridova velicine n-1 koji su razapinjuca stabla; maksimalni MEX.
import sys
from itertools import combinations
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
E = [(int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(m)]
best = 0
for comb in combinations(range(m), n - 1):
    p = list(range(n + 1))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    ok = True
    for i in comb:
        a, b = find(E[i][0]), find(E[i][1])
        if a == b:
            ok = False; break
        p[a] = b
    if not ok:
        continue
    ws = set(E[i][2] for i in comb)
    mex = 0
    while mex in ws:
        mex += 1
    best = max(best, mex)
print(best)
