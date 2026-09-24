# Brute force: isprobaj svih n! redoslijeda operacija i prebroji granice a_i != a_{i+1}.
import sys, itertools
data = sys.stdin.read().split()
n = int(data[0]); iv = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
best = 0
for perm in itertools.permutations(range(n)):
    a = [0] * (2 * n + 1)
    for i in perm:
        l, r = iv[i]
        for x in range(l, r): a[x] = i + 1
    best = max(best, sum(1 for i in range(2 * n) if a[i] != a[i + 1]))
print(best)
