import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def emit(n, k, rings):
    random.shuffle(rings)
    print(n, k)
    for i in range(n): print(' '.join(map(str, rings[i * k:(i + 1) * k])))
if mode == 'big':
    z = 4; print(z)
    n, k = 50, 10
    emit(n, k, [c for c in range(1, n + 1) for _ in range(k)])                    # n boja po k prstena
    emit(n, k, [c for c in range(1, n) for _ in range(k)] + [10**9] * (k - 1) + [7])  # n+1 stupova
    emit(n, k, [c for c in range(1, n) for _ in range(k)] + [10**9] * (k - 2) + [7, 8])  # n+2 stupova
    n, k = random.choice([50, 37]), random.choice([2, 3, 5, 9])
    cols = [c for c in range(1, n) for _ in range(k)]
    cols += [10**9] * (k - 2) + [10**9 - 1, 10**9 - 2] if k >= 3 else [10**9 - 1, 10**9 - 2]  # sitne boje
    emit(n, k, cols)
else:
    z = random.randint(1, 3); print(z)
    for _ in range(z):
        n = random.randint(1, 3); k = random.randint(1, 3)
        cols = random.randint(1, 3)
        emit(n, k, [random.randint(1, cols) for _ in range(n * k)])
