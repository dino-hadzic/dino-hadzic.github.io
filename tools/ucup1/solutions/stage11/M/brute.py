# Brute force: isprobaj sve rasporede ljutih jela (podskupove pozicija velicine a) i simuliraj definiciju.
import sys
from itertools import combinations
data = sys.stdin.read().split()
n, a = int(data[0]), int(data[1]); b = list(map(int, data[2:2 + n]))
best = 0
for S in combinations(range(n), a):
    spicy = set(S)
    tot = 0
    for i in range(n):
        for j in (i - 1, i, i + 1):
            j %= n
            if b[i] == 1 or j not in spicy:
                tot += 1
    best = max(best, tot)
print(best)
