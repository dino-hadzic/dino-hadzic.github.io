# Neovisna provjera: (1) slicnost odredimo matricno (skaliranje r, rotacijska matrica, zrcaljenje) i
# provjerimo da preslikava sva 4 vrha karte u vrhove parka; (2) odgovor = min po (i, j) kao u rjesenju;
# (3) sanity check optimalnosti: nasumicne dopustene strategije (proizvoljan redoslijed teleporta u oba
# smjera s hodanjem izmedu) nikad ne smiju biti jeftinije od odgovora.
import sys, math, random
random.seed(12345)
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    P = [(int(data[p + 2 * i]), int(data[p + 2 * i + 1])) for i in range(4)]; p += 8
    M = [(int(data[p + 2 * i]), int(data[p + 2 * i + 1])) for i in range(4)]; p += 8
    s = (int(data[p]), int(data[p + 1])); t = (int(data[p + 2]), int(data[p + 3])); p += 4
    k, n = int(data[p]), int(data[p + 1]); p += 2

    def sub(a, b): return (a[0] - b[0], a[1] - b[1])
    def norm(a): return math.hypot(a[0], a[1])
    u = sub(M[1], M[0]); v = sub(P[1], P[0])
    r = norm(v) / norm(u)
    # rotacija koja u/|u| prevodi u v/|v|
    c = (u[0] * v[0] + u[1] * v[1]) / (norm(u) * norm(v))
    sn = (u[0] * v[1] - u[1] * v[0]) / (norm(u) * norm(v))
    def f_try(mirror):
        def f(z):
            x, y = sub(z, M[0])
            if mirror:  # zrcaljenje preko pravca kroz u (prije rotacije)
                ux, uy = u[0] / norm(u), u[1] / norm(u)
                d = x * ux + y * uy; e = -x * uy + y * ux
                x, y = d * ux + e * uy, d * uy - e * ux
            X = r * (c * x - sn * y); Y = r * (sn * x + c * y)
            return (P[0][0] + X, P[0][1] + Y)
        return f
    f = None
    for mirror in (False, True):
        g = f_try(mirror)
        if all(norm(sub(g(M[i]), P[i])) < 1e-6 for i in range(4)):
            f = g; break
    assert f is not None
    def finv(w):
        # inverz numericki: f je afina, rijesimo 2x2 sustav preko slike baze
        o = f((0.0, 0.0)); ex = sub(f((1.0, 0.0)), o); ey = sub(f((0.0, 1.0)), o)
        det = ex[0] * ey[1] - ex[1] * ey[0]
        wx, wy = sub(w, o)
        return ((wx * ey[1] - wy * ey[0]) / det, (ex[0] * wy - ex[1] * wx) / det)
    S = [s]; Tt = [t]
    for i in range(n): S.append(finv(S[-1])); Tt.append(finv(Tt[-1]))
    best = min((i + j) * k + norm(sub(S[i], Tt[j])) for i in range(n + 1) for j in range(n + 1 - i))

    # je li tocka na karti (u pravokutniku M)? -> provjera preko inverzne slike u park [0,W]x[0,H]
    W = norm(sub(P[1], P[0])); H = norm(sub(P[2], P[1]))
    def in_map(z):
        w = f(z)
        d = sub(w, P[0]); a = sub(P[1], P[0]); bb = sub(P[3], P[0])
        pa = (d[0] * a[0] + d[1] * a[1]) / (W * W); pb = (d[0] * bb[0] + d[1] * bb[1]) / (H * H)
        return -1e-9 <= pa <= 1 + 1e-9 and -1e-9 <= pb <= 1 + 1e-9
    def rand_in_park():
        a = random.random(); b = random.random()
        return (P[0][0] + a * (P[1][0] - P[0][0]) + b * (P[3][0] - P[0][0]),
                P[0][1] + a * (P[1][1] - P[0][1]) + b * (P[3][1] - P[0][1]))
    for _ in range(300):
        m = random.randint(0, n)
        cur = s; cost = 0.0; ok = True
        for step in range(m):
            if random.random() < 0.5:
                nxt = rand_in_park(); cost += norm(sub(nxt, cur)); cur = nxt
            if random.random() < 0.5:
                cur = finv(cur)
            else:
                if not in_map(cur): ok = False; break
                cur = f(cur)
            cost += k
        if not ok: continue
        cost += norm(sub(t, cur))
        if cost < best - 1e-7:
            best = -1.0  # optimalnost narusena -> namjerno krivi odgovor
            break
    out.append('%.10f' % best)
print('\n'.join(out))
