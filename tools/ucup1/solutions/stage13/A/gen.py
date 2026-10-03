import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def bits(v, m):
    return format(v, 'b').zfill(m)

if mode == 'big':
    n = m = 2000
    kind = random.randint(0, 3)
    rows = []
    if kind == 0:
        rows = [random.getrandbits(m) for _ in range(n)]
    elif kind == 1:                      # standardna baza (reducirani problem izravno)
        rows = [1 << i for i in range(m)]
    elif kind == 2:                      # gornjotrokutasta baza s nasumičnim ostatkom
        rows = [(1 << i) | (random.getrandbits(i) if i else 0) for i in range(m)]
    else:                                # manji rang od m, nasumični X
        n = random.randint(1500, 1999)
        rows = [random.getrandbits(m) for _ in range(n)]
    X = random.choice([random.getrandbits(m), (1 << m) - 1, random.getrandbits(m) | (1 << (m - 1))])
else:
    m = random.randint(1, 6)
    kind = random.random()
    if kind < 0.6:
        # nezavisni redci: nasumični podskup pivota + nasumični ostali bitovi ispod pivota
        piv = sorted(random.sample(range(m), random.randint(1, m)), reverse=True)
        rows = [(1 << p) | (random.getrandbits(p) if p else 0) for p in piv]
        random.shuffle(rows)
        n = len(rows)
    else:
        n = random.randint(1, min(m + 1, 6))
        rows = []
        for _ in range(n):
            r = random.getrandbits(m)
            if rows and random.random() < 0.15:
                r = 0
                for b in rows:
                    if random.random() < 0.5:
                        r ^= b
            rows.append(r)
    X = random.choice([random.getrandbits(m), (1 << m) - 1, random.getrandbits(m) | (1 << (m - 1)),
                       random.getrandbits(m) | (1 << (m - 1))])
print(n, m)
for r in rows:
    print(bits(r, m))
print(bits(X, m))
