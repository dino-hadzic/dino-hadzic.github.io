# check.py <ulaz> <ocekivano> <dobiveno>: TAK/NIE se podudara; za TAK simuliramo partiju.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, k = int(inp[p]), int(inp[p+1]); p += 2
    b = inp[p:p+n]; p += n
    if e >= len(exp) or g >= len(got): fail("premalo izlaza")
    if exp[e] != got[g]: fail(f"test {tc}: {exp[e]} vs {got[g]}")
    verdict = got[g]; e += 1; g += 1
    if verdict == "TAK":
        cnt = sum(1 for r in b for c in r if c != '.')
        e += 2 * cnt
        moves = []
        for _ in range(cnt):
            if g + 1 >= len(got): fail("premalo poteza")
            moves.append((int(got[g]) - 1, int(got[g+1]) - 1)); g += 2
        if len(set(moves)) != cnt: fail(f"test {tc}: ponovljeno polje")
        board = [['.'] * n for _ in range(n)]
        def win(sym):
            for i in range(n):
                for j in range(n):
                    for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
                        cs = [(i + t * dx, j + t * dy) for t in range(k)]
                        if all(0 <= x < n and 0 <= y < n and board[x][y] == sym for x, y in cs): return True
            return False
        prev = None
        for t, (i, j) in enumerate(moves):
            if not (0 <= i < n and 0 <= j < n) or b[i][j] == '.': fail(f"test {tc}: krivo polje")
            sym = b[i][j]
            if prev is not None and sym == prev: fail(f"test {tc}: nije naizmjence")
            prev = sym
            board[i][j] = sym
            if win(sym) and t != cnt - 1: fail(f"test {tc}: pobjeda prije kraja")
        if board != [list(r) for r in b]: fail(f"test {tc}: ploca se ne podudara")
        last = b[moves[-1][0]][moves[-1][1]]
        if not win(last) and cnt != n * n: fail(f"test {tc}: igra nije zavrsena")
if g != len(got): fail("visak izlaza")
print("OK")
