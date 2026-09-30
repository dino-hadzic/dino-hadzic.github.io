# Brute force: za svakog Moniphanta doslovno čuvamo razinu i skup ljutih razina.
import sys
data = sys.stdin.read().split()
n, q = int(data[0]), int(data[1]); p = 2
L = [500000] * (n + 1)
angry = [set() for _ in range(n + 1)]
out = []
for _ in range(q):
    op, l, r = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    for i in range(l, r + 1):
        if op == 1:
            L[i] += 1
        elif op == 2:
            L[i] -= 1
            angry[i] = {x for x in angry[i] if x <= L[i]}   # Mofunfun dublje razine nestaje
        elif op == 3:
            angry[i].add(L[i])
        elif op == 4:
            if angry[i]:
                L[i] = min(angry[i])
                angry[i] = {x for x in angry[i] if x < L[i]}  # sve dublje nestaje, a ta više nije ljuta
        else:
            out.append(str(L[i]))
print('\n'.join(out))
