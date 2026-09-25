import sys
data = sys.stdin.read().split()
n, q = int(data[0]), int(data[1]); s = data[2]; p = 3
def f(t):
    return "".join(t[i] for i in range(len(t)) if i > 0 and t[i] == t[i - 1])
out = []
for _ in range(q):
    l, r, k = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    t = s[l - 1:r]
    for _ in range(k):
        if not t: break
        t = f(t)
    out.append(str(len(t)))
print("\n".join(out))
