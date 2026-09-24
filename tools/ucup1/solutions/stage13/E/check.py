# check.py <ulaz> <ocekivano|-> <dobiveno>: YES/NO se mora slagati, a indeksi moraju proci uvjet checkera.
import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
n = int(inp[0]); a = list(map(int, inp[1:1 + n]))
if not got:
    print("prazan izlaz"); sys.exit(1)
if exp is not None and exp[0] != got[0]:
    print(f"ocekivano {exp[0]}, dobiveno {got[0]}"); sys.exit(1)
if got[0] == "NO":
    sys.exit(0)
if got[0] != "YES" or len(got) != 5:
    print("los format"); sys.exit(1)
i, j, p, q = [int(x) - 1 for x in got[1:5]]
if not (0 <= i < j < p < q < n):
    print("indeksi nisu rastuci / u rasponu"); sys.exit(1)
if a[q] // a[p] != a[j] // a[i]:
    print("kvocijenti se razlikuju"); sys.exit(1)
sys.exit(0)
