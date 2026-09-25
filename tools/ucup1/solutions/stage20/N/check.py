# check.py <ulaz> <-> <dobiveni izlaz>
# Possible: prebroji raznobojne susjedne parove, mora biti tocno K.
# Impossible: za N <= 4 potvrda iscrpnom pretragom svih bojanja; za N >= 5
# prihvacamo samo K = 1 i K = 2N(N-1)-1 (dokazano nemoguce u editorijalu).
import sys
from functools import lru_cache
def fail(m): print(m); sys.exit(1)

@lru_cache(maxsize=None)
def dostizivi(n):
    s = set()
    for mask in range(1 << (n*n)):
        k = 0
        for i in range(n):
            for j in range(n):
                a = mask >> (i*n+j) & 1
                if i+1 < n and a != (mask >> ((i+1)*n+j) & 1): k += 1
                if j+1 < n and a != (mask >> (i*n+j+1) & 1): k += 1
        s.add(k)
    return s

inp = open(sys.argv[1]).read().split(); out = open(sys.argv[3]).read().split()
t = int(inp[0]); p = 1; q = 0
for tc in range(t):
    n, k = int(inp[p]), int(inp[p+1]); p += 2
    if q >= len(out): fail("premalo izlaza")
    v = out[q]; q += 1
    mx = 2*n*(n-1)
    if v == "Impossible":
        if n <= 4:
            if k in dostizivi(n): fail(f"test {tc}: Impossible, a rjesenje postoji (N={n}, K={k})")
        elif k not in (1, mx - 1): fail(f"test {tc}: Impossible za N={n}, K={k}")
        continue
    if v != "Possible": fail(f"test {tc}: los verdikt {v}")
    g = out[q:q+n]; q += n
    if len(g) != n or any(len(r) != n or set(r) - set("RB") for r in g): fail(f"test {tc}: losa mreza")
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i+1 < n and g[i][j] != g[i+1][j]: cnt += 1
            if j+1 < n and g[i][j] != g[i][j+1]: cnt += 1
    if cnt != k: fail(f"test {tc}: {cnt} parova umjesto {k}")
if q != len(out): fail("visak izlaza")
print("OK")
