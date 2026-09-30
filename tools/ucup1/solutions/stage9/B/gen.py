import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 1
    print(T)
    n = 100000; m = 100000
    print(n, m)
    print(' '.join(str(random.randint(1, random.choice([3, 100000]))) for _ in range(n)))
    edges = []
    typ = seed % 3
    if typ == 0:      # dugi lanac (duboko DFS stablo) + malo dodatnih bridova
        for i in range(1, n): edges.append((i, i + 1))
        while len(edges) < m: edges.append((random.randint(1, n), random.randint(1, n)))
    elif typ == 1:    # slucajno stablo + slucajni bridovi
        for i in range(2, n + 1): edges.append((random.randint(max(1, i - 5), i - 1), i))
        while len(edges) < m: edges.append((random.randint(1, n), random.randint(1, n)))
    else:             # potpuno slucajno (puno komponenti)
        for _ in range(m): edges.append((random.randint(1, n), random.randint(1, n)))
    random.shuffle(edges)
    for u, v in edges: print(u, v)
else:
    T = random.randint(1, 4)
    print(T)
    for _ in range(T):
        n = random.randint(1, 7); m = random.randint(1, 8)
        print(n, m)
        print(' '.join(str(random.randint(1, 3)) for _ in range(n)))
        for _ in range(m):
            print(random.randint(1, n), random.randint(1, n))
