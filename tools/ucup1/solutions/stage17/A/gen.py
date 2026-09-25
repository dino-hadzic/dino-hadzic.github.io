import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n = random.randint(1, 5)
else:
    n = 500000
edges = []
tip = random.random()
if tip < 0.6:
    # dva slucajna valjana stabla -> uvijek rjesivo
    for y in range(2, n + 1):
        edges.append((random.randint(1, y - 1), y))
    for x in range(1, n):
        edges.append((x, random.randint(x + 1, n)))
else:
    for _ in range(2 * n - 2):
        edges.append((random.randint(1, n), random.randint(1, n)))
random.shuffle(edges)
out = [str(n)]
for u, v in edges:
    if random.random() < 0.5:
        u, v = v, u
    out.append(f"{u} {v}")
print("\n".join(out))
