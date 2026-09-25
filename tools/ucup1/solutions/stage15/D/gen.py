import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 22
    print(n); print(*[random.randint(1, 10**9) for _ in range(n)])
else:
    n = random.randint(1, 5)
    print(n); print(*[random.randint(1, random.choice([3, 10, 10**9])) for _ in range(n)])
