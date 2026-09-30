# check.py <ulaz> <ocekivano> <dobiveno> – usporedba realnih brojeva s tolerancijom 1e-9
import sys
exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
if len(exp) != len(got): print('krivi broj linija'); sys.exit(1)
for e, g in zip(exp, got):
    e, g = float(e), float(g)
    if abs(e - g) > 1e-9 * max(1.0, abs(e)): print(f'{g} != {e}'); sys.exit(1)
print('OK')
