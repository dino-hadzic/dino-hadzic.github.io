import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(1, 5); m = random.randint(n, 8)
        print(n, m)
        hi = random.choice([3, 10, 1000])
        for i in range(n):
            print(random.randint(1, hi), random.randint(1, hi))
else:
    T = 2
    print(T)
    for t in range(T):
        n = 500000; m = random.choice([n, 2 * n - 1, 10**9, n + n // 3])
        print(n, m)
        out = []
        for i in range(n):
            out.append(f"{random.randint(1, 10**9)} {random.randint(1, 10**9)}")
        print("\n".join(out))
