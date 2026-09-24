# Checker: -1/0 točno; inače broj kružnica točno i polumjer s relativnom greškom <= 1e-6.
import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split("\n")
got = open(sys.argv[3]).read().split("\n")
exp = [l for l in exp if l.strip()]; got = [l for l in got if l.strip()]
T = int(inp[0])
if len(got) != T or len(exp) != T:
    print(f"broj redaka: očekivano {T}, dobiveno {len(got)}"); sys.exit(1)
for i in range(T):
    e, g = exp[i].split(), got[i].split()
    if len(e) != len(g):
        print(f"red {i}: '{exp[i]}' vs '{got[i]}'"); sys.exit(1)
    if e[0] != g[0]:
        print(f"red {i}: broj '{e[0]}' vs '{g[0]}'"); sys.exit(1)
    if len(e) == 2:
        a, b = float(e[1]), float(g[1])
        if abs(a - b) > 1e-6 * max(1.0, abs(a)):
            print(f"red {i}: polumjer {a} vs {b}"); sys.exit(1)
sys.exit(0)
