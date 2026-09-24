import random, sys
from itertools import product
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def rand_formula_solutions(M, k):
    # skup rjesenja slucajne 2-SAT formule s k klauzula (iscrpno, mali M)
    cl = []
    for _ in range(k):
        i, j = random.randrange(M), random.randrange(M)
        cl.append((i, random.choice('01'), j, random.choice('01')))
    sols = []
    for b in product('01', repeat=M):
        r = ''.join(b)
        if all(r[i] == vi or r[j] == vj for i, vi, j, vj in cl):
            sols.append(r)
    return sols

if mode == 'big':
    kind = seed % 3
    if kind == 1:
        # lanac x0 -> x1 -> ... : rjesenja su 0...01...1, tocno M+1 njih
        M = 1999
        rows = ['0' * (M - k) + '1' * k for k in range(M + 1)]
    elif kind == 2:
        M = 2000
        rows = ['0' * (M - k) + '1' * k for k in range(M + 1)]
        rows.remove(rows[random.randrange(len(rows))])   # -1 (rupa u lancu)
    else:
        M = 2000
        rows = set()
        while len(rows) < 2000:
            rows.add(''.join(random.choice('01') for _ in range(M)))
        rows = sorted(rows)
    random.shuffle(rows)
else:
    M = random.randint(1, 8)
    if random.random() < 0.6:
        rows = rand_formula_solutions(M, random.randint(0, 2 * M))
        if not rows:
            rows = [''.join(random.choice('01') for _ in range(M))]
        if random.random() < 0.3 and len(rows) > 1:
            rows = random.sample(rows, random.randint(1, len(rows) - 1))
    else:
        cnt = random.randint(1, min(2 ** M, 6))
        rows = random.sample([''.join(b) for b in product('01', repeat=M)], cnt)
    random.shuffle(rows)
print(len(rows), M)
print('\n'.join(rows))
