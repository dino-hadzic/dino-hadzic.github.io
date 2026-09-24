# Referentno rješenje u egzaktnoj aritmetici (Fraction + Decimal na 60 znamenki).
# Nepoznanice (x, y, R): (x - xi)^2 + (y - yi)^2 = (R - di)^2, R >= max di.
# Drugačiji redoslijed eliminacije nego u sol.cpp (parovi A-B i B-C, opći linearni sustav),
# a svaka pronađena kružnica se dodatno numerički provjeri na tangentnost.
import sys
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
getcontext().prec = 60
EPS = Decimal("1e-40")

def dsqrt(v):
    return Decimal(v.numerator).sqrt() / Decimal(v.denominator).sqrt() if isinstance(v, Fr) else v.sqrt()

def fr2dec(f):
    return Decimal(f.numerator) / Decimal(f.denominator)

def roots_ge(a, b, c, M):
    """Korijeni a R^2 + b R + c = 0 (Fraction) koji su >= M; None znači beskonačno."""
    if a == 0 and b == 0:
        return None if c == 0 else []
    if a == 0:
        r = -c / b
        return [fr2dec(r)] if r >= M else []
    D = b * b - 4 * a * c
    if D < 0:
        return []
    A, B = fr2dec(a), fr2dec(b)
    s = dsqrt(D)
    rs = sorted({(-B - s) / (2 * A), (-B + s) / (2 * A)}) if D > 0 else [(-B) / (2 * A)]
    res = []
    for r in rs:
        if r >= Decimal(M) - EPS:
            res.append(r)
    return res

def solve(pts):
    (xa, ya, da), (xb, yb, db), (xc, yc, dc) = pts
    M = max(da, db, dc)
    # L1 (B - A), L2 (C - B):  al*x + be*y = ga + de*R
    def lin(p, q):
        (x1, y1, d1), (x2, y2, d2) = p, q
        return (Fr(2 * (x2 - x1)), Fr(2 * (y2 - y1)),
                Fr(x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1 + d1 * d1 - d2 * d2), Fr(2 * (d2 - d1)))
    a1, b1, g1, e1 = lin(pts[0], pts[1])
    a2, b2, g2, e2 = lin(pts[1], pts[2])
    det = a1 * b2 - a2 * b1
    if det != 0:
        # x = px + qx R, y = py + qy R (Cramer)
        px = (g1 * b2 - g2 * b1) / det; qx = (e1 * b2 - e2 * b1) / det
        py = (a1 * g2 - a2 * g1) / det; qy = (a1 * e2 - a2 * e1) / det
        # (px + qx R - xa)^2 + (py + qy R - ya)^2 = (R - da)^2
        A = qx * qx + qy * qy - 1
        B = 2 * ((px - xa) * qx + (py - ya) * qy + da)
        C = (px - xa) ** 2 + (py - ya) ** 2 - da * da
        rs = roots_ge(A, B, C, M)
        if rs is None:
            return None
        circles = []
        for r in rs:
            x = fr2dec(px) + fr2dec(qx) * r
            y = fr2dec(py) + fr2dec(qy) * r
            circles.append((x, y, r))
        return circles
    # središta kolinearna: y-komponente normala su proporcionalne; problem garantira ya = yb = 0
    # pa je i yc = 0. Rješavamo sustav po (x, R): a1 x - e1 R = g1, a2 x - e2 R = g2.
    assert ya == 0 and yb == 0 and yc == 0
    det2 = a1 * (-e2) - a2 * (-e1)
    if det2 != 0:
        x = (g1 * (-e2) - g2 * (-e1)) / det2
        R = (a1 * g2 - a2 * g1) / det2
        if R < M:
            return []
        y2 = (R - da) ** 2 - (x - xa) ** 2
        if y2 < 0:
            return []
        Rd, xd = fr2dec(R), fr2dec(x)
        if y2 == 0:
            return [(xd, Decimal(0), Rd)]
        yd = dsqrt(y2)
        return [(xd, yd, Rd), (xd, -yd, Rd)]
    # identične ili nekonzistentne jednadžbe
    if a1 * g2 - a2 * g1 != 0:
        return []
    # x = (g1 + e1 R) / a1 ; G(R) = (R - da)^2 - (x - xa)^2 >= 0 na [M, inf)
    p = g1 / a1 - xa; q = e1 / a1
    al = 1 - q * q; be = -2 * da - 2 * p * q; ga = da * da - p * p
    def G(R):
        return al * R * R + be * R + ga
    if al == 0 and be == 0 and ga == 0:
        return None
    # postoji li R >= M s G(R) > 0 ?  (provjera na egzaktnim točkama: M, vrh, veliki R)
    cand = [Fr(M), Fr(M) + 1, Fr(M) + 10 ** 9]
    if al != 0:
        v = -be / (2 * al)
        if v >= M:
            cand.append(v)
    if any(G(R) > 0 for R in cand):
        return None
    # nema pozitivnog dijela: prebroji nultočke >= M
    rs = roots_ge(al, be, ga, M)
    if rs is None:
        return None
    circles = []
    for r in rs:
        x = fr2dec(g1 / a1) + fr2dec(q) * r
        circles.append((x, Decimal(0), r))
    return circles

def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1; out = []
    for _ in range(T):
        pts = []
        for _ in range(3):
            pts.append((int(data[p]), int(data[p + 1]), int(data[p + 2]))); p += 3
        res = solve(pts)
        if res is None:
            out.append("-1")
        elif not res:
            out.append("0")
        else:
            # numerička provjera tangentnosti svake kružnice
            for (x, y, r) in res:
                for (xi, yi, di) in pts:
                    dist = ((x - xi) ** 2 + (y - yi) ** 2).sqrt()
                    assert abs(dist - (r - di)) < Decimal("1e-30"), (pts, x, y, r)
                    assert r >= di - Decimal("1e-30")
            out.append(f"{len(res)} {min(r for _, _, r in res):.12f}")
    print("\n".join(out))

main()
