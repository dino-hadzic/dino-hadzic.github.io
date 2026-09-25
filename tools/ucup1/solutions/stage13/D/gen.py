import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    # zbroj n <= 10^4: jedan test s n = 5000 (odgovor 0 bez racunanja) i mnogo testova s n = 61
    tests = [5000] + [61] * ((10**4 - 5000) // 61)
    print(len(tests))
    for n in tests:
        print(n)
        print(*[random.getrandbits(60) for _ in range(n)])
        print(*[random.getrandbits(60) for _ in range(n)])
else:
    if seed % 10 == 0:
        # rubni slucaj oko ranga 61: n = 60..64 (za n >= 62 odgovor mora biti 0)
        t = 1
        print(t)
        n = random.randint(58, 64)
        print(n)
        print(*[random.getrandbits(60) for _ in range(n)])
        print(*[random.getrandbits(60) for _ in range(n)])
    else:
        t = random.randint(1, 5)
        print(t)
        for _ in range(t):
            n = random.randint(1, 6)
            bits = random.choice([1, 2, 3, 60])
            print(n)
            print(*[random.getrandbits(bits) for _ in range(n)])
            print(*[random.getrandbits(bits) for _ in range(n)])
