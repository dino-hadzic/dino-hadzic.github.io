# Brute force: BFS po svim stanjima DSU-a (n <= 6); ispisuje i najkraći niz operacija.
import sys
from collections import deque
data = sys.stdin.read().split()
T = int(data[0]); p = 1
def find(f, x):
    if f[x] == x: return x
    f[x] = find(f, f[x]); return f[x]
def unite(f, x, y):
    a = find(f, x); b = find(f, y)
    if a != b: f[a] = b
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    f = tuple(int(x) for x in data[p:p + n]); p += n
    g = tuple(int(x) for x in data[p:p + n]); p += n
    f0 = (0,) + f; g0 = (0,) + g
    prev = {f0: None}; dq = deque([f0]); ok = False
    while dq:
        s = dq.popleft()
        if s == g0: ok = True; break
        for x in range(1, n + 1):
            t = list(s); find(t, x); t = tuple(t)
            if t not in prev: prev[t] = (s, (1, x)); dq.append(t)
            for y in range(1, n + 1):
                t = list(s); unite(t, x, y); t = tuple(t)
                if t not in prev: prev[t] = (s, (2, x, y)); dq.append(t)
    if not ok:
        out.append("NO"); continue
    ops = []; s = g0
    while prev[s] is not None:
        s, op = prev[s]; ops.append(op)
    ops.reverse()
    out.append("YES"); out.append(str(len(ops)))
    out += [" ".join(map(str, op)) for op in ops]
print("\n".join(out))
