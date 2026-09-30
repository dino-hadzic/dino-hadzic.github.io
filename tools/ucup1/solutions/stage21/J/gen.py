import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def case(n, C):
    A = [[0] * (i + 1) for i in range(n)]; B = [[0] * (i + 1) for i in range(n)]; Cc = [[0] * (i + 1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i + 1):
            while True:
                a = random.randint(1, C); b = random.randint(1, C)
                lo, hi = abs(a - b) + 1, a + b - 1
                if lo <= hi: break
            c = random.randint(lo, hi)
            A[i][j], B[i][j], Cc[i][j] = a, b, c
    print(n)
    for M in (A, B, Cc):
        for i in range(1, n): print(*M[i][1:])
if mode == 'big':
    T = 16; print(T)
    for _ in range(T): case(300, random.choice([3, 10**9]))
else:
    T = random.randint(1, 4); print(T)
    for _ in range(T): case(random.choice([2, 2, 3, 3, 3, 4]), random.choice([3, 10, 10**9]))
