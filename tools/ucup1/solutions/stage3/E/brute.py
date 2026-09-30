# Brute force: za svaki par (x,y) BFS-om nademo najmanji broj koji se moze napisati
# (brojevi ograniceni na 3n; svi dobiveni brojevi su kongruentni x modulo y-x, a silazak
# do najmanjeg koristi samo brojeve <= y) i usporedimo s gcd.
import sys
from math import gcd
d = sys.stdin.read().split()
z = int(d[0]); out = []
for t in range(1, z + 1):
    n = int(d[t]); cnt = 0
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            seen = {x, y}; st = [x, y]; B = 3 * n
            while st:
                a = st.pop()
                for b in list(seen):
                    for c in (2 * a - b, 2 * b - a):
                        if 0 < c <= B and c not in seen:
                            seen.add(c); st.append(c)
            if min(seen) == gcd(x, y): cnt += 1
    out.append(str(cnt))
print('\n'.join(out))
