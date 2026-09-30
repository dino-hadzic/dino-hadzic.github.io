# Brute force: sve rijeci nad abecedom {a,n,i,z} iste duljine bez "ania", minimalna Hammingova
# udaljenost. Slova koja nisu u "ania" medusobno su ravnopravna, pa jedno dodatno slovo ('z') dostaje.
import sys, itertools
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    s = d[p]; p += 1
    best = len(s)
    for t in itertools.product('aniz', repeat=len(s)):
        t = ''.join(t)
        if 'ania' in t: continue
        best = min(best, sum(1 for x, y in zip(s, t) if x != y))
    out.append(str(best))
print('\n'.join(out))
