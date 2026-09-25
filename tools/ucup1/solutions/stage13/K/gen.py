import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def out(n, edges):
    print(n, len(edges))
    for a, b in edges:
        if random.random() < 0.5: a, b = b, a
        print(a, b)
if mode == 'big':
    t = seed % 3
    if t == 0:
        # Potpuni graf na 447 vrhova (99681 bridova) + izolirani vrhovi.
        k = 447
        edges = [(a, b) for a in range(1, k + 1) for b in range(a + 1, k + 1)]
        out(100000, edges)
    elif t == 1:
        # Gust slucajni graf na 500 vrhova, ostatak izoliran.
        k = 500
        s = set()
        while len(s) < 100000:
            a, b = random.sample(range(1, k + 1), 2)
            s.add((min(a, b), max(a, b)))
        out(100000, sorted(s))
    else:
        # Rijedak slucajni graf na 100000 vrhova + nekoliko klika velicine 60.
        n = 100000
        s = set()
        for c in range(20):
            vs = random.sample(range(1, n + 1), 60)
            for i in range(60):
                for j in range(i + 1, 60):
                    a, b = vs[i], vs[j]
                    s.add((min(a, b), max(a, b)))
        while len(s) < 100000:
            a, b = random.sample(range(1, n + 1), 2)
            s.add((min(a, b), max(a, b)))
        out(n, sorted(s))
else:
    n = random.randint(4, 12)
    p = random.choice([0.2, 0.5, 0.8, 1.0])
    edges = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1) if random.random() < p]
    random.shuffle(edges)
    out(n, edges)
