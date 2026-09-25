import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n1 = random.randint(1, 5); n2 = random.randint(1, 5)
    allp = [(b, g) for b in range(1, n1 + 1) for g in range(1, n2 + 1)]
    m = random.randint(1, min(10, len(allp)))
    E = random.sample(allp, m)
else:
    n1 = n2 = 100000
    m = 200000
    if seed == 1:
        # zvijezde + sparivanja
        E = set()
        while len(E) < m:
            b = random.randint(1, n1); g = random.randint(1, n2)
            if random.random() < 0.5:
                g = random.randint(1, 50)
            E.add((b, g))
        E = list(E)
    else:
        E = set()
        while len(E) < m:
            E.add((random.randint(1, n1), random.randint(1, n2)))
        E = list(E)
print(n1, n2, len(E))
print("\n".join(f"{b} {g}" for b, g in E))
