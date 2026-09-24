# Brute force: probaj sve cetvorke i < j < p < q, uvjet checkera a[q]//a[p] == a[j]//a[i].
import sys
data = sys.stdin.read().split()
n = int(data[0]); a = list(map(int, data[1:1 + n]))
for i in range(n):
    for j in range(i + 1, n):
        for p in range(j + 1, n):
            for q in range(p + 1, n):
                if a[q] // a[p] == a[j] // a[i]:
                    print("YES"); print(i + 1, j + 1, p + 1, q + 1); sys.exit(0)
print("NO")
