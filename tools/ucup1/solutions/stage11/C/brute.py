# Brute force: isprobavaj y = 1, 2, 3, ... i izravno broji prijenose pisanog zbrajanja.
import sys
data = sys.stdin.read().split()
T = int(data[0]); p = 1
out = []
def carries(x, y):
    c = 0; cnt = 0
    while x > 0 or y > 0 or c > 0:
        s = x % 10 + y % 10 + c
        c = 1 if s >= 10 else 0
        cnt += c
        x //= 10; y //= 10
    return cnt
for _ in range(T):
    x, k = int(data[p]), int(data[p + 1]); p += 2
    ans = -1
    for y in range(1, 2000001):
        if carries(x, y) == k:
            ans = y; break
    out.append(str(ans))
print('\n'.join(out))
