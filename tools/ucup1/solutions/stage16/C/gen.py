import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n, m = 500000, 30
    print(n, m)
    N = 1 << m
    kind = seed % 3
    for i in range(n):
        if kind == 0:      # slucajni upiti
            print(random.randrange(N), random.randrange(N))
        elif kind == 1:    # ugnijezdeni intervali (degeneracija nebalansiranog stabla)
            print(i, N - 1 - i)
        else:              # kratki intervali koji se pomicu
            l = (i * 2147) % N
            print(l, (l + random.randint(0, 5)) % N)
else:
    n = random.randint(1, 40)
    m = random.randint(1, 5)
    print(n, m)
    N = 1 << m
    for _ in range(n):
        print(random.randrange(N), random.randrange(N))
