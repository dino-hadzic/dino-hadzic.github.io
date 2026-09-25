import sys
from itertools import permutations
data = sys.stdin.read().split()
n = int(data[0]); a = [int(x) for x in data[1:1 + n]]; ops = data[1 + n] if n > 1 else ""
MOD = 998244353
total = 0
for order in permutations(range(n - 1)):
    nums = a[:]; op = list(ops); alive = list(range(n - 1))
    # order: redoslijed brisanja operatora (indeksi izvornih operatora)
    vals = a[:]; cur_ops = list(ops)
    idx = list(range(n - 1))  # izvorni indeksi operatora koji su jos zivi
    for o in order:
        k = idx.index(o)
        v = vals[k] + vals[k + 1] if cur_ops[k] == '+' else vals[k] - vals[k + 1]
        vals[k:k + 2] = [v]; del cur_ops[k]; del idx[k]
    total += vals[0]
print(total % MOD)
