import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def graph(n, extra):
    edges = set()
    perm = list(range(1, n+1)); random.shuffle(perm)
    for i in range(1, n):
        j = random.randint(max(0, i-3), i-1) if random.random() < 0.5 else random.randint(0, i-1)
        a, b = perm[i], perm[j]
        edges.add((min(a,b), max(a,b)))
    for _ in range(extra if n >= 2 else 0):
        a, b = random.sample(range(1, n+1), 2)
        edges.add((min(a,b), max(a,b)))
    return list(edges)
if mode == 'small':
    t = random.randint(1, 4); print(t)
    for _ in range(t):
        n = random.randint(1, 12)
        e = graph(n, random.randint(0, 6))
        print(n, len(e))
        for a, b in e: print(a, b)
else:
    t = 1; print(t)
    n = 200000
    kind = ['random', 'path', 'star'][seed % 3]
    if kind == 'path':
        e = [(i, i+1) for i in range(1, n)]
    elif kind == 'star':
        e = [(1, i) for i in range(2, n+1)]
    else:
        e = graph(n, 800000 - n + 1)
    print(n, len(e))
    print("\n".join(f"{a} {b}" for a, b in e))
