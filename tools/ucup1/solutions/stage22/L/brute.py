# Brute force: BFS po vrijednostima do granice B s doslovnim operacijama
# x -> x-1 i x -> x + floor(sqrt(2x) + 1.5)  (točno, cjelobrojno:
# floor(sqrt(2x)+1.5) = (isqrt(8x) + 3) // 2).
import sys
from math import isqrt
from collections import deque

def jump(x):
    return x + (isqrt(8 * x) + 3) // 2

data = sys.stdin.read().split()
T = int(data[0]); i = 1
out = []
for _ in range(T):
    x, y = int(data[i]), int(data[i + 1]); i += 2
    B = 6 * max(x, y) + 200
    dist = {x: 0}
    dq = deque([x])
    while dq:
        v = dq.popleft()
        if v == y:
            break
        for w in (v - 1, jump(v)):
            if 1 <= w <= B and w not in dist:
                dist[w] = dist[v] + 1
                dq.append(w)
    out.append(str(dist[y]))
print('\n'.join(out))
