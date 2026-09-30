import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)


def dag_of(s):
    subs = set(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
    names = list(subs)
    random.shuffle(names)
    idx = {t: i + 1 for i, t in enumerate(names)}
    edges = set()
    for t in subs:
        if len(t) > 1:
            edges.add((idx[t[:-1]], idx[t]))
            edges.add((idx[t[1:]], idx[t]))
    edges = list(edges)
    random.shuffle(edges)
    return len(subs), edges


MODH = (1 << 61) - 1
BASE = random.randrange(1000, MODH - 1)


def dag_of_long(s):
    # za duge nizove: podnizove predstavljamo parom (duljina, hash), O(L^2) uz prefiksne hasheve
    L = len(s)
    pre = [0] * (L + 1)
    pw = [1] * (L + 1)
    for i, ch in enumerate(s):
        pre[i + 1] = (pre[i] * BASE + ord(ch)) % MODH
        pw[i + 1] = pw[i] * BASE % MODH

    def h(i, ln):
        return (pre[i + ln] - pre[i] * pw[ln]) % MODH

    idx = {}
    nodes = []  # (i, ln) prvog pojavljivanja
    for ln in range(1, L + 1):
        for i in range(L - ln + 1):
            key = (ln, h(i, ln))
            if key not in idx:
                idx[key] = len(nodes) + 1
                nodes.append((i, ln))
    perm = list(range(1, len(nodes) + 1))
    random.shuffle(perm)
    edges = set()
    for (i, ln) in nodes:
        if ln > 1:
            v = perm[idx[(ln, h(i, ln))] - 1]
            edges.add((perm[idx[(ln - 1, h(i, ln - 1))] - 1], v))
            edges.add((perm[idx[(ln - 1, h(i + 1, ln - 1))] - 1], v))
    edges = list(edges)
    random.shuffle(edges)
    return len(nodes), edges


def dag_alt_plus_c(L):
    # niz 'abab...ab' (L paran) + 'c', DAG izgrađen izravno: alt(k, x) i suf(k)
    ids = {}

    def node(key):
        if key not in ids:
            ids[key] = len(ids) + 1
        return ids[key]
    edges = []
    for k in range(1, L):
        for x in 'ab':
            u = node(('alt', k, x))
            if k >= 2:
                o = 'b' if x == 'a' else 'a'
                edges.append((node(('alt', k - 1, x)), u))
                edges.append((node(('alt', k - 1, o)), u))
    u = node(('alt', L, 'a'))
    edges.append((node(('alt', L - 1, 'a')), u))
    edges.append((node(('alt', L - 1, 'b')), u))
    for k in range(1, L + 2):
        u = node(('suf', k))
        if k >= 2:
            x = 'ab'[(L - k + 1) % 2]  # prvo slovo alternirajućeg dijela sufiksa
            edges.append((node(('alt', k - 1, x)), u))
            edges.append((node(('suf', k - 1)), u))
    perm = list(range(1, len(ids) + 1))
    random.shuffle(perm)
    edges = [(perm[a - 1], perm[b - 1]) for a, b in edges]
    random.shuffle(edges)
    return len(ids), edges


def dag_run(N):
    # niz 'a' * N: lanac
    perm = list(range(1, N + 1))
    random.shuffle(perm)
    edges = [(perm[k - 1], perm[k]) for k in range(1, N)]
    random.shuffle(edges)
    return N, edges


def rand_small():
    L = random.randint(1, 8)
    k = random.choice([1, 2, 2, 2, 3, 3])
    typ = random.random()
    if typ < 0.15:
        s = ''.join(random.choice('ab') for _ in range(L))  # slučajno binarno
    elif typ < 0.3:
        s = ''.join('ab'[i % 2] for i in range(L))          # alternirajući
        if random.random() < 0.5 and L > 1:
            p = random.randint(0, L)
            s = s[:p] + 'c' + s[p:]
    elif typ < 0.45:
        s = 'a' * random.randint(1, 4) + random.choice(['', 'b', 'ba', 'bb', 'bab']) + 'a' * random.randint(0, 3)
    else:
        s = ''.join(chr(97 + random.randint(0, k - 1)) for _ in range(L))
    return s[:8]


def emit(tests):
    lines = [str(len(tests))]
    for s in tests:
        n, edges = s
        lines.append(f"{n} {len(edges)}")
        lines.extend(f"{u} {v}" for u, v in edges)
    sys.stdout.write('\n'.join(lines) + '\n')


if mode == 'small':
    T = random.randint(1, 3)
    emit([dag_of(rand_small()) for _ in range(T)])
else:
    if seed == 1:
        # dug alternirajući blok + jedno drugo slovo: korijen tipa 3, mnogo vrhova tipa 2
        emit([dag_alt_plus_c(330000)])
    elif seed == 2:
        # mnogo malih testova
        emit([dag_of(rand_small()) for _ in range(20000)])
    else:
        # slučajan binarni niz (n ~ L^2/2) i jedan niz od jednog slova (najdulji lanac)
        L = 1000
        s = ''.join(random.choice('ab') for _ in range(L))
        emit([dag_of_long(s), dag_run(400000)])
