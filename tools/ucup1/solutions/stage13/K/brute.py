# Brute force: provjeri svaku cetvorku vrhova.
import sys
from itertools import combinations
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
adj = [set() for _ in range(n + 1)]
for i in range(m):
    a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    adj[a].add(b); adj[b].add(a)
cnt = 0
for q in combinations(range(1, n + 1), 4):
    if all(b in adj[a] for a, b in combinations(q, 2)):
        cnt += 1
print(cnt)
