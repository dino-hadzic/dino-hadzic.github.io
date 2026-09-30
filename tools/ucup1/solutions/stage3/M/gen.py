import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    z = 1; print(z)
    n = 10**6; k = 10**6
    print(n, k)
    for _ in range(k):
        a = random.randint(1, n); b = random.randint(1, n)
        while b == a: b = random.randint(1, n)
        print(a, b)
    s = random.randint(1, n // 2)
    print(s); print(' '.join(map(str, sorted(random.sample(range(1, n + 1), s)))))
else:
    z = random.randint(1, 5); print(z)
    for _ in range(z):
        n = random.randint(2, 6); k = random.randint(1, 10)
        print(n, k)
        for _ in range(k):
            a = random.randint(1, n); b = random.randint(1, n)
            while b == a: b = random.randint(1, n)
            print(a, b)
        s = random.randint(1, n)
        print(s); print(' '.join(map(str, sorted(random.sample(range(1, n + 1), s)))))
