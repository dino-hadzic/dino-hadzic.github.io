import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def emit(n, maxc, kmax, deep=False):
    edges = []
    for v in range(2, n + 1):
        par = random.randint(max(1, v - 3), v - 1) if deep else random.randint(1, v - 1)
        edges.append((par, v))
    deg = [0] * (n + 1)
    for a, b in edges: deg[a] += 1; deg[b] += 1
    loops = set(v for v in range(1, n + 1) if deg[v] <= 1)
    for v in range(1, n + 1):
        if random.random() < .3: loops.add(v)
    if len(loops) < 2: loops.add(1); loops.add(n)
    print(n, len(loops)); print(' '.join(map(str, sorted(loops))))
    for a, b in edges:
        c = random.randint(1, maxc)
        if random.random() < .6: c = 2 * random.randint(1, max(1, maxc // 2))
        print(a, b, c)
    k = random.randint(1, min(kmax, n - 1))
    print(k); print(' '.join(map(str, sorted(random.sample(range(1, n), k)))))
if mode == 'big':
    z = 4; print(z)
    for t in range(z): emit(500000, 10**9, 500000 if t % 2 else 1000, deep=(t >= 2))
else:
    z = random.randint(1, 3); print(z)
    for _ in range(z): emit(random.randint(2, 6), 3, 4)
