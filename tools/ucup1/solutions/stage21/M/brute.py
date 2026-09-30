import sys, itertools
data = sys.stdin.read().split(); p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n, m = int(data[p]), int(data[p + 1]); p += 2
    par = [0] * (n + 1); ch = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        par[i] = int(data[p]); p += 1; ch[par[i]].append(i)
    keys = [int(x) for x in data[p:p + m]]; p += m
    nodes = [v for v in range(n + 1) if ch[v]]
    perms = [list(itertools.permutations(range(len(ch[v])))) for v in nodes]
    best = None
    for choice in itertools.product(*perms):
        letter = [''] * (n + 1)
        for v, pm in zip(nodes, choice):
            for idx, c in zip(pm, ch[v]): letter[c] = chr(ord('a') + idx)
        s = [''] * (n + 1)
        for v in range(1, n + 1): s[v] = s[par[v]] + letter[v]
        B = sorted(s[k] for k in keys)
        ans = ''.join(letter[1:])
        if best is None or (B, ans) < best: best = (B, ans)
    out.append(best[1])
print('\n'.join(out))
