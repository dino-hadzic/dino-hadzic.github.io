import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 100000
    kind = seed % 3  # 0: slucajno stablo, 1: lanac (dubina), 2: zvijezda
else:
    n = random.randint(2, 12)
    kind = random.randint(0, 2)
print(n)
print(*[random.randint(0, 1) for _ in range(n)])
perm = list(range(1, n + 1))
random.shuffle(perm)
edges = []
for i in range(2, n + 1):
    if kind == 1:
        p = i - 1
    elif kind == 2:
        p = 1 if random.random() < 0.7 else random.randint(1, i - 1)
    else:
        p = random.randint(1, i - 1)
    edges.append((perm[i - 1], perm[p - 1]))
random.shuffle(edges)
for u, v in edges:
    if random.random() < 0.5:
        u, v = v, u
    print(u, v)
