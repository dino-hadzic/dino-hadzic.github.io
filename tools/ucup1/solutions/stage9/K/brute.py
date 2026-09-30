# Brute force: doslovna simulacija kretanja po pravilima zadatka za svaki x0 u sirokom rasponu.
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
for _ in range(T):
    n, y0 = int(data[p]), int(data[p+1]); p += 2
    pts = []
    for i in range(n):
        pts.append((int(data[p]), int(data[p+1]))); p += 2
    xs = [q[0] for q in pts]
    best = []
    for x0 in range(min(xs) - 2, max(xs) + 3):
        pos = {i: pts[i] for i in range(n)}
        alive = set(range(n))
        while any(pos[i] != (x0, y0) for i in alive):
            newpos = {}
            for i in alive:
                x, y = pos[i]
                if (x, y) == (x0, y0): newpos[i] = (x, y); continue
                cands = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                bestd = min(abs(a - x0) + abs(b - y0) for a, b in cands)
                for cnd in cands:
                    if abs(cnd[0] - x0) + abs(cnd[1] - y0) == bestd:
                        newpos[i] = cnd; break
            where = {}
            for i in alive: where.setdefault(newpos[i], []).append(i)
            for q, lst in where.items():
                if q != (x0, y0) and len(lst) >= 2:
                    for i in lst: alive.discard(i)
            pos = newpos
        best.append(len(alive))
    out.append(f'{min(best)} {max(best)}')
print('\n'.join(out))
