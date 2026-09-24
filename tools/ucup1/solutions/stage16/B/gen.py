import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    print(1)
    n, m = 100, 100
    print(n, m, random.randint(1, n - 1))
    print(*[random.randint(0, 100) for _ in range(n)])
else:
    t = random.randint(1, 3)
    print(t)
    for _ in range(t):
        n = random.randint(2, 5)
        m = random.randint(1, 3)
        v = random.randint(1, n - 1)
        A = random.choice([2, 4, 8])
        print(n, m, v)
        print(*[random.randint(0, A) for _ in range(n)])
