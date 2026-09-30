# Brute force: nabroji sve nizove od m dopustenih intervala i provjeri jesu li sve dvojke pokrivene.
import sys, itertools
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
MOD = 10**9 + 7
for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); p += 2
    a = [int(x) for x in data[p:p+n]]; p += n
    ints = [(l, r) for l in range(n) for r in range(l, n) if all(a[i] != 1 for i in range(l, r + 1))]
    twos = [i for i in range(n) if a[i] == 2]
    cnt = 0
    for seq in itertools.product(ints, repeat=m):
        cov = set()
        for l, r in seq: cov.update(range(l, r + 1))
        if all(i in cov for i in twos): cnt += 1
    out.append(str(cnt % MOD))
print('\n'.join(out))
