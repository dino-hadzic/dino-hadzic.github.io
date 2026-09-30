import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def word(alpha, lo, hi): return ''.join(random.choice(alpha) for _ in range(random.randint(lo, hi)))
if mode == 'big':
    z = 2; print(z)
    n = 200000; print(n)
    for _ in range(n): print(word('ab', 1, 3), word('ab', 1, 3))      # mnogo kolizija -> c velik
    print(n)
    for _ in range(n): print(word('abcdefghijklmnopqrstuvwxyz', 1, 7), word('abcdefghijklmnopqrstuvwxyz', 1, 6))
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z):
        n = random.randint(1, 12); print(n)
        alpha = random.choice(['ab', 'abc', 'abcdefgh'])
        base = [(word(alpha, 1, 4), word(alpha, 1, 4)) for _ in range(random.randint(1, 4))]
        for _ in range(n):
            if random.random() < .5: print(*random.choice(base))
            else: print(word(alpha, 1, 4), word(alpha, 1, 4))
