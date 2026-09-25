import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n = random.randint(1, 10); q = random.randint(1, 10)
    alpha = random.choice([1, 2, 3])
    s = "".join(str(random.randint(0, alpha - 1)) for _ in range(n))
else:
    n = q = 500000
    s = "".join(str(random.randint(0, 2)) for _ in range(n))
    if seed == 1:
        # puno izbrisivih parova
        half = "".join(str(random.randint(0, 2)) for _ in range(n // 2))
        s = (half + half[::-1])[:n]
lines = [f"{n} {q}", s]
for _ in range(q):
    l = random.randint(1, n); r = random.randint(l, n)
    if mode != 'small' and random.random() < 0.5:
        l = random.randint(1, n // 10 + 1); r = random.randint(n - n // 10, n)
    lines.append(f"{random.randint(1, 2)} {l} {r}")
print("\n".join(lines))
