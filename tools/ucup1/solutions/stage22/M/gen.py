import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def tree(n, kind):
    edges = []
    for v in range(2, n + 1):
        if kind == 'path': p = v - 1
        elif kind == 'star': p = 1
        elif kind == 'cater': p = v - 1 if v % 2 == 0 else max(1, v - 2)
        elif kind == 'bin': p = v // 2
        elif kind == 'deep': p = random.randint(max(1, v - 3), v - 1)
        else: p = random.randint(1, v - 1)
        edges.append((p, v))
    perm = list(range(1, n + 1)); random.shuffle(perm)
    out = []
    for a, b in edges:
        a, b = perm[a - 1], perm[b - 1]
        out.append((min(a, b), max(a, b)))
    random.shuffle(out)
    return out

kind = random.choice(['path', 'star', 'cater', 'bin', 'deep', 'rand', 'rand'])
if mode == 'big':
    n = 500
else:
    n = random.choice([random.randint(3, 12), random.randint(3, 100), random.randint(3, 500)])
print(n)
for a, b in tree(n, kind):
    print(a, b)
