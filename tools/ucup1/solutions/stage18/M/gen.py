import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(2, 6); m = random.randint(2, 6)
        print(n, m)
        for _ in range(m):
            l = random.randint(1, n - 1); r = random.randint(l + 1, n)
            print(l, random.randint(1, 2), r, random.randint(1, 2))
else:
    kind = random.randint(0, 2)
    print(1)
    n = 500000; m = 500000
    print(n, m)
    out = []
    if kind == 0:
        for _ in range(m):
            l = random.randint(1, n - 1); r = random.randint(l + 1, n)
            out.append(f"{l} {random.randint(1, 2)} {r} {random.randint(1, 2)}")
    elif kind == 1:
        # dugački lanac (duboki DFS): i -> i+1 s (1,2)
        for i in range(1, n):
            out.append(f"{i} 1 {i + 1} 2")
        out.append(f"1 2 {n} 1")
    else:
        # mnogo malih ciklusa i (2,2) operacija
        for i in range(m):
            l = random.randint(1, n - 3); r = l + random.randint(1, 3)
            if random.random() < 0.1:
                out.append(f"{l} 2 {r} 2")
            else:
                out.append(f"{l} {random.randint(1, 2)} {r} {random.randint(1, 2)}")
    print("\n".join(out))
