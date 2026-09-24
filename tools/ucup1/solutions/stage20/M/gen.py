import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 5); print(t)
    for _ in range(t):
        n = random.randint(2, 9)
        k = random.randint(1, min(n*(n-1)//2, n//2 + 2))
        print(n, k)
else:
    t = 100; print(t)
    for _ in range(t):
        n = 100
        print(n, random.choice([1, 2, 49, 50, 51, 4950]))
