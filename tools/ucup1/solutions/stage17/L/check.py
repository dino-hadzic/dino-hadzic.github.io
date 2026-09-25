import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); p = 1; g = 0; e = 0
for _ in range(T):
    n, k = int(inp[p]), int(inp[p + 1]); p += 2
    if exp is not None:
        exp_neg = exp[e] == '-1'
        e += 1 if exp_neg else n
    else:
        exp_neg = (n + k) % 2 == 1
    if got[g] == '-1':
        if not exp_neg:
            print("rekao -1, a rjesenje postoji"); sys.exit(1)
        g += 1
        continue
    if exp_neg:
        print("dao rjesenje, a ocekivano -1"); sys.exit(1)
    f = [0] + [int(x) for x in got[g:g + n]]; g += n
    if any(v not in (1, -1) for v in f[1:]) or f[1] != 1:
        print("krive vrijednosti"); sys.exit(1)
    if sum(f[1:]) != k:
        print("krivi zbroj"); sys.exit(1)
    lp = list(range(n + 1))
    for i in range(2, n + 1):
        if lp[i] == i:
            for j in range(i * i, n + 1, i):
                if lp[j] == j: lp[j] = i
    for i in range(2, n + 1):
        if lp[i] != i and f[i] != f[lp[i]] * f[i // lp[i]]:
            print("nije potpuno multiplikativna"); sys.exit(1)
if g != len(got):
    print("visak izlaza"); sys.exit(1)
sys.exit(0)
