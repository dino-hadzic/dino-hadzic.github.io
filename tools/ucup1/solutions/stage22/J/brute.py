# Brute force: doslovno točno m zamjena. Stanje = vektor "zamijenjen/ne" po
# unutarnjim vrhovima; nakon t koraka skup dostižnih stanja, pa minimum niza listova.
import sys
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1]); p = 2
L = [0] * (n + 1); R = [0] * (n + 1); lab = [0] * (n + 1)
for i in range(1, n + 1):
    t = int(data[p]); p += 1
    if t == 1:
        L[i], R[i] = int(data[p]), int(data[p + 1]); p += 2
    else:
        lab[i] = int(data[p]); p += 1
internal = [i for i in range(1, n + 1) if L[i]]
states = {frozenset()}
for _ in range(m):
    nxt = set()
    for s in states:
        for v in internal:
            nxt.add(s ^ frozenset([v]))
    states = nxt

def seq(v, s):
    if L[v] == 0:
        return [lab[v]]
    a, b = L[v], R[v]
    if v in s:
        a, b = b, a
    return seq(a, s) + seq(b, s)

best = min(seq(1, s) for s in states)
print(' '.join(map(str, best)))
