# Brute force: BFS po svim stanjima (mali n, k) - neovisno provjerava postoji li plan.
import sys
from collections import deque
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, k = int(d[p]), int(d[p+1]); p += 2
    poles = [()]
    for i in range(n):
        poles.append(tuple(int(x) for x in d[p:p+k])); p += k
    poles.append(())
    start = tuple(poles)
    def goal(s): return all(len(set(t)) <= 1 for t in s)
    seen = {start}; dq = deque([start]); ok = False
    while dq:
        s = dq.popleft()
        if goal(s): ok = True; break
        for a in range(n + 2):
            if not s[a]: continue
            for b in (a - 1, a + 1):
                if 0 <= b <= n + 1 and len(s[b]) < k:
                    t = list(s); t[b] = s[b] + (s[a][-1],); t[a] = s[a][:-1]; t = tuple(t)
                    if t not in seen: seen.add(t); dq.append(t)
    out.append("TAK\n0" if ok else "NIE")
print('\n'.join(out))
