import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 7000
    kind = seed % 3
    edges = set()
    if kind == 0:
        while len(edges) < 7000:
            a, b = random.sample(range(1, n + 1), 2)
            edges.add((a, b))
    elif kind == 1:
        # dugacak lanac + slucajni bridovi unaprijed (duboka rekurzija, dugi putevi)
        for i in range(1, n):
            edges.add((i, i + 1))
        while len(edges) < 7000:
            a = random.randint(1, n - 1); b = random.randint(a + 1, n)
            edges.add((a, b))
    else:
        # velika SCC (ciklus) + grane
        for i in range(1, 3001):
            edges.add((i, i % 3000 + 1))
        while len(edges) < 7000:
            a, b = random.sample(range(1, n + 1), 2)
            edges.add((a, b))
else:
    n = random.randint(1, 8)
    maxm = n * (n - 1)
    m = random.randint(0, min(maxm, 12))
    edges = set()
    while len(edges) < m:
        a, b = random.sample(range(1, n + 1), 2)
        edges.add((a, b))
edges = list(edges)
random.shuffle(edges)
print(n, len(edges))
for a, b in edges:
    print(a, b)
