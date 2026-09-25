import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 6)
    out = [str(T)]
    for _ in range(T):
        n = random.randint(1, 30)
        k = random.randint(0, n)
        out.append(f"{n} {k}")
else:
    tests = []
    if seed == 1:
        tests = [(1000000, 0), (1000000, 1000000)]
    elif seed == 2:
        tests = [(1000000, 2), (999999, random.randint(0, 999999))]
    else:
        rem = 2000000
        while rem > 0:
            n = random.randint(1, min(rem, random.choice([500, 5000, 1000000])))
            tests.append((n, random.randint(0, n)))
            rem -= n
    out = [str(len(tests))] + [f"{n} {k}" for n, k in tests]
print("\n".join(out))
