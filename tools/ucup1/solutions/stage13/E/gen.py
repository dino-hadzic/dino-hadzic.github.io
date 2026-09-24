import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def rastuci(n, lo, hi):
    s = set()
    while len(s) < n:
        s.add(random.randint(lo, hi))
    return sorted(s)
if mode == 'big':
    n = 500000
    if seed % 2:
        a = rastuci(n, 1, 10**18)
    else:
        # prvih ~59 elemenata udvostrucava, ostatak gusto
        a = [1]
        while len(a) < 59:
            a.append(a[-1] * 2 + random.randint(0, 1))
        rest = rastuci(n - len(a), a[-1] + 1, 10**18)
        a += rest
    print(n); print(*a)
else:
    n = random.randint(4, 9)
    tip = random.random()
    if seed % 5 == 0:
        # n >= 63: sol koristi brzi put; ~55 udvostrucenja i ostatak s kvocijentom 1
        n = random.randint(63, 66)
        a = [random.randint(1, 3)]
        dup = set(random.sample(range(n - 1), 55))
        for t in range(n - 1):
            a.append(a[-1] * 2 + random.randint(0, 1) if t in dup else a[-1] + random.randint(1, 3))
    elif tip < 0.4:
        a = rastuci(n, 1, 30)
    elif tip < 0.7:
        # eksponencijalno rastuci niz - cesto NO
        a = [random.randint(1, 5)]
        for _ in range(n - 1):
            a.append(a[-1] * random.randint(2, 4) + random.randint(0, 3))
    else:
        a = rastuci(n, 1, 10**18)
    print(n); print(*a)
