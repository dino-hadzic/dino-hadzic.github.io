import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    t = 100
    print(t)
    for _ in range(t):
        n = random.choice([10**9, 10**9 - 2, 223092868, 510510 * 1957 - 2, random.randint(10**8, 10**9)])
        print(n, random.randint(1, 10**9))
else:
    t = random.randint(1, 4)
    print(t)
    for _ in range(t):
        n = random.randint(1, 11)
        print(n, random.randint(1, n + 3))
