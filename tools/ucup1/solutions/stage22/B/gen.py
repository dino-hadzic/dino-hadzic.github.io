import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 1000; r = random.choice([1, 50, 1000]); d = random.choice([1, 10, 1000]); C = 10**4; TM = 1000
else:
    n = random.randint(1, 7); r = random.randint(1, 3); d = random.randint(1, 3)
    C = random.choice([6, 10, 20]); TM = random.choice([4, 8])
print(n, r, d)
for _ in range(n):
    if random.random() < 0.4:
        print(1, random.randint(1, C), random.randint(1, C), random.randint(1, TM))
    else:
        u = random.randint(1, TM - 1); v = random.randint(u + 1, TM)
        print(2, random.randint(1, C), random.randint(1, C), random.randint(1, C), random.randint(1, C), u, v)
