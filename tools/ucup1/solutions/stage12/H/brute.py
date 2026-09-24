# Brute force: tocka je u konveksnoj ljusci tocno kada lezi u nekom
# nedegeneriranom tetraedru s vrhovima iz skupa (Caratheodory).
import sys
from itertools import combinations
data = list(map(int, sys.stdin.read().split()))
n, K = data[0], data[1]
P = [(data[2 + 3 * i] * K, data[3 + 3 * i] * K, data[4 + 3 * i] * K) for i in range(n)]

def orient(a, b, c, d):
    ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
    wx, wy, wz = d[0] - a[0], d[1] - a[1], d[2] - a[2]
    return ux * (vy * wz - vz * wy) - uy * (vx * wz - vz * wx) + uz * (vx * wy - vy * wx)

tets = []
for a, b, c, d in combinations(P, 4):
    o = orient(a, b, c, d)
    if o != 0:
        tets.append((a, b, c, d, o))

def inside(q):
    for a, b, c, d, o in tets:
        s = 1 if o > 0 else -1
        if all(s * v >= 0 for v in (orient(a, b, c, q), orient(a, b, q, d), orient(a, q, c, d), orient(q, b, c, d))):
            return True
    return False

B = max(abs(v) for p in P for v in p)
cnt = 0
for x in range(-B, B + 1):
    for y in range(-B, B + 1):
        for z in range(-B, B + 1):
            if inside((x, y, z)):
                cnt += 1
print(cnt % 998244353)
