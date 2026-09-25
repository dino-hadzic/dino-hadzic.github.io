import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n, m, q = 100000, 100000, 100000
    bits = 30
    K = random.choice([(1 << 30) - 1, random.randint(0, (1 << 30) - 1), 1 << 29, 0x2AAAAAAA])
else:
    n = random.randint(2, 6); m = random.randint(1, 8); q = random.randint(1, 6)
    bits = random.choice([2, 3, 4, 8])
    K = random.randint(0, (1 << bits) - 1)
print(n, m, K)
for _ in range(m):
    a, b = random.sample(range(1, n + 1), 2)
    if a > b: a, b = b, a
    print(a, b, random.randint(0, (1 << bits) - 1))
print(q)
for _ in range(q):
    print(random.randint(0, (1 << bits) - 1))
