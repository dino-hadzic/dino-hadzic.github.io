# Brute force: svaki podskup bridova sa stupnjevima <= 2; komponente su putovi
# ili ciklusi; put s v vrhova daje v mod 2 trojki, ciklus 0.
import sys
data = sys.stdin.read().split()
n1, n2, m = int(data[0]), int(data[1]), int(data[2])
E = [(int(data[3 + 2 * i]) - 1, n1 + int(data[4 + 2 * i]) - 1) for i in range(m)]
N = n1 + n2
best = None
for mask in range(1 << m):
    deg = [0] * N
    adj = [[] for _ in range(N)]
    ok = True
    for i in range(m):
        if mask >> i & 1:
            u, v = E[i]
            deg[u] += 1; deg[v] += 1
            adj[u].append(v); adj[v].append(u)
            if deg[u] > 2 or deg[v] > 2:
                ok = False; break
    if not ok:
        continue
    seen = [False] * N
    singles = 0; triples = 0
    for s in range(N):
        if seen[s]:
            continue
        comp = []; st = [s]; seen[s] = True; edges = 0
        while st:
            x = st.pop(); comp.append(x); edges += len(adj[x])
            for y in adj[x]:
                if not seen[y]:
                    seen[y] = True; st.append(y)
        edges //= 2
        v = len(comp)
        if v == 1:
            singles += 1
        elif edges == v:      # ciklus
            pass
        else:                 # put
            triples += v % 2
    cand = (singles, triples)
    if best is None or cand < best:
        best = cand
print(best[0], best[1])
