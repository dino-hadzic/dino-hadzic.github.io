import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 4); print(t)
    for _ in range(t):
        n = random.randint(1, 4); c = random.randint(1, 3 if n == 4 else 4)
        print(n, c)
else:
    t = 1; print(t)
    print(10**7, random.choice([10**7, 1, 2, 123456]))
