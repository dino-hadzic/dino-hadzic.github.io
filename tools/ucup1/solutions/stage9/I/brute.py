# Brute force: nabroji sve podjele na timove od 1 ili 2 susjedna vojnika (2^(n-1) maski).
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
for _ in range(T):
    n = int(data[p]); p += 1
    a = [int(x) for x in data[p:p+n]]; p += n
    best = None
    def rec(i, cur):
        global best
        if i == n:
            d = max(cur) - min(cur)
            if best is None or d < best: best = d
            return
        rec(i + 1, cur + [a[i]])
        if i + 1 < n: rec(i + 2, cur + [a[i] + a[i + 1]])
    rec(0, [])
    out.append(str(best))
print('\n'.join(out))
