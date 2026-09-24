import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 100000; m = 200000; d = random.choice([1, 2, 3, 7, 300, 200000])
else:
    n = random.randint(2, 8); m = random.randint(n - 1, min(n * (n - 1) // 2, n + 6)); d = random.randint(1, 6)
k = random.randint(1, n)
edges = set()
perm = list(range(1, n + 1)); random.shuffle(perm)
for i in range(1, n):
    a, b = perm[i], perm[random.randint(0, i - 1)]
    edges.add((min(a, b), max(a, b)))
while len(edges) < m:
    a, b = random.randint(1, n), random.randint(1, n)
    if a != b: edges.add((min(a, b), max(a, b)))
print(n, len(edges), k, d)
for a, b in edges: print(a, b)
