import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 10000
    print(T)
    for _ in range(T):
        print(random.choice([random.randint(1, 10**40), 10**40, random.randint(1, 10**20), random.randint(1, 10**6)]))
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        print(random.choice([random.randint(1, 30), random.randint(1, 3000), random.randint(1, 200000)]))
