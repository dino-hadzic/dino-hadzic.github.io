import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = random.choice([200000, random.randint(1, 200000)])
    m = random.choice([1, random.randint(1, 200000), 200000, random.randint(1, 50)])
    k = random.choice([1, random.randint(1, 10**9), random.randint(1, 1000), 10**9])
    print(n, m, k)
    r = random.random()
    for _ in range(n):
        if r < 0.5:
            print(random.randint(1, 10**9))
        else:
            print(random.randint(1, 5))
else:
    n = random.randint(1, 6)
    m = random.randint(1, 5)
    f = [random.randint(1, 3) for _ in range(n)]
    k = random.randint(1, sum(f) + 1)
    print(n, m, k)
    for x in f:
        print(x)
