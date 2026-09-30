import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = random.choice([1, 2, 1000, 700, random.randint(1, 1000)])
    m = 10**6 // n
    if random.random() < 0.5: n, m = m, n
    print(n, m)
else:
    if seed % 3 == 0:
        n = random.randint(1, 60); m = random.randint(1, 60)
    else:
        n = random.randint(1, 16); m = random.randint(1, 16 // n)
    print(n, m)
