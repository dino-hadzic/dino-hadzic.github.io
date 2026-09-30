import sys
sys.setrecursionlimit(10000)
# check.py <ulaz> <ocekivani ili -> <dobiveni>
# Dobiveni izlaz mora biti valjan nezavisan skup (u punom grafu: kaktus + ciklus
# listova DFS-stabla + stablo trece faze) cija je tezina jednaka ispisanom W;
# ako je ocekivani izlaz zadan, W mora biti jednak ocekivanom W.
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()

def fail(msg):
    print(msg); sys.exit(1)

p = 0
N, M = int(inp[p]), int(inp[p + 1]); p += 2
T = [int(x) for x in inp[p:p + N]]; p += N
g = [[] for _ in range(N)]
edges = set()
for _ in range(M):
    u, v = int(inp[p]), int(inp[p + 1]); p += 2
    g[u].append(v); g[v].append(u); edges.add((u, v))
K = int(inp[p]); p += 1
for _ in range(K):
    x, y = int(inp[p]), int(inp[p + 1]); p += 2
    edges.add((min(x, y), max(x, y)))
vis = [False] * N; par = [-1] * N; chc = [0] * N; pre = []
def dfs(v):
    vis[v] = True; pre.append(v)
    for w in g[v]:
        if not vis[w]:
            par[w] = v; chc[v] += 1; dfs(w)
dfs(0)
leaves = [v for v in pre if (v == 0 and chc[v] == 1) or (v != 0 and chc[v] == 0)]
for i in range(len(leaves)):
    a, b = leaves[i], leaves[(i + 1) % len(leaves)]
    edges.add((min(a, b), max(a, b)))

if len(got) < 2: fail('prekratak izlaz')
W, L = int(got[0]), int(got[1])
if L < 0 or L > N or len(got) != 2 + L: fail('los broj tokena')
S = [int(x) for x in got[2:]]
if any(not (0 <= s < N) for s in S): fail('vrh izvan raspona')
if any(S[i] >= S[i + 1] for i in range(L - 1)): fail('popis nije strogo rastuci')
if sum(T[s] for s in S) != W: fail('W ne odgovara zbroju tezina')
ss = set(S)
for (u, v) in edges:
    if u in ss and v in ss: fail('vrhovi %d i %d su susjedni' % (u, v))
if exp is not None and int(exp[0]) != W: fail('W=%d, ocekivano %s' % (W, exp[0]))
sys.exit(0)
