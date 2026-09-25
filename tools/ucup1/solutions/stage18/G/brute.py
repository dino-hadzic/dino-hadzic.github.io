# Sporo rješenje: Kruskal na eksplicitnom potpunom grafu.
import sys
def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1; out = []
    for _ in range(T):
        n, m = int(data[p]), int(data[p + 1]); p += 2
        w = {}
        for _ in range(m):
            u, v, x = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
            w[(u, v)] = x
        edges = []
        for x in range(1, n + 1):
            for y in range(x + 1, n + 1):
                edges.append((w.get((x, y), y - x), x, y))
        edges.sort()
        par = list(range(n + 1))
        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]; a = par[a]
            return a
        tot = 0
        for c, x, y in edges:
            a, b = find(x), find(y)
            if a != b:
                par[a] = b; tot += c
        out.append(str(tot))
    print("\n".join(out))
main()
