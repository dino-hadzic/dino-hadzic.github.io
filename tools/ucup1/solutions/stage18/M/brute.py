# Sporo rješenje: sve permutacije operacija.
import sys
from itertools import permutations
def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1; out = []
    for _ in range(T):
        n, m = int(data[p]), int(data[p + 1]); p += 2
        ops = []
        for _ in range(m):
            ops.append(tuple(int(v) for v in data[p:p + 4])); p += 4
        best = -1; bo = None
        for perm in permutations(range(m)):
            a = [0] * (n + 1)
            for i in perm:
                l, x, r, y = ops[i]
                a[l] = x; a[r] = y
            s = sum(a)
            if s > best:
                best = s; bo = perm
        out.append(str(best)); out.append(' '.join(str(i + 1) for i in bo))
    print("\n".join(out))
main()
