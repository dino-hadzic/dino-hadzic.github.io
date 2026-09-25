# Brute force: prodji sve 2^n podnizove, prebroji rekorde, zbroji (-1)^len.
import sys
MOD = 998244353
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
p = list(map(int, data[2:2 + n]))
ans = 0
for mask in range(1, 1 << n):
    rec = 0
    mx = 0
    ln = 0
    for i in range(n):
        if mask >> i & 1:
            ln += 1
            if p[i] > mx:
                mx = p[i]
                rec += 1
    if rec == k:
        ans += -1 if ln % 2 else 1
print(ans % MOD)
