import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def graf(n, oblik):
    # stablo + 2 dodatna brida (bridovi kao (a, b), a < b)
    perm = list(range(1, n + 1)); random.shuffle(perm)
    edges = set()
    for i in range(1, n):
        if oblik == 'lanac':
            par = perm[i - 1]
        elif oblik == 'zvijezda':
            par = perm[0]
        elif oblik == 'dubok':
            par = perm[max(0, i - random.randint(1, 3))]
        else:
            par = perm[random.randint(0, i - 1)]
        a, b = sorted((par, perm[i]))
        edges.add((a, b))
    while len(edges) < n + 1:
        a, b = random.sample(range(1, n + 1), 2)
        edges.add((min(a, b), max(a, b)))
    edges = list(edges); random.shuffle(edges)
    return edges

if mode == 'big':
    n = 50000; q = 50000
    oblik = random.choice(['lanac', 'zvijezda', 'dubok', 'slucajno'])
else:
    n = random.randint(4, 9); q = random.randint(1, 10)
    oblik = random.choice(['lanac', 'zvijezda', 'dubok', 'slucajno'])
edges = graf(n, oblik)
print(n, q)
for a, b in edges:
    print(a, b)
for _ in range(q):
    u, v = random.sample(range(1, n + 1), 2)
    print(min(u, v), max(u, v))
