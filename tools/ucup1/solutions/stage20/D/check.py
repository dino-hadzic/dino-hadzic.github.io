# check.py <ulaz> <-> <dobiveni izlaz>
# |S| <= ceil(sqrt N), vrhovi razliciti i valjani, svaki vrh na udaljenosti <= ceil(sqrt N) od S (multi-source BFS).
import sys, math
from collections import deque
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); out = open(sys.argv[3]).read().split()
t = int(inp[0]); p = 1; q = 0
for tc in range(t):
    n, m = int(inp[p]), int(inp[p+1]); p += 2
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = int(inp[p]), int(inp[p+1]); p += 2
        adj[a].append(b); adj[b].append(a)
    s = math.isqrt(n)
    if s * s < n: s += 1
    if q >= len(out): fail("premalo izlaza")
    sz = int(out[q]); q += 1
    if sz == -1: fail(f"test {tc}: -1, a podskup uvijek postoji")
    if not (1 <= sz <= s): fail(f"test {tc}: |S|={sz} > {s}")
    S = [int(x) for x in out[q:q+sz]]; q += sz
    if len(set(S)) != sz or any(not (1 <= v <= n) for v in S): fail(f"test {tc}: losi vrhovi")
    dist = [-1] * (n+1); dq = deque()
    for v in S: dist[v] = 0; dq.append(v)
    while dq:
        x = dq.popleft()
        for y in adj[x]:
            if dist[y] < 0: dist[y] = dist[x] + 1; dq.append(y)
    if min(dist[1:]) < 0 or max(dist[1:]) > s: fail(f"test {tc}: neki vrh je predaleko")
if q != len(out): fail("visak izlaza")
print("OK")
