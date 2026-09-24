import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def rvec(lo, hi):
    while True:
        v = (random.randint(lo, hi), random.randint(lo, hi), random.randint(lo, hi))
        if v != (0, 0, 0): return v

if mode == 'big':
    n = random.choice([500, 500, 499, 499, 497])
    tip = random.choice(['slucajno', 'pravci', 'kolinearni', 'mreza'])
    R = 10 ** 6
else:
    n = random.randint(1, 7)
    tip = random.choice(['slucajno', 'pravci', 'kolinearni', 'kolinearni', 'mreza'])
    R = random.choice([3, 6, 20])

tocke = set()
def dodaj(p):
    if p not in tocke: tocke.add(p)

if tip == 'slucajno':
    while len(tocke) < n: dodaj(rvec(-R, R))
elif tip == 'kolinearni':
    A = rvec(-R, R); u = rvec(-3, 3)
    ts = random.sample(range(-max(n, R) * 2, max(n, R) * 2 + 1), n) if mode == 'small' else random.sample(range(-300000, 300000), n)
    for t in ts: dodaj((A[0] + t * u[0], A[1] + t * u[1], A[2] + t * u[2]))
elif tip == 'pravci':
    k = random.randint(1, 3)
    pravci = [(rvec(-R, R), rvec(-3, 3)) for _ in range(k)]
    lim = 2 * max(n, R) if mode == 'small' else 500
    while len(tocke) < n:
        A, u = random.choice(pravci); t = random.randint(-lim, lim)
        dodaj((A[0] + t * u[0], A[1] + t * u[1], A[2] + t * u[2]))
else:  # mreza
    s = 2 if mode == 'small' else 8
    while len(tocke) < n: dodaj((random.randint(-s, s), random.randint(-s, s), random.randint(0, 1) if mode == 'small' else random.randint(-s, s)))

pts = list(tocke); random.shuffle(pts)
out = [str(n)]
for i, p in enumerate(pts):
    r = random.random()
    if r < 0.45 and n > 1:
        j = random.randrange(n)
        while j == i: j = random.randrange(n)
        v = (pts[j][0] - p[0], pts[j][1] - p[1], pts[j][2] - p[2])
        if random.random() < 0.5:  # ponekad skaliraj (isti smjer)
            v = tuple(x * random.randint(1, 3) for x in v)
        if max(abs(x) for x in v) > 10 ** 6: v = rvec(-R, R)
    elif r < 0.6:
        v = rvec(-1, 1)
    else:
        v = rvec(-R, R)
    out.append("%d %d %d %d %d %d" % (p[0], p[1], p[2], v[0], v[1], v[2]))
print("\n".join(out))
