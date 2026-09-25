#!/usr/bin/env python3
# Brute force: isprobaj sva savrsena sparivanja 2n tocaka, uzmi najmanje prijateljskih.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
t = int(data[0]); p = 1
out = []
for _ in range(t):
    n = int(data[p]); p += 1
    pts = []
    for i in range(2 * n):
        pts.append((int(data[p]), int(data[p + 1]))); p += 2
    def fr(i, j):
        return pts[i][0] == pts[j][0] or pts[i][1] == pts[j][1]
    best = [-1, None]
    def rec(rem, pairs, cnt):
        if not rem:
            if best[0] < 0 or cnt < best[0]:
                best[0] = cnt; best[1] = list(pairs)
            return
        a = rem[0]
        for k in range(1, len(rem)):
            b = rem[k]
            pairs.append((a + 1, b + 1))
            rec(rem[1:k] + rem[k + 1:], pairs, cnt + fr(a, b))
            pairs.pop()
    rec(list(range(2 * n)), [], 0)
    out.append(str(best[0]))
    out.extend(f'{a} {b}' for a, b in best[1])
print('\n'.join(out))
