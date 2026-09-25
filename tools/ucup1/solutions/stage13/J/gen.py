import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 10**6
    m = random.choice([1, 2, 3, 4, 10**6, random.randint(3, 10**6)])
    k = random.choice([1, 12, 13, 10**18, random.randint(1, 10**18)])
    print(n, m, k)
else:
    while True:
        n = random.randint(1, 12)
        m = random.randint(1, 6)
        if m ** n <= 60000:
            break
    if random.random() < 0.3:
        k = random.randint(1, 10**18)
    else:
        k = random.randint(1, min(10**18, m ** n + 2))
    print(n, m, k)
