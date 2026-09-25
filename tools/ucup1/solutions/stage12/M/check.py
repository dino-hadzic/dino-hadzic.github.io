# Checker: bojanje mora biti valjano (iste boje -> dostizivi) i koristiti
# jednako malo boja kao ocekivano (brute force ili sluzbeni izlaz).
import sys
inp = open(sys.argv[1]).read().split()
n, m = int(inp[0]), int(inp[1])
reach = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = int(inp[2 + 2 * i]), int(inp[3 + 2 * i])
    reach[a][b] = True
for v in range(1, n + 1):
    reach[v][v] = True
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if reach[i][k]:
            for j in range(1, n + 1):
                if reach[k][j]:
                    reach[i][j] = True
got = open(sys.argv[3]).read().split()
if len(got) != n:
    print('krivi broj vrijednosti'); sys.exit(1)
try:
    c = [int(x) for x in got]
except ValueError:
    print('nije broj'); sys.exit(1)
if any(x < 1 or x > n for x in c):
    print('boja izvan [1, N]'); sys.exit(1)
for i in range(n):
    for j in range(i + 1, n):
        if c[i] == c[j] and not (reach[i + 1][j + 1] or reach[j + 1][i + 1]):
            print(f'vrhovi {i+1} i {j+1} iste boje nisu dostizivi'); sys.exit(1)
if sys.argv[2] != '-':
    exp = [int(x) for x in open(sys.argv[2]).read().split()]
    if max(c) != max(exp):
        print(f'broj boja {max(c)} != optimalno {max(exp)}'); sys.exit(1)
sys.exit(0)
