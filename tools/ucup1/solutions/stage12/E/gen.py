import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
MOD = 998244353
if mode == 'big':
    n = 100000
    hi = MOD - 1 if seed % 2 else 3
else:
    n = random.randint(1, 5)
    hi = random.choice([1, 3, 10, MOD - 1])
print(n)
for _ in range(5):
    print(*[random.randint(0, hi) for _ in range(n)])
