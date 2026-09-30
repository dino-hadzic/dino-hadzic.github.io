import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def test(n, v, P):
    print(n, v)
    cops = []
    cops.append((-random.randint(1, P), random.randint(1, v - 1)))
    cops.append((random.randint(1, P), random.randint(1, v - 1)))
    for _ in range(n - 2):
        s = random.choice([-1, 1])
        cops.append((s * random.randint(1, P), random.randint(1, v - 1)))
    random.shuffle(cops)
    for a, b in cops: print(a, b)
if mode == 'big':
    z = 5; print(z)
    for _ in range(z): test(400000, 10**6, 10**12)
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z):
        n = random.randint(2, 7)
        v = random.randint(2, random.choice([5, 20, 10**6]))
        test(n, v, random.choice([10, 1000, 10**12]))
