# Brute force: simuliraj proces dok se neki niz ne ponovi; broj razlicitih nizova = broj koraka do ponavljanja.
import sys
data = sys.stdin.read().split()
T = int(data[0]); out = []
for s in data[1:1 + T]:
    seen = set(); n = len(s)
    while s not in seen:
        seen.add(s)
        t = list(s)
        for i in range(n):
            if s[i] == '0' and s[(i + 1) % n] == '1':
                t[i] = '1'; t[(i + 1) % n] = '0'
        s = ''.join(t)
    out.append(str(len(seen) % 998244353))
print('\n'.join(out))
