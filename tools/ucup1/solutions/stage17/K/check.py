import sys
inp = open(sys.argv[1]).read().split()
exp_tok = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); p = 1; gi = 0
# iz očekivanog izlaza izvuci samo presude (moguće / -1)
exp = None
if exp_tok is not None:
    exp = []; e = 0
    while e < len(exp_tok):
        s = int(exp_tok[e]); e += 1
        exp.append(s >= 0)
        if s > 0: e += 4 * s
for tc in range(T):
    n = int(inp[p]); p += 1
    rows = []
    for _ in range(4):
        rows.append([0] + [int(x) for x in inp[p:p + n]]); p += n
    a = [None, rows[0], rows[1]]; b = [None, rows[2], rows[3]]
    s = int(got[gi]); gi += 1
    if exp is not None and exp[tc] != (s >= 0):
        print(f"test {tc}: ocekivano {'moguce' if exp[tc] else '-1'}, dobiveno {s}"); sys.exit(1)
    if s < 0:
        continue
    if s > 5 * n:
        print(f"test {tc}: previse koraka {s}"); sys.exit(1)
    for _ in range(s):
        x1, x2, y1, y2 = (int(got[gi + k]) for k in range(4)); gi += 4
        if x2 == y2 or not (1 <= x1 <= 2 and 1 <= y1 <= 2 and 1 <= x2 <= n and 1 <= y2 <= n):
            print(f"test {tc}: nevaljan potez"); sys.exit(1)
        if a[x1][x2] < a[3 - x1][x2] or a[y1][y2] < a[3 - y1][y2]:
            print(f"test {tc}: potez ne mijenja maksimume"); sys.exit(1)
        a[x1][x2], a[y1][y2] = a[y1][y2], a[x1][x2]
    if a != b:
        print(f"test {tc}: konacno stanje razlicito"); sys.exit(1)
if gi != len(got):
    print("visak izlaza"); sys.exit(1)
sys.exit(0)
