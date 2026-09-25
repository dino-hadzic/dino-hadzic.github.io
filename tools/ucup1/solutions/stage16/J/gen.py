import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    kind = seed % 3
    if kind == 0:
        n = 200000
        print(1); print(n, random.randint(1, 2 * 10**14))
        for _ in range(n): print(random.randint(1, 10**9), random.randint(1, n))
    elif kind == 1:
        n = 200000                        # sve b velike, jeftine teme: mora se uciti mnogo
        print(1); print(n, 10**14)
        for _ in range(n): print(random.randint(1, 10**9), random.randint(n // 2, n))
    else:
        q = 10000
        print(q)
        for _ in range(q):
            n = 20
            print(n, random.randint(1, 200))
            for _ in range(n): print(random.randint(1, 20), random.randint(1, n))
else:
    q = random.randint(1, 5)
    print(q)
    for _ in range(q):
        n = random.randint(1, 9)
        A = random.choice([3, 10, 100])
        print(n, random.randint(1, A * n))
        for _ in range(n): print(random.randint(1, A), random.randint(1, n))
