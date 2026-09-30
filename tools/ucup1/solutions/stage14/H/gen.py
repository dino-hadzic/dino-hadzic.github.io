import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def cactus(n, tries, pathlike=False):
    # slucajno stablo + bridovi koji zatvaraju cikluse s bridovno disjunktnim putevima
    par = [-1] * n; dep = [0] * n
    for i in range(1, n):
        par[i] = i - 1 if (pathlike and random.random() < 0.8) else random.randrange(i)
        dep[i] = dep[par[i]] + 1
    edges = set((par[i], i) for i in range(1, n))
    on_cycle = set()
    for _ in range(tries):
        u, v = random.sample(range(n), 2)
        path = []
        a, b = u, v
        while a != b:
            if dep[a] >= dep[b]: path.append((par[a], a)); a = par[a]
            else: path.append((par[b], b)); b = par[b]
        e = (min(u, v), max(u, v))
        if len(path) >= 2 and e not in edges and not any(x in on_cycle for x in path):
            edges.add(e); on_cycle.update(path)
    perm = list(range(n)); random.shuffle(perm)
    out = [(min(perm[u], perm[v]), max(perm[u], perm[v])) for (u, v) in edges]
    random.shuffle(out)
    return out

def star(n, leaves_cnt):
    vs = random.sample(range(n), leaves_cnt + 1)
    c = vs[0]
    return [(min(c, x), max(c, x)) for x in vs[1:]]

def caterpillar(n, internal, K):
    # lanac od 'internal' unutarnjih vrhova, listovi rasporedjeni tako da svaki ima stupanj >= 12
    need = [12] * internal
    for i in range(internal):
        if i > 0: need[i] -= 1
        if i + 1 < internal: need[i] -= 1
    total_leaves = K - (internal - 1)
    assert total_leaves >= sum(need)
    extra = total_leaves - sum(need)
    for _ in range(extra): need[random.randrange(internal)] += 1
    vs = random.sample(range(n), internal + total_leaves)
    ins = vs[:internal]; lv = vs[internal:]
    edges = [(ins[i], ins[i + 1]) for i in range(internal - 1)]
    p = 0
    for i in range(internal):
        for _ in range(need[i]): edges.append((ins[i], lv[p])); p += 1
    edges = [(min(a, b), max(a, b)) for (a, b) in edges]
    random.shuffle(edges)
    return edges

if mode == 'big':
    n = 500
    kind = seed % 3
    ce = cactus(n, 3000, pathlike=(kind == 2))
    if kind == 1: te = star(n, 100)
    else: te = caterpillar(n, 9, 100)
    T = [random.randint(1, 200000) for _ in range(n)]
else:
    n = random.randint(2, 16)
    ce = cactus(n, random.randint(0, 3 * n))
    if n >= 13 and random.random() < 0.6:
        te = star(n, random.randint(12, n - 1))
    else:
        u, v = random.sample(range(n), 2)
        te = [(min(u, v), max(u, v))]
    T = [random.randint(1, 10 if random.random() < 0.5 else 200000) for _ in range(n)]

out = ['%d %d' % (n, len(ce)), ' '.join(map(str, T))]
out += ['%d %d' % e for e in ce]
out.append(str(len(te)))
out += ['%d %d' % e for e in te]
print('\n'.join(out))
