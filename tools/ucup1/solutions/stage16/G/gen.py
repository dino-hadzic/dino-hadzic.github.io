import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def graf(n, extra, kind):
    """Povezan graf bez visestrukih bridova, svaki vrh ima <= 2 susjedna lista."""
    edges = set()
    def add(a, b):
        if a != b:
            edges.add((min(a, b), max(a, b)))
    if kind == 'gusjenica':      # kicma + po 2 lista na svakom vrhu kicme
        spine = max(1, n // 3)
        for v in range(2, spine + 1):
            add(v - 1, v)
        nxt = spine + 1
        for v in range(1, spine + 1):
            for _ in range(2):
                if nxt <= n:
                    add(v, nxt); nxt += 1
        while nxt <= n:
            add(random.randint(1, spine), nxt); nxt += 1
    elif kind == 'trojke':       # cvorista s 2 lista, povezana preko vrhova stupnja 2
        hubs = max(2, n // 5)
        nxt = hubs + 1
        for h in range(1, hubs + 1):
            for _ in range(2):
                if nxt <= n:
                    add(h, nxt); nxt += 1
        prev = 1
        while nxt <= n:
            h = random.randint(1, hubs)
            add(prev, nxt); add(nxt, h); nxt += 1
            prev = h
        for h in range(2, hubs + 1):
            if not any((min(h, u), max(h, u)) in edges for u in range(1, n + 1) if u != h and u > hubs) or random.random() < 0.3:
                add(h - 1, h)
    elif kind == 'put':
        for v in range(2, n + 1):
            add(v - 1, v)
    elif kind == 'ciklus':
        for v in range(2, n + 1):
            add(v - 1, v)
        if n >= 3:
            add(n, 1)
    else:                        # slucajno stablo + dodatni bridovi
        for v in range(2, n + 1):
            add(random.randint(max(1, v - 3) if kind == 'dubok' else 1, v - 1), v)
    for _ in range(extra):
        add(random.randint(1, n), random.randint(1, n))
    # popravi: povezi komponente i razbij vrhove s > 2 susjedna lista
    while True:
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        bad = False
        comp = [0] * (n + 1)
        reps = []
        for v in range(1, n + 1):
            if not comp[v]:
                reps.append(v); comp[v] = len(reps); st = [v]
                while st:
                    x = st.pop()
                    for u in adj[x]:
                        if not comp[u]:
                            comp[u] = len(reps); st.append(u)
        if len(reps) > 1:
            bad = True
            for i in range(1, len(reps)):
                add(random.choice([v for v in range(1, n + 1) if comp[v] == i]), reps[i])
        for v in range(1, n + 1):
            leaves = [u for u in adj[v] if len(adj[u]) == 1]
            if len(leaves) > 2:
                bad = True
                for u in leaves[2:]:
                    w = random.randint(1, n)
                    while w == u or w == v:
                        w = random.randint(1, n)
                    add(u, w)
        if not bad:
            break
    return list(edges)

def ispisi(testovi):
    print(len(testovi))
    for n, e in testovi:
        random.shuffle(e)
        print(n, len(e))
        for a, b in e:
            if random.random() < 0.5: a, b = b, a
            print(a, b)

if mode == 'big':
    kind = seed % 3
    if kind == 0:
        n = 200000
        ispisi([(n, graf(n, 300000, 'slucajno'))])
    elif kind == 1:
        n = 200000
        ispisi([(n, graf(n, 0, 'gusjenica'))])
    else:
        ispisi([(20, graf(20, random.randint(0, 20), random.choice(['slucajno', 'gusjenica', 'dubok'])))
                for _ in range(10000)])
else:
    testovi = []
    for _ in range(random.randint(1, 15)):
        n = random.randint(2, 14)
        kind = random.choice(['slucajno', 'gusjenica', 'put', 'ciklus', 'dubok', 'trojke', 'trojke'])
        testovi.append((n, graf(n, random.randint(0, n), kind)))
    ispisi(testovi)
