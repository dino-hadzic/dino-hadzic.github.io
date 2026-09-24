import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    kind = seed % 3
    if kind == 0: print(10**6, 10**6)
    elif kind == 1: print(10**6, 10**6 - 1)
    else: print(random.randint(2, 10**6), random.randint(2, 10**6))
else:
    while True:
        n = random.randint(2, 9); k = random.randint(2, 9)
        if n ** k <= 300000: break
    print(n, k)
