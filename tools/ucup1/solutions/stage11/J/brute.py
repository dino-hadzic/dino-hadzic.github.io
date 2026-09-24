# Brute force: za svaki podskup nedostajucih bridova (po rastucoj velicini) izravno odigraj igru
# potjere (retrogradna analiza) iz SVAKOG pocetnog para (u, v) i provjeri hvata li Pang.
import sys
from itertools import combinations
data = sys.stdin.read().split()
pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    n = int(data[pos]); pos += 1
    edges = set()
    for i in range(n - 1):
        a, b = int(data[pos]) - 1, int(data[pos + 1]) - 1; pos += 2
        edges.add((min(a, b), max(a, b)))
    missing = [(a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in edges]

    def pang_catches_someone(E):
        N = [{v} for v in range(n)]
        for a, b in E: N[a].add(b); N[b].add(a)
        # win[s][p][t]: Pang sigurno hvata iz stanja (Shou u s, Pang u p, t = 0 Shou na potezu, 1 Pang)
        win = [[[False, False] for _ in range(n)] for _ in range(n)]
        for s in range(n):
            win[s][s][0] = win[s][s][1] = True
        changed = True
        while changed:
            changed = False
            for s in range(n):
                for p in range(n):
                    if s == p: continue
                    if not win[s][p][1] and any(win[s][q][0] for q in N[p]):
                        win[s][p][1] = True; changed = True
                    if not win[s][p][0] and all(win[t][p][1] for t in N[s]):
                        win[s][p][0] = True; changed = True
        return any(win[s][p][0] for s in range(n) for p in range(n) if s != p)

    ans = -1
    for k in range(len(missing) + 1):
        found = False
        for extra in combinations(missing, k):
            if not pang_catches_someone(edges | set(extra)):
                found = True; break
        if found:
            ans = k; break
    out.append(str(ans))
print('\n'.join(out))
