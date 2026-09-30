# Brute force: backtracking koji gradi raspored rundu po rundu, viteza po vitezu, uvijek najmanjim
# dopustenim protivnikom; prvi pronadeni potpuni raspored je leksikografski najmanji.
import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []

def solve(n, k):
    rounds = []
    fought = [set() for _ in range(n)]

    def ok_pair(r, x, y):
        # provjeri uvjet turnira za novu borbu (x,y) u rundi r protiv svih prethodnih rundi
        for q in range(len(rounds)):
            prev = rounds[q]
            # (x vs y sada), a = x, b = y; c = prev[x]; d mora biti prev[y] -- ako je c vec sparen u r
            c = prev[x]; dcur = r[c]
            if dcur is not None and dcur != prev[y]: return False
            c2 = prev[y]; dcur2 = r[c2]
            if dcur2 is not None and dcur2 != prev[x]: return False
        # i simetricno: nova borba je (c,d) za neki raniji par (a,b) -- pokriveno gornjim jer provjeravamo oba kraja
        return True

    def fill(r, j):
        while j < n and r[j] is not None: j += 1
        if j == n: return True
        for y in range(j + 1, n):
            if r[y] is None and y not in fought[j] and ok_pair(r, j, y):
                r[j] = y; r[y] = j
                if fill(r, j + 1): return True
                r[j] = None; r[y] = None
        return False

    def rec():
        if len(rounds) == k: return True
        r = [None] * n
        # nabroji sve dopustene runde leksikografski (backtracking preko svih moguc. za tu rundu)
        return rec_round(r, 0)

    def rec_round(r, j):
        while j < n and r[j] is not None: j += 1
        if j == n:
            rounds.append(r[:])
            for x in range(n): fought[x].add(r[x])
            if rec(): return True
            for x in range(n): fought[x].discard(r[x])
            rounds.pop()
            return False
        for y in range(j + 1, n):
            if r[y] is None and y not in fought[j] and ok_pair(r, j, y):
                r[j] = y; r[y] = j
                if rec_round(r, j + 1): return True
                r[j] = None; r[y] = None
        return False

    if rec(): return rounds
    return None

for _ in range(T):
    n, k = int(data[p]), int(data[p+1]); p += 2
    res = solve(n, k)
    if res is None: out.append('Impossible')
    else:
        for r in res: out.append(' '.join(str(x + 1) for x in r))
print('\n'.join(out))
