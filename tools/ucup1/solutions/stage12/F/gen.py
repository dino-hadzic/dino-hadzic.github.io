import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 300000
    kind = seed % 4  # 0 slucajno, 1 lanac, 2 zvijezda, 3 "metla"
    A = [random.randint(1, 10 ** 9) for _ in range(n)]
    if seed % 2 == 0:
        A = list(range(1, n + 1))  # rastuce po lancu: najgori slucaj propagacije
        if kind == 1:
            A = A[::-1]
else:
    n = random.randint(2, 10)
    kind = random.randint(0, 3)
    A = [random.randint(1, random.choice([3, 10, 10 ** 9])) for _ in range(n)]
print(n)
print(*A)
perm = list(range(1, n + 1))
if mode != 'big' or seed % 2:
    random.shuffle(perm)
edges = []
for i in range(2, n + 1):
    if kind == 1:
        p = i - 1
    elif kind == 2:
        p = 1 if random.random() < 0.8 else random.randint(1, i - 1)
    elif kind == 3:
        p = i - 1 if i <= n // 2 else random.randint(1, i - 1)
    else:
        p = random.randint(1, i - 1)
    edges.append((perm[i - 1], perm[p - 1]))
random.shuffle(edges)
for u, v in edges:
    print(u, v)
