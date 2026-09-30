# Brute force: memoizirana pretraga po podskupu odigranih polja; simuliramo pravila igre
# (igra zavrsava odmah nakon pobjednickog poteza ili kad je ploca puna).
import sys
from functools import lru_cache
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, k = int(d[p]), int(d[p+1]); p += 2
    b = d[p:p+n]; p += n
    cells = [(i, j) for i in range(n) for j in range(n) if b[i][j] != '.']
    idx = {c: t for t, c in enumerate(cells)}
    full = (1 << len(cells)) - 1
    lines = []
    for i in range(n):
        for j in range(n):
            for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
                cs = [(i + t * dx, j + t * dy) for t in range(k)]
                if all(0 <= x < n and 0 <= y < n for x, y in cs): lines.append(cs)
    def wins(mask, sym):
        for cs in lines:
            if all(c in idx and mask >> idx[c] & 1 and b[c[0]][c[1]] == sym for c in cs): return True
        return False
    @lru_cache(maxsize=None)
    def go(mask, turn):
        # vraca listu poteza od stanja mask (na potezu turn) do zavrsne ploce, ili None
        if mask == full:
            # bez pobjede igra zavrsava samo na punoj ploci
            return [] if len(cells) == n * n else None
        for t, c in enumerate(cells):
            if mask >> t & 1 or b[c[0]][c[1]] != turn: continue
            m2 = mask | 1 << t
            if wins(m2, turn):
                if m2 == full: return [c]
                continue
            r = go(m2, 'o' if turn == 'x' else 'x')
            if r is not None: return [c] + r
        return None
    res = None
    if cells:
        for start in 'xo':
            r = go(0, start)
            if r is not None:
                res = r; break
    if res is None: out.append("NIE")
    else:
        out.append("TAK")
        for i, j in res: out.append(f"{i+1} {j+1}")
print('\n'.join(out))
