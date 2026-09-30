import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    z = 6; print(z)
    for t in range(z):
        n = 500000; print(n)
        if t == 0: arr = [10**9] * n
        elif t == 1: arr = [random.randint(1, 10**9) for _ in range(n)]
        elif t == 2: arr = [10**9 - (i - n // 2) ** 2 // 100 for i in range(n)]   # konkavno: svi na ljusci
        elif t == 3: arr = [1 + i * 1000 for i in range(n)]
        else: arr = [random.randint(1, 10) for _ in range(n)]
        arr = [max(1, min(10**9, x)) for x in arr]
        print(' '.join(map(str, arr)))
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z):
        n = random.randint(2, 10); print(n)
        hi = random.choice([3, 10, 10**9])
        print(' '.join(str(random.randint(1, hi)) for _ in range(n)))
