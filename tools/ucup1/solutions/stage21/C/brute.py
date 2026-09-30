import sys
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    edges = []
    for _ in range(n - 1):
        a, b = int(data[p]), int(data[p + 1]); p += 2; edges.append((a, b))
    ans = 0
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            par = list(range(n + 1))
            def find(x):
                while par[x] != x: par[x] = par[par[x]]; x = par[x]
                return x
            comps = r - l + 1
            for a, b in edges:
                if l <= a <= r and l <= b <= r:
                    fa, fb = find(a), find(b)
                    if fa != fb: par[fa] = fb; comps -= 1
            if comps == 1: ans += 1
    out.append(str(ans))
print('\n'.join(out))
