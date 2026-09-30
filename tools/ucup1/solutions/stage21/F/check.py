# check.py <ulaz> <-> <dobiveni izlaz>
# Provjera: "Yes", k <= (n^2-1)/3, svaki L unutar mreže, h,w != 0,
# svako bijelo polje pokriveno točno jednom, crno polje nepokriveno.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); out = open(sys.argv[3]).read().split()
n, bi, bj = int(inp[0]), int(inp[1]), int(inp[2])
if not out or out[0] != 'Yes': fail('ocekivano Yes (rjesenje uvijek postoji)')
k = int(out[1])
if not (0 <= k <= (n * n - 1) // 3): fail(f'k={k} izvan dopustenog')
if len(out) != 2 + 4 * k: fail('krivi broj brojeva u izlazu')
cov = [[0] * (n + 1) for _ in range(n + 1)]
p = 2
for _ in range(k):
    r, c, h, w = map(int, out[p:p + 4]); p += 4
    if not (1 <= r <= n and 1 <= c <= n and 1 <= r + h <= n and 1 <= c + w <= n and h != 0 and w != 0):
        fail(f'nevaljan L {(r, c, h, w)}')
    lo, hi = sorted((r, r + h))
    for i in range(lo, hi + 1): cov[i][c] += 1
    lo, hi = sorted((c, c + w))
    for j in range(lo, hi + 1):
        if j != c: cov[r][j] += 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        want = 0 if (i, j) == (bi, bj) else 1
        if cov[i][j] != want: fail(f'polje {(i, j)} pokriveno {cov[i][j]} puta')
print('OK')
