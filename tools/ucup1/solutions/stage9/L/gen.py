import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 300
    print(T)
    for _ in range(T):
        n = random.randint(90000, 100000); m = random.randint(0, n + 3)
        print(n, m)
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 6); m = random.randint(0, n * (n - 1) // 2)
        print(n, m)
