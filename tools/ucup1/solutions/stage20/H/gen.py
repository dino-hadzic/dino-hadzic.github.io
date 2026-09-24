import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 4); print(t)
    for _ in range(t):
        n = random.randint(2, 8)
        kind = random.random()
        par = []
        for i in range(2, n + 1):
            if kind < 0.3: par.append(i - 1)
            elif kind < 0.5: par.append(random.randint(max(1, i - 2), i - 1))
            else: par.append(random.randint(1, i - 1))
        print(n); print(" ".join(map(str, par)))
else:
    t = 1; print(t)
    n = 10**6
    kind = seed % 3
    if kind == 0: par = [i - 1 for i in range(2, n + 1)]
    elif kind == 1: par = [random.randint(1, i - 1) for i in range(2, n + 1)]
    else: par = [random.randint(max(1, i - 3), i - 1) for i in range(2, n + 1)]
    print(n); print(" ".join(map(str, par)))
