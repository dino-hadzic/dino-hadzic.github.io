import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def random_game(n, k):
    # odigraj slucajnu partiju do kraja i vrati plocu (uvijek TAK)
    b = [['.'] * n for _ in range(n)]
    turn = random.choice('xo'); cells = [(i, j) for i in range(n) for j in range(n)]; random.shuffle(cells)
    def win(sym):
        for i in range(n):
            for j in range(n):
                for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
                    cs = [(i + t * dx, j + t * dy) for t in range(k)]
                    if all(0 <= x < n and 0 <= y < n and b[x][y] == sym for x, y in cs): return True
        return False
    for i, j in cells:
        b[i][j] = turn
        if win(turn): break
        turn = 'o' if turn == 'x' else 'x'
    return [''.join(r) for r in b]
def random_board(n):
    return [''.join(random.choice('xo.') for _ in range(n)) for _ in range(n)]
if mode == 'big':
    z = 10000; print(z)
    for _ in range(z):
        n = 6; k = random.randint(2, 6); print(n, k)
        for r in (random_game(n, k) if random.random() < .5 else random_board(n)): print(r)
else:
    z = random.randint(1, 4); print(z)
    for _ in range(z):
        n = random.choice([3, 3, 4]); k = random.randint(2, n); print(n, k)
        r = random.random()
        if r < .4: rows = random_game(n, k)
        elif r < .7:
            rows = random_game(n, k)
            # pokvari jedno polje
            i, j = random.randrange(n), random.randrange(n)
            rows[i] = rows[i][:j] + random.choice('xo.') + rows[i][j+1:]
        else: rows = random_board(n)
        for row in rows: print(row)
