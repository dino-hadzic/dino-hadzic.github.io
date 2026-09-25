import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    print(random.randint(1, 6), random.randint(2, 60))
else:
    print(100, random.choice([2, 3, 32, 59, 60]))
