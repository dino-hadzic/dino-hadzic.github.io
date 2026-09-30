import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = q = 200000
    X = random.choice([10**12, 10**9, 10**6])
    print(n, q)
    print(*[random.randint(0, X) for _ in range(n)])
    cnt = 0; lines = []
    for _ in range(q):
        t = random.choices([1, 2, 3], weights=[3, 3, 4])[0]
        if t == 1:
            scale = X + cnt * n
            lines.append(f'1 {random.randint(0, random.choice([10**12, scale, scale // 2 + 1]))}')
        elif t == 2: cnt += 1; lines.append('2')
        else:
            l = random.randint(1, n); r = random.randint(l, n); lines.append(f'3 {l} {r}')
    print('\n'.join(lines))
else:
    n = random.randint(1, 7); q = random.randint(1, 10)
    A = random.choice([5, 20, 100])
    print(n, q); print(*[random.randint(0, A) for _ in range(n)])
    for _ in range(q):
        t = random.randint(1, 3)
        if t == 1: print(1, random.randint(0, A * 2))
        elif t == 2: print(2)
        else:
            l = random.randint(1, n); print(3, l, random.randint(l, n))
