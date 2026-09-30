import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def make(n, m):
    A = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(n - 1)]
    B = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(m - 1)]
    return ''.join(str(a * b) for a in A for b in B)
if mode == 'big':
    T = 3
    print(T)
    for _ in range(T):
        n = random.choice([1, 2, 300, 1000, 100000]); m = max(1, 100000 // n)
        c = make(n, m)
        if random.random() < 0.3:
            c = list(c); i = random.randrange(len(c)); c[i] = str(random.randint(0, 9)); c = ''.join(c)
        print(n, m); print(c)
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 3); m = random.randint(1, 3)
        c = make(n, m)
        r = random.random()
        if r < 0.25:
            c = list(c); i = random.randrange(len(c)); c[i] = str(random.randint(0, 9)); c = ''.join(c)
        elif r < 0.35:
            c = c + str(random.randint(0, 9))
        elif r < 0.45 and len(c) > 1:
            c = c[:-1]
        print(n, m); print(c)
