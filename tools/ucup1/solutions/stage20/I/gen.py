import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def disjoint(a, b):
    (x1, y1, r1), (x2, y2, r2) = a, b
    return (x1-x2)**2 + (y1-y2)**2 > (r1+r2)**2
if mode == 'small':
    n = random.randint(2, 10)
    C = random.choice([8, 15, 30]); R = random.choice([2, 4, 8])
    disks = []
    tries = 0
    while len(disks) < n and tries < 10000:
        tries += 1
        d = (random.randint(0, C), random.randint(0, C), random.randint(1, R))
        if all(disjoint(d, e) for e in disks): disks.append(d)
    n = len(disks)
    if n < 2: disks = [(1, 1, 1), (3, 3, 1)]; n = 2
    print(n)
    for d in disks: print(*d)
else:
    n = 200000
    print(n)
    kind = seed % 3
    if kind == 0:                          # mreza 500 x 400, korak 2e6, slucajni radijusi
        pts = [(i * 2000000 + 1000000, j * 2000000 + 1000000) for i in range(500) for j in range(400)]
        for (x, y) in pts: print(x, y, random.randint(1, 999999))
    elif kind == 1:                        # okomiti stupci s istim X ulaza (mnogo istih dogadaja)
        for i in range(n):
            col = i % 400; row = i // 400
            print(col * 2500000 + 1000000, row * 2000000 + 1000000, 999999)
    else:                                  # jedan ogroman disk i mnogo malih desno + rupe
        print(0, 500000000, 400000000)
        k = n - 1
        for i in range(k):
            col = i % 500; row = i // 500
            print(500000000 + col * 1000000 + 500000, row * 2500000 + 500000, random.randint(1, 499999))
