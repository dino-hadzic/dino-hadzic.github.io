import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 60
    print(T)
    for _ in range(T):
        n = 100; m = random.randint(1, 10**9)
        print(n, m)
        w = random.choice([[1, 1, 1], [1, 0, 3], [0, 1, 1], [1, 1, 4]])
        print(' '.join(str(random.choices([0, 1, 2], weights=w)[0]) for _ in range(n)))
else:
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(1, 5); m = random.randint(1, 3)
        print(n, m)
        print(' '.join(str(random.randint(0, 2)) for _ in range(n)))
