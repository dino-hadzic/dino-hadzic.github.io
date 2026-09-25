import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    t = random.randint(1, 5); out = [str(t)]
    for _ in range(t):
        n = random.randint(1, 6)
        if random.random() < 0.5:
            b = [1]
            for i in range(n-1): b.append(b[-1] + random.randint(0, 1))
        else:
            b = [random.randint(1, n) for _ in range(n)]
        out.append(str(n)); out.append(" ".join(map(str, b)))
else:
    t = 4000; out = [str(t)]
    for _ in range(t):
        n = 10
        if random.random() < 0.5:
            b = [1]
            for i in range(n-1): b.append(b[-1] + random.randint(0, 1))
        else:
            b = [random.randint(1, 10) for _ in range(n)]
        out.append(str(n)); out.append(" ".join(map(str, b)))
print("\n".join(out))
