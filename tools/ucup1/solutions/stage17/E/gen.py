import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 5)
    out = [str(T)]
    for _ in range(T):
        n = random.randint(1, 12)
        w = random.choice([(1, 1, 1), (3, 1, 3), (5, 1, 1), (1, 3, 1)])
        out.append("".join(random.choices("cp?", weights=w, k=n)))
else:
    out = ["2"]
    out.append("".join(random.choices("cp?", weights=(8, 1, 8), k=500000)))
    out.append("?" * 500000)
print("\n".join(out))
