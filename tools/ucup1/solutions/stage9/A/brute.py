# Brute force: izravno racunanje niza Q do n (Python veliki brojevi).
import sys
data = sys.stdin.read().split()
T = int(data[0]); ns = [int(x) for x in data[1:1+T]]
N = max(ns)
Q = [0] * (N + 1)
if N >= 1: Q[1] = 1
k = 1; cnt = 0   # P(i): k se pojavljuje k+1 puta
P = 1
for i in range(2, N + 1):
    cnt += 1
    if cnt == k + 1: k += 1; cnt = 0
    P = k
    Q[i] = Q[i - 1] + Q[P]
print('\n'.join(str(Q[n]) for n in ns))
