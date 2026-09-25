import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
n = 2000 if mode == 'big' else random.randint(2, 5)
grid = [[0] * (i + 1) for i in range(n)]
if random.random() < 0.6:
    # rješiv ulaz: primijeni slučajne poteze na ugašenu lampu
    r = [random.randint(0, 1) for _ in range(n)]
    c = [random.randint(0, 1) for _ in range(n)]
    d = [random.randint(0, 1) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            grid[i][j] = r[i] ^ c[j] ^ d[i - j]
    if random.random() < 0.5:
        # pokvari nekoliko ćelija
        for _ in range(random.randint(1, 3)):
            i = random.randint(0, n - 1); j = random.randint(0, i)
            grid[i][j] ^= 1
else:
    for i in range(n):
        for j in range(i + 1):
            grid[i][j] = random.randint(0, 1)
out = [str(n)] + [''.join(map(str, row)) for row in grid]
print('\n'.join(out))
