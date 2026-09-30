import sys
data = sys.stdin.read().split(); p = 0
n, q = int(data[p]), int(data[p + 1]); p += 2
a = [0] + [int(x) for x in data[p:p + n]]; p += n
out = []
for _ in range(q):
    t = int(data[p]); p += 1
    if t == 1:
        v = int(data[p]); p += 1
        for i in range(1, n + 1): a[i] = min(a[i], v)
    elif t == 2:
        for i in range(1, n + 1): a[i] += i
    else:
        l, r = int(data[p]), int(data[p + 1]); p += 2
        out.append(str(sum(a[l:r + 1])))
print('\n'.join(out))
