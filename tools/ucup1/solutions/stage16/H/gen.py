import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def tocke(n, R):
    s = set()
    while len(s) < 2 * n:
        s.add((random.randint(-R, R), random.randint(-R, R)))
    l = list(s); random.shuffle(l)
    return l

if mode == 'big':
    kind = seed % 3
    if kind == 0:
        n = 100000
        print(1); print(n)
        for x, y in tocke(n, 300): print(x, y)
    elif kind == 1:
        n = 100000                      # dugacak lanac: (i, i), (i, i+1) -> dubina DFS-a 2n
        print(1); print(n)
        pts = []
        for i in range(n):
            pts.append((i, i)); pts.append((i, i + 1))
        random.shuffle(pts)
        for x, y in pts: print(x, y)
    else:
        t = 10000
        print(t)
        for _ in range(t):
            n = 10
            print(n)
            for x, y in tocke(n, random.choice([2, 3, 5])): print(x, y)
else:
    t = random.randint(1, 5)
    print(t)
    for _ in range(t):
        n = random.randint(1, 4)
        R = random.choice([1, 1, 2, 3])
        print(n)
        for x, y in tocke(n, R): print(x, y)
