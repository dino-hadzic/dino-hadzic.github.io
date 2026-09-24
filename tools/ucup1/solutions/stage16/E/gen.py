import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = (1 << 17) - 1
    kind = seed % 4
    if kind == 0:
        a = sorted(random.randint(1, n) for _ in range(n))
    elif kind == 1:
        h = n // 2
        a = [h] * (n - h) + [n] * h   # k ~ n/2, t ~ k u oba smjera
    elif kind == 2:
        a = sorted(random.randint(n // 2 - 5, n // 2 + 5) for _ in range(n))
    else:
        a = [n - 1] + [n] * (n - 1)   # k = t = n - 1: najveca evaluacija
    print(n); print(*a)
else:
    n = random.randint(1, 60) if seed % 4 else random.randint(200, 400)
    a = sorted(random.randint(1, n) for _ in range(n))
    print(n); print(*a)
