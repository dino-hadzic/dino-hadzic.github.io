import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    print(random.choice([10**7, 10**7 - 1, 9999999 - random.randint(0, 100)]))
else:
    print(random.randint(1, 6))
