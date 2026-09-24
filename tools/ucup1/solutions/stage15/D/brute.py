# Brute force izravno po definiciji: Dijkstra nad multiskupovima (sortirane n-torke),
# operacija = (podskup T, pomak y) s cijenom w_y. Za n <= 5.
import sys, heapq
data = sys.stdin.read().split()
n = int(data[0]); w = list(map(int, data[1:1 + n]))
MOD = 998244353

def f(S):
    start = tuple(sorted(S))
    goal = tuple([0] * len(S))
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, s = heapq.heappop(pq)
        if dist[s] != d:
            continue
        if s == goal:
            return d
        k = len(s)
        for T in range(1, 1 << k):
            for y in range(n):
                ns = tuple(sorted((s[i] + y) % n if T >> i & 1 else s[i] for i in range(k)))
                nd = d + w[y]
                if nd < dist.get(ns, 10 ** 30):
                    dist[ns] = nd
                    heapq.heappush(pq, (nd, ns))

ans = 0
for mask in range(1, 1 << n):
    S = [v for v in range(n) if mask >> v & 1]
    ans = (ans + f(S) * mask) % MOD
print(ans)
