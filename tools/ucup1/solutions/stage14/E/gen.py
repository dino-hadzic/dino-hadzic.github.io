import random, sys, math
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = 1000000
    out = [str(n)]
    half = seed % 2 == 0   # svaki drugi test: svi krugovi u gornjoj poluravnini (odgovor No)
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(5000 if half else -10**6, 10**6)
        if not half and abs(x) < 5000 and abs(y) < 5000:
            x = 5000
        out.append('%d %d %d' % (x, y, random.randint(0, 3000)))
    print('\n'.join(out))
    sys.exit(0)

# mali test: odbacujemo konfiguracije u kojima je ishodište bliže od 1 rubu
# ljuske (uvjet zadatka), da bi brute force s aproksimacijom bio pouzdan
K = 360

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2:
        return pts
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

def seg_dist(a, b):
    ax, ay = a; bx, by = b
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    if L == 0:
        return math.hypot(ax, ay)
    t = max(0.0, min(1.0, -(ax * dx + ay * dy) / L))
    return math.hypot(ax + t * dx, ay + t * dy)

def boundary_dist(circles):
    pts = []
    for x, y, r in circles:
        if r == 0:
            pts.append((float(x), float(y)))
        else:
            for k in range(K):
                t = 2 * math.pi * k / K
                pts.append((x + r * math.cos(t), y + r * math.sin(t)))
    h = hull(pts)
    if len(h) == 1:
        return math.hypot(*h[0])
    return min(seg_dist(h[i], h[(i + 1) % len(h)]) for i in range(len(h)))

while True:
    n = random.randint(1, 6)
    R = random.choice([5, 10, 30])
    circles = []
    for _ in range(n):
        circles.append((random.randint(-R, R), random.randint(-R, R), random.randint(0, R // 2 + 1)))
    if boundary_dist(circles) >= 1.2:
        break
print(n)
for x, y, r in circles:
    print(x, y, r)
