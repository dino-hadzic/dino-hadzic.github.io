# Iscrpna pretraga: za n <= 6 probamo sve nizove a s vrijednostima 1..n (vise nije potrebno,
# jer LIS ovisi samo o relativnom poretku) i provjerimo daje li neki trazeni b.
import sys, itertools

def lis_pref(a):
    n = len(a); dp = [0]*n; res = []; best = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i]: dp[i] = max(dp[i], dp[j]+1)
        best = max(best, dp[i]); res.append(best)
    return res

def main():
    data = sys.stdin.read().split(); p = 0
    t = int(data[p]); p += 1
    out = []
    for _ in range(t):
        n = int(data[p]); p += 1
        b = [int(x) for x in data[p:p+n]]; p += n
        ans = None
        for a in itertools.product(range(1, n+1), repeat=n):
            if lis_pref(a) == b:
                ans = a; break
        if ans is None: out.append("NO")
        else: out.append("YES"); out.append(" ".join(map(str, ans)))
    print("\n".join(out))
main()
