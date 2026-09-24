import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tapalib import RING
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def instanca(n, m, p_prazno, iz_osjencanja):
    R, C = 2 * n - 1, 2 * m - 1
    grid = [['.'] * C for _ in range(R)]
    if iz_osjencanja:
        # slucajno osjencanje s malo praznih celija; tragovi = stvarni broj osjencanih susjeda
        # (ako netko ima >1 praznu ili neuzastopne, vrijednost se ipak zaokruzi na max/max-1)
        sol = [['#'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if (i % 2 or j % 2) and random.random() < p_prazno:
                    sol[i][j] = '.'
    for a in range(n):
        for b in range(m):
            r, c = 2 * a, 2 * b
            sus = [(r + dr, c + dc) for dr, dc in RING if 0 <= r + dr < R and 0 <= c + dc < C]
            k = len(sus)
            if iz_osjencanja:
                v = sum(1 for (i, j) in sus if sol[i][j] == '#')
                v = max(v, k - 1)
            else:
                v = k - random.randint(0, 1)
            grid[r][c] = str(v)
    return [''.join(row) for row in grid]

def iz_sparivanja(n, m, gustoca):
    # slucajni dopusteni parovi susjednih tragova (svaki trag u najvise jednom paru) -> sigurno YES
    R, C = 2 * n - 1, 2 * m - 1
    uparen = [[False] * m for _ in range(n)]
    sol = [['#'] * C for _ in range(R)]
    rub = lambda a, b: a == 0 or a == n - 1 or b == 0 or b == m - 1
    for _ in range(int(gustoca * n * m)):
        a, b = random.randrange(n), random.randrange(m)
        da, db = random.choice([(1, 0), (0, 1)])
        a2, b2 = a + da, b + db
        if a2 >= n or b2 >= m or uparen[a][b] or uparen[a2][b2]: continue
        cr, cc = 2 * a + da, 2 * b + db
        na_rubu = cr == 0 or cr == R - 1 or cc == 0 or cc == C - 1
        if (rub(a, b) or rub(a2, b2)) and not na_rubu: continue
        uparen[a][b] = uparen[a2][b2] = True
        sol[cr][cc] = '.'
    grid = [['.'] * C for _ in range(R)]
    for a in range(n):
        for b in range(m):
            r, c = 2 * a, 2 * b
            sus = [(r + dr, c + dc) for dr, dc in RING if 0 <= r + dr < R and 0 <= c + dc < C]
            grid[r][c] = str(sum(1 for (i, j) in sus if sol[i][j] == '#'))
    return [''.join(row) for row in grid]

if mode == 'big':
    n, m = 50, 50
    if seed % 3 == 1: grid = iz_sparivanja(n, m, random.choice([0.5, 2.0, 10.0]))
    elif seed % 3 == 2: grid = instanca(n, m, 0.0, False)          # slucajne vrijednosti
    else: grid = instanca(n, m, 0.05, True)
else:
    while True:
        n, m = random.randint(2, 4), random.randint(2, 4)
        if (2 * n - 1) * (2 * m - 1) - n * m <= 17: break
    u = random.random()
    if u < 0.35: grid = iz_sparivanja(n, m, random.choice([0.5, 2.0, 10.0]))
    else: grid = instanca(n, m, random.choice([0.05, 0.15, 0.4]), u < 0.7)
print(n, m)
print('\n'.join(grid))
