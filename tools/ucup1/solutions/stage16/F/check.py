#!/usr/bin/env python3
# Checker: simulira pritiske gumba i provjerava da je konacna boja unutar 1e-6 od cilja.
import sys, math
inp = open(sys.argv[1]).read().split()
got = open(sys.argv[3]).read().split()
t = int(inp[0])
pos = 0
for tc in range(t):
    r, g, b = (int(inp[1 + 3 * tc + i]) for i in range(3))
    if pos >= len(got):
        print('premalo izlaza'); sys.exit(1)
    m = int(got[pos]); pos += 1
    if not 0 <= m <= 10:
        print('krivi m', m); sys.exit(1)
    p = [0.0, 0.0, 0.0]
    for _ in range(m):
        c = [int(got[pos]), int(got[pos + 1]), int(got[pos + 2])]
        d = float(got[pos + 3]); pos += 4
        if any(x not in (0, 255) for x in c) or not (0 <= d <= 1e4):
            print('nevaljan potez', c, d); sys.exit(1)
        v = [c[i] - p[i] for i in range(3)]
        L = math.sqrt(sum(x * x for x in v))
        if L > 0:
            s = min(d, L) / L
            p = [p[i] + v[i] * s for i in range(3)]
    dist = math.sqrt((p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2)
    if dist > 1e-6:
        print(f'test {tc}: udaljenost {dist}'); sys.exit(1)
if pos != len(got):
    print('visak izlaza'); sys.exit(1)
sys.exit(0)
