# Brute force: BFS po stanjima (vrh, trenutni AND) – radi za male težine.
import sys
from collections import deque
data = sys.stdin.read().split(); p = 0
n, m, q, V = int(data[0]), int(data[1]), int(data[2]), int(data[3]); p = 4
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    adj[u].append((v, w)); adj[v].append((u, w))
out = []
for _ in range(q):
    u, v = int(data[p]), int(data[p + 1]); p += 2
    seen = set()
    dq = deque()
    for (y, w) in adj[u]:
        if (y, w) not in seen: seen.add((y, w)); dq.append((y, w))
    ok = False
    while dq:
        x, a = dq.popleft()
        if x == v and a >= V: ok = True; break
        for (y, w) in adj[x]:
            s = (y, a & w)
            if s not in seen: seen.add(s); dq.append(s)
    out.append('Yes' if ok else 'No')
print('\n'.join(out))
