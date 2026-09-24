import sys
from itertools import permutations
# Iscrpno: sve uređene šestorke (a, b, c, d, e, f) različitih vrhova, a < b,
# s bridovima ab, bc, ca, cd, de, ef.
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
adj = [[False] * n for _ in range(n)]
for i in range(m):
    u, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    adj[u][v] = adj[v][u] = True
cnt = 0
for a, b, c, d, e, f in permutations(range(n), 6):
    if a < b and adj[a][b] and adj[b][c] and adj[c][a] and adj[c][d] and adj[d][e] and adj[e][f]:
        cnt += 1
print(cnt % 998244353)
