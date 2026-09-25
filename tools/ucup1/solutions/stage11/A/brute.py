# Brute force: Dijkstra po svim 2^n obojenjima; operacija i postavlja c_i = c_{a_i} uz cijenu p_i.
# Odgovor = max po dostignutim stanjima (zbroj w jedinica - najmanja cijena dolaska).
import sys, heapq
data = sys.stdin.read().split()
n, s = int(data[0]), int(data[1])
w = list(map(int, data[2:2 + n])); p = list(map(int, data[2 + n:2 + 2 * n])); a = [int(x) - 1 for x in data[2 + 2 * n:2 + 3 * n]]
start = 1 << (s - 1)
dist = {start: 0}
pq = [(0, start)]
while pq:
    d, st = heapq.heappop(pq)
    if dist.get(st, None) != d: continue
    for i in range(n):
        bit = (st >> a[i]) & 1
        ns = (st & ~(1 << i)) | (bit << i)
        nd = d + p[i]
        if ns not in dist or nd < dist[ns]:
            dist[ns] = nd; heapq.heappush(pq, (nd, ns))
best = None
for st, d in dist.items():
    v = sum(w[i] for i in range(n) if (st >> i) & 1) - d
    best = v if best is None else max(best, v)
print(best)
