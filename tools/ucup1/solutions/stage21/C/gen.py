import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def tree(n, kind):
    edges = []
    for i in range(2, n + 1):
        if kind == 'path': par = i - 1
        elif kind == 'star': par = 1
        elif kind == 'cat': par = random.randint(max(1, i - 3), i - 1)
        else: par = random.randint(1, i - 1)
        edges.append((par, i))
    perm = list(range(1, n + 1)); random.shuffle(perm)
    if random.random() < 0.3: perm = list(range(1, n + 1))
    return [(perm[a - 1], perm[b - 1]) for a, b in edges]
if mode == 'big':
    print(1); n = 300000; print(n)
    for a, b in tree(n, random.choice(['path', 'star', 'cat', 'rand'])): print(a, b)
else:
    T = random.randint(1, 6); print(T)
    for _ in range(T):
        n = random.randint(1, 9); print(n)
        for a, b in tree(n, random.choice(['path', 'star', 'cat', 'rand'])): print(a, b)
