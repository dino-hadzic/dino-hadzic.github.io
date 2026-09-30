import sys
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
def insert(a, v, is_max):
    a.append(v); i = len(a)
    while i > 1:
        par = i // 2
        if (not is_max and a[par - 1] <= a[i - 1]) or (is_max and a[par - 1] >= a[i - 1]): break
        a[par - 1], a[i - 1] = a[i - 1], a[par - 1]; i = par
for _ in range(T):
    n = int(data[p]); p += 1
    v = [int(x) for x in data[p:p + n]]; p += n
    fin = [int(x) for x in data[p:p + n]]; p += n
    ans = None
    for mask in range(1 << n):
        b = ''.join('1' if mask >> (n - 1 - i) & 1 else '0' for i in range(n))
        a = []
        for i in range(n): insert(a, v[i], b[i] == '1')
        if a == fin: ans = b; break
    out.append(ans if ans is not None else 'Impossible')
print('\n'.join(out))
