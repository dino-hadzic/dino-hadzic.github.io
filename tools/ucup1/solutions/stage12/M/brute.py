# Iscrpno: najmanji broj boja tako da su vrhovi iste boje medusobno dostizivi
# (u barem jednom smjeru). Ispisuje jedno optimalno bojanje.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
reach = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    reach[a][b] = True
for v in range(1, n + 1):
    reach[v][v] = True
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if reach[i][k]:
            for j in range(1, n + 1):
                if reach[k][j]:
                    reach[i][j] = True
comparable = lambda i, j: reach[i][j] or reach[j][i]
best = None
color = [0] * (n + 1)
def rec(v, used):
    global best
    if best is not None and used >= best[0]:
        return
    if v > n:
        best = (used, color[:])
        return
    for c in range(1, used + 2):
        if all(color[u] != c or comparable(u, v) for u in range(1, v)):
            color[v] = c
            rec(v + 1, max(used, c))
            color[v] = 0
rec(1, 0)
print(*best[1][1:])
