import sys
data = sys.stdin.read().split()
n, M = int(data[0]), int(data[1])
A = [int(x) for x in data[2:2 + n]]
MOD = 998244353
total = 0
def rec(i, rem, prod):
    global total
    if i == n - 1:
        total += prod * (rem + A[i])
        return
    d = 1
    while d * d <= rem:
        if rem % d == 0:
            rec(i + 1, rem // d, prod * (d + A[i]))
            if d * d != rem:
                rec(i + 1, d, prod * (rem // d + A[i]))
        d += 1
rec(0, M, 1)
print(total % MOD)
