import sys
# Doslovna simulacija: dok poligon nije konveksan, nadi dzep (put izmedu dva
# susjedna vrha na rubu konveksne ljuske) i zrcali ga kroz poloviste tetive.
data = sys.stdin.read().split()
n = int(data[0])
P = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2: return pts
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

def on_hull_boundary(H, p):
    m = len(H)
    for i in range(m):
        if cross(H[i], H[(i + 1) % m], p) < 0: return False
    for i in range(m):
        if cross(H[i], H[(i + 1) % m], p) == 0: return True
    return False

while True:
    H = hull(P)
    on = [on_hull_boundary(H, p) for p in P]
    if all(on): break
    u = next(i for i in range(n) if on[i] and not on[(i + 1) % n])
    v = (u + 1) % n
    while not on[v]: v = (v + 1) % n
    sx, sy = P[u][0] + P[v][0], P[u][1] + P[v][1]
    path = []
    k = (u + 1) % n
    while k != v:
        path.append(P[k]); k = (k + 1) % n
    path.reverse()
    k = (u + 1) % n
    for w in path:
        P[k] = (sx - w[0], sy - w[1]); k = (k + 1) % n

# izbaci kolinearne vrhove, pocni od leksikografski najmanjeg
Q = [p for i, p in enumerate(P) if cross(P[i - 1], p, P[(i + 1) % n]) != 0]
s = Q.index(min(Q))
Q = Q[s:] + Q[:s]
print(len(Q))
for x, y in Q: print(x, y)
