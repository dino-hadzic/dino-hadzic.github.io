import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 200000; q = 200000
    kind = random.choice(['path', 'rand', 'star', 'caterpillar'])
    K = random.choice([1, 2, 3, 200000])
    fa = []
    for i in range(2, n + 1):
        if kind == 'path': fa.append(i - 1)
        elif kind == 'star': fa.append(1 if random.random() < 0.9 else random.randint(1, i - 1))
        elif kind == 'caterpillar': fa.append(i - 1 if i % 2 == 0 else max(1, i - 3))
        else: fa.append(random.randint(max(1, i - 5), i - 1) if random.random() < 0.5 else random.randint(1, i - 1))
    W = 10**9
else:
    n = random.randint(1, 8); q = random.randint(1, 8)
    K = random.randint(1, 3)
    fa = [random.randint(1, i - 1) for i in range(2, n + 1)]
    W = 10
print(n, q)
print(' '.join(str(random.randint(1, K)) for _ in range(n)))
print(' '.join(map(str, fa)))
print(' '.join(str(random.randint(1, K)) for _ in range(n - 1)))
print(' '.join(str(random.randint(0, W)) for _ in range(n - 1)))
out = []
for _ in range(q):
    out.append(f"{random.randint(1, n)} {random.randint(1, K)}")
print('\n'.join(out))
