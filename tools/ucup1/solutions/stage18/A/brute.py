# Sporo rješenje: minimax po bitmaskama uklonjenih vrhova (n <= 12).
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
def main():
    data = sys.stdin.read().split()
    n = int(data[0]); a = [int(v) for v in data[1:1 + n]]
    adj = [[] for _ in range(n)]
    p = 1 + n
    for _ in range(n - 1):
        u, v = int(data[p]) - 1, int(data[p + 1]) - 1; p += 2
        adj[u].append(v); adj[v].append(u)
    par = [-1] * n; seen = [False] * n; seen[0] = True; st = [0]
    while st:
        v = st.pop()
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True; par[u] = v; st.append(u)
    @lru_cache(maxsize=None)
    def val(removed):
        if removed == (1 << n) - 1:
            return 0
        best = None
        for v in range(n):
            if not (removed >> v) & 1 and (par[v] < 0 or (removed >> par[v]) & 1):
                r = a[v] - val(removed | (1 << v))
                if best is None or r > best:
                    best = r
        return best
    print((sum(a) + val(0)) // 2)
main()
