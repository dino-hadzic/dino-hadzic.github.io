import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def build(n_internal, kind, maxlab):
    # počinjemo s korijenom-listom i širimo listove; djeca dobivaju veće indekse
    L = {1: 0}; R = {1: 0}; lab = {}
    leaves = [1]; nxt = 2
    for _ in range(n_internal):
        if kind == 'cater': v = leaves[-1]
        elif kind == 'bal': v = leaves[0]
        else: v = random.choice(leaves)
        leaves.remove(v)
        L[v], R[v] = nxt, nxt + 1
        L[nxt] = R[nxt] = 0; L[nxt + 1] = R[nxt + 1] = 0
        leaves.append(nxt); leaves.append(nxt + 1)
        nxt += 2
    n = nxt - 1
    for v in leaves: lab[v] = random.randint(1, maxlab)
    return n, L, R, lab

if mode == 'big':
    k = 499
    kind = random.choice(['cater', 'bal', 'rand'])
    maxlab = random.choice([2, 10**9])
else:
    k = random.randint(0, 7)
    kind = random.choice(['cater', 'bal', 'rand', 'rand'])
    maxlab = random.choice([2, 3, 100])
n, L, R, lab = build(k, kind, maxlab)
m = random.randint(0, (n - 1) // 2)
if mode == 'big' and random.random() < 0.5:
    m = (n - 1) // 2 - random.randint(0, 3)
print(n, m)
for i in range(1, n + 1):
    if L[i]: print(1, L[i], R[i])
    else: print(2, lab[i])
