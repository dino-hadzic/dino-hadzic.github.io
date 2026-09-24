import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
g = [list(data[2 + i]) for i in range(n)]
MOD = 998244353
# orijentacija = par ćelija kutije 3x3 koje nedostaju
MISS = [((0, 1), (1, 1)), ((1, 1), (2, 1)), ((1, 0), (1, 1)), ((1, 1), (1, 2))]
CELLS = [[(dr, dc) for dr in range(3) for dc in range(3) if (dr, dc) not in miss] for miss in MISS]

def count(pos):
    # pos = linearni indeks; nađi prvu slobodnu ćeliju
    while pos < n * m and g[pos // m][pos % m] != '0':
        pos += 1
    if pos == n * m:
        return 1
    i, j = pos // m, pos % m
    total = 0
    for cells in CELLS:
        ok = True
        for dr, dc in cells:
            r, c = i + dr, j + dc
            if r >= n or c >= m or g[r][c] != '0':
                ok = False; break
        if not ok:
            continue
        for dr, dc in cells:
            g[i + dr][j + dc] = 'x'
        total += count(pos + 1)
        for dr, dc in cells:
            g[i + dr][j + dc] = '0'
    return total

print(count(0) % MOD)
