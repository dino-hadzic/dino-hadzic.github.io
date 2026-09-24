#!/usr/bin/env python3
# Spora referenca: prolazimo kroz SVE matrice B nad F_q, provjeravamo det B != 0 i brojimo
# f(B) izravno - za male ulaze nabrajanjem svih matrica A (AB = A), a za malo vece ulaze
# preko dimenzije jezgre od B - I (f(B) = q^{n * dim ker(B - I)}), sto slijedi iz A(B - I) = 0.
import sys
from itertools import product


def matmul(A, B, n, q):
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % q for j in range(n)] for i in range(n)]


def rank(M, n, q):
    M = [row[:] for row in M]
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, n):
            if M[i][c] % q:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [(v * inv) % q for v in M[r]]
        for i in range(n):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(n)]
        r += 1
    return r


def main():
    n, q, mod = map(int, sys.stdin.read().split())
    cells = n * n
    all_mats = None
    if q ** cells <= 1000:
        all_mats = [[list(t[i * n:(i + 1) * n]) for i in range(n)] for t in product(range(q), repeat=cells)]
    ans = 0
    for t in product(range(q), repeat=cells):
        B = [list(t[i * n:(i + 1) * n]) for i in range(n)]
        if rank(B, n, q) < n:
            continue
        if all_mats is not None:
            f = sum(1 for A in all_mats if matmul(A, B, n, q) == A)
        else:
            C = [[(B[i][j] - (1 if i == j else 0)) % q for j in range(n)] for i in range(n)]
            f = q ** (n * (n - rank(C, n, q)))
        ans = (ans + pow(3, f, mod)) % mod
    print(ans)


main()
