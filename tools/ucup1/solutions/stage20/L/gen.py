import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 5); print(t)
    for _ in range(t):
        n = random.randint(1, 6)
        mx = random.choice([1, 2, 3, 4])
        print(n); print(" ".join(str(random.randint(1, mx)) for _ in range(n)))
else:
    t = 1; print(t)
    n = 100000
    print(n); print(" ".join(str(random.choice([1, 1, 1, 10**9])) for _ in range(n)))
