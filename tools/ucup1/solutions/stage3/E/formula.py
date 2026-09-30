# Neovisna (spora, O(n^{3/4})) implementacija formule sum_d D(floor(n/d)-1) za srednje n.
import sys
def D(m):
    r = 0; i = 1
    while i <= m:
        q = m // i; j = m // q
        r += q * (j - i + 1); i = j + 1
    return r
for tok in sys.stdin.read().split()[1:]:
    n = int(tok); d = 1; ans = 0
    while d <= n:
        v = n // d; j = n // v
        ans += (j - d + 1) * D(v - 1); d = j + 1
    print(ans)
