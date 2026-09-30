import sys
data = sys.stdin.read().split()
n, m, k = int(data[0]), int(data[1]), int(data[2])
pts = [(int(data[3 + 2 * i]), int(data[4 + 2 * i])) for i in range(k)]
ans = 0
for d in range(1, min(n, m) + 1):
    for x in range(0, n - d + 1):
        for y in range(0, m - d + 1):
            if not any(x < px < x + d and y < py < y + d for px, py in pts): ans += d * d
print(ans % 998244353)
