import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 1
    print(T)
    n = 100000; m = random.choice([10**12, random.randint(1, 10**12)])
    print(n, m)
    print(' '.join(str(random.randint(1, 10**5)) for _ in range(n)))
else:
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(1, 4); m = random.randint(0, 9)
        print(n, m)
        print(' '.join(str(random.randint(1, 6)) for _ in range(n)))
