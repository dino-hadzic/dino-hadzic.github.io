# check.py <ulaz> <-> <dobiveni izlaz>
# Provjera: n redaka, 6 razlicitih brojeva u [0, 10^6], i skup svih mogucih XOR-ova
# (dinamika po kockicama nad skupom dostizivih vrijednosti) sadrzi samo visekratnike d.
import sys
def fail(m): print(m); sys.exit(1)
n, d = map(int, open(sys.argv[1]).read().split())
out = open(sys.argv[3]).read().split()
if len(out) != 6 * n: fail(f"ocekivano {6*n} brojeva, dobiveno {len(out)}")
vals = [int(x) for x in out]
if any(not (0 <= x <= 10**6) for x in vals): fail("broj izvan [0, 10^6]")
reach = {0}
for i in range(n):
    face = vals[6*i:6*i+6]
    if len(set(face)) != 6: fail(f"kockica {i+1}: lica nisu razlicita")
    reach = {r ^ f for r in reach for f in face}
    if len(reach) > 2_000_000: fail("skup dostizivih XOR-ova prevelik za provjeru")
if any(x % d for x in reach): fail("postoji XOR koji nije visekratnik d")
print("OK")
