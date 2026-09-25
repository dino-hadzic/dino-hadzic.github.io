import sys
from itertools import product
data = sys.stdin.read().split()
n = int(data[0])
arr = [[int(x) for x in data[1 + t * n:1 + (t + 1) * n]] for t in range(5)]
s = 0
for tup in product(*arr):
    s += sorted(tup)[2]
print(s % 998244353)
