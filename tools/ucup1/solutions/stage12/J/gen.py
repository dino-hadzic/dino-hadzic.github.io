import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 300000
    L, R = [], []
    for i in range(n):
        if seed % 3 == 0:
            base = (i - n // 2) ** 2 // 75000 + 1  # konveksan oblik, gotovo napeto
            l = max(1, base - random.randint(0, 2)); r = l + random.randint(0, 3)
        else:
            l = random.randint(1, 10 ** 9); r = random.randint(l, 10 ** 9)
        L.append(l); R.append(min(r, 10 ** 9))
else:
    n = random.randint(3, 6)
    hi = random.choice([3, 6, 12])
    L, R = [], []
    for i in range(n):
        l = random.randint(1, hi); r = random.randint(l, hi)
        L.append(l); R.append(r)
print(n)
print(*L)
print(*R)
