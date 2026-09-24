import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n, m = random.choice([(1000, 1000), (1000, 999), (997, 1000)])
else:
    while True:
        n = random.randint(2, 8); m = random.randint(1, 4)
        if n * m <= 8:
            break
print(n, m)
