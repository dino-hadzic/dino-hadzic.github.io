# Brute force: simuliraj kupnju za svaki iznos novca 0..sum(a)+1; ako i sum(a)+1 daje m knjiga -> Richman.
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1
out = []
for _ in range(T):
    n, m = int(data[p]), int(data[p+1]); p += 2
    a = [int(x) for x in data[p:p+n]]; p += n
    def kupi(money):
        c = 0
        for x in a:
            if money >= x: money -= x; c += 1
        return c
    best = None
    for money in range(0, sum(a) + 2):
        if kupi(money) == m: best = money
    if best is None: out.append('Impossible')
    elif best == sum(a) + 1: out.append('Richman')
    else: out.append(str(best))
print('\n'.join(out))
