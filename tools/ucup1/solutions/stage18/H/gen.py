import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(2, 8)
        bits = random.choice([2, 3, 4])
        print(n)
        print(*[random.randint(0, (1 << bits) - 1) for _ in range(n)])
else:
    n = 100000
    FULL = (1 << 29) - 1
    kind = random.randint(0, 2)
    a = []
    if kind == 0:
        a = [random.randint(0, 10**9) for _ in range(n)]
    elif kind == 1:
        # mnogo ključnih točaka na oba kraja, sredina "puna"
        a = [FULL] * n
        for i in range(29):
            a[i] = FULL & ~(1 << (28 - i)) & ~random.choice([0, 1 << random.randint(0, 28)])
            a[n - 1 - i] = FULL & ~(1 << i)
        for i in range(30, n - 30):
            a[i] = FULL & ~(1 << random.randint(0, 28)) if random.random() < 0.001 else FULL
    else:
        # bitovi se gube postupno duž niza (mnogo komada za svaki ključ)
        a = [FULL] * n
        for i in range(n):
            if random.random() < 0.0005:
                a[i] = FULL & ~(1 << random.randint(0, 28))
        for i in range(29):
            a[i * (n // 60)] = FULL & ~(1 << i)
            a[n - 1 - i * (n // 60)] = FULL & ~(1 << (28 - i))
    print(1)
    print(n)
    print(*a)
