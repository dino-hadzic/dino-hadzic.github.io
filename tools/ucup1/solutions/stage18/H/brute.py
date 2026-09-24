# Sporo rješenje: sve zamjene (i bez zamjene), pa svi rezovi.
import sys
def F(a):
    n = len(a); best = 0
    for k in range(1, n):
        p = a[0]
        for v in a[1:k]: p &= v
        s = a[k]
        for v in a[k + 1:]: s &= v
        best = max(best, p + s)
    return best
def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1; out = []
    for _ in range(T):
        n = int(data[p]); p += 1
        a = [int(v) for v in data[p:p + n]]; p += n
        best = F(a)
        for i in range(n):
            for j in range(i + 1, n):
                b = a[:]; b[i], b[j] = b[j], b[i]
                best = max(best, F(b))
        out.append(str(best))
    print("\n".join(out))
main()
