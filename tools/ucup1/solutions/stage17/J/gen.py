import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 8)
    out = [str(T)]
    for _ in range(T):
        hi = random.choice([3, 7, 15, 40])
        K = random.choice([0, 1, 2, 3, 4, 7, random.randint(0, hi)])
        out.append(f"{random.randint(0, hi)} {random.randint(0, hi)} {K}")
else:
    T = 100000
    out = [str(T)]
    for _ in range(T):
        out.append(f"{random.getrandbits(60)} {random.getrandbits(60)} {random.getrandbits(random.randint(0, 60))}")
print("\n".join(out))
