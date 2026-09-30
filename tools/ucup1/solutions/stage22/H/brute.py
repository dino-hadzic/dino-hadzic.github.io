# Brute force izravno po definiciji: f(x) = 1 + sum_{k>=2, kx<=n} f(kx), f(x)=0 za x>n.
# Računamo f(x) za x = n, n-1, ..., 1 (za male n je gornja granica sume 20210926
# nevažna jer je kx <= n < 20210926).
import sys
MOD = 998244353
n = int(sys.stdin.read().split()[0])
f = [0] * (n + 2)
for x in range(n, 0, -1):
    s = 1
    k = 2
    while k * x <= n:
        s += f[k * x]
        k += 1
    f[x] = s % MOD
print(f[1])
