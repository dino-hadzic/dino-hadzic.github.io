import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def tree(n):
    kind = random.random()
    edges = []
    for v in range(2, n + 1):
        if kind < 0.3: p = random.randint(max(1, v - 2), v - 1)          # dugacki lanci
        elif kind < 0.5: p = random.randint(1, min(v - 1, 2))             # zvijezde / dvije zvijezde
        else: p = random.randint(1, v - 1)
        edges.append((p, v))
    perm = list(range(1, n + 1)); random.shuffle(perm)
    return [(perm[a - 1], perm[b - 1]) for a, b in edges]
if mode == 'big':
    tests = [100000, 100000]
else:
    tests = [random.randint(2, 6) for _ in range(random.randint(1, 3))]
print(len(tests))
for n in tests:
    print(n)
    for a, b in tree(n): print(a, b)
