#!/usr/bin/env python3
# Brute force: za r = 1, 2, ... isprobaj sve rasporede r topova i provjeri pokrivenost.
import sys
from itertools import combinations
MOD = 998244353
data = sys.stdin.read().split()
n = int(data[0]); a = [int(x) for x in data[1:1 + n]]
cells = [(i, j) for i in range(n) for j in range(a[i])]
cellset = set(cells)

def covered(rooks):
    rs = set(rooks)
    for (i, j) in cells:
        if (i, j) in rs:
            continue
        ok = False
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = i + di, j + dj
            while (x, y) in cellset:
                if (x, y) in rs:
                    ok = True
                    break
                x += di; y += dj
            if ok:
                break
        if not ok:
            return False
    return True

r = 1
while True:
    cnt = sum(1 for c in combinations(cells, r) if covered(c))
    if cnt:
        print(r, cnt % MOD)
        break
    r += 1
