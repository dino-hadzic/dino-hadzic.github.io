import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 5000
    kind = seed % 3
    if kind == 0:   # sve se krizaju: l_i = i, r_i = n + i
        iv = [(i, n + i) for i in range(1, n + 1)]
    elif kind == 1: # nasumicno sparivanje
        pts = list(range(1, 2 * n + 1)); random.shuffle(pts)
        iv = [tuple(sorted(pts[2 * i:2 * i + 2])) for i in range(n)]
    else:           # "ljestve" s malim pomacima (mnogo krizanja)
        iv = []
        pts = list(range(1, 2 * n + 1))
        used = set()
        # parovi (2i-1 + slucajni pomak) -- generiraj kao slucajno sparivanje unutar prozora
        order = list(range(1, 2 * n + 1))
        i = 0
        while i < 2 * n:
            w = min(2 * n - i, 40)
            block = order[i:i + w]; random.shuffle(block)
            for j in range(0, w, 2): iv.append(tuple(sorted(block[j:j + 2])))
            i += w
else:
    n = random.randint(1, 6)
    pts = list(range(1, 2 * n + 1)); random.shuffle(pts)
    iv = [tuple(sorted(pts[2 * i:2 * i + 2])) for i in range(n)]
print(n)
for l, r in iv: print(l, r)
