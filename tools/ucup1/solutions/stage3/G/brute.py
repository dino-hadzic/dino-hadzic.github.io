# Brute force: tocno racionalno racunanje trenutka prvog susreta lijevog i desnog policajca
# (minimum po svim parovima), odgovor v*T ispisan s 15 decimala.
import sys
from fractions import Fraction
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, v = int(d[p]), int(d[p+1]); p += 2
    L = []; R = []
    for _ in range(n):
        pos, sp = int(d[p]), int(d[p+1]); p += 2
        (L if pos < 0 else R).append((pos, sp))
    T = min(Fraction(pr - pl, vl + vr) for pl, vl in L for pr, vr in R)
    ans = T * v
    q = ans.numerator * 10**15 // ans.denominator
    out.append(f"{q // 10**15}.{q % 10**15:015d}")
print('\n'.join(out))
