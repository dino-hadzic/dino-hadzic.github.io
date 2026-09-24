# Brute force: isprobaj sve vektore plaćenih letova p (0 <= p_j <= f_j) i provjeri
# uvjet za sve prozore od m uzastopnih mjeseci koji sijeku [1, n] (izvan njega 0 letova).
import sys, itertools
data = sys.stdin.read().split()
n, m, k = int(data[0]), int(data[1]), int(data[2])
f = [int(x) for x in data[3:3 + n]]

def ok(p):
    for r in range(0, n + m - 1):
        l = r - m + 1
        fl = sum(f[j] for j in range(max(0, l), min(n - 1, r) + 1))
        pl = sum(p[j] for j in range(max(0, l), min(n - 1, r) + 1))
        if pl < min(k, fl):
            return False
    return True

best = None
for p in itertools.product(*[range(x + 1) for x in f]):
    if ok(p):
        s = sum(p)
        if best is None or s < best:
            best = s
print(best)
