import sys
from itertools import product
# Brute force za mali M: uzmemo sve klauzule (2 literala, moguce jednaka) koje
# vrijede u svim zadanim redovima, iscrpno nabrojimo sva 2^M rjesenja te formule
# i usporedimo sa zadanim skupom. Ispis: -1 ili popis klauzula.
data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])
rows = set(data[2:2 + N])

def lit_val(row, p):            # literal p: varijabla p//2, p paran = "spasen" (bit '1')
    return (row[p // 2] == '1') == (p % 2 == 0)

clauses = []
for p in range(2 * M):
    for q in range(p, 2 * M):
        if (p ^ 1) == q:
            continue
        if all(lit_val(r, p) or lit_val(r, q) for r in rows):
            clauses.append((p, q))

sols = set()
for bits in product('01', repeat=M):
    r = ''.join(bits)
    if all(lit_val(r, p) or lit_val(r, q) for p, q in clauses):
        sols.add(r)
if sols != rows:
    print(-1)
else:
    print(len(clauses))
    for p, q in clauses:
        i, j = p // 2, q // 2
        pi, pj = p % 2 == 0, q % 2 == 0
        t = (4 if pj else 2) if pi else (3 if pj else 1)
        print(i, j, t)
