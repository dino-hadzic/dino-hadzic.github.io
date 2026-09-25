# Checker: ispisano stablo mora biti stablo i svaki D_i mora biti valjan DFS
# poredak toga stabla (ukorijenjenog u i).
import sys
sys.setrecursionlimit(10000)

def is_dfs_order(adj, order):
    n = len(order)
    pos = {v: i for i, v in enumerate(order)}
    if len(pos) != n:
        return False
    # iterativna provjera: stog aktivnih vrhova; sljedeci vrh mora biti
    # neposjeceni susjed vrha na vrhu stoga (nakon popanja zavrsenih vrhova)
    stack = [order[0]]
    seen = {order[0]}
    for v in order[1:]:
        while stack and all(u in seen for u in adj[stack[-1]]):
            stack.pop()
        if not stack or v not in adj[stack[-1]] or v in seen:
            return False
        seen.add(v)
        stack.append(v)
    return True

def main():
    inp = open(sys.argv[1]).read().split()
    got = open(sys.argv[3]).read().split()
    p = 0
    T = int(inp[p]); p += 1
    g = 0
    for _ in range(T):
        n = int(inp[p]); p += 1
        D = []
        for i in range(n):
            D.append([int(x) for x in inp[p:p + n]]); p += n
        adj = [set() for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = int(got[g]), int(got[g + 1]); g += 2
            if not (1 <= u <= n and 1 <= v <= n) or u == v or v in adj[u]:
                print("bad edge"); sys.exit(1)
            adj[u].add(v); adj[v].add(u)
        # povezanost
        seen = {1}; st = [1]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        if len(seen) != n:
            print("not a tree"); sys.exit(1)
        for order in D:
            if not is_dfs_order(adj, order):
                print("order mismatch"); sys.exit(1)
    if g != len(got):
        print("extra output"); sys.exit(1)
    sys.exit(0)

main()
