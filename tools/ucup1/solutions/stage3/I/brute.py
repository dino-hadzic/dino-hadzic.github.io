# Brute force izravno po definiciji: probamo sve nizove od najvise k operacija
# (interval [l,r], prirast x u {1..4}) i brojimo inverzije. Za a_i <= 3 prirast x = 3 vec
# potpuno razdvaja blokove, pa x <= 4 ne gubi optimum.
import sys, itertools
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
def invs(b): return sum(1 for i in range(len(b)) for j in range(i + 1, len(b)) if b[i] > b[j])
for _ in range(z):
    n, k = int(d[p]), int(d[p+1]); p += 2
    a = [int(x) for x in d[p:p+n]]; p += n
    ops = [None] + [(l, r, x) for l in range(n) for r in range(l, n) for x in range(1, 5)]
    best = invs(a)
    for combo in itertools.product(ops, repeat=k):
        b = a[:]
        for op in combo:
            if op is None: continue
            l, r, x = op
            for i in range(l, r + 1): b[i] += x
        best = min(best, invs(b))
    out.append(str(best))
print('\n'.join(out))
