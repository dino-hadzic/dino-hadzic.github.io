import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def triples(n, m, wmax):
    pairs = set()
    allp = [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1)]
    random.shuffle(allp)
    res = []
    for (u, v) in allp[:m]:
        res.append((u, v, random.randint(0, wmax)))
    return res
if mode == 'small':
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 9)
        m = random.randint(0, min(6, n * (n - 1) // 2))
        print(n, m)
        wmax = random.choice([0, 1, 3, 10, 100])
        for (u, v, w) in triples(n, m, wmax):
            print(u, v, w)
else:
    kind = random.randint(0, 2)
    if kind == 0:
        # jedan veliki test: n = 10^9, m = 10^5 slučajnih trojki
        n = 10**9; m = 100000
        print(1); print(n, m)
        pairs = set()
        while len(pairs) < m:
            u = random.randint(1, n); v = random.randint(1, n)
            if u != v: pairs.add((min(u, v), max(u, v)))
        print("\n".join(f"{u} {v} {random.choice([0, 1, random.randint(0, 10**9), 10**9])}" for (u, v) in pairs))
    elif kind == 1:
        # gusti mali raspon: posebni vrhovi blizu, zvijezda + lanac
        n = 10**9; m = 100000
        print(1); print(n, m)
        pairs = set()
        c = random.randint(1, 1000)
        for i in range(m // 2):
            v = random.randint(1, 300000)
            if v != c: pairs.add((min(c, v), max(c, v)))
        while len(pairs) < m:
            u = random.randint(1, 300000); v = u + random.randint(1, 3)
            pairs.add((u, v))
        print("\n".join(f"{u} {v} {random.choice([0, 10**9, random.randint(0, 5)])}" for (u, v) in pairs))
    else:
        # mnogo malih testova: T = 10^5, m = 5
        T = 100000
        print(T)
        out = []
        for _ in range(T):
            n = random.randint(6, 10**9); m = 5
            pairs = set()
            while len(pairs) < m:
                u = random.randint(1, min(n, 12)); v = random.randint(1, min(n, 12))
                if u != v: pairs.add((min(u, v), max(u, v)))
            out.append(f"{n} {m}")
            for (u, v) in pairs:
                out.append(f"{u} {v} {random.randint(0, 10**9)}")
        print("\n".join(out))
