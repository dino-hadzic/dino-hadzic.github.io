# check.py <ulaz> <ocekivano> <dobiveno>: TAK/NIE mora se podudarati; za TAK simuliramo niz T/N.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, k = int(inp[p]), int(inp[p+1]); p += 2
    ab = [(int(inp[p+2*i]), int(inp[p+2*i+1])) for i in range(k)]; p += 2*k
    s = int(inp[p]); p += 1
    en = [int(x) for x in inp[p:p+s]]; p += s
    if e >= len(exp) or g >= len(got): fail("premalo izlaza")
    ve, vg = exp[e], got[g]; e += 1; g += 1
    if ve != vg: fail(f"test {tc}: ocekivano {ve}, dobiveno {vg}")
    if ve == "TAK":
        e += 1
        if g >= len(got): fail("nema niza")
        st = got[g]; g += 1
        if len(st) != k or any(c not in "TN" for c in st): fail(f"test {tc}: los niz")
        alive = [True] * (n + 1)
        for i, (a, b) in enumerate(ab):
            if st[i] == 'T' and alive[a] and alive[b]: alive[b] = False
        if any(alive[x] for x in en): fail(f"test {tc}: neprijatelj prezivio")
if g != len(got): fail("visak izlaza")
print("OK")
