# Brute force: isprobaj sve nizove operacija duljine 0, 1, 2, ... dok neki ne sortira permutaciju.
import sys
from itertools import product
data = sys.stdin.read().split()
n = int(data[0]); p = list(map(int, data[1:1 + n]))
def primijeni(p, ops):
    a = p[:]
    for k, o in enumerate(ops, 1):
        if o == 'P':
            a[:k] = sorted(a[:k])
        else:
            a[n - k:] = sorted(a[n - k:])
    return a
target = list(range(1, n + 1))
for m in range(0, n + 1):
    for ops in product('SP', repeat=m):
        if primijeni(p, ops) == target:
            print(''.join(ops) + '.')
            sys.exit(0)
