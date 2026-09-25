import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 30; K = 10
    dens = [0.15, 0.5, 1.0][seed % 3]
    edges = set()
    for u in range(1, n + 1):
        edges.add((u, random.randint(1, n)))
        for v in range(1, n + 1):
            if random.random() < dens:
                edges.add((u, v))
    A, B = random.sample(range(1, n + 1), 2)
    free = [v for v in range(1, n + 1) if v not in (A, B)]
    X = sorted(random.sample(free, K))
    W = [random.randint(1, 10 ** 8) for _ in range(K)]
else:
    n = random.randint(2, 4)
    K = random.randint(1, min(2, n - 1))
    edges = set()
    for u in range(1, n + 1):
        edges.add((u, random.randint(1, n)))
        if random.random() < 0.5:
            edges.add((u, random.randint(1, n)))
    A = random.randint(1, n); B = random.randint(1, n)
    free = [v for v in range(1, n + 1) if v not in (A, B)]
    K = min(K, len(free))
    if K == 0:
        # trebamo barem jedan dragulj: pomakni Boba na Alicein vrh
        B = A
        free = [v for v in range(1, n + 1) if v != A]
        K = 1
    X = sorted(random.sample(free, K))
    W = [random.randint(1, 10) for _ in range(K)]
edges = sorted(edges)
print(n, len(edges), A, B)
for u, v in edges:
    print(u, v)
print(K)
for x, w in zip(X, W):
    print(x, w)
