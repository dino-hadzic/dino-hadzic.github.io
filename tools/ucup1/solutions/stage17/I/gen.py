import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n = random.randint(1, 12); q = random.randint(1, 10)
    pr = random.choice([0.2, 0.5, 0.8])
    s = "".join('1' if random.random() < pr else '0' for _ in range(n))
    lines = [f"{n} {q}", s]
    for _ in range(q):
        l = random.randint(1, n); r = random.randint(l, n)
        lines.append(f"{l} {r} {random.randint(0, n)}")
else:
    n = q = 500000
    if seed == 1:
        s = "".join(random.choice("01") for _ in range(n))
    elif seed == 2:
        s = "".join(random.choice("01") * random.randint(1, 40) for _ in range(n))[:n]
    else:
        s = ("0" * (n // 2) + "1" * (n - n // 2))
    lines = [f"{n} {q}", s]
    for _ in range(q):
        l = random.randint(1, n); r = random.randint(l, n)
        if random.random() < 0.5:
            l = random.randint(1, 1000); r = random.randint(n - 1000, n)
        lines.append(f"{l} {r} {random.choice([random.randint(0, n), random.randint(0, 30)])}")
print("\n".join(lines))
