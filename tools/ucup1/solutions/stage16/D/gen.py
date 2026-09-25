import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 5000
    kind = seed % 3
    if kind == 0:
        a = sorted(random.randint(1, n) for _ in range(n))
    elif kind == 1:
        a = [n] * n           # puna ploca
    else:
        a = [i + 1 for i in range(n)]  # stubiste
    print(n); print(*a)
else:
    n = random.randint(1, 4) if seed % 5 else 5
    a = sorted(random.randint(1, n) for _ in range(n))
    print(n); print(*a)
