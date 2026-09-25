# Checker: zbroj mora biti jednak očekivanom maksimumu, redoslijed mora biti permutacija
# i simulacija tog redoslijeda mora dati ispisani zbroj.
import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); p = 1; g = 0; e = 0
for tc in range(T):
    n, m = int(inp[p]), int(inp[p + 1]); p += 2
    ops = []
    for _ in range(m):
        ops.append(tuple(int(v) for v in inp[p:p + 4])); p += 4
    if g + 1 + m > len(got):
        print("prekratak izlaz"); sys.exit(1)
    s = int(got[g]); order = [int(v) for v in got[g + 1:g + 1 + m]]; g += 1 + m
    if sorted(order) != list(range(1, m + 1)):
        print(f"test {tc}: nije permutacija"); sys.exit(1)
    a = [0] * (n + 1)
    for i in order:
        l, x, r, y = ops[i - 1]
        a[l] = x; a[r] = y
    if sum(a) != s:
        print(f"test {tc}: zbroj {s} ne odgovara simulaciji {sum(a)}"); sys.exit(1)
    if exp is not None:
        es = int(exp[e]); e += 1 + m
        if es != s:
            print(f"test {tc}: očekivano {es}, dobiveno {s}"); sys.exit(1)
if g != len(got):
    print("previše izlaza"); sys.exit(1)
sys.exit(0)
