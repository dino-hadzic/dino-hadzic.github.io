import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def rng(N, maxlen):
    a = random.randint(1, N); b = min(N, a + random.randint(0, maxlen - 1)); return a, b
if mode == 'big':
    z = 3; print(z)
    for t in range(z):
        n = 33333; q = 100000 if t < 2 else 100000
        print(n, q)
        N = 3 * n
        for _ in range(q):
            ml = random.choice([1, 5, 100, N]) if t != 1 else random.choice([1, 3])
            a, b = rng(N, ml); c, d = rng(N, ml)
            print(a, b, c, d)
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z):
        n = random.randint(1, 3); q = random.randint(1, 6); N = 3 * n
        print(n, q)
        for _ in range(q):
            a, b = rng(N, random.randint(1, N)); c, d = rng(N, random.randint(1, N))
            print(a, b, c, d)
