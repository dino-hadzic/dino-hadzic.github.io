# check.py <ulaz> <ocekivano> <dobiveno>: TAK/NIE se podudara; za TAK provjeravamo raspored.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, q = int(inp[p]), int(inp[p+1]); p += 2
    cons = [tuple(int(x) for x in inp[p+4*i:p+4*i+4]) for i in range(q)]; p += 4 * q
    if e >= len(exp) or g >= len(got): fail("premalo izlaza")
    if exp[e] != got[g]: fail(f"test {tc}: {exp[e]} vs {got[g]}")
    v = got[g]; e += 1; g += 1
    if v == "TAK":
        e += 1
        if g >= len(got): fail("nema rasporeda")
        s = got[g]; g += 1
        if len(s) != 3 * n or any(c not in "FR" for c in s): fail(f"test {tc}: los niz")
        if s.count('F') > 2 * n or s.count('R') > 2 * n: fail(f"test {tc}: previse cvjetova jedne vrste")
        for a, b, c, d in cons:
            if not (set(s[a-1:b]) == {'R'} or set(s[c-1:d]) == {'F'}): fail(f"test {tc}: uvjet {a,b,c,d} prekrsen")
if g != len(got): fail("visak izlaza")
print("OK")
