# Brute force: isprobaj sve nizove poteza duljine <= m (lijevo/desno), s pocetkom na poziciji 0 lijevo od biljke 1.
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []

def solve(n, m, a):
    best = [0]
    def rec(pos, d, k):
        best[0] = max(best[0], min(d))
        if k == 0: return
        for np in (pos - 1, pos + 1):
            if 1 <= np <= n:
                d[np - 1] += a[np - 1]
                rec(np, d, k - 1)
                d[np - 1] -= a[np - 1]
            elif np == n + 1:
                rec(np, d, k - 1)
    rec(0, [0] * n, m)
    return best[0]

for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); p += 2
    a = [int(x) for x in data[p:p+n]]; p += n
    out.append(str(solve(n, m, a)))
print('\n'.join(out))
