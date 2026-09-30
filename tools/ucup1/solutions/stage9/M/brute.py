import sys
R = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
def f(x): return sum(R[int(c)] for c in str(x))
data = sys.stdin.read().split()
T = int(data[0]); p = 1; out = []
for _ in range(T):
    x, k = int(data[p]), int(data[p+1]); p += 2
    for _ in range(min(k, 50)):   # nakon 50 koraka vrijednost je sigurno u ciklusu 0,1
        x = f(x)
    if k > 50 and (k - 50) % 2 == 1: x = 1 - x
    out.append(str(x))
print('\n'.join(out))
