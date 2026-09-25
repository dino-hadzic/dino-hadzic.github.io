import sys
# check.py <ulaz> <ocekivani ili -> <dobiveni>
# Neovisni validator za output-only zadatak A:
#  - format, rasponi, razliciti vrhovi, jednostavan CCW poligon (O(N^2) test presjeka),
#  - svaki flipturn: (a,b) i (c,d) su vrhovi na rubu trenutne ljuske i CCW put
#    izmedu njih nema drugih tocaka na rubu ljuske; put se zatim zrcali kroz poloviste,
#  - na kraju poligon mora biti konveksan (svi vrhovi na ljusci, svi zavoji lijevo).
# Ljuska se za N <= 120 racuna ispocetka nakon svakog koraka (monotoni lanac);
# za velike N koristi se inkrementalno azuriranje (ljuska pri flipturnu samo raste).
inp = open(sys.argv[1]).read().split()
got = open(sys.argv[3]).read().split()
wantN = int(inp[0]) if inp else None

def fail(msg):
    print(msg); sys.exit(1)

try:
    pos = 0
    N = int(got[pos]); pos += 1
    if not (3 <= N <= 1000): fail('los N')
    if wantN is not None and N != wantN: fail('N nije jednak trazenom')
    P = []
    for i in range(N):
        x, y = int(got[pos]), int(got[pos + 1]); pos += 2
        if not (0 <= x <= 10**9 and 0 <= y <= 10**9): fail('koordinata izvan raspona')
        P.append((x, y))
    Q = int(got[pos]); pos += 1
    if wantN is None and not (120000 <= Q <= 1000000): fail('Q izvan [120000, 1000000]')
    if not (1 <= Q <= 1000000): fail('los Q')
    moves = []
    for i in range(Q):
        a, b, c, d = (int(got[pos + k]) for k in range(4)); pos += 4
        for v in (a, b, c, d):
            if not (0 <= v <= 10**9): fail('koordinata poteza izvan raspona')
        if (a, b) == (c, d): fail('u == v')
        moves.append((a, b, c, d))
    if pos != len(got): fail('visak tokena')
except (ValueError, IndexError):
    fail('los format')

if len(set(P)) != N: fail('vrhovi nisu razliciti')

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

area2 = sum(P[i][0] * P[(i + 1) % N][1] - P[(i + 1) % N][0] * P[i][1] for i in range(N))
if area2 <= 0: fail('poligon nije CCW')

# jednostavnost: nijedan par nesusjednih bridova se ne sijece i ne dodiruje
def on_seg(a, b, q):
    return cross(a, b, q) == 0 and min(a[0], b[0]) <= q[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= q[1] <= max(a[1], b[1])

def seg_intersect(a, b, c, d):
    d1, d2 = cross(c, d, a), cross(c, d, b)
    d3, d4 = cross(a, b, c), cross(a, b, d)
    if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0:
        return True
    return on_seg(c, d, a) or on_seg(c, d, b) or on_seg(a, b, c) or on_seg(a, b, d)

import numpy as np
X = np.array([p[0] for p in P], dtype=np.int64)
Y = np.array([p[1] for p in P], dtype=np.int64)
X2, Y2 = np.roll(X, -1), np.roll(Y, -1)
for i in range(N):
    js = np.array([j for j in range(N) if j != i and j != (i + 1) % N and (j + 1) % N != i], dtype=np.int64)
    ax, ay, bx, by = X[i], Y[i], X2[i], Y2[i]
    cx, cy, dx, dy = X[js], Y[js], X2[js], Y2[js]
    d1 = (dx - cx) * (ay - cy) - (dy - cy) * (ax - cx)
    d2 = (dx - cx) * (by - cy) - (dy - cy) * (bx - cx)
    d3 = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    d4 = (bx - ax) * (dy - ay) - (by - ay) * (dx - ax)
    proper = ((d1 > 0) != (d2 > 0)) & ((d3 > 0) != (d4 > 0)) & (d1 != 0) & (d2 != 0) & (d3 != 0) & (d4 != 0)
    if proper.any(): fail('poligon se samopresijeca')
    if (d1 == 0).any() or (d2 == 0).any() or (d3 == 0).any() or (d4 == 0).any():
        for j in js[(d1 == 0) | (d2 == 0) | (d3 == 0) | (d4 == 0)]:
            j = int(j)
            if seg_intersect(P[i], P[(i + 1) % N], P[j], P[(j + 1) % N]): fail('poligon se dodiruje')

def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2: return pts
    lo, up = [], []
    for q in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0: lo.pop()
        lo.append(q)
    for q in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], q) <= 0: up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]

pts = list(P)
idx = {p: i for i, p in enumerate(pts)}
FULL = N <= 120

H = hull(pts)
if FULL:
    def flags_full():
        f = [False] * N
        Hn = len(H)
        for t in range(N):
            f[t] = any(on_seg(H[k], H[(k + 1) % Hn], pts[t]) for k in range(Hn))
        return f
    onb = flags_full()
else:
    HX = np.array([h[0] for h in H], dtype=np.int64); HY = np.array([h[1] for h in H], dtype=np.int64)
    def edge_flags(ax, ay, bx, by):
        # koji od svih N vrhova leze na segmentu (a,b)
        cr = (bx - ax) * (Y - ay) - (by - ay) * (X - ax)
        return (cr == 0) & (np.minimum(ax, bx) <= X) & (X <= np.maximum(ax, bx)) & (np.minimum(ay, by) <= Y) & (Y <= np.maximum(ay, by))
    onb_np = np.zeros(N, dtype=bool)
    Hn = len(H)
    for k in range(Hn):
        onb_np |= edge_flags(HX[k], HY[k], HX[(k + 1) % Hn], HY[(k + 1) % Hn])

    def insert_point(t):
        # ubaci vrh t u ljusku (ljuska samo raste) i azuriraj oznake
        global HX, HY, onb_np
        qx, qy = pts[t]
        Hn = len(HX)
        cr = (np.roll(HX, -1) - HX) * (qy - HY) - (np.roll(HY, -1) - HY) * (qx - HX)
        vis = cr < 0
        if not vis.any():
            onb_np[t] = bool((cr == 0).any())
            return
        if vis.all(): fail('interna greska: svi bridovi ljuske vidljivi')
        # ciklicki interval vidljivih bridova [i, j]
        prev = np.roll(vis, 1)
        i = int(np.nonzero(vis & ~prev)[0][0])
        j = i
        while vis[(j + 1) % Hn]: j = (j + 1) % Hn
        removed = []
        k = i
        while True:
            removed.append(k)
            if k == j: break
            k = (k + 1) % Hn
        for k in removed:
            onb_np &= ~edge_flags(HX[k], HY[k], HX[(k + 1) % Hn], HY[(k + 1) % Hn])
        hi = (HX[i], HY[i]); hj = (HX[(j + 1) % Hn], HY[(j + 1) % Hn])
        onb_np |= edge_flags(hi[0], hi[1], qx, qy)
        onb_np |= edge_flags(qx, qy, hj[0], hj[1])
        keep = []
        k = (j + 1) % Hn
        while True:
            keep.append(k)
            if k == i: break
            k = (k + 1) % Hn
        HX = np.append(HX[keep], qx); HY = np.append(HY[keep], qy)

for step, (a, b, c, d) in enumerate(moves):
    if (a, b) not in idx or (c, d) not in idx: fail('korak %d: tocka nije vrh poligona' % step)
    u, v = idx[(a, b)], idx[(c, d)]
    if FULL:
        if not (onb[u] and onb[v]): fail('korak %d: u ili v nije na rubu ljuske' % step)
    else:
        if not (onb_np[u] and onb_np[v]): fail('korak %d: u ili v nije na rubu ljuske' % step)
    path = []
    k = (u + 1) % N
    while k != v:
        path.append(k); k = (k + 1) % N
    if not path: fail('korak %d: put u-v je jedan brid' % step)
    for k in path:
        if (onb[k] if FULL else onb_np[k]): fail('korak %d: tocka na rubu ljuske unutar puta' % step)
    sx, sy = a + c, b + d
    old = [pts[k] for k in path]
    for k in path: del idx[pts[k]]
    for m, k in enumerate(path):
        w = old[len(path) - 1 - m]
        npnt = (sx - w[0], sy - w[1])
        if npnt in idx: fail('korak %d: vrhovi se poklapaju' % step)
        pts[k] = npnt; idx[npnt] = k
    if FULL:
        H = hull(pts); onb = flags_full()
    else:
        for k in path:
            X[k], Y[k] = pts[k]
        for k in path:
            insert_point(k)

# zavrsni poligon: svi vrhovi na ljusci i svi zavoji lijevo (ili ravno)
final_on = onb if FULL else list(onb_np)
if not all(final_on): fail('zavrsni poligon nije konveksan (vrh unutar ljuske)')
for i in range(N):
    if cross(pts[i - 1], pts[i], pts[(i + 1) % N]) < 0: fail('zavrsni poligon ima desni zavoj')
sys.exit(0)
