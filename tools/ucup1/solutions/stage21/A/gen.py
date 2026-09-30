import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def case(n, C):
    print(n)
    for _ in range(n):
        l = random.randint(1, C); r = random.randint(l, C)
        print(l, r, random.randint(0, 1))
if mode == 'big':
    T = 5; print(T)
    for _ in range(T): case(100000, random.choice([100, 10**5, 10**9]))
else:
    T = random.randint(1, 5); print(T)
    for _ in range(T): case(random.randint(1, 12), random.choice([3, 6, 20]))
