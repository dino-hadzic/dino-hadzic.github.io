import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    print(1)
    n = 6000; k = random.choice([1, 50, 3000, 5990])
    print(n, k)
    print(' '.join(str(random.randint(0, 10**9)) for _ in range(n)))
else:
    z = random.randint(1, 3); print(z)
    for _ in range(z):
        k = random.randint(0, 2)
        n = random.randint(1, 6) if k <= 2 else random.randint(1, 4)
        print(n, k)
        print(' '.join(str(random.randint(0, 3)) for _ in range(n)))
