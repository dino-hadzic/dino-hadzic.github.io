import random, sys
sys.setrecursionlimit(10000)
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def dfs_order(adj, root):
    order = []
    stack = [(root, -1)]
    while stack:
        x, p = stack.pop()
        order.append(x)
        ch = [y for y in adj[x] if y != p]
        random.shuffle(ch)
        for y in ch:
            stack.append((y, x))
    return order

def case(n):
    adj = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        if random.random() < 0.3:
            p = v - 1           # dugi lanci
        else:
            p = random.randint(1, v - 1)
        adj[v].append(p); adj[p].append(v)
    # slucajna permutacija oznaka
    perm = list(range(1, n + 1)); random.shuffle(perm)
    adj2 = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        for u in adj[v]:
            adj2[perm[v - 1]].append(perm[u - 1])
    out = [str(n)]
    for r in range(1, n + 1):
        out.append(" ".join(map(str, dfs_order(adj2, r))))
    return out

if mode == 'small':
    T = random.randint(1, 5)
    out = [str(T)]
    for _ in range(T):
        out += case(random.randint(1, 7))
else:
    T = 2
    out = [str(T)]
    for _ in range(T):
        out += case(1000)
print("\n".join(out))
