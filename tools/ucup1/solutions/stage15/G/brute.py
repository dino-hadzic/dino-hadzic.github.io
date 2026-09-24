# Nabroji sve putove 1 -> n (n <= 9) i uzmi leksikografski najveci sortirani multiskup.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split(); pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    n, L, R = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
    x = [int(v) for v in data[pos:pos + n]]; pos += n
    a = [int(v) for v in data[pos:pos + n]]; pos += n
    best = None
    def dfs(i, skup):
        global best
        if i == n - 1:
            s = sorted(skup, reverse=True)
            if best is None or s > best: best = s
            return
        for j in range(i + 1, n):
            if L <= x[j] - x[i] <= R: dfs(j, skup + [a[j]])
    dfs(0, [a[0]])
    if best is None: out.append('-1')
    else: out.append(str(len(best))); out.append(' '.join(map(str, best)))
print('\n'.join(out))
