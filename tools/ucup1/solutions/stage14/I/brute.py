import sys
# Iscrpno: za svaki podskup stapova provjeri razlicite boje i Lamanov uvjet
# (|T| <= 2|V(T)| - 3 za svaki neprazni podskup T), uzmi najveci. Odgovor 2N - max.
data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])
E = [(int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(M)]

def laman(sub):
    k = len(sub)
    for mask in range(1, 1 << k):
        vs = set(); cnt = 0
        for i in range(k):
            if mask >> i & 1:
                u, v, _ = sub[i]; vs.add(u); vs.add(v); cnt += 1
        if cnt > 2 * len(vs) - 3:
            return False
    return True

best = 0
for mask in range(1 << M):
    sub = [E[i] for i in range(M) if mask >> i & 1]
    if len(sub) <= best: continue
    cols = [c for _, _, c in sub]
    if len(set(cols)) != len(cols): continue
    if laman(sub): best = len(sub)
print(2 * N - best)
