# Brute force: sve četvorke (a, b, c, d) s a <= b < c <= d, provjeri je li s[a..b]+s[c..d] oblika WW.
import sys
s = sys.stdin.readline().strip()
n = len(s)
cnt = 0
for a in range(n):
    for b in range(a, n):
        for c in range(b + 1, n):
            for d in range(c, n):
                t = s[a:b + 1] + s[c:d + 1]
                if len(t) % 2 == 0 and t[:len(t) // 2] == t[len(t) // 2:]:
                    cnt += 1
print(cnt)
