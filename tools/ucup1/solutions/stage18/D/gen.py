import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def hull_keep_collinear(pts):
    pts = sorted(set(pts))
    if len(pts) < 3:
        return pts
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    def half(points):
        h = []
        for q in points:
            while len(h) >= 2 and cross(h[-2], h[-1], q) < 0:
                h.pop()
            h.append(q)
        return h
    lower = half(pts)
    upper = half(pts[::-1])
    # ukloni kolinearne točke koje bi se dvaput pojavile na krajevima
    hull = lower[:-1] + upper[:-1]
    # dedupliciraj (moguće kad su svi kolinearni)
    res = []
    for q in hull:
        if q not in res:
            res.append(q)
    return res

def convex_polygon(nmin, nmax, coord):
    while True:
        k = random.randint(nmin, nmax + 6)
        pts = [(random.randint(0, coord), random.randint(0, coord)) for _ in range(k)]
        h = hull_keep_collinear(pts)
        # površina > 0?
        s = 0
        for a in range(len(h)):
            x1, y1 = h[a]; x2, y2 = h[(a + 1) % len(h)]
            s += x1 * y2 - x2 * y1
        if nmin <= len(h) <= nmax and s > 0:
            return h

if mode == 'small':
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        coord = random.choice([2, 3, 5, 10])
        h = convex_polygon(4, 8, coord)
        print(len(h))
        for (x, y) in h:
            print(x, y)
else:
    # veliki test: n = 5000 vrhova na (skoro) kružnici, uz nekoliko kolinearnih
    import math
    n = 5000
    pts = set()
    R = 4 * 10**8
    cx = cy = 5 * 10**8
    while len(pts) < n:
        t = random.random() * 2 * math.pi
        pts.add((cx + int(R * math.cos(t)), cy + int(R * math.sin(t))))
    h = hull_keep_collinear(list(pts))
    print(1)
    print(len(h))
    print("\n".join(f"{x} {y}" for x, y in h))
