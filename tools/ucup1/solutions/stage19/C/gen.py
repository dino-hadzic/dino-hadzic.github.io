import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = 2000; m = 3000
    tip = random.choice(['slucajno', 'jednake', 'lanac_tezak'])
    maxw = 10 ** 9
else:
    n = random.randint(2, 6); m = random.randint(n - 1, min(8, n - 1 + 5))
    tip = 'slucajno'
    maxw = random.choice([2, 3, 5, 10])

perm = list(range(1, n + 1)); random.shuffle(perm)
edges = []
# prvih n-1 bridova: slučajno razapinjuće stablo
for i in range(1, n):
    if tip == 'lanac_tezak':
        par = perm[i - 1]
    else:
        par = perm[random.randint(0, i - 1)]
    u, v = par, perm[i]
    if random.random() < 0.5:
        u, v = v, u
    if tip == 'jednake':
        w = 7
    elif tip == 'lanac_tezak':
        w = random.randint(maxw // 2, maxw)
    else:
        w = random.randint(1, maxw)
    edges.append((u, v, w))
# ostali bridovi (mogu biti višestruki)
while len(edges) < m:
    u, v = random.sample(range(1, n + 1), 2)
    if tip == 'jednake':
        w = 7
    elif tip == 'lanac_tezak':
        w = random.randint(1, maxw // 2)
    else:
        w = random.randint(1, maxw)
    edges.append((u, v, w))
print(n, m)
for u, v, w in edges:
    print(u, v, w)
