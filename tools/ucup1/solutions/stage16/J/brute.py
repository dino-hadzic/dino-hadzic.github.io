#!/usr/bin/env python3
# Brute force: isprobaj sve podskupove tema (n <= 10).
import sys
data = sys.stdin.read().split()
q = int(data[0]); p = 1
out = []
for _ in range(q):
    n, t = int(data[p]), int(data[p + 1]); p += 2
    a = []; b = []
    for i in range(n):
        a.append(int(data[p])); b.append(int(data[p + 1])); p += 2
    best = (0, [])
    for mask in range(1 << n):
        S = [i for i in range(n) if mask >> i & 1]
        if sum(a[i] for i in S) > t:
            continue
        k = len(S)
        c = sum(1 for i in S if b[i] <= k)
        if c > best[0]:
            best = (c, S)
    out.append(str(best[0]))
    out.append(str(len(best[1])))
    out.append(' '.join(str(i + 1) for i in best[1]))
print('\n'.join(out))
