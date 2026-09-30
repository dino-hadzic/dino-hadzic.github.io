import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    print(random.choice([10**9, 10**9 - random.randint(0, 1000), random.randint(9 * 10**8, 10**9)]))
else:
    print(random.randint(1, 3000))
