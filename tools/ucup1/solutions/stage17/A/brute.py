# Brute force: za svaki brid probamo obje uloge (T1 ili T2) i provjerimo
# nastaju li dva valjana korijenska stabla.
import sys
from itertools import product

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = 2 * n - 2
    edges = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(m)]
    cnt = 0
    for mask in product((0, 1), repeat=m):
        p1 = {}
        p2 = {}
        ok = True
        for (u, v), t in zip(edges, mask):
            if t == 0:  # brid u T1: dijete je veci vrh
                c, p = max(u, v), min(u, v)
                if c == p or c in p1:
                    ok = False
                    break
                p1[c] = p
            else:  # brid u T2: dijete je manji vrh
                c, p = min(u, v), max(u, v)
                if c == p or c in p2:
                    ok = False
                    break
                p2[c] = p
        if ok and len(p1) == n - 1 and len(p2) == n - 1:
            cnt += 1
    print(cnt % 998244353)

main()
