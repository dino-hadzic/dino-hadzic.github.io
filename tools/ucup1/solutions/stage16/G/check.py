#!/usr/bin/env python3
# Checker: |S| = floor(n/2), vrhovi razliciti, S i V\S oba dominirajuci.
import sys
inp = open(sys.argv[1]).read().split()
got = open(sys.argv[3]).read().split()
t = int(inp[0]); p = 1; q = 0
for tc in range(t):
    n, m = int(inp[p]), int(inp[p + 1]); p += 2
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = int(inp[p]), int(inp[p + 1]); p += 2
        adj[a].append(b); adj[b].append(a)
    k = n // 2
    S = got[q:q + k]; q += k
    if len(S) != k:
        print('premalo izlaza'); sys.exit(1)
    S = [int(x) for x in S]
    if any(not 1 <= v <= n for v in S) or len(set(S)) != k:
        print('nevaljani vrhovi'); sys.exit(1)
    inS = [False] * (n + 1)
    for v in S: inS[v] = True
    for v in range(1, n + 1):
        if not any(inS[u] != inS[v] for u in adj[v]):
            print(f'test {tc}: vrh {v} nema susjeda u suprotnom skupu'); sys.exit(1)
if q != len(got):
    print('visak izlaza'); sys.exit(1)
sys.exit(0)
