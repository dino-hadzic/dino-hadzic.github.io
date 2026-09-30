import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 10
    print(T)
    for _ in range(T):
        n = 100000
        m = random.randint(0, n)
        print(n, m)
        print(' '.join(str(random.choice([0, random.randint(1, 10**9)])) for _ in range(n)))
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 7)
        m = random.randint(0, n)
        print(n, m)
        print(' '.join(str(random.randint(0, 6)) for _ in range(n)))
