import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = random.choice([10**9, 10**9 - 7]); m = random.choice([10**9, 999999937]); k = 5000
    kind = seed % 3
    pts = set()
    if kind == 0:            # slučajno
        while len(pts) < k: pts.add((random.randint(1, n - 1), random.randint(1, m - 1)))
    elif kind == 1:          # dva padajuca "sloja": svi parovi (A_i, B_j) s x_A < x_B su valjani
        h = k // 2; step = (n - 2) // k
        for i in range(h):
            pts.add((1 + 2 * i * step, m // 4 - i))
            pts.add((1 + (2 * i + 1) * step, m - 2 - i))
    else:                    # isto, ali gusto (male koordinate) i s jednakim koordinatama
        h = k // 2
        for i in range(h):
            pts.add((1 + 2 * i, 3000 - i))
            pts.add((2 + 2 * i, 20000 - i // 2))
    pts = list(pts)
    print(n, m, len(pts))
    print('\n'.join(f'{a} {b}' for a, b in pts))
else:
    n = random.randint(2, 9); m = random.randint(2, 9)
    cand = [(a, b) for a in range(1, n) for b in range(1, m)]
    k = random.randint(1, min(len(cand), random.choice([2, 4, 8])))
    pts = random.sample(cand, k)
    print(n, m, k)
    for a, b in pts: print(a, b)
