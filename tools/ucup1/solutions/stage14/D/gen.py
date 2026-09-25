import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

MISS = [((0, 1), (1, 1)), ((1, 1), (2, 1)), ((1, 0), (1, 1)), ((1, 1), (1, 2))]
UP, DOWN, LEFT, RIGHT = range(4)
CELLS = [[(dr, dc) for dr in range(3) for dc in range(3) if (dr, dc) not in miss] for miss in MISS]
# spojeni komadi (dva isprepletena U-komada): kutija 4x4 bez dva nasuprotna kuta
MERGED_A = [(dr, dc) for dr in range(4) for dc in range(4) if (dr, dc) not in ((0, 3), (3, 0))]
MERGED_B = [(dr, dc) for dr in range(4) for dc in range(4) if (dr, dc) not in ((0, 0), (3, 3))]
SHAPES = CELLS + [MERGED_A, MERGED_B, MERGED_A, MERGED_B]

# Uzorci koji pogađaju dvoznačne grane analize slučajeva (relativno prema (i, j)).
PATTERNS = [
    [(MERGED_A, 0, 0), (CELLS[DOWN], 1, -3), (CELLS[UP], 3, -2)],          # A i B stanu, bira se A
    [(MERGED_B, 0, -1), (CELLS[RIGHT], 0, 3), (CELLS[DOWN], 3, 2)],        # A i B stanu, bira se B
    [(CELLS[DOWN], 0, 0), (CELLS[UP], 2, 1), (CELLS[DOWN], 2, -3), (CELLS[UP], 4, -2)],  # BL i BR, bira se BR
    [(CELLS[DOWN], 0, 0), (CELLS[UP], 2, -1), (CELLS[DOWN], 2, 3), (CELLS[UP], 4, 2)],   # BL i BR, bira se BL
    [(CELLS[DOWN], 0, 0), (CELLS[UP], 2, 1), (CELLS[UP], 1, -3), (CELLS[DOWN], 4, -2)],  # BL i BR, (i+1, j-1) slobodna
    [(CELLS[LEFT], 0, 0), (CELLS[RIGHT], 1, -2)],                          # konfiguracija L
    [(CELLS[RIGHT], 0, 0), (CELLS[LEFT], 1, 2)],                           # konfiguracija R
]

if mode == 'big':
    n = m = 1000
else:
    n = random.randint(3, 9); m = random.randint(3, 9)

grid = [['1'] * m for _ in range(n)]

def can_place(cells, a, b):
    for dr, dc in cells:
        r, c = a + dr, b + dc
        if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '0':
            return False
    return True

def place(cells, a, b):
    for dr, dc in cells:
        grid[a + dr][b + dc] = '0'

def fill_dense(p):
    # prolazimo ćelije leksikografski i pokušavamo staviti komad s kutom u svakoj
    for a in range(n):
        for b in range(m):
            if grid[a][b] == '1' and random.random() < p:
                shape = random.choice(SHAPES)
                if can_place(shape, a, b):
                    place(shape, a, b)

kind = random.random()
if mode == 'big':
    fill_dense(0.9)
elif kind < 0.45:
    # ubaci jedan dvoznačan uzorak pa gusto popuni ostatak
    pat = random.choice(PATTERNS)
    for _ in range(30):
        i = random.randint(0, n - 1); j = random.randint(0, m - 1)
        if all(can_place(c, i + da, j + db) for c, da, db in pat):
            for c, da, db in pat:
                place(c, i + da, j + db)
            break
    fill_dense(random.choice([0.5, 0.9]))
elif kind < 0.8:
    fill_dense(random.choice([0.3, 0.6, 0.9]))
elif kind < 0.93:
    p = random.choice([0.1, 0.2, 0.35])
    for i in range(n):
        for j in range(m):
            grid[i][j] = '1' if random.random() < p else '0'
else:
    for i in range(n):
        for j in range(m):
            grid[i][j] = '0'
    for _ in range(random.randint(0, 3)):
        grid[random.randint(0, n - 1)][random.randint(0, m - 1)] = '1'

if mode != 'big' and kind < 0.8 and random.random() < 0.3:
    # pokvari jednu ili dvije ćelije (često daje 0 i ispituje razlučivanje slučajeva)
    for _ in range(random.randint(1, 2)):
        i = random.randint(0, n - 1); j = random.randint(0, m - 1)
        grid[i][j] = '1' if grid[i][j] == '0' else '0'

print(n, m)
print('\n'.join(''.join(row) for row in grid))
