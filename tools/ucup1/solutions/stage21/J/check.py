# check.py <ulaz> <ocekivano (prvi token = optimalna duljina) ili -> <dobiveno>
# Provjera: staza kreće u (1,1), završava u (n,n), susjedni vrhovi spojeni cestom,
# svaka cesta najviše jednom, zbroj duljina = ispisani l = optimum.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); p = 0
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split(); q = 0
T = int(inp[p]); p += 1
if exp is not None and len(exp) != T:      # očekivani izlaz u punom formatu (l, m, staza): uzmi samo l
    full, e, r = exp, 0, []
    for _ in range(T):
        r.append(full[e]); e += 2 + 2 * int(full[e + 1])
    exp = r
for tc in range(T):
    n = int(inp[p]); p += 1
    edges = {}
    for kind in range(3):
        for i in range(1, n):
            for j in range(1, i + 1):
                w = int(inp[p]); p += 1
                a, b = ((i, j), (i + 1, j)) if kind == 0 else ((i, j), (i + 1, j + 1)) if kind == 1 else ((i + 1, j), (i + 1, j + 1))
                edges[(a, b)] = w; edges[(b, a)] = w
    l = int(got[q]); m = int(got[q + 1]); q += 2
    path = [(int(got[q + 2 * k]), int(got[q + 2 * k + 1])) for k in range(m)]; q += 2 * m
    if path[0] != (1, 1) or path[-1] != (n, n): fail(f'test {tc}: krivi krajevi')
    used = set(); s = 0
    for a, b in zip(path, path[1:]):
        if (a, b) not in edges: fail(f'test {tc}: {a}-{b} nije cesta')
        key = (min(a, b), max(a, b))
        if key in used: fail(f'test {tc}: cesta {key} dvaput')
        used.add(key); s += edges[(a, b)]
    if s != l: fail(f'test {tc}: zbroj {s} != l {l}')
    if exp is not None and l != int(exp[tc]): fail(f'test {tc}: l={l}, optimum {exp[tc]}')
if q != len(got): fail('visak izlaza')
print('OK')
