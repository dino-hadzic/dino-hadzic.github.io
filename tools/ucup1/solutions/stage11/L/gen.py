import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
tests = []
if mode == 'big':
    k = seed % 4
    if k == 0: tests = [(1000, 1000)]
    elif k == 1: tests = [(2, 1000), (1000, 2), (3, 1000), (1000, 3), (999, 999)]
    elif k == 2: tests = [(31, 32)] * 1000
    else:
        s = 0
        while s < 950000:
            n, m = random.randint(2, 1000), random.randint(2, 1000)
            if s + n * m > 10**6: break
            tests.append((n, m)); s += n * m
            if len(tests) == 1000: break
else:
    for _ in range(random.randint(1, 3)):
        while True:
            n = random.randint(2, 6); m = random.randint(2, 12)
            if n * m <= 24: break
        tests.append((n, m))
print(len(tests))
for n, m in tests: print(n, m)
