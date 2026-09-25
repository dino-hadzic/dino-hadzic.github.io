import sys
data = sys.stdin.read().split(); pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    n, p = int(data[pos]), int(data[pos + 1]); pos += 2
    S = [int(x) for x in data[pos:pos + n]]; pos += n
    best = -1; cs = []
    for c in range(p):
        Sc = set(c * x % p for x in S)
        m = 0
        while m in Sc: m += 1
        if m > best: best, cs = m, [c]
        elif m == best: cs.append(c)
    out.append('%d %d' % (len(cs), best)); out.append(' '.join(map(str, cs)))
print('\n'.join(out))
