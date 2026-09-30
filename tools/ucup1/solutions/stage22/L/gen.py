import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    t = 10**5
    print(t)
    for _ in range(t):
        print(random.randint(1, 10**18), random.randint(1, 10**18))
else:
    t = random.randint(1, 30)
    print(t)
    for _ in range(t):
        m = random.choice([10, 40, 120])
        print(random.randint(1, m), random.randint(1, m))
