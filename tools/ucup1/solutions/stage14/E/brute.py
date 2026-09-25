import sys, math

# Svaki krug aproksimiramo pravilnim mnogokutom s mnogo vrhova, izračunamo
# konveksnu ljusku svih točaka (monotoni lanac) i provjerimo je li ishodište
# unutar nje. Generator odbacuje ulaze u kojima je ishodište preblizu rubu.
K = 720

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

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = []
    for i in range(n):
        x, y, r = map(int, data[1 + 3 * i:4 + 3 * i])
        if r == 0:
            pts.append((float(x), float(y)))
        else:
            for k in range(K):
                t = 2 * math.pi * k / K
                pts.append((x + r * math.cos(t), y + r * math.sin(t)))
    h = hull(pts)
    if len(h) < 3:
        # degenerirano: segment ili točka
        if len(h) == 1:
            print('Yes' if abs(h[0][0]) < 1e-9 and abs(h[0][1]) < 1e-9 else 'No')
            return
        a, b = h
        c = cross(a, b, (0.0, 0.0))
        on = abs(c) < 1e-7 and min(a[0], b[0]) - 1e-9 <= 0 <= max(a[0], b[0]) + 1e-9 \
            and min(a[1], b[1]) - 1e-9 <= 0 <= max(a[1], b[1]) + 1e-9
        print('Yes' if on else 'No')
        return
    inside = True
    m = len(h)
    for i in range(m):
        if cross(h[i], h[(i + 1) % m], (0.0, 0.0)) < 0:
            inside = False
    print('Yes' if inside else 'No')

main()
