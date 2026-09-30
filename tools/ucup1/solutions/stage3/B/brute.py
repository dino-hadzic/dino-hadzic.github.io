# Brute force: svi neprazni podskupovi barova, prihod izravno po definiciji.
import sys
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n = int(d[p]); p += 1
    a = [int(x) for x in d[p:p+n]]; p += n
    best = 0
    for mask in range(1, 1 << n):
        bars = [i for i in range(n) if mask >> i & 1]
        tot = 0
        for r in range(n):
            left = [i for i in bars if i < r]
            right = [i for i in bars if i > r]
            if left: tot += a[max(left)]
            if right: tot += a[min(right)]
        best = max(best, tot)
    out.append(str(best))
print('\n'.join(out))
