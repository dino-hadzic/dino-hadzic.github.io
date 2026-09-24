import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    t = 10000
    print(t)
    for _ in range(t):
        print(random.randint(1, 10**18), random.choice([1, 2, 3, random.randint(1, 10**18)]))
else:
    t = random.randint(1, 20)
    print(t)
    for _ in range(t):
        if random.random() < 0.3:
            print(random.randint(1, 10**18), random.randint(1, 10**18))
        else:
            print(random.randint(1, 100), random.randint(1, 10))
