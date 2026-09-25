# Checker: format, pravilo "bez 4 uzastopne jednake", povezanost jedinica, broj jedinica = tvrdnja = optimum.
# Optimum: iz izlaza brute forcea (ako postoji), inače iz formule; oboje se mora slagati.
import sys
from collections import deque
def optimum(n, m):
    if n > m: n, m = m, n
    if m <= 3: return n * m
    if n == 2: return 2 * m - m // 2
    if n == 3: return 3 * m - m // 4 - m // 2
    kc = [0] * 4
    for i in range(n):
        for j in range(m): kc[(i + j) % 4] += 1
    return n * m - min(kc)
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); pi = 1; pe = 0; pg = 0
for t in range(T):
    n, m = int(inp[pi]), int(inp[pi + 1]); pi += 2
    opt = optimum(n, m)
    if exp is not None:
        be = int(exp[pe]); pe += 1 + n
        if be != opt: print(f"test {t}: brute {be} != formula {opt}"); sys.exit(1)
    try:
        cnt = int(got[pg]); rows = got[pg + 1:pg + 1 + n]; pg += 1 + n
    except (IndexError, ValueError): print(f"test {t}: los format"); sys.exit(1)
    if len(rows) != n or any(len(r) != m or set(r) - {'0', '1'} for r in rows): print(f"test {t}: losa matrica"); sys.exit(1)
    ones = sum(r.count('1') for r in rows)
    if cnt != ones: print(f"test {t}: tvrdnja {cnt} != broj jedinica {ones}"); sys.exit(1)
    if cnt != opt: print(f"test {t}: {cnt} != optimum {opt}"); sys.exit(1)
    for i in range(n):
        for j in range(m - 3):
            if rows[i][j] == rows[i][j+1] == rows[i][j+2] == rows[i][j+3]: print(f"test {t}: 4 u retku {i}"); sys.exit(1)
    for j in range(m):
        for i in range(n - 3):
            if rows[i][j] == rows[i+1][j] == rows[i+2][j] == rows[i+3][j]: print(f"test {t}: 4 u stupcu {j}"); sys.exit(1)
    start = next(((i, j) for i in range(n) for j in range(m) if rows[i][j] == '1'), None)
    if start is None: print(f"test {t}: nema jedinica"); sys.exit(1)
    seen = {start}; dq = deque([start])
    while dq:
        x, y = dq.popleft()
        for a, b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= a < n and 0 <= b < m and rows[a][b] == '1' and (a, b) not in seen: seen.add((a, b)); dq.append((a, b))
    if len(seen) != ones: print(f"test {t}: jedinice nisu povezane"); sys.exit(1)
if pg != len(got): print("visak izlaza"); sys.exit(1)
print("OK")
