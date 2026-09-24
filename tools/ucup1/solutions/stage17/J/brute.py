# BFS po vrijednostima u [0, LIM)
import sys
from collections import deque
data = sys.stdin.read().split()
T = int(data[0]); p = 1
for _ in range(T):
    X, Y, K = map(int, data[p:p + 3]); p += 3
    LIM = 4 * max(X, Y, K, 1) + 8
    dist = [-1] * LIM
    dist[X] = 0
    dq = deque([X])
    while dq:
        x = dq.popleft()
        if x == Y:
            break
        nb = []
        if x + 1 < LIM: nb.append(x + 1)
        if x > 0: nb.append(x - 1)
        for t in range(K + 1):
            if x ^ t < LIM: nb.append(x ^ t)
        for y in nb:
            if dist[y] < 0:
                dist[y] = dist[x] + 1
                dq.append(y)
    print(dist[Y])
