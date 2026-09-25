# Brute force: sažmi koordinate u segmente s konstantnim skupom dodirnutih pravokutnika,
# pa izbroji sve neuređene trojke različitih pravaca (s multiplicitetima segmenata).
import sys
MOD = 998244353; C = 10**9
def segments(iv):
    # iv: lista (l, r); vraća listu (duljina, maska pokrivenih) za particiju [1, C]
    pts = sorted(set([1, C + 1] + [l for l, r in iv] + [r + 1 for l, r in iv]))
    res = []
    for a, b in zip(pts, pts[1:]):
        mask = 0
        for i, (l, r) in enumerate(iv):
            if l <= a <= r: mask |= 1 << i
        res.append((b - a, mask))
    return res
def c2(x): return x * (x - 1) // 2
def c3(x): return x * (x - 1) * (x - 2) // 6
def three(seg, full):
    k = len(seg); tot = 0
    for i in range(k):
        li, mi = seg[i]
        if mi == full: tot += c3(li)
        for j in range(i + 1, k):
            lj, mj = seg[j]
            if mi | mj == full: tot += c2(li) * lj + li * c2(lj)
            for t in range(j + 1, k):
                lt, mt = seg[t]
                if mi | mj | mt == full: tot += li * lj * lt
    return tot
def two_one(seg2, seg1, full):
    tot = 0
    pairs = []
    k = len(seg2)
    for i in range(k):
        pairs.append((c2(seg2[i][0]), seg2[i][1]))
        for j in range(i + 1, k): pairs.append((seg2[i][0] * seg2[j][0], seg2[i][1] | seg2[j][1]))
    for cnt, m in pairs:
        for l1, m1 in seg1:
            if m | m1 == full: tot += cnt * l1
    return tot
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
for _ in range(T):
    n = int(data[p]); p += 1
    X, Y = [], []
    for i in range(n):
        x1, y1, x2, y2 = map(int, data[p:p + 4]); p += 4
        X.append((x1, x2)); Y.append((y1, y2))
    full = (1 << n) - 1
    sx, sy = segments(X), segments(Y)
    ans = three(sx, full) + three(sy, full) + two_one(sx, sy, full) + two_one(sy, sx, full)
    print(ans % MOD)
