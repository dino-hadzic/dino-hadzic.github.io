import sys
data = sys.stdin.read().split()
n = int(data[0])
L = [int(x) for x in data[1:1 + n]]
R = [int(x) for x in data[1 + n:1 + 2 * n]]
cnt = 0
for a in range(L[0], R[0] + 1):
    for d in range(L[1] - a, R[1] - a + 1):
        if all(L[i] <= a + i * d <= R[i] for i in range(n)):
            cnt += 1
print(cnt % 998244353)
