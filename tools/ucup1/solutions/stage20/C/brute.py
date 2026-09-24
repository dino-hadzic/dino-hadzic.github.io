# Brute force: probamo sve podskupove ispita (N <= 10).
import sys
data = sys.stdin.read().split(); t = int(data[0]); p = 1
for _ in range(t):
    n, m = int(data[p]), int(data[p+1]); p += 2
    iv = []
    for i in range(n):
        iv.append((int(data[p]), int(data[p+1]))); p += 2
    req = []
    for j in range(m):
        req.append((int(data[p]) - 1, int(data[p+1]) - 1)); p += 2
    ok = False
    for mask in range(1 << n):
        ch = [i for i in range(n) if mask >> i & 1]
        if any(not (iv[a][1] < iv[b][0] or iv[b][1] < iv[a][0]) for x, a in enumerate(ch) for b in ch[x+1:]): continue
        if all(mask >> a & 1 or mask >> b & 1 for a, b in req): ok = True; break
    print("YES" if ok else "NO")
