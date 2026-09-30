# check.py <ulaz> <ocekivano> <dobiveno>: relativna ili apsolutna greska <= 1e-8 po broju.
import sys
from decimal import Decimal, getcontext
getcontext().prec = 50
exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
if len(exp) != len(got): print("broj brojeva"); sys.exit(1)
for a, b in zip(exp, got):
    if 'e' in b.lower(): print("znanstveni zapis"); sys.exit(1)
    A, B = Decimal(a), Decimal(b)
    if abs(A - B) / max(Decimal(1), A) > Decimal("1e-8"): print(f"{a} vs {b}"); sys.exit(1)
print("OK")
