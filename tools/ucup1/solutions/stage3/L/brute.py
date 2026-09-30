# Brute force: sve permutacije krada; valjanost dana provjeravamo IZRAVNO po definiciji -
# pretragom (backtracking) nenegativnih visestrukosti svih jednostavnih putova medu petljama
# cije se sume po bridovima tocno podudaraju s opterecenjima aktivnih bridova.
import sys, itertools
sys.setrecursionlimit(10000)
d = sys.stdin.read().split(); p = 0
z = int(d[p]); p += 1
out = []
for _ in range(z):
    n, pp = int(d[p]), int(d[p+1]); p += 2
    loops = set(int(x) for x in d[p:p+pp]); p += pp
    E = {}
    for i in range(1, n):
        u, v, c = int(d[p]), int(d[p+1]), int(d[p+2]); p += 3
        E[i] = (u, v, c)
    k = int(d[p]); p += 1
    K = [int(x) for x in d[p:p+k]]; p += k
    def valid(active):
        adj = {v: [] for v in range(1, n + 1)}
        for i in active:
            u, v, c = E[i]; adj[u].append((v, i)); adj[v].append((u, i))
        paths = []
        for s in loops:
            stack = [(s, [], set([s]))]
            while stack:
                v, es, vis = stack.pop()
                if es and v in loops and v > s: paths.append(es)
                for w, i in adj[v]:
                    if w not in vis: stack.append((w, es + [i], vis | {w}))
        need = {i: E[i][2] for i in active}
        by_edge = {i: [pt for pt in paths if i in pt] for i in active}
        def rec():
            rest = [i for i in active if need[i] > 0]
            if not rest: return True
            e = min(rest, key=lambda i: need[i])
            for pt in by_edge[e]:
                if all(need[i] >= 1 for i in pt):
                    for i in pt: need[i] -= 1
                    if rec(): return True
                    for i in pt: need[i] += 1
            return False
        return rec()
    res = None
    if valid(set(E)):
        for perm in itertools.permutations(K):
            act = set(E); good = True
            for e in perm:
                act.discard(e)
                if not valid(act): good = False; break
            if good: res = perm; break
    if res is None: out.append("NIE")
    else: out.append("TAK"); out.append(' '.join(map(str, res)))
print('\n'.join(out))
