import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 300000
    L, R = [], []
    if seed % 3 == 0:
        # siroki intervali: ogroman broj nizova
        for i in range(n):
            L.append(random.randint(1, 10)); R.append(random.randint(10 ** 12 - 10, 10 ** 12))
    elif seed % 3 == 1:
        # oko fiksnog aritmetickog niza
        a, d = 5 * 10 ** 11, random.randint(-1000, 1000)
        for i in range(n):
            v = a + i * d
            L.append(max(1, v - random.randint(0, 5))); R.append(min(10 ** 12, v + random.randint(0, 5)))
    else:
        for i in range(n):
            l = random.randint(1, 10 ** 12); r = random.randint(l, 10 ** 12)
            L.append(l); R.append(r)
else:
    n = random.randint(2, 6)
    hi = random.choice([3, 6, 15, 40])
    L, R = [], []
    for i in range(n):
        l = random.randint(1, hi); r = random.randint(l, hi)
        L.append(l); R.append(r)
print(n)
print(*L)
print(*R)
