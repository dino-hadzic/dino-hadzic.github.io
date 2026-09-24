import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
C = 10**9
def rect(pal):
    while True:
        x1, x2 = sorted(random.sample(pal, 2)); y1, y2 = sorted(random.sample(pal, 2))
        return x1, y1, x2, y2
tests = []
if mode == 'big':
    k = seed % 3
    if k == 0:
        n = 100000
        tests.append([(random.randint(1, C - 1), random.randint(1, C - 1), 0, 0) for _ in range(n)])
        tests[-1] = [(x, y, random.randint(x + 1, C), random.randint(y + 1, C)) for x, y, _, _ in tests[-1]]
        tests.append([rect(random.sample(range(1, C + 1), 8)) for _ in range(n)])
    elif k == 1:
        # mnogo malih testova
        for _ in range(100000):
            tests.append([rect(random.sample(range(1, C + 1), 5)) for _ in range(2)])
    else:
        n = 100000
        pal = list(range(1, 3000)) + [C]
        tests.append([rect(random.sample(pal, 4)) for _ in range(n)])
        tests.append([(i, i, i + 1, i + 1) for i in range(1, n + 1)])
else:
    for _ in range(random.randint(1, 3)):
        n = random.randint(1, 5)
        kind = random.random()
        if kind < 0.5: pal = list(range(1, 11))
        elif kind < 0.8: pal = [1, C] + random.sample(range(2, C), 6)
        else: pal = random.sample(range(1, C + 1), 7)
        tests.append([rect(pal) for _ in range(n)])
print(len(tests))
for t in tests:
    print(len(t))
    for r in t: print(*r)
