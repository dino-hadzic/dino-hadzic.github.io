# Brute force: potpuni minimax nad skupom preostalih riječi (bitmaska), bez ikakvih redukcija.
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
n = int(data[0])
words = data[1:1 + n]
first = [w[0] for w in words]
last = [w[-1] for w in words]

@lru_cache(maxsize=None)
def win(letter, mask):
    # pobjeđuje li igrač na potezu koji mora odabrati riječ koja počinje slovom `letter`
    for i in range(n):
        if mask >> i & 1 and first[i] == letter:
            if not win(last[i], mask & ~(1 << i)):
                return True
    return False

full = (1 << n) - 1
ans = 0
for i in range(n):
    if not win(last[i], full & ~(1 << i)):
        ans += 1
print(ans)
