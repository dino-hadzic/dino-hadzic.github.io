# check.py <ulaz> <-> <dobiveni izlaz>
# NO je ispravno tocno kad je K > floor(N/2) (nuzan uvjet iz broja bridova; dovoljnost
# potvrdjuje sama konstrukcija). Za YES: sve boje u [1,K], svaka boja povezana s dijametrom <= 4.
import sys
from collections import deque
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); out = open(sys.argv[3]).read().split()
t = int(inp[0]); p = 1; q = 0
for tc in range(t):
    n, k = int(inp[p]), int(inp[p+1]); p += 2
    if q >= len(out): fail("premalo izlaza")
    v = out[q]; q += 1
    if v == "NO":
        if k <= n // 2: fail(f"test {tc}: NO, a rjesenje postoji (N={n}, K={k})")
        continue
    if v != "YES": fail(f"test {tc}: los verdikt {v}")
    if k > n // 2: fail(f"test {tc}: YES, a K > N/2")
    adj = [[[] for _ in range(n)] for _ in range(k)]
    for i in range(1, n):
        for j in range(i):
            c = int(out[q]); q += 1
            if not (1 <= c <= k): fail(f"test {tc}: boja {c} izvan [1,{k}]")
            adj[c-1][i].append(j); adj[c-1][j].append(i)
    for c in range(k):
        for s in range(n):
            dist = [-1]*n; dist[s] = 0; dq = deque([s])
            while dq:
                x = dq.popleft()
                for y in adj[c][x]:
                    if dist[y] < 0: dist[y] = dist[x] + 1; dq.append(y)
            if min(dist) < 0 or max(dist) > 4: fail(f"test {tc}: boja {c+1} nema dijametar <= 4")
if q != len(out): fail("visak izlaza")
print("OK")
