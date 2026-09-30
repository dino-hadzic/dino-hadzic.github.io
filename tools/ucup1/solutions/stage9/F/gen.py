import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 1
    print(T)
    n = random.choice([1024, 2048, 4096, 1536]); k = random.randint(1, n - 1)
    print(n, k)
else:
    T = random.randint(1, 3)
    print(T)
    for _ in range(T):
        n = random.choice([2, 2, 4, 4, 4, 6, 6, 8, 8]); k = random.randint(1, min(n - 1, 4))
        print(n, k)
