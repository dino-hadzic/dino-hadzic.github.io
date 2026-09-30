# Brute force: nakon svake promjene, iz svakog vrha DFS po dobrim putevima
# (isti vrhovi iste boje, svi bridovi boje prvog brida) i pamti najdulji.
import sys
data = sys.stdin.read().split(); p = 0
n, q = int(data[0]), int(data[1]); p = 2
a = [0] + [int(x) for x in data[p:p + n]]; p += n
fa = [0, 0] + [int(x) for x in data[p:p + n - 1]]; p += n - 1
fc = [0, 0] + [int(x) for x in data[p:p + n - 1]]; p += n - 1
w = [0, 0] + [int(x) for x in data[p:p + n - 1]]; p += n - 1
adj = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    adj[i].append((fa[i], fc[i], w[i])); adj[fa[i]].append((i, fc[i], w[i]))
def best():
    res = 0
    for s in range(1, n + 1):
        st = [(s, 0, 0, 0)]
        while st:
            v, prev, col, ln = st.pop()
            res = max(res, ln)
            for u, c, ww in adj[v]:
                if u == prev or a[u] != a[s]: continue
                if col and c != col: continue
                st.append((u, v, c, ln + ww))
    return res
out = [best()]
for _ in range(q):
    x, c = int(data[p]), int(data[p + 1]); p += 2
    a[x] = c
    out.append(best())
print('\n'.join(map(str, out)))
