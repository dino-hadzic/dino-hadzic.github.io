# Brute force: za svaki upit DFS iz x s trenutnim težinama i brojanje vrhova na udaljenosti <= d.
import sys
data = sys.stdin.read().split(); p = 0
n, q = int(data[0]), int(data[1]); p = 2
adj = [[] for _ in range(n + 1)]; w = [0] * n
for i in range(1, n):
    x, y, ww = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    adj[x].append((y, i)); adj[y].append((x, i)); w[i] = ww
out = []
for _ in range(q):
    t, a, b = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    if t == 1:
        w[a] = b
    else:
        dist = {a: 0}; st = [a]
        while st:
            v = st.pop()
            for u, i in adj[v]:
                if u not in dist:
                    dist[u] = dist[v] + w[i]; st.append(u)
        out.append(str(sum(1 for v in dist if dist[v] <= b)))
print('\n'.join(out))
