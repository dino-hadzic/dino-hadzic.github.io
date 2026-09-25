# Brute force: Dijkstra po stanjima (polozaj Shoua, polozaj Panga) izravno po pravilima igre.
# Shou smije i ostati na mjestu (da provjerimo da to nikad ne pomaze).
import sys, heapq
from collections import deque
data = sys.stdin.read().split()
n, m, k, d = map(int, data[:4])
adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = int(data[4 + 2 * i]), int(data[5 + 2 * i])
    adj[a].append(b); adj[b].append(a)
dist = [None] * (n + 1)
for s in range(1, n + 1):
    dd = [-1] * (n + 1); dd[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dd[v] < 0: dd[v] = dd[u] + 1; q.append(v)
    dist[s] = dd
INF = float('inf')
best = {(1, k): 0}
pq = [(0, 1, k)]
ans = INF
while pq:
    c, s, p = heapq.heappop(pq)
    if best.get((s, p), INF) < c: continue
    if s == n: ans = min(ans, c); continue
    for t in adj[s] + [s]:
        dis = dist[p][t]
        if dis >= d: nc, np_ = c + d, t
        else: nc, np_ = c + d - dis, p
        if nc < best.get((t, np_), INF):
            best[(t, np_)] = nc; heapq.heappush(pq, (nc, t, np_))
print(ans)
