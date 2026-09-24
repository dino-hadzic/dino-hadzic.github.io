import sys
from itertools import product
data = list(map(int, sys.stdin.read().split()))
N = data[0]
A = tuple(data[1:4]); B = tuple(data[4:7]); C = tuple(data[7:10])
# 9 nerijesenih kombinacija (Alice, Bob, Chris), 0=R,1=P,2=S
ties = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (1, 0, 2), (2, 1, 0)]
cnt = 0
for seq in product(ties, repeat=N):
    a = [0, 0, 0]; b = [0, 0, 0]; c = [0, 0, 0]
    for x, y, z in seq:
        a[x] += 1; b[y] += 1; c[z] += 1
    if tuple(a) == A and tuple(b) == B and tuple(c) == C:
        cnt += 1
print(cnt % 998244353)
