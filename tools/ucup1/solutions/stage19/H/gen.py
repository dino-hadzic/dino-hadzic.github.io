import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = random.choice([1000, random.randint(900, 1000)])
    k = random.choice([10, 10, random.randint(2, 10)])
    print(n, k)
else:
    n = random.randint(2, 7)
    k = random.choice([2, 2, 3, 3, 4, random.randint(2, 10)])
    print(n, k)
