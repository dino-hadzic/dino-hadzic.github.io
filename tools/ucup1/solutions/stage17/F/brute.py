# Brute force: rjesavanje igre unatrag za sve parove pocetnih vrhova.
import sys
data = sys.stdin.read().split()
p = 0
T = int(data[p]); p += 1
for _ in range(T):
    n = int(data[p]); p += 1
    perm = [int(x) for x in data[p:p + n]]; p += n
    adj1 = [set() for _ in range(n + 1)]
    adj2 = [set() for _ in range(n + 1)]
    for i in range(1, n):
        adj1[i].add(i + 1); adj1[i + 1].add(i)
        adj2[perm[i - 1]].add(perm[i]); adj2[perm[i]].add(perm[i - 1])
    for v in range(1, n + 1):
        adj1[v].add(v); adj2[v].add(v)   # ostati na mjestu
    # winA[a][b]: progonitelj pobjeduje kad je bjegunac na potezu
    # winB[a][b]: progonitelj pobjeduje kad je progonitelj na potezu
    winA = [[a == b for b in range(n + 1)] for a in range(n + 1)]
    winB = [[a == b for b in range(n + 1)] for a in range(n + 1)]
    changed = True
    while changed:
        changed = False
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a == b:
                    continue
                if not winB[a][b] and any(winA[a][b2] for b2 in adj2[b]):
                    winB[a][b] = True; changed = True
                if not winA[a][b] and all(winB[a2][b] for a2 in adj1[a]):
                    winA[a][b] = True; changed = True
    ok = all(winA[a][b] for a in range(1, n + 1) for b in range(1, n + 1))
    print("Yes" if ok else "No")
