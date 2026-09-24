import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 4); print(t)
    for _ in range(t):
        n = random.choice([1, 3, 5, 7]); m = random.randint(2, 8)
        K = random.randint(0, 30)
        print(n, m, K)
        print(" ".join(str(random.randint(1, m)) for _ in range(n)))
        print(" ".join(str(random.randint(1, 10)) for _ in range(m)))
else:
    t = 1; print(t)
    n = 999999; m = 1000000; K = random.choice([10**9, 10**6, 0])
    print(n, m, K)
    print(" ".join(str(random.randint(1, m)) for _ in range(n)))
    print(" ".join(str(random.randint(1, 10**9)) for _ in range(m)))
