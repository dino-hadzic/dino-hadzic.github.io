# Sporo rješenje: iteracija Bellmanove jednadžbe igre. dis[v] = max po skupovima od
# najviše d_v blokiranih bridova od min po preostalim bridovima (w + dis[u]).
import sys
from itertools import combinations
INF = float('inf')
def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1; out = []
    for _ in range(T):
        n, m, k = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
        exits = set(int(v) for v in data[p:p + k]); p += k
        d = [0] + [int(v) for v in data[p:p + n]]; p += n
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
            adj[x].append((y, w)); adj[y].append((x, w))
        dis = [INF] * (n + 1)
        for e in exits: dis[e] = 0
        changed = True
        while changed:
            changed = False
            for v in range(1, n + 1):
                if v in exits: continue
                edges = adj[v]
                b = min(d[v], len(edges))
                best = -1
                for blocked in combinations(range(len(edges)), b):
                    bs = set(blocked)
                    cur = INF
                    for idx, (u, w) in enumerate(edges):
                        if idx not in bs:
                            cur = min(cur, w + dis[u])
                    if cur > best or best == -1:
                        best = cur
                if best != dis[v]:
                    dis[v] = best; changed = True
        out.append(str(dis[1] if dis[1] != INF else -1))
    print("\n".join(out))
main()
