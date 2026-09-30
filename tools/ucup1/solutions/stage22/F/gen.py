import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def make_tree(n, maxdeg, kind):
    deg = [0] * (n + 1); edges = []
    for v in range(2, n + 1):
        while True:
            if kind == 'path': p = v - 1
            elif kind == 'bushy': p = random.randint(max(1, v - 40), v - 1)
            else: p = random.randint(1, v - 1)
            if deg[p] < maxdeg: break
            kind = 'rand'
        deg[p] += 1; deg[v] += 1; edges.append((p, v))
    return edges, max(deg[1:])

if mode == 'big':
    n = 100000; m = 500000
    kind = random.choice(['path', 'bushy', 'rand'])
    edges, k = make_tree(n, 12, kind)
    if k < 12 and random.random() < 0.5: k = 12
    print(n, m, k)
    perm = list(range(1, n + 1)); random.shuffle(perm)
    out = []
    for a, b in edges: out.append(f"{perm[a-1]} {perm[b-1]}")
    for _ in range(m):
        a = random.randint(1, n); b = random.randint(1, n)
        while b == a: b = random.randint(1, n)
        if kind == 'path' and random.random() < 0.7:
            b = min(n, max(1, a + random.randint(-50, 50)))
            if b == a: b = a + 1 if a < n else a - 1
        out.append(f"{a} {b} {random.randint(0, 10**9)}")
    print('\n'.join(out))
else:
    n = random.randint(2, 8); m = random.randint(0, 11)
    edges, k = make_tree(n, random.randint(2, 4), random.choice(['path', 'rand', 'rand']))
    print(n, m, max(k, 1))
    for a, b in edges: print(a, b)
    for _ in range(m):
        a = random.randint(1, n); b = random.randint(1, n)
        while b == a: b = random.randint(1, n)
        print(a, b, random.randint(0, 10))
