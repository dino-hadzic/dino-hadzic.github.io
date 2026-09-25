import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    N = 200; M = 1000
    ncol = [1000, 400, 150][seed % 3]        # broj razlicitih boja
else:
    N = random.randint(2, 7); M = random.randint(0, 9)
    ncol = random.randint(1, max(1, M))
print(N, M)
for _ in range(M):
    u, v = random.sample(range(N), 2)
    if u > v: u, v = v, u
    print(u, v, random.randrange(min(ncol, max(M, 1))))
