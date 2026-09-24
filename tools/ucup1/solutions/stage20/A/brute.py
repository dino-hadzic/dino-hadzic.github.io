# Brute force: BFS po svim stanjima niza B (male vrijednosti), poteze primjenjujemo doslovno.
import sys
from collections import deque
data = sys.stdin.read().split(); T = int(data[0]); p = 1
out = []
for _ in range(T):
    n, q = int(data[p]), int(data[p+1]); p += 2
    a = [int(x) for x in data[p:p+n]]; p += n
    for _ in range(q):
        L, R = int(data[p]), int(data[p+1]); p += 2
        start = tuple(a[L-1:R])
        dist = {start: 0}; dq = deque([start])
        best = -1; moves = 0
        while dq:
            cur = dq.popleft()
            o = 0
            for v in cur: o |= v
            if o > best or (o == best and dist[cur] < moves): best, moves = o, dist[cur]
            for j in range(len(cur)):
                x = cur[j]; i = 0
                while (1 << i) <= x:
                    nx = cur[:j] + (x ^ (x - (1 << i)),) + cur[j+1:]
                    if nx not in dist: dist[nx] = dist[cur] + 1; dq.append(nx)
                    i += 1
        out.append(f"{best} {moves}")
print("\n".join(out))
