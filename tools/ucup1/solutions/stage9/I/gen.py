import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 2
    print(T)
    for _ in range(T):
        n = 100000
        print(n)
        print(' '.join(str(random.randint(-10**9, 10**9)) for _ in range(n)))
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 9)
        print(n)
        print(' '.join(str(random.randint(-6, 6)) for _ in range(n)))
