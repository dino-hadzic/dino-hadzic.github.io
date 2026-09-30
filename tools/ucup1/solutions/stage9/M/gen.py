import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 100000
    print(T)
    for _ in range(T):
        print(random.randint(0, 10**9), random.randint(0, 10**9))
else:
    T = random.randint(1, 20)
    print(T)
    for _ in range(T):
        x = random.choice([random.randint(0, 20), random.randint(0, 10**9), int(''.join(random.choice('0468899') for _ in range(random.randint(1, 9))))])
        k = random.choice([0, 1, 2, 3, random.randint(0, 10), random.randint(0, 10**9)])
        print(x, k)
