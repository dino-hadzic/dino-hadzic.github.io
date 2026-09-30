import sys
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n, k = int(data[p]), int(data[p + 1]); p += 2
    pts = []
    for i in range(n): pts.append((int(data[p]), int(data[p + 1]))); p += 2
    def cr(i, j):
        i %= n; j %= n
        return pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
    best = 0
    for b in range(n):
        c = b + k
        chain = sum(cr(j, j + 1) for j in range(b, c))
        for a in range(c + 1, b + n):
            s = chain + cr(c, a) + cr(a, b)
            best = max(best, s)
    out.append(f'{best // 2}.{"5" if best % 2 else "0"}')
print('\n'.join(out))
