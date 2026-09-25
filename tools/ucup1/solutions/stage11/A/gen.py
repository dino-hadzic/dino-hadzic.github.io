import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 5000
    kind = seed % 3
    if kind == 0:   # dugačak ciklus + mala stabla
        L = random.randint(2500, 5000)
        a = [0] * (n + 1)
        for i in range(1, L + 1): a[i] = i + 1 if i < L else 1
        for i in range(L + 1, n + 1): a[i] = random.randint(1, i - 1)
    elif kind == 1: # ciklus duljine 2 + dugački lanci (velika visina)
        a = [0] * (n + 1); a[1] = 2; a[2] = 1
        for i in range(3, n + 1): a[i] = i - 1 if random.random() < 0.9 else random.randint(1, i - 1)
    else:           # slučajan funkcijski graf, s negdje u stablu ili na ciklusu
        a = [0] + [0] * n
        for i in range(1, n + 1):
            a[i] = random.randint(1, n)
            while a[i] == i: a[i] = random.randint(1, n)
    s = random.randint(1, n)
    w = [random.randint(-10**9, 10**9) for _ in range(n)]
    p = [random.randint(0, 10**9) for _ in range(n)]
else:
    n = random.randint(2, 8)
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = random.randint(1, n)
        while a[i] == i: a[i] = random.randint(1, n)
    s = random.randint(1, n)
    w = [random.randint(-6, 6) for _ in range(n)]
    p = [random.randint(0, 4) for _ in range(n)]
print(n, s)
print(*w); print(*p); print(*a[1:])
