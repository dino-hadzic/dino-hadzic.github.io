# Brute force: DFS koji nabraja sve jednostavne putove od u do v (mali n).
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
p = 0
n, q = int(data[p]), int(data[p + 1]); p += 2
adj = [[] for _ in range(n + 1)]
for _ in range(n + 1):
    a, b = int(data[p]), int(data[p + 1]); p += 2
    adj[a].append(b); adj[b].append(a)

def count(u, v):
    vis = [False] * (n + 1)
    cnt = 0
    def dfs(x):
        nonlocal cnt
        if x == v:
            cnt += 1
            return
        for y in adj[x]:
            if not vis[y]:
                vis[y] = True
                dfs(y)
                vis[y] = False
    vis[u] = True
    dfs(u)
    return cnt

out = []
for _ in range(q):
    u, v = int(data[p]), int(data[p + 1]); p += 2
    out.append(str(count(u, v)))
print("\n".join(out))
