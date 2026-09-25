# Usporedba YES/NO s brute forceom; za YES provjera ispisanog sparivanja.
import sys
inp, exp, got = sys.argv[1:4]
data = open(inp).read().split()
n = int(data[0]); par = [0] * (n + 1); dep = [0] * (n + 1); tip = [''] * (n + 1)
p = 1
for _ in range(n - 1):
    v, pp, t = int(data[p]), int(data[p + 1]), data[p + 2]; p += 3
    par[v] = pp; dep[v] = dep[pp] + 1; tip[v] = t
tok = open(got).read().split()
ocek = open(exp).read().split()[0] if exp != '-' else None
if not tok: print('prazan izlaz'); sys.exit(1)
if ocek is not None and tok[0] != ocek:
    print('ocekivano', ocek, 'dobiveno', tok[0]); sys.exit(1)
if tok[0] == 'NO':
    sys.exit(0)
pairs = [(int(tok[i]), int(tok[i + 1])) for i in range(1, len(tok), 2)]
marked = set(v for v in range(2, n + 1) if tip[v] != '-')
seen = set(); used = set()
for a, b in pairs:
    if a not in marked or b not in marked or a in seen or b in seen or a == b:
        print('los par', a, b); sys.exit(1)
    seen |= {a, b}
    ta, tb = tip[a], tip[b]
    if 'Tong' in (ta, tb):
        ok = ta == tb and dep[a] == dep[b]
    else:
        ok = {ta, tb} == {'Chang', 'Duan'} and (dep[a] > dep[b] if ta == 'Chang' else dep[a] < dep[b])
    if not ok: print('nekompatibilan par', a, b); sys.exit(1)
    x, y = a, b
    while x != y:
        if dep[x] < dep[y]: x, y = y, x
        if x in used: print('brid koristen dvaput', x); sys.exit(1)
        used.add(x); x = par[x]
if seen != marked: print('nisu svi spareni'); sys.exit(1)
sys.exit(0)
