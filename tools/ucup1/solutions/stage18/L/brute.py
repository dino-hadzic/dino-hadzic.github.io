# Sporo rješenje: sve rasporede n ljudi u m kuća (odabir kuća + permutacija ljudi).
import sys
from itertools import combinations, permutations
def main():
    data = sys.stdin.read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        n, m = int(data[p]), int(data[p + 1]); p += 2
        a = []; b = []
        for i in range(n):
            a.append(int(data[p])); b.append(int(data[p + 1])); p += 2
        best = 0
        for houses in combinations(range(m), n):
            hs = set(houses)
            status = [(h - 1 in hs) or (h + 1 in hs) for h in houses]
            for perm in permutations(range(n)):
                tot = sum(a[perm[i]] if status[i] else b[perm[i]] for i in range(n))
                best = max(best, tot)
        out.append(str(best))
    print("\n".join(out))
main()
