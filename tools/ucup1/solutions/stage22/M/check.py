# check.py <ulaz> <očekivano|-> <dobiveno>
# Simulira operacije: u svakoj operaciji odabrani vrhovi moraju postojati, biti
# različiti i međusobno nespojeni; brisanje vrha spaja sve njegove susjede.
# Na kraju svi vrhovi moraju biti izbrisani, a operacija je najviše 10.
import sys
inp, exp, got = sys.argv[1], sys.argv[2], sys.argv[3]
d = open(inp).read().split()
n = int(d[0])
adj = [set() for _ in range(n + 1)]
for i in range(n - 1):
    x, y = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    adj[x].add(y); adj[y].add(x)
g = open(got).read().split()
if not g:
    print('prazan izlaz'); sys.exit(1)
m = int(g[0]); p = 1
if m < 0 or m > 10:
    print('broj operacija', m); sys.exit(1)
alive = [True] * (n + 1)
for _ in range(m):
    if p >= len(g):
        print('prekratak izlaz'); sys.exit(1)
    k = int(g[p]); p += 1
    sel = [int(x) for x in g[p:p + k]]; p += k
    if len(sel) != k or len(set(sel)) != k:
        print('krivi broj/vrhovi u operaciji'); sys.exit(1)
    for v in sel:
        if not (1 <= v <= n) or not alive[v]:
            print('vrh ne postoji', v); sys.exit(1)
    ss = set(sel)
    for v in sel:
        if adj[v] & ss:
            print('odabrani vrhovi su spojeni', v); sys.exit(1)
    for v in sel:
        nb = list(adj[v])
        for a in nb:
            adj[a].discard(v)
            for b in nb:
                if a != b:
                    adj[a].add(b)
        adj[v] = set()
        alive[v] = False
if p != len(g):
    print('suvišni tokeni'); sys.exit(1)
if any(alive[1:]):
    print('nisu svi vrhovi izbrisani'); sys.exit(1)
sys.exit(0)
