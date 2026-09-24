import random, sys, math
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def orient(a, b, c, d):
    ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
    wx, wy, wz = d[0] - a[0], d[1] - a[1], d[2] - a[2]
    return ux * (vy * wz - vz * wy) - uy * (vx * wz - vz * wx) + uz * (vx * wy - vy * wx)

def coplanar(pts):
    from itertools import combinations
    return all(orient(*c) == 0 for c in combinations(pts, 4))

if mode == 'big':
    n, K = 100, random.randint(1, 10 ** 15)
    R = 200
else:
    n = random.randint(4, 6)
    K = random.choice([1, 1, 2, 2, 3, 4])
    R = random.choice([1, 2, 3])
while True:
    pts = set()
    while len(pts) < n:
        if mode == 'big' and seed % 2 == 0:
            # tocke blizu sfere: ljuska ima najvise stranica (2N-4)
            th = random.random() * 2 * math.pi; ph = math.acos(2 * random.random() - 1)
            pts.add((round(R * math.sin(ph) * math.cos(th)), round(R * math.sin(ph) * math.sin(th)), round(R * math.cos(ph))))
        else:
            pts.add((random.randint(-R, R), random.randint(-R, R), random.randint(-R, R)))
    pts = list(pts)
    if mode == 'big' or not coplanar(pts):
        break
print(n, K)
for p in pts:
    print(*p)
