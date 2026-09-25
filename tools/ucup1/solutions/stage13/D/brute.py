# Brute force: egzaktna determinanta u cijelim brojevima (Python veliki brojevi).
# n <= 6: Leibnizova formula po svim permutacijama; vece n: Bareissov algoritam bez dijeljenja s ostatkom.
import sys
from itertools import permutations
MOD = 998244353

def leibniz(A, n):
    det = 0
    for perm in permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        prod = 1
        for i in range(n):
            prod *= A[i][perm[i]]
        det += -prod if inv % 2 else prod
    return det

def bareiss(A, n):
    M = [row[:] for row in A]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((r for r in range(k + 1, n) if M[r][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]

data = sys.stdin.read().split()
t = int(data[0]); pos = 1
out = []
for _ in range(t):
    n = int(data[pos]); pos += 1
    b = list(map(int, data[pos:pos + n])); pos += n
    c = list(map(int, data[pos:pos + n])); pos += n
    A = [[b[i] ^ c[j] for j in range(n)] for i in range(n)]
    det = leibniz(A, n) if n <= 6 else bareiss(A, n)
    out.append(str(det % MOD))
print('\n'.join(out))
