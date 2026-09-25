import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(2, 6); m = random.randint(1, 8); k = random.randint(1, n)
        print(n, m, k)
        print(*random.sample(range(1, n + 1), k))
        print(*[random.choice([0, 0, 1, 1, 2, m]) for _ in range(n)])
        for _ in range(m):
            x = random.randint(1, n); y = random.randint(1, n)
            while y == x:
                y = random.randint(1, n)
            print(x, y, random.randint(1, 5))
else:
    T = 1
    print(T)
    n = 100000; m = 1000000; k = random.randint(1, 100)
    print(n, m, k)
    print(*random.sample(range(2, n + 1), k))
    print(*[random.choice([0, 1, 2, 3, 20]) for _ in range(n)])
    out = []
    for _ in range(m):
        x = random.randint(1, n); y = random.randint(1, n)
        while y == x:
            y = random.randint(1, n)
        out.append(f"{x} {y} {random.randint(1, 10000)}")
    print("\n".join(out))
