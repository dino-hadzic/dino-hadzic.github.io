import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        while True:
            n = random.randint(1, 5); m = random.randint(1, 5)
            if n * m <= 14: break
        vals = list(range(n * m))
        random.shuffle(vals)
        print(n, m)
        for i in range(n):
            print(*vals[i * m:(i + 1) * m])
else:
    # jedan veliki test: n*m = 10^6, razni oblici mreže
    n, m = random.choice([(1000, 1000), (1, 1000000), (1000000, 1), (2, 500000), (10, 100000)])
    print(1)
    print(n, m)
    vals = list(range(n * m))
    if random.random() < 0.5:
        # "dobar" ulaz: mali brojevi duž jednog monotonog puta -> velik odgovor
        random.shuffle(vals)
        path = []
        i = j = 0
        path.append((i, j))
        while i < n - 1 or j < m - 1:
            if i == n - 1: j += 1
            elif j == m - 1: i += 1
            elif random.random() < 0.5: j += 1
            else: i += 1
            path.append((i, j))
        grid = [vals[i * m:(i + 1) * m] for i in range(n)]
        # stavi vrijednosti 0..len(path)-1 na put (zamjenom)
        pos = {}
        for i in range(n):
            for j in range(m):
                pos[grid[i][j]] = (i, j)
        for k, (i, j) in enumerate(path):
            (pi, pj) = pos[k]
            grid[pi][pj], grid[i][j] = grid[i][j], grid[pi][pj]
            pos[grid[pi][pj]] = (pi, pj)
            pos[k] = (i, j)
    else:
        random.shuffle(vals)
        grid = [vals[i * m:(i + 1) * m] for i in range(n)]
    out = []
    for i in range(n):
        out.append(' '.join(map(str, grid[i])))
    sys.stdout.write('\n'.join(out) + '\n')
