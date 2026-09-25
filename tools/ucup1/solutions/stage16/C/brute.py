#!/usr/bin/env python3
# Brute force: izravna simulacija za male m.
import sys
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
N = 1 << m
a = [0] * N
x = 0
pos = 2
for i in range(1, n + 1):
    p, q = int(data[pos]), int(data[pos + 1]); pos += 2
    l, r = (p + x) % N, (q + x) % N
    if l > r:
        l, r = r, l
    for j in range(l, r + 1):
        a[j] += i
        x += a[j]
print(x % (1 << 30))
