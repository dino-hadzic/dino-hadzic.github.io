# check.py <ulaz> <ocekivano> <dobiveno>: TAK/NIE se podudara; plan simuliramo i provjeravamo
# svaki potez (susjedni stupovi, izvor neprazan, cilj nije pun), broj poteza <= 1e6 i da su
# na kraju svi stupovi jednobojni.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, k = int(inp[p]), int(inp[p+1]); p += 2
    st = [[]] + [[int(x) for x in inp[p + i * k:p + (i + 1) * k]] for i in range(n)] + [[]]
    p += n * k
    if e >= len(exp) or g >= len(got): fail("premalo izlaza")
    if exp[e] != got[g]: fail(f"test {tc}: {exp[e]} vs {got[g]}")
    v = got[g]; e += 1; g += 1
    if v == "TAK":
        e += 1 + 2 * int(exp[e])
        m = int(got[g]); g += 1
        if m > 10**6: fail(f"test {tc}: previse poteza")
        for t in range(m):
            a, b = int(got[g]), int(got[g+1]); g += 2
            if abs(a - b) != 1 or not (0 <= a <= n + 1 and 0 <= b <= n + 1): fail(f"test {tc}: potez {t} nisu susjedni")
            if not st[a]: fail(f"test {tc}: potez {t} izvor prazan")
            if len(st[b]) >= k: fail(f"test {tc}: potez {t} cilj pun")
            st[b].append(st[a].pop())
        if any(len(set(s)) > 1 for s in st): fail(f"test {tc}: stupovi nisu jednobojni")
if g != len(got): fail("visak izlaza")
print("OK")
