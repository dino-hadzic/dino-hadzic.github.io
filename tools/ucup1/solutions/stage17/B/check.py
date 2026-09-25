import sys
sys.setrecursionlimit(10000)
inp = open(sys.argv[1]).read().split()
exp_tok = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); p = 1; gi = 0
def find(f, x):
    if f[x] == x: return x
    f[x] = find(f, f[x]); return f[x]
# iz očekivanog izlaza izvuci samo presude YES/NO
exp = None
if exp_tok is not None:
    exp = []; e = 0
    while e < len(exp_tok):
        exp.append(exp_tok[e]); e += 1
        if exp[-1] == 'YES':
            m = int(exp_tok[e]); e += 1
            for _ in range(m):
                e += 2 if exp_tok[e] == '1' else 3
for tc in range(T):
    n = int(inp[p]); p += 1
    f = [0] + [int(x) for x in inp[p:p + n]]; p += n
    g = [0] + [int(x) for x in inp[p:p + n]]; p += n
    ans = got[gi]; gi += 1
    if exp is not None and exp[tc] != ans:
        print(f"test {tc}: ocekivano {exp[tc]}, dobiveno {ans}"); sys.exit(1)
    if ans == "NO":
        continue
    if ans != "YES":
        print("krivi format"); sys.exit(1)
    m = int(got[gi]); gi += 1
    if m > 2 * n * n:
        print("previse operacija"); sys.exit(1)
    for _ in range(m):
        t = got[gi]; gi += 1
        if t == '1':
            x = int(got[gi]); gi += 1
            find(f, x)
        else:
            x = int(got[gi]); y = int(got[gi + 1]); gi += 2
            a = find(f, x); b = find(f, y)
            if a != b: f[a] = b
    if f != g:
        print(f"test {tc}: konacno stanje {f[1:]} != {g[1:]}"); sys.exit(1)
if gi != len(got):
    print("visak izlaza"); sys.exit(1)
sys.exit(0)
