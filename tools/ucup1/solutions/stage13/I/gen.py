import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 10**6
    p = list(range(1, n + 1))
    t = seed % 4
    if t == 0:
        random.shuffle(p)
    elif t == 1:
        p.reverse()
    elif t == 2:
        # gotovo sortirano: nekoliko zamjena
        for _ in range(20):
            i, j = random.randrange(n), random.randrange(n)
            p[i], p[j] = p[j], p[i]
    else:
        # sortirano osim kaosa u sredini
        lo, hi = n // 2 - 1000, n // 2 + 1000
        mid = p[lo:hi]; random.shuffle(mid); p[lo:hi] = mid
    print(n); print(*p)
else:
    n = random.randint(1, 11)
    p = list(range(1, n + 1))
    if random.random() < 0.8:
        random.shuffle(p)
    else:
        for _ in range(random.randint(0, 2)):
            i, j = random.randrange(n), random.randrange(n)
            p[i], p[j] = p[j], p[i]
    print(n); print(*p)
