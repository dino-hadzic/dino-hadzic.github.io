import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 6)
    print(T)
    for _ in range(T):
        hi = random.choice([10, 40, 120])
        x = random.randint(1, hi); y = random.randint(1, hi)
        if random.random() < 0.3:
            # namjerno par s istim zapisom
            a = random.randint(2, 12); b = random.randint(2, 12)
            L = random.randint(1, 3)
            d = [random.randint(0, min(a, b) - 1) for _ in range(L)]
            if d[-1] == 0: d[-1] = 1
            x = sum(v * a**i for i, v in enumerate(d)); y = sum(v * b**i for i, v in enumerate(d))
        A = random.randint(2, 60); B = random.randint(2, 60)
        print(x, y, A, B)
else:
    T = 1000
    print(T)
    for i in range(T):
        if i < 50:
            x = random.randint(10**8, 10**9); y = random.randint(10**8, 10**9)
            if random.random() < 0.5:
                a = random.randint(2, 31000); b = random.randint(2, 31000)
                m = min(a, b)
                d = [random.randint(0, m - 1) for _ in range(3)]
                d[-1] = max(1, d[-1])
                x = sum(v * a**k for k, v in enumerate(d)); y = sum(v * b**k for k, v in enumerate(d))
                if x > 10**9 or y > 10**9:
                    x = random.randint(10**8, 10**9); y = random.randint(10**8, 10**9)
        else:
            x = random.randint(1, 10**6); y = random.randint(1, 10**6)
        # male gornje granice A, B: dvoznamenkasti slučaj rijetko uspije, pa se izvrši
        # i puna pretraga po a, b <= sqrt
        print(x, y, random.randint(2, 40000), random.randint(2, 40000))
