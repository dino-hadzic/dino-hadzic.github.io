import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def on_seg(a, b, p):
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def seg_inter(a, b, c, d):
    d1, d2 = cross(a, b, c), cross(a, b, d)
    d3, d4 = cross(c, d, a), cross(c, d, b)
    if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 * d2 < 0 and d3 * d4 < 0: return True
    return on_seg(a, b, c) or on_seg(a, b, d) or on_seg(c, d, a) or on_seg(c, d, b)

def simple(P):
    n = len(P)
    for i in range(n):
        a, b = P[i], P[(i + 1) % n]
        if a == b: return False
        c = P[(i + 2) % n]
        if cross(a, b, c) == 0 and (c[0] - b[0]) * (b[0] - a[0]) + (c[1] - b[1]) * (b[1] - a[1]) <= 0: return False
        for j in range(i + 2, n):
            if (j + 1) % n == i: continue
            if seg_inter(a, b, P[j], P[(j + 1) % n]): return False
    return True

def area2(P):
    return sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P)))

if mode == 'big':
    n = 100000; C = 300000
    kind = seed % 3
    if kind == 0:                                  # zvjezdasti poligon
        pts = set()
        while len(pts) < n: pts.add((random.randint(0, C), random.randint(0, C)))
        import math
        P = sorted(pts, key=lambda p: (math.atan2(p[1] - C // 2, p[0] - C // 2), (p[0] - C // 2) ** 2 + (p[1] - C // 2) ** 2))
    else:                                          # cik-cak "cesalj" s mnogo dzepova
        half = n // 2
        P = []
        for i in range(half):
            x = 3 * i
            top = C // 2 if kind == 1 else 3000
            y = random.randint(1, top) if i % 2 else random.randint(0, 50)
            P.append((x, y))
        for i in range(half - 1, -1, -1):
            x = 3 * i + 1
            y = C - (random.randint(1, C // 2 - 100) if i % 2 == 0 else random.randint(0, 50))
            P.append((x, y))
else:
    while True:
        n = random.randint(3, 9); C = random.choice([4, 6, 12])
        pts = set()
        while len(pts) < n: pts.add((random.randint(0, C), random.randint(0, C)))
        P = list(pts); random.shuffle(P)
        if simple(P) and area2(P) != 0: break
    if area2(P) < 0: P.reverse()
print(len(P))
for x, y in P: print(x, y)
