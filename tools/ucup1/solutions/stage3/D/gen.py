import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def tree(n, kind):
    edges = []
    for v in range(2, n + 1):
        if kind == 0: par = random.randint(1, v - 1)
        elif kind == 1: par = v - 1                      # put
        else: par = random.randint(max(1, v - 3), v - 1)  # dubok
        edges.append((par, v))
    perm = list(range(1, n + 1)); rest = perm[1:]; random.shuffle(rest); perm = [1] + rest
    random.shuffle(edges)
    return [(perm[a-1], perm[b-1]) if random.random() < .5 else (perm[b-1], perm[a-1]) for a, b in edges]
if mode == 'big':
    z = 3; print(z)
    for kind in range(3):
        n = 10**6; print(n)
        for a, b in tree(n, kind): print(a, b)
else:
    z = random.randint(1, 5); print(z)
    for _ in range(z):
        n = random.randint(2, 9); print(n)
        for a, b in tree(n, random.randint(0, 2)): print(a, b)
