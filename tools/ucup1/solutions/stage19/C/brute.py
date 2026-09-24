# Brute force: BFS po svim razapinjućim stablima (skupovi od n-1 bridova), potez = zamjena
# jednog brida stabla bridom izvan stabla uz uvjet da rezultat ostane razapinjuće stablo.
# Ispisuje samo minimalni broj zamjena (checker uspoređuje k i provjerava valjanost niza).
import sys
from itertools import combinations
from collections import deque

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
E = []
for i in range(m):
    u, v, w = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
    E.append((u, v, w))

def je_stablo(S):
    p = list(range(n + 1))
    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for e in S:
        a, b = f(E[e][0]), f(E[e][1])
        if a == b:
            return False
        p[a] = b
    return True

stabla = [frozenset(c) for c in combinations(range(m), n - 1) if je_stablo(c)]
skup = set(stabla)
mst_w = min(sum(E[e][2] for e in S) for S in stabla)
start = frozenset(range(n - 1))
dist = {start: 0}
dq = deque([start])
while dq:
    S = dq.popleft()
    if sum(E[e][2] for e in S) == mst_w:
        print(dist[S])
        break
    for a in S:
        for b in range(m):
            if b in S:
                continue
            T = (S - {a}) | {b}
            if T in skup and T not in dist:
                dist[T] = dist[S] + 1
                dq.append(T)
