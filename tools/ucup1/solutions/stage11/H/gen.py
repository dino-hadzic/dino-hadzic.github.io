import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
LEN = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]
cells = [(r + 1, c + 1) for r in range(17) for c in range(LEN[r])]
if mode == 'big':
    T = 100; sizes = [random.choice([121, 120, 60, 30, 90, 2, 1, 15]) for _ in range(T)]
else:
    T = random.randint(1, 4); sizes = [random.choice([1, 2, 3, 5, 8, 15, 40, 100, 121]) for _ in range(T)]
print(T)
for n in sizes:
    print(n)
    for r, c in random.sample(cells, n): print(r, c)
