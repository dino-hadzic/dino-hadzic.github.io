# Potpuna pretraga stanja igre: stanje = (sortirane hrpe, tko je na potezu, koliko poteza Grundy jos mora odigrati).
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def win(piles, grundy, second):
    # vraca True ako igrac na potezu (Sprague ako grundy=False) pobjeduje
    # second=True: Grundy je vec odigrao prvi potez i sad igra drugi
    if not piles:
        # kamenja nema: zadnji je uzeo protivnik igraca koji bi sad igrao
        return False
    for i, a in enumerate(piles):
        for j in range(1, a + 1):
            rest = list(piles[:i]) + list(piles[i+1:])
            if a - j > 0: rest.append(a - j)
            rest = tuple(sorted(rest))
            if not rest:
                return True  # uzeo zadnji kamen
            if grundy and not second:
                # Grundy mora odigrati jos jedan potez
                if win(rest, True, True): return True
            else:
                if not win(rest, not grundy, False): return True
    return False

data = sys.stdin.read().split(); p = 0
t = int(data[p]); p += 1
for _ in range(t):
    n = int(data[p]); p += 1
    a = tuple(sorted(int(x) for x in data[p:p+n])); p += n
    print("Sprague" if win(a, False, False) else "Grundy")
