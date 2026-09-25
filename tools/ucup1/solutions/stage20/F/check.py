# check.py <ulaz> <ocekivani izlaz ili -> <dobiveni izlaz>
# YES/NO se mora slagati s brute forceom, a ispisani niz a mora imati trazene LIS-ove prefiksa.
import sys

def lis_pref(a):
    n = len(a); dp = [0]*n; res = []; best = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i]: dp[i] = max(dp[i], dp[j]+1)
        best = max(best, dp[i]); res.append(best)
    return res

def fail(msg):
    print(msg); sys.exit(1)

inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
out = open(sys.argv[3]).read().split()
p = 0; t = int(inp[p]); p += 1; q = 0; r = 0
for tc in range(t):
    n = int(inp[p]); p += 1; b = [int(x) for x in inp[p:p+n]]; p += n
    if q >= len(out): fail("premalo izlaza")
    verdict = out[q]; q += 1
    if exp is not None:
        ev = exp[r]; r += 1
        if verdict != ev: fail(f"test {tc}: {verdict} != {ev}")
        if ev == "YES": r += n
    else:
        # bez brute forcea: odgovor NO prihvacamo samo ako je nuzan uvjet narusen
        moguce = b[0] == 1 and all(b[i+1] - b[i] in (0, 1) for i in range(n-1))
        if (verdict == "YES") != moguce: fail(f"test {tc}: krivi verdikt {verdict}")
    if verdict == "YES":
        a = [int(x) for x in out[q:q+n]]; q += n
        if len(a) != n or any(not (1 <= x <= 10**9) for x in a): fail(f"test {tc}: los niz")
        if lis_pref(a) != b: fail(f"test {tc}: LIS prefiksa ne odgovara")
    elif verdict != "NO":
        fail(f"test {tc}: nepoznat verdikt {verdict}")
if q != len(out): fail("visak izlaza")
print("OK")
