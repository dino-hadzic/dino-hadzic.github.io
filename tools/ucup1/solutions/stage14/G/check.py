import sys
from itertools import product
# check.py <ulaz> <ocekivani ili -> <dobiveni>
# Ako je ocekivani -1, dobiveni mora biti -1. Inace dobiveni mora biti valjan
# popis klauzula (K <= 2 M^2) ciji je skup rjesenja TOCNO skup zadanih redova
# (provjera iscrpno za mali M, inace samo da svaki zadani red zadovoljava sve).
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
N, M = int(inp[0]), int(inp[1])
rows = set(inp[2:2 + N])

def fail(msg):
    print(msg); sys.exit(1)

if not got: fail('prazan izlaz')
if got[0] == '-1':
    if exp is not None and exp[0] != '-1': fail('ispisao -1, a rjesenje postoji')
    if exp is None: fail('ne mogu potvrditi -1 bez ocekivanog izlaza')
    sys.exit(0)
if exp is not None and exp[0] == '-1': fail('ocekivano -1')
K = int(got[0])
if K < 0 or K > 2 * M * M: fail('los K')
if len(got) != 1 + 3 * K: fail('los broj tokena')
clauses = []
for k in range(K):
    i, j, t = int(got[1 + 3 * k]), int(got[2 + 3 * k]), int(got[3 + 3 * k])
    if not (0 <= i < M and 0 <= j < M and 1 <= t <= 4): fail('los indeks/tip')
    # literal: (varijabla, trazena vrijednost) ; t=1: (~i|~j), 2: (i|~j), 3: (~i|j), 4: (i|j)
    vi = '1' if t in (2, 4) else '0'
    vj = '1' if t in (3, 4) else '0'
    clauses.append((i, vi, j, vj))

def sat(r):
    return all(r[i] == vi or r[j] == vj for i, vi, j, vj in clauses)

for r in rows:
    if not sat(r): fail('zadani red ne zadovoljava klauzule')
if M <= 12:
    sols = {''.join(b) for b in product('01', repeat=M) if sat(''.join(b))}
    if sols != rows: fail('skup rjesenja formule nije jednak zadanom')
sys.exit(0)
