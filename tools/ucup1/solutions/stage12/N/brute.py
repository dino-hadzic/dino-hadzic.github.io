import sys
data = list(map(int, sys.stdin.read().split()))
n, m, K = data[0], data[1], data[2]
E = [(data[3 + 3 * i], data[4 + 3 * i], data[5 + 3 * i]) for i in range(m)]
q = data[3 + 3 * m]
out = []
for t in range(q):
    D = data[4 + 3 * m + t]
    par = list(range(n + 1))
    def find(x):
        while par[x] != x:
            x = par[x]
        return x
    for a, b, c in E:
        if (c ^ D) < K:
            ra, rb = find(a), find(b)
            if ra != rb:
                par[ra] = rb
    cnt = {}
    for v in range(1, n + 1):
        r = find(v); cnt[r] = cnt.get(r, 0) + 1
    out.append(sum(s * (s - 1) // 2 for s in cnt.values()))
print(*out, sep='\n')
