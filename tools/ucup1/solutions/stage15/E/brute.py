# Iscrpno po svim osjencanjima celija bez traga (do 17 celija); ispisuje YES/NO.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tapalib import valjano
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1]); grid = data[2:2 + 2 * n - 1]
R, C = 2 * n - 1, 2 * m - 1
cells = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == '.']
assert len(cells) <= 17
for mask in range(1 << len(cells)):
    sol = [list(row) for row in grid]
    for t, (i, j) in enumerate(cells):
        sol[i][j] = '#' if mask >> t & 1 else '.'
    if valjano(n, m, grid, [''.join(r) for r in sol]) is None:
        print('YES'); sys.exit(0)
print('NO')
