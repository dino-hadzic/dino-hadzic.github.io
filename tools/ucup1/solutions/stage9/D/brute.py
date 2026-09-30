# Brute force: nabroji sve A duljine n i B duljine m (bez vodecih nula), izracunaj C i uzmi najmanji par.
import sys, itertools
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); c = data[p+2]; p += 3
    best = None
    for A in itertools.product(range(10), repeat=n):
        if A[0] == 0: continue
        for B in itertools.product(range(10), repeat=m):
            if B[0] == 0: continue
            s = ''.join(str(a * b) for a in A for b in B)
            if s == c:
                cand = (''.join(map(str, A)), ''.join(map(str, B)))
                if best is None or cand < best: best = cand
    out.append('Impossible' if best is None else best[0] + ' ' + best[1])
print('\n'.join(out))
