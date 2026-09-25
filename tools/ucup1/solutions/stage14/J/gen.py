import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

# prost M = 3 (mod 4) da bi korijen bio jednostavan: sqrt(a) = a^((M+1)/4)
while True:
    M = random.randint(900000000, 1000000000) | 3
    if M % 4 == 3 and is_prime(M): break
E = random.randint(1, 100); V = random.randint(1, 100)
inv2 = pow(2, M - 2, M)

def random_point():
    # slučajna afina točka (x, y) na y^2 = x^3 + E x + V
    while True:
        x = random.randrange(M)
        rhs = (x**3 + E * x + V) % M
        if rhs == 0: return (x, 0)
        if pow(rhs, (M - 1) // 2, M) == 1:
            y = pow(rhs, (M + 1) // 4, M)
            return (x, y if random.random() < 0.5 else M - y)

def cell_from_point(pt):
    if pt is None:
        a = random.randrange(1, M)
        return (0, a, M - a)                      # null-stanje: L = 0, A = -I != 0
    x, y = pt
    k = random.randrange(1, M)                    # slučajno skaliranje reprezentanta
    A = (x + y) * inv2 % M; I = (x - y) * inv2 % M
    return (k, k * A % M, k * I % M)

def random_cell(pool):
    r = random.random()
    if r < 0.1: return cell_from_point(None)
    pt = random.choice(pool)
    if r < 0.3: pt = (pt[0], (M - pt[1]) % M)     # negacija točke iz bazena
    return cell_from_point(pt)

if mode == 'big':
    n = q = 100000
    pool = [random_point() for _ in range(50)]
else:
    n = random.randint(1, 7); q = random.randint(1, 10)
    pool = [random_point() for _ in range(random.randint(1, 3))]

out = ['%d %d %d' % (M, E, V), str(n)]
for _ in range(n):
    out.append('%d %d %d' % random_cell(pool))
out.append(str(q))
for _ in range(q):
    if random.random() < 0.3:
        out.append('1 %d %d %d %d' % ((random.randrange(n),) + random_cell(pool)))
    else:
        l = random.randrange(n); r = random.randint(l + 1, n)
        out.append('2 %d %d' % (l, r))
print('\n'.join(out))
