# check.py <ulaz> <očekivano|-> <dobiveno>
# Provjera: broj jedinica = ispisani broj = optimum (iz brute forcea ako postoji,
# inače ceil((N+M)/2)), i simulacija punjenja ispuni cijelu matricu.
import sys
from collections import deque
inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
N, M = map(int, open(inp).read().split())
g = open(got).read().split()
if not g:
    print('prazan izlaz'); sys.exit(1)
c = int(g[0])
cells = g[1:]
if len(cells) != N * M:
    print('krivi broj ćelija', len(cells)); sys.exit(1)
filled = [[cells[i * M + j] == '1' for j in range(M)] for i in range(N)]
if any(v not in ('0', '1') for v in cells):
    print('znak koji nije 0/1'); sys.exit(1)
if sum(map(sum, filled)) != c:
    print('broj jedinica ne odgovara', c); sys.exit(1)
best = (N + M + 1) // 2
if exp != '-':
    e = open(exp).read().split()
    if e:
        best = int(e[0])
if c != best:
    print('nije optimalno', c, best); sys.exit(1)
cnt = [[0] * M for _ in range(N)]
dq = deque()
for i in range(N):
    for j in range(M):
        if filled[i][j]:
            dq.append((i, j))
total = c
while dq:
    i, j = dq.popleft()
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = i + di, j + dj
        if 0 <= x < N and 0 <= y < M and not filled[x][y]:
            cnt[x][y] += 1
            if cnt[x][y] >= 2:
                filled[x][y] = True
                total += 1
                dq.append((x, y))
if total != N * M:
    print('matrica se ne ispuni', total, N * M); sys.exit(1)
sys.exit(0)
