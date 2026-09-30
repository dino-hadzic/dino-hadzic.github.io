import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
n = 1000 if mode == 'big' else random.randint(1, 12)
print(n, random.randint(1, n), random.randint(1, n))
