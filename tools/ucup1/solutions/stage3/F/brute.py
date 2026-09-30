# Brute force: svih 2^(3n) rasporeda, provjera uvjeta i brojeva cvjetova.
import sys
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, q = int(d[p]), int(d[p+1]); p += 2
    cons = []
    for _ in range(q):
        cons.append(tuple(int(x) for x in d[p:p+4])); p += 4
    N = 3 * n; res = None
    for mask in range(1 << N):
        s = ['F' if mask >> i & 1 else 'R' for i in range(N)]
        f = s.count('F')
        if f > 2 * n or N - f > 2 * n: continue
        ok = True
        for a, b, c, dd in cons:
            if not (all(s[i] == 'R' for i in range(a - 1, b)) or all(s[i] == 'F' for i in range(c - 1, dd))):
                ok = False; break
        if ok: res = ''.join(s); break
    if res is None: out.append("NIE")
    else: out.append("TAK"); out.append(res)
print('\n'.join(out))
