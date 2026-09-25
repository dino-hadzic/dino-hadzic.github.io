import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 6); print(t)
    for _ in range(t):
        n = random.randint(1, 7)
        mx = 2*n*(n-1)
        k = random.choice([random.randint(0, mx), 0, 1, mx, mx-1, mx-2, random.randint(0, min(mx, 5))])
        print(n, k)
else:
    t = 1; print(t)
    n = 1000; mx = 2*n*(n-1)
    print(n, random.choice([mx-2, random.randint(0, mx), 2, mx//2 + 1]))
