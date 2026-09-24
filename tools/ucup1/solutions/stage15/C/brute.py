# Iscrpno: sva savrsena sparivanja oznacenih vrhova s provjerom tipova i disjunktnosti bridova.
# Ispisuje samo YES/NO (check.py provjerava konkretno sparivanje rjesenja).
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
n = int(data[0]); par = [0] * (n + 1); dep = [0] * (n + 1); tip = [''] * (n + 1)
p = 1
for _ in range(n - 1):
    v, pp, t = int(data[p]), int(data[p + 1]), data[p + 2]; p += 3
    par[v] = pp; dep[v] = dep[pp] + 1; tip[v] = t
marked = [v for v in range(2, n + 1) if tip[v] != '-']

def put(a, b):
    # bridovi (kao dijete-vrh) na putu a-b
    e = set()
    while a != b:
        if dep[a] < dep[b]: a, b = b, a
        e.add(a); a = par[a]
    return e

def kompatibilni(a, b):
    ta, tb, da, db = tip[a], tip[b], dep[a], dep[b]
    if ta == 'Tong' or tb == 'Tong':
        return ta == tb == 'Tong' and da == db
    return {ta, tb} == {'Chang', 'Duan'} and (da > db if ta == 'Chang' else da < db)

def rek(ostali, koristeni):
    if not ostali:
        return True
    a = ostali[0]
    for b in ostali[1:]:
        if not kompatibilni(a, b): continue
        e = put(a, b)
        if e & koristeni: continue
        if rek([x for x in ostali if x != a and x != b], koristeni | e):
            return True
    return False

print('YES' if len(marked) % 2 == 0 and rek(marked, set()) else 'NO')
