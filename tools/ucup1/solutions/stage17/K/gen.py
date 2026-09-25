import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def rand_table(n):
    v = list(range(1, 2 * n + 1)); random.shuffle(v)
    return [v[:n], v[n:]]
def rand_moves(t, n, k):
    for _ in range(k):
        i, j = random.sample(range(n), 2)
        ri = 0 if t[0][i] > t[1][i] else 1
        rj = 0 if t[0][j] > t[1][j] else 1
        t[ri][i], t[rj][j] = t[rj][j], t[ri][i]
tests = []
if mode == 'small':
    for _ in range(random.randint(1, 2)):
        n = random.choice([2, 3, 3, 4, 4, 4])
        a = rand_table(n)
        b = [a[0][:], a[1][:]]
        if random.random() < 0.6:
            rand_moves(b, n, random.randint(1, 3 * n))
        else:
            b = rand_table(n)
        tests.append((n, a, b))
else:
    if seed == 1:
        ns = [2000]
    elif seed == 2:
        ns = [1000] * 4
    else:
        ns = [100] * 400
    for n in ns:
        a = rand_table(n)
        b = [a[0][:], a[1][:]]
        rand_moves(b, n, random.randint(1, 5 * n))
        tests.append((n, a, b))
print(len(tests))
for n, a, b in tests:
    print(n)
    for r in a + b: print(" ".join(map(str, r)))
