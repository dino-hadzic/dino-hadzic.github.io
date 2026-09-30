# Brute force: običan BFS u kojem za svaki i <= k doslovno računamo f_i(x,y)
# iteriranjem definicije f_i(x,y) = f_{i-1}(y+1, x).  O(n^2 k).
import sys
from collections import deque
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
g = data[2:2 + n]
def ok(x, y):
    return 1 <= x <= n and 1 <= y <= n and g[x - 1][y - 1] == '.'
dist = {(1, 1): 0}
dq = deque([(1, 1)])
while dq:
    x, y = dq.popleft()
    if (x, y) == (n, n):
        break
    cand = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    a, b = x, y
    for i in range(1, k + 1):
        a, b = b + 1, a
        cand.append((a, b))
    for c in cand:
        if ok(*c) and c not in dist:
            dist[c] = dist[(x, y)] + 1
            dq.append(c)
print(dist.get((n, n), -1))
