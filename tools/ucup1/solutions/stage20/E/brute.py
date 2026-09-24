# Brute force: BFS po stvarnim stringovima (poteze primjenjujemo doslovno), uz gornju granicu duljine
# |T| + 2K + max|S_i| koja je dovoljna: u optimalnom rjesenju duljina nikad ne prelazi |T| + K + max|S_i|.
import sys
from collections import deque
data = sys.stdin.read().split(); q = int(data[0]); p = 1
for _ in range(q):
    n, K = int(data[p]), int(data[p+1]); p += 2
    S = data[p:p+n]; p += n
    T = data[p]; p += 1
    cap = len(T) + 2 * K + max(len(s) for s in S)
    dist = {"": 0}; dq = deque([""])
    ans = -1
    while dq:
        cur = dq.popleft()
        if cur == T: ans = dist[cur]; break
        cand = [cur + s for s in S if len(cur) + len(s) <= cap]
        if len(cur) >= K: cand.append(cur[:-K])
        for nx in cand:
            if nx not in dist:
                dist[nx] = dist[cur] + 1; dq.append(nx)
    print(ans)
