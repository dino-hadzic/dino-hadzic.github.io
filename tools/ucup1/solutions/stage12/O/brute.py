# Doslovna simulacija igre s pravilom ponavljanja: stanje (potez, pozicije, maska)
# uz skup vec videnih stanja; minimax po svim potezima.
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
data = sys.stdin.read().split()
n, m, A, B = map(int, data[:4])
g = [[] for _ in range(n + 1)]
p = 4
for _ in range(m):
    u, v = int(data[p]), int(data[p + 1]); p += 2
    g[u].append(v)
K = int(data[p]); p += 1
jewel = {}
for i in range(K):
    x, w = int(data[p]), int(data[p + 1]); p += 2
    jewel[x] = (i, w)

@lru_cache(maxsize=None)
def play(turn, pa, pb, mask, hist):
    # buduca razlika (Alice - Bob) iz ovog stanja; hist = frozenset videnih stanja (ukljucuje ovo)
    if mask == 0:
        return 0
    frm = pa if turn == 0 else pb
    best = None
    for v in g[frm]:
        gain = 0
        nm = mask
        if v in jewel and (mask >> jewel[v][0]) & 1:
            nm = mask ^ (1 << jewel[v][0])
            gain = jewel[v][1] if turn == 0 else -jewel[v][1]
        npa, npb = (v, pb) if turn == 0 else (pa, v)
        st = (1 - turn, npa, npb, nm)
        if nm == 0:
            val = gain
        elif st in hist:
            val = gain  # ponavljanje: igra zavrsava
        else:
            val = gain + play(1 - turn, npa, npb, nm, hist | {st})
        if best is None or (turn == 0 and val > best) or (turn == 1 and val < best):
            best = val
    return best

print(play(0, A, B, (1 << K) - 1, frozenset([(0, A, B, (1 << K) - 1)])))
