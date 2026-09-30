import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = random.choice([15000000, 14999999, 1000000]); d = random.choice([15000000, 14999983, 7])
    print(n, d, random.randint(1, n))
else:
    n = random.randint(1, 5); d = random.randint(1, 6)
    print(n, d, random.randint(1, n))
