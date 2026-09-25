# Checker: YES + n-1 segmenata s cjelobrojnim koordinatama u [0, 1e9]; svaki segment dira <= 2 diska
# (egzaktna cjelobrojna geometrija), segmenti se ne sijeku osim u zajednickoj krajnjoj tocki,
# graf disk-segment je povezan.
import sys
def main():
    inp = open(sys.argv[1]).read().split()
    got = open(sys.argv[3]).read().split()
    n = int(inp[0]); D = [(int(inp[1+3*i]), int(inp[2+3*i]), int(inp[3+3*i])) for i in range(n)]
    if not got or got[0] != "YES": print("ocekujem YES"); sys.exit(1)
    vals = got[1:]
    if len(vals) != 4 * (n - 1): print("krivi broj brojeva"); sys.exit(1)
    seg = [tuple(int(v) for v in vals[4*i:4*i+4]) for i in range(n - 1)]
    for (x1, y1, x2, y2) in seg:
        if (x1, y1) == (x2, y2): print("degeneriran segment"); sys.exit(1)
        for v in (x1, y1, x2, y2):
            if v < 0 or v > 10**9: print("koordinata izvan raspona"); sys.exit(1)
    def dist2_le(px, py, ax, ay, bx, by, r):
        # je li udaljenost tocke P od segmenta AB <= r  (egzaktno)
        dx, dy = bx - ax, by - ay
        L = dx*dx + dy*dy
        t = (px - ax) * dx + (py - ay) * dy           # projekcija * L
        if t <= 0: qx, qy = ax, ay; return (px-qx)**2 + (py-qy)**2 <= r*r
        if t >= L: qx, qy = bx, by; return (px-qx)**2 + (py-qy)**2 <= r*r
        # najbliza tocka je unutrasnja: udaljenost^2 = cross^2 / L
        cr = (px - ax) * dy - (py - ay) * dx
        return cr * cr <= r * r * L
    parent = list(range(n))
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for (x1, y1, x2, y2) in seg:
        touched = [i for i, (cx, cy, cr) in enumerate(D) if dist2_le(cx, cy, x1, y1, x2, y2, cr)]
        if len(touched) > 2: print("segment dira", len(touched), "diskova"); sys.exit(1)
        if len(touched) == 2: parent[find(touched[0])] = find(touched[1])
    if len({find(i) for i in range(n)}) != 1: print("nije povezano"); sys.exit(1)
    def cross(ox, oy, ax, ay, bx, by): return (ax-ox)*(by-oy) - (ay-oy)*(bx-ox)
    def on_seg(px, py, ax, ay, bx, by):
        return cross(ax, ay, bx, by, px, py) == 0 and min(ax,bx) <= px <= max(ax,bx) and min(ay,by) <= py <= max(ay,by)
    def intersect(s, t):
        ax, ay, bx, by = s; cx, cy, dx, dy = t
        d1 = cross(cx, cy, dx, dy, ax, ay); d2 = cross(cx, cy, dx, dy, bx, by)
        d3 = cross(ax, ay, bx, by, cx, cy); d4 = cross(ax, ay, bx, by, dx, dy)
        if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 and d2 and d3 and d4: return True
        return on_seg(ax, ay, cx, cy, dx, dy) or on_seg(bx, by, cx, cy, dx, dy) or on_seg(cx, cy, ax, ay, bx, by) or on_seg(dx, dy, ax, ay, bx, by)
    for i in range(len(seg)):
        for j in range(i + 1, len(seg)):
            s, t = seg[i], seg[j]
            if not intersect(s, t): continue
            # dopusteno samo dijeljenje tocno jedne krajnje tocke, bez dodatnog preklapanja
            P = {(s[0], s[1]), (s[2], s[3])}; Q = {(t[0], t[1]), (t[2], t[3])}
            common = P & Q
            if len(common) != 1: print("segmenti se sijeku"); sys.exit(1)
            (px, py), = common
            # jedini presjek smije biti ta tocka: provjeri da druge krajnje tocke nisu na drugom segmentu
            for (ex, ey) in (P - common):
                if on_seg(ex, ey, *t): print("segmenti se preklapaju"); sys.exit(1)
            for (ex, ey) in (Q - common):
                if on_seg(ex, ey, *s): print("segmenti se preklapaju"); sys.exit(1)
            # kolinearni s zajednickom tockom u istom smjeru -> preklapanje (pokriveno gore), inace OK
    print("OK")
main()
