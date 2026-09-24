import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
MOD = 998244353
if mode == 'big':
    n = 200000
    M = random.choice([963761198400, 10 ** 12, 999999999989, 2 ** 39])  # mnogo faktora / 10^12 / prost / 2^39
    A = [random.randint(0, MOD - 1) for _ in range(n)]
else:
    n = random.randint(1, 5)
    M = random.choice([1, 2, 6, 12, 36, 60, random.randint(1, 100), 2 ** random.randint(0, 6), 97])
    A = [random.randint(0, random.choice([3, 10, MOD - 1])) for _ in range(n)]
print(n, M)
print(*A)
