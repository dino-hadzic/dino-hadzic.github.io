import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def emit(n, m, wmax, wset=None):
    edges = set()
    for i in range(1, n): edges.add((i, i + 1))
    edges.add((1, n))
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u == v: continue
        if u > v: u, v = v, u
        if v - u == 1 or (u == 1 and v == n): continue
        edges.add((u, v))
    print(n, m)
    for u, v in edges:
        w = random.choice(wset) if wset else random.randint(1, wmax)
        if random.random() < .5: u, v = v, u
        print(u, v, w)
if mode == 'big':
    print(3)
    emit(100000, 300000, 50000)                 # opceniti test
    emit(100000, 300000, 3, wset=[1, 2, 3])       # puno jednako kratkih putova
    emit(100000, 300000, 50000, wset=[2, 3, 6, 49999, 50000])
else:
    z = random.randint(1, 3); print(z)
    for _ in range(z):
        n = random.randint(3, 7); m = random.randint(n, min(n * (n - 1) // 2, n + 5))
        emit(n, m, random.randint(1, 4))
