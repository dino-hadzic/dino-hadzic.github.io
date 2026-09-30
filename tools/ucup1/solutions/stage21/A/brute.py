import sys
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
MOD = 998244353
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    seg = []
    for i in range(n): seg.append((int(data[p]), int(data[p + 1]), int(data[p + 2]))); p += 3
    cnt = 0
    for mask in range(1 << n):
        ok = True
        ch = [i for i in range(n) if mask >> i & 1]
        for a in range(len(ch)):
            for b in range(a + 1, len(ch)):
                i, j = ch[a], ch[b]
                if seg[i][2] != seg[j][2] and max(seg[i][0], seg[j][0]) <= min(seg[i][1], seg[j][1]): ok = False
        cnt += ok
    out.append(str(cnt % MOD))
print('\n'.join(out))
