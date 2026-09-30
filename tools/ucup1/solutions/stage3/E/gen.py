import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    print(3)
    for _ in range(3): print(random.randint(9 * 10**10, 10**11))
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z): print(random.randint(2, 40))
