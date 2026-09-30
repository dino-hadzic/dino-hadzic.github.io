import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n, m, q = 100000, 500000, 500000
    B = 60
    V = 0
    for i in range(B):
        if random.random() < 0.5: V |= 1 << i
    print(n, m, q, V)
    lines = []
    for _ in range(m):
        u = random.randint(1, n); v = random.randint(1, n)
        while v == u: v = random.randint(1, n)
        w = 0
        for i in range(B):
            if random.random() < 0.85: w |= 1 << i
        lines.append(f'{u} {v} {w}')
    for _ in range(q):
        u = random.randint(1, n); v = random.randint(1, n)
        while v == u: v = random.randint(1, n)
        lines.append(f'{u} {v}')
    print('\n'.join(lines))
else:
    n = random.randint(2, 7); m = random.randint(0, 10); q = random.randint(1, 8)
    B = random.randint(1, 4)
    V = random.randint(0, (1 << B) - 1)
    print(n, m, q, V)
    for _ in range(m):
        u = random.randint(1, n); v = random.randint(1, n)
        while v == u: v = random.randint(1, n)
        print(u, v, random.randint(0, (1 << B) - 1))
    for _ in range(q):
        u = random.randint(1, n); v = random.randint(1, n)
        while v == u: v = random.randint(1, n)
        print(u, v)
