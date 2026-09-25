# Checker: simulira program (2000 varijabli, 4 "CPU-a", citanja prije pisanja),
# provjerava A[i] = (1..i) za i <= N i da je L = max(ceil(log2 N), ceil(2(N-1)/5))
# (dokazana donja granica iz sluzbenog rjesenja; za uzorke i jednako sluzbenom L).
import sys, math
N = int(open(sys.argv[1]).read().split()[0])
toks = open(sys.argv[3]).read().split()
try:
    vals = [int(x) for x in toks]
except ValueError:
    print('nije broj'); sys.exit(1)
if not vals:
    print('prazan izlaz'); sys.exit(1)
L = vals[0]
if len(vals) != 1 + 12 * L:
    print('krivi broj brojeva'); sys.exit(1)
if any(v < 1 or v > 2000 for v in vals[1:]):
    print('vrijednost izvan [1,2000]'); sys.exit(1)
A = {i: (i,) for i in range(1, 2001)}
p = 1
for _ in range(L):
    ins = [(vals[p + 3 * k], vals[p + 3 * k + 1], vals[p + 3 * k + 2]) for k in range(4)]
    p += 12
    C = [A[a] + A[b] for c, a, b in ins]
    for (c, a, b), v in zip(ins, C):
        A[c] = v
for i in range(1, N + 1):
    if A[i] != tuple(range(1, i + 1)):
        print(f'A[{i}] nije (1..{i})'); sys.exit(1)
Lopt = max(math.ceil(math.log2(N)), -(-2 * (N - 1) // 5))
if sys.argv[2] != '-':
    Lexp = int(open(sys.argv[2]).read().split()[0])
    if Lexp != Lopt:
        print(f'formula {Lopt} ne odgovara sluzbenom L={Lexp}'); sys.exit(1)
if L != Lopt:
    print(f'L={L}, optimalno {Lopt}'); sys.exit(1)
sys.exit(0)
