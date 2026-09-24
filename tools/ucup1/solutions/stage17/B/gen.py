import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def find(f, x):
    if f[x] == x: return x
    f[x] = find(f, f[x]); return f[x]
def rand_ops(f, n, k):
    for _ in range(k):
        if random.random() < 0.4:
            find(f, random.randint(1, n))
        else:
            a = find(f, random.randint(1, n)); b = find(f, random.randint(1, n))
            if a != b: f[a] = b
def rand_forest(n):
    # slucajna suma: slucajni roditelj s manjim "rangom"
    perm = list(range(1, n + 1)); random.shuffle(perm)
    g = [0] * (n + 1)
    for i, v in enumerate(perm):
        g[v] = v if (i == 0 or random.random() < 0.3) else perm[random.randrange(i)]
    return g
if mode == 'small':
    T = random.randint(1, 3)
    tests = []
    for _ in range(T):
        n = random.choice([3, 3, 4, 4, 5, 5, 6])
        f = list(range(n + 1)); rand_ops(f, n, random.randint(0, n))
        g = f[:]
        if random.random() < 0.5:
            rand_ops(g, n, random.randint(1, 2 * n))
        else:
            g = rand_forest(n)
        tests.append((n, f, g))
else:
    tests = []
    if seed == 1:
        ns = [1000] * 5
    elif seed == 2:
        ns = [300] * 55
    else:
        ns = [50] * 2000
    for n in ns:
        f = list(range(n + 1)); rand_ops(f, n, random.randint(0, 2 * n))
        g = f[:]
        rand_ops(g, n, random.randint(1, 3 * n))
        tests.append((n, f, g))
sys.setrecursionlimit(10000)
print(len(tests))
for n, f, g in tests:
    print(n); print(" ".join(map(str, f[1:]))); print(" ".join(map(str, g[1:])))
