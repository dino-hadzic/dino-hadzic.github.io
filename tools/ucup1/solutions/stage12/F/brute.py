import sys
data = sys.stdin.read().split()
n = int(data[0])
A = [0] + [int(x) for x in data[1:1 + n]]
edges = []
p = 1 + n
for _ in range(n - 1):
    edges.append((int(data[p]), int(data[p + 1]))); p += 2
total = 0
for mask in range(1 << (n - 1)):
    par = list(range(n + 1))
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            par[find(u)] = find(v)
    mn = {}
    for v in range(1, n + 1):
        r = find(v)
        mn[r] = min(mn.get(r, 10 ** 18), A[v])
    total += sum(mn.values())
print(total % 998244353)
