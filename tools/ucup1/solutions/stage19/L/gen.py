import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    t = 1000
    print(t)
    for _ in range(t):
        n = random.choice([2, 3, 49, 50, random.randint(2, 50)])
        r = random.random()
        if r < 0.3:
            piles = [random.randint(1, 10**12) for _ in range(n)]
        elif r < 0.6:
            # sve hrpe s istom valuacijom 2^p
            p = random.randint(0, 39)
            piles = [(2 * random.randint(0, (10**12 >> p) // 2 - 1 if (10**12 >> p) >= 2 else 0) + 1) << p for _ in range(n)]
            piles = [min(x, 10**12) for x in piles]
        else:
            # ista valuacija osim jedne hrpe
            p = random.randint(0, 28)
            piles = [(2 * random.randint(0, 1000) + 1) << p for _ in range(n)]
            j = random.randrange(n)
            piles[j] = (2 * random.randint(0, 1000) + 1) << random.randint(0, 28)
        print(n)
        print(*piles)
else:
    t = random.randint(1, 4)
    print(t)
    for _ in range(t):
        n = random.choice([2, 3, 4, 5])
        maxs = 8 if n <= 3 else 5
        r = random.random()
        if r < 0.5:
            piles = [random.randint(1, maxs) for _ in range(n)]
        else:
            p = random.randint(0, 2)
            piles = [(2 * random.randint(0, 1) + 1) << p for _ in range(n)]
            if random.random() < 0.5:
                piles[random.randrange(n)] = random.randint(1, maxs)
        print(n)
        print(*piles)
