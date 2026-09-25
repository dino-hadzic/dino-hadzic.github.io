# Brute force: potpuno pretraživanje igre s memoizacijom po sortiranoj n-torci hrpi.
import sys
from itertools import combinations
from functools import lru_cache
sys.setrecursionlimit(100000)
data = sys.stdin.read().split()
pos = 0
t = int(data[pos]); pos += 1

@lru_cache(maxsize=None)
def win(state):
    n = len(state)
    idx = list(range(n))
    for k in range(1, n // 2 + 1):
        for rem in combinations(idx, k):
            rest = [state[i] for i in idx if i not in rem]
            cand = [i for i in range(len(rest)) if rest[i] >= 2]
            for spl in combinations(cand, k):
                base = [rest[i] for i in range(len(rest)) if i not in spl]
                # sve kombinacije dijeljenja odabranih hrpi
                def rec(j, cur):
                    if j == k:
                        return not win(tuple(sorted(cur)))
                    x = rest[spl[j]]
                    for a in range(1, x // 2 + 1):
                        if rec(j + 1, cur + [a, x - a]):
                            return True
                    return False
                if rec(0, base):
                    return True
    return False

out = []
for _ in range(t):
    n = int(data[pos]); pos += 1
    s = tuple(sorted(int(x) for x in data[pos:pos + n])); pos += n
    out.append('1' if win(s) else '0')
print('\n'.join(out))
