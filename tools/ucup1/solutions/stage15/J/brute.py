import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom import sijeku
data = sys.stdin.read().split(); pos = 0
n, q = int(data[pos]), int(data[pos + 1]); pos += 2
P = []
for _ in range(n): P.append((int(data[pos]), int(data[pos + 1]))); pos += 2
out = []
for _ in range(q):
    a = (int(data[pos]), int(data[pos + 1])); b = (int(data[pos + 2]), int(data[pos + 3])); pos += 4
    out.append('YES' if any(sijeku(a, b, P[i], P[(i + 1) % n]) for i in range(n)) else 'NO')
print('\n'.join(out))
