# check.py <ulaz> <ocekivano> <dobiveno>: trojka mora davati jedinstvene aliase i imati isti zbroj kao ocekivana.
import sys
from collections import Counter
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1
if len(got) != 3 * z: fail("broj tokena")
for tc in range(z):
    n = int(inp[p]); p += 1
    ppl = [(inp[p + 2*i], inp[p + 2*i + 1]) for i in range(n)]; p += 2*n
    a, b, c = (int(x) for x in got[3*tc:3*tc+3])
    ea, eb, ec = (int(x) for x in exp[3*tc:3*tc+3])
    if min(a, b, c) < 0 or a + b + c == 0: fail(f"test {tc}: nedopustena trojka")
    if a + b + c != ea + eb + ec: fail(f"test {tc}: zbroj {a+b+c} != {ea+eb+ec}")
    cnt = Counter(im[:a] + pr[:b] for im, pr in ppl)
    if max(cnt.values()) > 10 ** c: fail(f"test {tc}: aliasi nisu jedinstveni")
print("OK")
