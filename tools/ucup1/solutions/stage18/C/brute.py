# Sporo rješenje: isprobaj sve k-podskupove i za svaki izračunaj najveći lcp para.
import sys
from itertools import combinations
def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]
def main():
    data = sys.stdin.read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        n, k = int(data[p]), int(data[p + 1]); p += 2
        w = data[p:p + n]; p += n
        best = None
        for S in combinations(range(n), k):
            v = ""
            for i in range(len(S)):
                for j in range(i + 1, len(S)):
                    v = max(v, lcp(w[S[i]], w[S[j]]))
            if best is None or v < best:
                best = v
        out.append(best if best else "EMPTY")
    print("\n".join(out))
main()
