import sys
from itertools import permutations

def perms_of(v):
    s = str(v)
    return {int(''.join(p)) for p in permutations(s)}

data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
a = [int(t) for t in data[2:2 + n]]
# stanje: tocan iznos -> najveci broj kupnji
dp = {x: 0}
for c in a:
    nd = dict(dp)
    for v, cnt in dp.items():
        for k in perms_of(v):
            if k >= c:
                r = k - c
                if nd.get(r, -1) < cnt + 1:
                    nd[r] = cnt + 1
    dp = nd
print(max(dp.values()))
