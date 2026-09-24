import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n = random.randint(2, 11)
    a = [random.randint(1, random.choice([2, 4, 10, 10**9])) for _ in range(n)]
    shape = random.randint(0, 2)
    par = [0] * (n + 1)
    for v in range(2, n + 1):
        if shape == 0:
            par[v] = random.randint(1, v - 1)
        elif shape == 1:
            par[v] = v - 1          # lanac
        else:
            par[v] = max(1, v - random.randint(1, 2))
else:
    n = 100000
    a = [random.randint(1, 10**9) for _ in range(n)]
    shape = random.randint(0, 2)
    par = [0] * (n + 1)
    for v in range(2, n + 1):
        if shape == 0:
            par[v] = random.randint(1, v - 1)
        elif shape == 1:
            par[v] = v - 1          # dugačak lanac
        else:
            par[v] = max(1, v - random.randint(1, 3))
# nasumično permutiraj oznake (osim korijena) i ispiši bridove u nasumičnom poretku
perm = list(range(2, n + 1)); random.shuffle(perm); lab = [0, 1] + perm
edges = []
for v in range(2, n + 1):
    e = [lab[v], lab[par[v]]]; random.shuffle(e); edges.append(e)
random.shuffle(edges)
vals = [0] * (n + 1)
for v in range(1, n + 1): vals[lab[v]] = a[v - 1]
print(n)
print(*vals[1:])
print("\n".join(f"{x} {y}" for x, y in edges))
