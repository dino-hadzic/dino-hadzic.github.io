import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
MODS = [100000007, 998244353, 1000000007, 999999937, 100000037]
if mode == 'small':
    # brute nabraja sve q^{n^2} matrica B, pa (n, q) mora biti malo
    n, q = random.choice([(1, 2), (1, 3), (1, 5), (1, 7), (2, 2), (2, 3), (2, 5), (3, 2), (3, 3)])
    mod = random.choice(MODS)
else:
    n = 10**7
    q = random.choice([2, 3, 127, 999999937, 999999893])
    mod = random.choice([998244353, 1000000007])
    if q >= mod:
        q = 127
print(n, q, mod)
