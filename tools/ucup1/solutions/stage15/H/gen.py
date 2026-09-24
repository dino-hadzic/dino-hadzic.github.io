import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 100000; k = random.choice([2, 3, 1000, 50000, n])
    xs = sorted(random.sample(range(0, 10**9 + 1), n))
    ys = [random.randint(0, 10**9) for _ in range(n)]
else:
    n = random.randint(2, 8); k = random.randint(2, n)
    lim = random.choice([5, 20, 10**9])
    xs = sorted(random.sample(range(0, lim + 1 if lim >= n else n), n))
    ys = [random.randint(0, lim) for _ in range(n)]
print(n, k)
for a, b in zip(xs, ys):
    print(a, b)
