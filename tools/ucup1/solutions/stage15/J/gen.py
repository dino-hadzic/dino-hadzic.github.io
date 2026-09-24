import random, sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom import jednostavan
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def zvjezdast(n, C):
    # slucajne tocke sortirane po kutu oko sredista -> zvjezdast poligon, provjeri jednostavnost
    for _ in range(1000):
        pts = set()
        while len(pts) < n: pts.add((random.randint(0, C), random.randint(0, C)))
        pts = list(pts)
        cx = sum(p[0] for p in pts) / n; cy = sum(p[1] for p in pts) / n
        pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        if jednostavan(pts): return pts
    return [(0, 0), (C, 0), (C, C)]

def zubati(spacing, dubina, kosi):
    # pravokutnik [0,30000]^2 sa zupcima na sve cetiri strane (sve unutra, bez sudara)
    W = 30000; P = []
    lo, hi = 6000, 24000
    def zubi(strana):
        x = lo
        while x + 1 <= hi:
            d = random.randint(1, dubina); d2 = random.randint(1, dubina) if kosi else d
            for (u, v) in [(x, 0), (x, d), (x + 1, d2), (x + 1, 0)]:
                if strana == 0: P.append((u, v))            # dno, zubi prema gore
                elif strana == 1: P.append((W - v, u))      # desno, zubi prema lijevo
                elif strana == 2: P.append((W - u, W - v))  # vrh, zubi prema dolje
                else: P.append((v, W - u))                  # lijevo, zubi prema desno
            x += spacing
    P.append((0, 0)); zubi(0); P.append((W, 0)); zubi(1); P.append((W, W)); zubi(2); P.append((0, W)); zubi(3)
    return P

if mode == 'big':
    P = zubati(2, 5000, seed % 2 == 0)
    q = 200000; C = 30000
    upiti = []
    for _ in range(q):
        u = random.random()
        if u < 0.3:
            x1, y1 = random.randint(0, C), random.randint(0, C); x2, y2 = random.randint(0, C), random.randint(0, C)
        elif u < 0.6:
            x1, y1 = random.randint(0, C), random.randint(0, C); x2 = x1 + random.randint(-30, 30); y2 = y1 + random.randint(-30, 30)
        elif u < 0.8:
            x1, y1 = random.randint(0, C), random.randint(0, C); x2 = x1; y2 = y1 + random.randint(-3000, 3000)
        else:
            x1, y1 = random.randint(0, C), random.randint(0, C); x2 = x1 + random.randint(-3000, 3000); y2 = y1
        x2 = min(max(x2, 0), C); y2 = min(max(y2, 0), C)
        if (x1, y1) == (x2, y2): x2 = x1 + 1 if x1 < C else x1 - 1
        upiti.append((x1, y1, x2, y2))
else:
    C = random.choice([4, 6, 10, 30])
    n = random.randint(3, 8) if C < 30 else random.randint(3, 24)
    P = zvjezdast(n, C)
    if random.random() < 0.5 and len(P) > 3: P = P[::-1]
    q = random.randint(1, 25) if C < 30 else random.randint(1, 60)
    upiti = []
    while len(upiti) < q:
        x1, y1, x2, y2 = [random.randint(0, C + 1) for _ in range(4)]
        if (x1, y1) != (x2, y2): upiti.append((x1, y1, x2, y2))
print(len(P), len(upiti))
for x, y in P: print(x, y)
for u in upiti: print(*u)
