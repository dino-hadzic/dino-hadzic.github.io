# Brute force: potpuna pretraga igre (stanje = permutacija + skupovi iskorištenih
# vrijednosti p_1 za oba igrača + tko je na potezu). Igrač koji mora odigrati
# operaciju s p_1 koje je već koristio gubi.
import sys
from itertools import permutations
from functools import lru_cache

MOD = 998244353

@lru_cache(maxsize=None)
def wins(perm, used_me, used_op):
    """Vraća True ako igrač na potezu pobjeđuje."""
    k = perm[0]
    if k in used_me:
        return False
    used_me2 = used_me | frozenset([k])
    prefix = perm[:k]
    rest = perm[k:]
    for q in set(permutations(prefix)):
        if not wins(q + rest, used_op, used_me2):
            return True
    return False

n = int(sys.stdin.read().split()[0])
cnt = 0
for p in permutations(range(1, n + 1)):
    if not wins(p, frozenset(), frozenset()):
        cnt += 1
print(cnt % MOD)
