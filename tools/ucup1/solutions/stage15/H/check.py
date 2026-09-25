# Usporedba realnog odgovora s tolerancijom 1e-6 (apsolutna ili relativna).
import sys
inp, exp, got = sys.argv[1:4]
b = float(open(exp).read().split()[0])
a = float(open(got).read().split()[0])
if abs(a - b) / max(1.0, abs(b)) <= 1e-6:
    sys.exit(0)
print('ocekivano', b, 'dobiveno', a)
sys.exit(1)
