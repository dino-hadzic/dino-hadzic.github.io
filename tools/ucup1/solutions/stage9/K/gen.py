import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 1
    print(T)
    n = 100000; y0 = random.randint(1, 100000)
    print(n, y0)
    S = set()
    R = random.choice([300, 100000])
    while len(S) < n:
        S.add((random.randint(1, R), random.randint(max(1, y0 - R), min(100000, y0 + R))))
    for x, y in S: print(x, y)
else:
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        y0 = random.randint(1, 4)
        S = set()
        n = random.randint(1, 6)
        while len(S) < n: S.add((random.randint(1, 5), random.randint(1, 6)))
        print(n, y0)
        for x, y in S: print(x, y)
