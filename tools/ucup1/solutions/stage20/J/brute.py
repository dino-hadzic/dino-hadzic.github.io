# Brute force: izgradimo w izravno (kvadratni ostaci mod p) i prebrojimo trojke u O(p^2).
import sys
data = sys.stdin.read().split(); T = int(data[0]); q = 1
for _ in range(T):
    p, t = int(data[q]), int(data[q+1]); q += 2
    qr = {(z * z) % p for z in range(1, p)}
    w = [0] + [1 if x in qr else 0 for x in range(1, p)]   # w[1..p-1]
    cnt = 0
    for d in range(1, t + 1):
        for i in range(1, p - 2 * d):
            if w[i] == w[i + d] == w[i + 2 * d]: cnt += 1
    print(cnt)
