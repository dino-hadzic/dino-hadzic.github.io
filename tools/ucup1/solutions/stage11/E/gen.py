import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
DIRS = [(1, 0, 1), (0, 1, 1), (3, 4, 5), (4, 3, 5), (-3, 4, 5), (5, 12, 13), (-1, 0, 1), (0, -1, 1), (-4, -3, 5)]
def case(big):
    a, b, L = random.choice(DIRS)
    m, m2 = random.randint(1, 3), random.randint(1, 3)
    S = random.randint(L, L + (40 if big else 6))            # r = S / L >= 1
    if random.random() < 0.15: S = L                          # karta = park (r = 1)
    W, H = m * S, m2 * S
    mirror = random.random() < 0.5
    v1 = (m * a, m * b); v2 = (-m2 * b, m2 * a) if not mirror else (m2 * b, -m2 * a)
    corners = [(0, 0), v1, (v1[0] + v2[0], v1[1] + v2[1]), v2]
    xs = [c[0] for c in corners]; ys = [c[1] for c in corners]
    bw, bh = max(xs) - min(xs), max(ys) - min(ys)
    if bw > W or bh > H:
        return None
    ox = random.randint(0, W - bw) - min(xs); oy = random.randint(0, H - bh) - min(ys)
    Mc = [(x + ox, y + oy) for x, y in corners]
    Pc = [(0, 0), (W, 0), (W, H), (0, H)]
    sx, sy = random.randint(-10**6 if big else -20, 10**6 if big else 20), random.randint(-10**6 if big else -20, 10**6 if big else 20)
    Pc = [(x + sx, y + sy) for x, y in Pc]; Mc = [(x + sx, y + sy) for x, y in Mc]
    rot = random.randint(0, 3); Pc = Pc[rot:] + Pc[:rot]; Mc = Mc[rot:] + Mc[:rot]
    if random.random() < 0.5: Pc.reverse(); Mc.reverse()
    s = (random.randint(0, W) + sx, random.randint(0, H) + sy); t = (random.randint(0, W) + sx, random.randint(0, H) + sy)
    k = random.choice([0, 1, 2, random.randint(0, 10)]) if not big else random.randint(0, 2 * 10**6)
    n = random.randint(0, 5) if not big else 100
    return Pc, Mc, s, t, k, n
tests = []
while len(tests) < (100 if mode == 'big' else random.randint(1, 3)):
    c = case(mode == 'big')
    if c: tests.append(c)
print(len(tests))
for Pc, Mc, s, t, k, n in tests:
    print(' '.join(f'{x} {y}' for x, y in Pc))
    print(' '.join(f'{x} {y}' for x, y in Mc))
    print(s[0], s[1], t[0], t[1])
    print(k, n)
