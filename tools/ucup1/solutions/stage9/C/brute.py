# Brute force: isprobaj sve uređene parove intervala (a1,a2,a3,a4).
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1
out = []
for _ in range(T):
    n = int(data[p]); s = data[p+1]; t = data[p+2]; p += 3
    d = [int(s[i] != t[i]) for i in range(n)]
    cnt = 0
    for a1 in range(n):
        for a2 in range(a1, n):
            for a3 in range(n):
                for a4 in range(a3, n):
                    x = d[:]
                    for i in range(a1, a2 + 1): x[i] ^= 1
                    for i in range(a3, a4 + 1): x[i] ^= 1
                    if not any(x): cnt += 1
    out.append(str(cnt))
print('\n'.join(out))
