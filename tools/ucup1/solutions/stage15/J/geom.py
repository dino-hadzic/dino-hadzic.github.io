# Cjelobrojna geometrija: presjek dvaju segmenata (ukljucujuci dodir).
def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def on_seg(p, a, b):
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def sijeku(a, b, c, d):
    d1 = cross(c, d, a); d2 = cross(c, d, b); d3 = cross(a, b, c); d4 = cross(a, b, d)
    if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 and d2 and d3 and d4: return True
    return on_seg(a, c, d) or on_seg(b, c, d) or on_seg(c, a, b) or on_seg(d, a, b)
def jednostavan(P):
    n = len(P)
    if len(set(P)) != n: return False
    for i in range(n):
        a, b, c = P[i], P[(i + 1) % n], P[(i + 2) % n]
        if cross(a, b, c) == 0: return False
    for i in range(n):
        for j in range(i + 1, n):
            if j == i + 1 or (i == 0 and j == n - 1): continue
            if sijeku(P[i], P[(i + 1) % n], P[j], P[(j + 1) % n]): return False
    return True
