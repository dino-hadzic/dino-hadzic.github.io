import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 200
    print(T)
    for _ in range(T):
        r = random.random()
        if r < 0.5: print(1, 10**18)
        elif r < 0.8: print(random.randint(1, 10**6), 10**18)
        else:
            N = random.randint(1, 10**18); print(random.randint(1, N), N)
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        N = random.randint(1, 3000)
        n = random.randint(1, N) if random.random() < 0.7 else random.randint(1, min(N, 20))
        print(n, N)
