import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 200000; q = 200000
    kind = random.choice(['path', 'rand', 'star', 'binary'])
    W = 10**9
    edges = []
    for i in range(2, n + 1):
        if kind == 'path': p = i - 1
        elif kind == 'star': p = 1 if random.random() < 0.7 else random.randint(1, i - 1)
        elif kind == 'binary': p = i // 2
        else: p = random.randint(max(1, i - 20), i - 1) if random.random() < 0.7 else random.randint(1, i - 1)
        edges.append((p, i))
    perm = list(range(1, n + 1)); random.shuffle(perm)
    print(n, q)
    out = [f"{perm[a-1]} {perm[b-1]} {random.randint(1, W)}" for a, b in edges]
    upd = random.choice([0.1, 0.5, 0.9])
    for _ in range(q):
        if random.random() < upd: out.append(f"1 {random.randint(1, n - 1)} {random.randint(1, W)}")
        else: out.append(f"2 {random.randint(1, n)} {random.randint(0, 2 * 10**14) if random.random() < 0.3 else random.randint(0, 2 * 10**11)}")
    print('\n'.join(out))
else:
    n = random.randint(2, 9); q = random.randint(1, 10)
    W = random.choice([3, 10])
    print(n, q)
    for i in range(2, n + 1):
        print(random.randint(1, i - 1), i, random.randint(1, W))
    for _ in range(q):
        if random.random() < 0.4: print(1, random.randint(1, n - 1), random.randint(1, W))
        else: print(2, random.randint(1, n), random.randint(0, 3 * W))
