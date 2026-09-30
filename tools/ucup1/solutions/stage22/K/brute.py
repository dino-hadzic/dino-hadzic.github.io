# Brute force za N*M <= 16: iscrpno po podskupovima (rastući broj jedinica),
# simulira punjenje i ispisuje najmanji broj jedinica s jednom optimalnom matricom.
# Za veće matrice (samo mjerenje/kontrola konstrukcije) ispisuje formulu ceil((N+M)/2)
# bez matrice; check.py tada uspoređuje samo broj.
import sys
from itertools import combinations
from collections import deque
N, M = map(int, sys.stdin.read().split())

def fills(cells):
    filled = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    dq = deque()
    for (i, j) in cells:
        filled[i][j] = True; dq.append((i, j))
    total = len(cells)
    while dq:
        i, j = dq.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < N and 0 <= y < M and not filled[x][y]:
                cnt[x][y] += 1
                if cnt[x][y] >= 2:
                    filled[x][y] = True; total += 1; dq.append((x, y))
    return total == N * M

if N * M > 16:
    print((N + M + 1) // 2)
    sys.exit(0)
allc = [(i, j) for i in range(N) for j in range(M)]
for c in range(1, N * M + 1):
    for sub in combinations(allc, c):
        if fills(sub):
            s = set(sub)
            print(c)
            for i in range(N):
                print(' '.join('1' if (i, j) in s else '0' for j in range(M)))
            sys.exit(0)
