import sys
# Iscrpno: probamo svih 2^(3N) izbora linija (N <= 5).
data = sys.stdin.read().split()
n = int(data[0]); s = data[1:1 + n]
cells = [(i, j) for i in range(n) for j in range(i + 1)]
for mask in range(1 << (3 * n)):
    r = [(mask >> i) & 1 for i in range(n)]
    c = [(mask >> (n + j)) & 1 for j in range(n)]
    d = [(mask >> (2 * n + k)) & 1 for k in range(n)]
    if all((r[i] ^ c[j] ^ d[i - j]) == int(s[i][j]) for i, j in cells):
        print('Yes'); break
else:
    print('No')
