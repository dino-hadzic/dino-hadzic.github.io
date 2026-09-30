# Brute force: sve trojke (a,b,c) po rastucem zbroju, provjera uniqueness izravnom gradnjom aliasa.
import sys
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n = int(d[p]); p += 1
    ppl = []
    for _ in range(n):
        ppl.append((d[p], d[p+1])); p += 2
    def ok(a, b, c):
        from collections import Counter
        cnt = Counter(im[:a] + pr[:b] for im, pr in ppl)
        return max(cnt.values()) <= 10 ** c
    res = None
    for s in range(1, 30):
        for a in range(s + 1):
            for b in range(s - a + 1):
                c = s - a - b
                if ok(a, b, c):
                    res = (a, b, c); break
            if res: break
        if res: break
    out.append('%d %d %d' % res)
print('\n'.join(out))
