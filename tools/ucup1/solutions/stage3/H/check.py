# check.py <ulaz> <ocekivano> <dobiveno>: staza mora biti valjana (1 -> n, razliciti vrhovi, postojeci
# bridovi) i imati isti zbroj i isti sortirani multiskup duljina kao ocekivana staza.
import sys
def fail(m): print(m); sys.exit(1)
inp = open(sys.argv[1]).read().split(); exp = open(sys.argv[2]).read().split(); got = open(sys.argv[3]).read().split()
z = int(inp[0]); p = 1; e = 0; g = 0
for tc in range(z):
    n, m = int(inp[p]), int(inp[p+1]); p += 2
    E = {}
    for _ in range(m):
        u, v, w = int(inp[p]), int(inp[p+1]), int(inp[p+2]); p += 3
        E[(u, v)] = w; E[(v, u)] = w
    def multiset(tokens, pos, who):
        k = int(tokens[pos]); path = [int(x) for x in tokens[pos+1:pos+1+k]]
        if len(path) != k or path[0] != 1 or path[-1] != n or len(set(path)) != k: fail(f"test {tc}: {who}: losa staza")
        ws = []
        for a, b in zip(path, path[1:]):
            if (a, b) not in E: fail(f"test {tc}: {who}: nema brida {a}-{b}")
            ws.append(E[(a, b)])
        return pos + 1 + k, sorted(ws, reverse=True)
    e, me = multiset(exp, e, "ocekivano")
    g, mg = multiset(got, g, "dobiveno")
    if sum(me) != sum(mg): fail(f"test {tc}: razlicita duljina {sum(mg)} vs {sum(me)}")
    if me != mg: fail(f"test {tc}: multiskup {mg} vs {me}")
if g != len(got): fail("visak izlaza")
print("OK")
