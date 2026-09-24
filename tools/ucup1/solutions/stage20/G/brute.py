# Brute force: nabrojimo sve c^(2n) stringove i provjerimo intervalnom dinamikom postoji li
# nekrizajuce sparivanje jednakih znakova (neovisno o triku sa stogom).
import sys, itertools
from functools import lru_cache
MOD = 10**9 + 7
def perfect(s):
    n = len(s)
    @lru_cache(maxsize=None)
    def ok(i, j):
        if i > j: return True
        for k in range(i + 1, j + 1, 2):
            if s[i] == s[k] and ok(i + 1, k - 1) and ok(k + 1, j): return True
        return False
    return ok(0, n - 1)
data = sys.stdin.read().split(); t = int(data[0]); p = 1
for _ in range(t):
    n, c = int(data[p]), int(data[p+1]); p += 2
    cnt = sum(1 for s in itertools.product(range(c), repeat=2*n) if perfect(s))
    print(cnt % MOD)
