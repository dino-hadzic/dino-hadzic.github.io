# Neovisna implementacija: ploca u kubnim koordinatama (x+y+z=0) kao unija dvaju velikih trokuta,
# potezi se traze DFS-om, a skok se provjerava eksplicitnim nabrajanjem polja segmenta.
import sys
sys.setrecursionlimit(10000)
board = set()
for x in range(-12, 13):
    for y in range(-12, 13):
        z = -x - y
        if (x >= -4 and y >= -4 and z >= -4) or (x <= 4 and y <= 4 and z <= 4):
            board.add((x, y, z))
rows = {}
for c in board: rows.setdefault(c[2], []).append(c)
for z in rows: rows[z].sort()            # po x: lijevo -> desno (zrcaljenje ne mijenja odgovor)
zs = sorted(rows)
def cell(row, col): return rows[zs[row - 1]][col - 1]
DIRS = [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1)]
def add(a, d, k=1): return (a[0] + k * d[0], a[1] + k * d[1], a[2] + k * d[2])
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    S = set()
    for i in range(n):
        S.add(cell(int(data[p]), int(data[p + 1]))); p += 2
    total = 0
    for a in S:
        others = S - {a}
        seen = set()
        def dfs(pos):
            for d in DIRS:
                for k in range(1, 30):
                    b = add(pos, d, k)
                    if b not in board: break
                    if b in others:
                        tgt = add(pos, d, 2 * k)
                        seg = [add(pos, d, t) for t in range(1, 2 * k + 1)]
                        if tgt in board and all(c not in others for c in seg if c != b) and tgt != a and tgt not in seen:
                            seen.add(tgt); dfs(tgt)
                        break
        dfs(a)
        total += len(seen)
    out.append(str(total))
print('\n'.join(out))
