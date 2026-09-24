import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = [450, 100000, 20000][seed % 3]   # gust graf, rijedak graf, srednji
    maxm = n * (n - 1) // 2
    m = min(100000, maxm)
    edges = set()
    if n == 450:
        # gotovo potpun graf
        allp = [(u, v) for u in range(n) for v in range(u + 1, n)]
        random.shuffle(allp)
        edges = set(allp[:m])
    else:
        while len(edges) < m:
            u, v = random.randrange(n), random.randrange(n)
            if u == v: continue
            if u > v: u, v = v, u
            edges.add((u, v))
else:
    n = random.randint(2, 8)
    maxm = n * (n - 1) // 2
    m = random.randint(0, maxm)
    allp = [(u, v) for u in range(n) for v in range(u + 1, n)]
    random.shuffle(allp)
    edges = allp[:m]
out = ['%d %d' % (n, len(edges))]
for u, v in edges:
    out.append('%d %d' % (u, v))
print('\n'.join(out))
