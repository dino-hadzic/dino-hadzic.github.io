import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 100
    x = random.randint(0, 9999)
    a = [random.randint(1, 9999) for _ in range(n)]
else:
    n = random.randint(1, 6)
    if random.random() < 0.5:
        x = random.randint(0, 9999)
        a = [random.randint(1, 9999) for _ in range(n)]
    else:
        x = random.randint(0, 300)
        a = [random.randint(1, 120) for _ in range(n)]
print(n, x)
print(*a)
