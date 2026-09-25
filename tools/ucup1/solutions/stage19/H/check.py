# Checker: usporedba realnih brojeva s apsolutnom/relativnom greškom 1e-6.
import sys
inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
n = int(open(inp).read().split()[0])
e = open(exp).read().split()
g = open(got).read().split()
if len(e) != n or len(g) != n:
    print("krivi broj brojeva: očekivano %d, dobiveno %d" % (len(e), len(g)))
    sys.exit(1)
for i in range(n):
    a, b = float(e[i]), float(g[i])
    if abs(a - b) > 1e-6 * max(1.0, abs(a)):
        print("redak %d: očekivano %s, dobiveno %s" % (i + 1, e[i], g[i]))
        sys.exit(1)
sys.exit(0)
