import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 3); print(T)
    for _ in range(T):
        n = random.randint(1, 4); q = random.randint(1, 4)
        mx = random.choice([7, 15, 31]) if n <= 3 else 7
        print(n, q); print(" ".join(str(random.randint(0, mx)) for _ in range(n)))
        for _ in range(q):
            l = random.randint(1, n); r = random.randint(l, n); print(l, r)
else:
    kind = seed % 4
    if kind == 3:                     # mnogo sicusnih testova
        T = 100000; print(T)
        for _ in range(T):
            print(1, 1); print(random.randint(0, 10**9)); print(1, 1)
        sys.exit(0)
    T = 1; print(T)
    n = 100000; q = 100000
    if kind == 0: arr = [random.randint(0, 10**9) for _ in range(n)]
    elif kind == 1: arr = [random.choice([1 << random.randint(0, 29), random.randint(0, 10**9)]) for _ in range(n)]
    else: arr = [random.randint(0, 3) << random.randint(0, 28) for _ in range(n)]
    print(n, q); print(" ".join(map(str, arr)))
    for _ in range(q):
        l = random.randint(1, n); r = random.randint(l, n); print(l, r)
