# Brute force: doslovno slaganje pravokutnika u S x S mrežu backtrackingom –
# uvijek popunjavamo prvu (najgornju-najljeviju) praznu ćeliju, probamo svaki
# nekorišteni pravokutnik u obje orijentacije.
import sys, math
data = sys.stdin.read().split()
rects = [(int(data[2 * i]), int(data[2 * i + 1])) for i in range(4)]
area = sum(w * h for w, h in rects)
S = math.isqrt(area)
if S * S != area:
    print(0); sys.exit()

grid = [[False] * S for _ in range(S)]

def fits(r, c, w, h):
    if r + h > S or c + w > S:
        return False
    for i in range(r, r + h):
        row = grid[i]
        for j in range(c, c + w):
            if row[j]:
                return False
    return True

def fill(r, c, w, h, val):
    for i in range(r, r + h):
        for j in range(c, c + w):
            grid[i][j] = val

def solve(used):
    # nađi prvu praznu ćeliju
    for r in range(S):
        for c in range(S):
            if not grid[r][c]:
                for i in range(4):
                    if used >> i & 1:
                        continue
                    w, h = rects[i]
                    for (ww, hh) in {(w, h), (h, w)}:
                        if fits(r, c, ww, hh):
                            fill(r, c, ww, hh, True)
                            if solve(used | (1 << i)):
                                return True
                            fill(r, c, ww, hh, False)
                return False
    return used == 15

print(1 if solve(0) else 0)
