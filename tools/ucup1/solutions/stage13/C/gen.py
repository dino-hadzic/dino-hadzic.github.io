import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 10**6
    p = list(range(1, n + 1))
    if seed % 2 == 0:
        random.shuffle(p)
    k = random.randint(1, n if seed % 3 else 20)
else:
    n = random.randint(1, 12)
    p = list(range(1, n + 1))
    random.shuffle(p)
    k = random.randint(1, n)
print(n, k)
print(*p)
