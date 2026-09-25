import random, sys, string
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def rs(n, a): return "".join(random.choice(a) for _ in range(n))
if mode == 'small':
    q = random.randint(1, 3); print(q)
    for _ in range(q):
        n = random.randint(1, 3); K = random.randint(1, 3); a = 'ab'
        print(n, K)
        for _ in range(n): print(rs(random.randint(1, 3), a))
        print(rs(random.randint(1, 5), a))
else:
    q = 1; print(q)
    kind = seed % 3
    if kind == 0:
        n = 1000; K = 5000; a = 'ab'
        print(n, K)
        for _ in range(n): print(rs(1000, a))
        print(rs(5000, a))
    elif kind == 1:
        n = 1; K = 4999
        print(n, K)
        print('a' * 1000000)
        print('a' * 5000)
    else:
        n = 1400; K = 5000; a = 'abc'
        print(n, K)
        for i in range(n): print(rs(i % 700 + 1, a))
        print(rs(5000, a))
