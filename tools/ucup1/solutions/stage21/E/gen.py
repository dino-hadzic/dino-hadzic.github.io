import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def hull(pts, keep_collinear):
    pts = sorted(set(pts))
    if len(pts) <= 2: return pts
    def cr(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    def half(seq):
        h = []
        for q in seq:
            while len(h) >= 2 and (cr(h[-2], h[-1], q) < 0 or (cr(h[-2], h[-1], q) == 0 and not keep_collinear)): h.pop()
            h.append(q)
        return h
    lo = half(pts); up = half(pts[::-1])
    return lo[:-1] + up[:-1]
def poly(m, C, keep):
    while True:
        pts = [(random.randint(-C, C), random.randint(-C, C)) for _ in range(m)]
        h = hull(pts, keep)
        if len(h) >= 3: return h
if mode == 'big':
    T = 1; print(T)
    # veliki poligon: točke na kružnici (radijus ~1e9), zaokružene, pa konveksna ljuska
    import math
    m = 100000; R = 10**9
    pts = [(int(R*math.cos(2*math.pi*i/m)), int(R*math.sin(2*math.pi*i/m))) for i in range(m)]
    h = hull(pts, False)
    n = len(h); print(n, random.randint(1, n - 2))
    print('\n'.join(f'{a} {b}' for a, b in h))
else:
    T = random.randint(1, 5); print(T)
    for _ in range(T):
        h = poly(random.randint(3, 12), random.choice([3, 5, 20, 10**9]), random.random() < 0.4)
        n = len(h); print(n, random.randint(1, n - 2))
        for a, b in h: print(a, b)
