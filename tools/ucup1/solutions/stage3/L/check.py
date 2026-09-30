# check.py <ulaz> <ocekivano> <dobiveno>: TAK/NIE se podudara; za TAK provjeravamo da je izlaz
# permutacija ukradenih bridova i da je svaki dan valjan po lokalnom kriteriju
# (vrh bez petlje: paran zbroj i 2*max <= zbroj).
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, pp = int(inp[p]), int(inp[p+1]); p += 2
    loops = set(int(x) for x in inp[p:p+pp]); p += pp
    E = {}
    for i in range(1, n):
        E[i] = (int(inp[p]), int(inp[p+1]), int(inp[p+2])); p += 3
    k = int(inp[p]); p += 1
    K = [int(x) for x in inp[p:p+k]]; p += k
    if e >= len(exp) or g >= len(got): fail("premalo izlaza")
    if exp[e] != got[g]: fail(f"test {tc}: {exp[e]} vs {got[g]}")
    v = got[g]; e += 1; g += 1
    if v == "TAK":
        e += k
        order = [int(x) for x in got[g:g+k]]; g += k
        if sorted(order) != sorted(K): fail(f"test {tc}: nije permutacija")
        act = set(E)
        def valid():
            S = {}; mx = {}
            for i in act:
                u, w, c = E[i]
                for x in (u, w): S[x] = S.get(x, 0) + c; mx[x] = max(mx.get(x, 0), c)
            return all(x in loops or (S[x] % 2 == 0 and 2 * mx[x] <= S[x]) for x in S)
        if not valid(): fail(f"test {tc}: dan 0 nevaljan")
        for x in order:
            act.discard(x)
            if not valid(): fail(f"test {tc}: nevaljan dan nakon krade {x}")
if g != len(got): fail("visak izlaza")
print("OK")
