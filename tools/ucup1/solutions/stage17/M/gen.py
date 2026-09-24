import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    n = random.randint(2, 7)
    a = [random.randint(0, 10) for _ in range(n)]
    ops = "".join(random.choice("+-") for _ in range(n - 1))
else:
    n = 200000
    a = [random.randint(0, 10**9) for _ in range(n)]
    ops = "".join(random.choice("+-") for _ in range(n - 1))
print(n); print(" ".join(map(str, a))); print(ops)
