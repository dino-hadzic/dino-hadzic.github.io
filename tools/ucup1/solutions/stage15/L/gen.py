import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
PR = [2, 3, 5, 7, 11, 13]

def vrijednost(lim):
    # produkt malih prostih brojeva -> zanimljivi gcd-ovi
    v = 1
    for pnum in PR:
        e = random.choice([0, 0, 1, 2, 3])
        v *= pnum ** e
    return v if v <= lim else random.randint(1, lim)

if mode == 'big':
    n = 100000; q = 66666
    if seed % 2 == 0:
        a = [2 ** (59 - (i % 60)) * random.choice([1, 3, 5]) % (10**18) or 1 for i in range(n)]
        a = [min(x, 10**18) for x in a]
    else:
        a = [vrijednost(10**18) * random.choice([1, 2**random.randint(0, 40)]) for _ in range(n)]
        a = [min(x, 10**18) for x in a]
    ks = [1] * 66000 + [2] * 660 + [3] * 6
    random.shuffle(ks)
    qs = []
    for k in ks:
        if random.random() < 0.5:
            l = random.randint(1, n // 2); r = random.randint(max(l + k, n // 2), n)
        else:
            l = random.randint(1, n - k); r = random.randint(l + k, n)
        qs.append((l, r, k))
else:
    n = random.randint(2, 8); q = random.randint(1, 6)
    a = [vrijednost(10**18) if random.random() < 0.8 else random.randint(1, 10**18) for _ in range(n)]
    qs = []
    for _ in range(q):
        l = random.randint(1, n - 1); r = random.randint(l + 1, n)
        k = random.randint(1, min(3, r - l))
        qs.append((l, r, k))
print(n, q)
print(*a)
for l, r, k in qs:
    print(l, r, k)
