import sys, itertools
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n, k = int(data[p]), int(data[p + 1]); s = data[p + 2]; p += 3
    qs = [i for i in range(n) if s[i] == '?']
    best = None
    for bits in itertools.product('01', repeat=len(qs)):
        t = list(s)
        for i, b in zip(qs, bits): t[i] = b
        t = ''.join(t)
        if sum(t[i] != t[i + 1] for i in range(n - 1)) == k and (best is None or t < best): best = t
    out.append(best if best is not None else 'Impossible')
print('\n'.join(out))
