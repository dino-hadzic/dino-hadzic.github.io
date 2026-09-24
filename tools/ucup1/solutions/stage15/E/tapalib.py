# Provjera rjesenja po izvornom pravilu Tape: oko svakog traga osjencane celije cine jedan
# uzastopan blok (u kruznom poretku 8 susjeda; celije izvan mreze racunaju se kao neosjencane).
RING = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def valjano(n, m, grid, sol):
    R, C = 2 * n - 1, 2 * m - 1
    if len(sol) != R or any(len(row) != C for row in sol):
        return 'kriva dimenzija'
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '.':
                if sol[i][j] != grid[i][j]: return 'trag promijenjen'
            elif sol[i][j] not in '.#':
                return 'nedopusten znak'
    for a in range(n):
        for b in range(m):
            r, c = 2 * a, 2 * b
            bits = []
            for dr, dc in RING:
                rr, cc = r + dr, c + dc
                bits.append(1 if 0 <= rr < R and 0 <= cc < C and sol[rr][cc] == '#' else 0)
            k = sum(bits)
            if k != int(grid[r][c]): return 'krivi broj oko traga (%d,%d)' % (r, c)
            # broj prijelaza 0->1 u kruznom nizu mora biti tocno 1 (ili 0 ako je sve osjencano)
            prijelazi = sum(1 for i in range(8) if bits[i] == 1 and bits[i - 1] == 0)
            if k == 8:
                continue
            if prijelazi != 1: return 'nisu uzastopne oko traga (%d,%d)' % (r, c)
    return None
