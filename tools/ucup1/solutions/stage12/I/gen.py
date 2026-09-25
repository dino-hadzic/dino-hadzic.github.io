import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
ties = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (1, 0, 2), (2, 1, 0)]
if mode == 'big':
    N = 1500000
else:
    N = random.randint(1, 6)
if mode == 'big' or random.random() < 0.6:
    # brojevi iz stvarnog nerijesenog niza (odgovor > 0)
    a = [0, 0, 0]; b = [0, 0, 0]; c = [0, 0, 0]
    if mode == 'big':
        w = [random.random() for _ in range(9)]
        tot = sum(w); k = [int(N * x / tot) for x in w]
        k[0] += N - sum(k)
        for (x, y, z), m in zip(ties, k):
            a[x] += m; b[y] += m; c[z] += m
    else:
        for _ in range(N):
            x, y, z = random.choice(ties)
            a[x] += 1; b[y] += 1; c[z] += 1
else:
    def rnd():
        r = random.randint(0, N); p = random.randint(0, N - r)
        return [r, p, N - r - p]
    a, b, c = rnd(), rnd(), rnd()
print(N)
print(*a)
print(*b)
print(*c)
