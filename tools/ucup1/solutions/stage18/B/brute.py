# Sporo rješenje: isprobaj sve monotone putove i izračunaj mex svakog.
import sys
def main():
    data = sys.stdin.read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        n, m = int(data[p]), int(data[p + 1]); p += 2
        a = []
        for i in range(n):
            a.append([int(x) for x in data[p:p + m]]); p += m
        best = 0
        def go(i, j, s):
            nonlocal best
            s = s | {a[i][j]}
            if i == n - 1 and j == m - 1:
                mex = 0
                while mex in s:
                    mex += 1
                best = max(best, mex)
                return
            if j + 1 < m:
                go(i, j + 1, s)
            if i + 1 < n:
                go(i + 1, j, s)
        go(0, 0, set())
        out.append(str(best))
    print("\n".join(out))
main()
