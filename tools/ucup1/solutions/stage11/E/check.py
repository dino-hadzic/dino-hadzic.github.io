import sys
inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
e = open(exp).read().split(); g = open(got).read().split()
if len(e) != len(g): print('broj redaka', len(e), len(g)); sys.exit(1)
for a, b in zip(e, g):
    a = float(a); b = float(b)
    if abs(a - b) > 1e-6 * max(1.0, abs(a)):
        print('razlika', a, b); sys.exit(1)
sys.exit(0)
