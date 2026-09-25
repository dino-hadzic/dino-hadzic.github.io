# Sporo rješenje: za svaki par vrhova provjeri da oba dijela imaju pozitivnu
# površinu (formulom za površinu), pa dijametre računaj po definiciji.
import sys
def main():
    data = sys.stdin.read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        n = int(data[p]); p += 1
        pts = []
        for i in range(n):
            pts.append((int(data[p]), int(data[p + 1]))); p += 2
        def area2(idx):
            s = 0
            for k in range(len(idx)):
                (x1, y1) = pts[idx[k]]; (x2, y2) = pts[idx[(k + 1) % len(idx)]]
                s += x1 * y2 - x2 * y1
            return abs(s)
        def diam(idx):
            b = 0
            for a in idx:
                for c in idx:
                    b = max(b, (pts[a][0] - pts[c][0]) ** 2 + (pts[a][1] - pts[c][1]) ** 2)
            return b
        best = None
        for i in range(n):
            for j in range(i + 1, n):
                q = list(range(i, j + 1))
                r = list(range(j, n)) + list(range(0, i + 1))
                if len(q) < 3 or len(r) < 3 or area2(q) == 0 or area2(r) == 0:
                    continue
                v = diam(q) + diam(r)
                if best is None or v < best:
                    best = v
        out.append(str(best))
    print("\n".join(out))
main()
