import sys
from itertools import permutations
n, m = map(int, sys.stdin.read().split())
cnt = 0
for p in permutations(range(n * m)):
    if all(i // m != p[i] // m for i in range(n * m)):
        cnt += 1
print(cnt % 998244353)
