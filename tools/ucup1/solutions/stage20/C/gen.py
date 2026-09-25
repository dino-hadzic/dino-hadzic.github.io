import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def test(n, m, coord):
    print(n, m)
    for _ in range(n):
        a = random.randint(0, coord); b = random.randint(a, min(coord, a + random.choice([0, 1, 3, coord])))
        print(a, b)
    for _ in range(m):
        a, b = random.sample(range(1, n + 1), 2)
        print(a, b)
if mode == 'small':
    t = random.randint(1, 4); print(t)
    for _ in range(t):
        n = random.randint(2, 9); m = random.randint(0, n + 2)
        test(n, m, random.choice([3, 6, 12]))
else:
    t = 1; print(t)
    n = 100000; m = 100000
    test(n, m, random.choice([10**9, 1000, 100000]))
