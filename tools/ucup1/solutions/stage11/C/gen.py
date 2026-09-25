import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 100000
    print(T)
    for _ in range(T):
        r = random.random()
        if r < 0.3: x = random.randint(1, 10**18 - 1)
        elif r < 0.5: x = 10**random.randint(0, 17)
        elif r < 0.7: x = int('9' * random.randint(1, 18))
        else: x = random.randint(1, 10**random.randint(1, 18) - 1)
        print(x, random.randint(0, 18))
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        r = random.random()
        if r < 0.3: x = random.randint(1, 999)
        elif r < 0.5: x = random.choice([1, 10, 100, 9, 99, 999, 90, 909, 190, 999])
        else: x = random.randint(1, 99)
        print(x, random.randint(0, 3))
