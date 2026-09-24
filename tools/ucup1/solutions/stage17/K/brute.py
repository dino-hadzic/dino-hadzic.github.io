# Brute force: BFS po svim stanjima 2 x n tablice (n <= 4), ispisuje najkraći niz zamjena ili -1.
import sys
from collections import deque
data = sys.stdin.read().split()
T = int(data[0]); p = 1
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    rows = []
    for _ in range(4):
        rows.append(tuple(int(x) for x in data[p:p + n])); p += n
    a = (rows[0], rows[1]); b = (rows[2], rows[3])
    prev = {a: None}; dq = deque([a]); ok = False
    while dq:
        s = dq.popleft()
        if s == b: ok = True; break
        for i in range(n):
            for j in range(i + 1, n):
                ri = 0 if s[0][i] > s[1][i] else 1
                rj = 0 if s[0][j] > s[1][j] else 1
                t = [list(s[0]), list(s[1])]
                t[ri][i], t[rj][j] = t[rj][j], t[ri][i]
                t = (tuple(t[0]), tuple(t[1]))
                if t not in prev:
                    prev[t] = (s, (ri + 1, i + 1, rj + 1, j + 1)); dq.append(t)
    if not ok:
        out.append("-1"); continue
    ops = []; s = b
    while prev[s] is not None:
        s, op = prev[s]; ops.append(op)
    ops.reverse()
    out.append(str(len(ops)))
    out += [" ".join(map(str, op)) for op in ops]
print("\n".join(out))
