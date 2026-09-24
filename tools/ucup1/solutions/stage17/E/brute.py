import sys
def ccpc(t):
    n = len(t)
    if n % 3 != 1 or n < 4:
        return False
    k = n // 3
    for i, ch in enumerate(t):
        need = 'p' if i == 2 * k else 'c'
        if ch != '?' and ch != need:
            return False
    return True
data = sys.stdin.read().split()
T = int(data[0])
for s in data[1:1 + T]:
    n = len(s)
    print(sum(1 for l in range(n) for r in range(l, n) if ccpc(s[l:r + 1])))
