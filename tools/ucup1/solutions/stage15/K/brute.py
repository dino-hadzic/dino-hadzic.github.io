# Za svaki upit: brid pripada Steinerovu stablu ako su otvoreni vrhovi iz [l,r] s obje strane.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split(); pos = 0
n, q = int(data[pos]), int(data[pos + 1]); pos += 2
s = list(data[pos]); pos += 1
otvoren = [False] + [ch == '1' for ch in s]
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
    adj[u].append((v, w)); adj[v].append((u, w))
par = [0] * (n + 1); pw = [0] * (n + 1); red = []
st = [1]; par[1] = -1
while st:
    v = st.pop(); red.append(v)
    for w, c in adj[v]:
        if w != par[v]: par[w] = v; pw[w] = c; st.append(w)
out = []
for _ in range(q):
    t = int(data[pos]); pos += 1
    if t == 1:
        x = int(data[pos]); pos += 1; otvoren[x] = not otvoren[x]
    else:
        l, r = int(data[pos]), int(data[pos + 1]); pos += 2
        cnt = [0] * (n + 1)
        for v in range(l, r + 1):
            if otvoren[v]: cnt[v] = 1
        ukupno = sum(cnt)
        if ukupno == 0: out.append('-1'); continue
        for v in reversed(red):
            if par[v] > 0: cnt[par[v]] += cnt[v]
        ans = 0
        for v in range(2, n + 1):
            if 0 < cnt[v] < ukupno: ans += pw[v]
        out.append(str(2 * ans))
print('\n'.join(out))
