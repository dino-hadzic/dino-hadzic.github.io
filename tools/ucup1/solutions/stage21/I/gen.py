import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def insert(a, v, is_max):
    a.append(v); i = len(a)
    while i > 1:
        par = i // 2
        if (not is_max and a[par - 1] <= a[i - 1]) or (is_max and a[par - 1] >= a[i - 1]): break
        a[par - 1], a[i - 1] = a[i - 1], a[par - 1]; i = par
def case(n, maxv):
    v = [random.randint(1, maxv) for _ in range(n)]
    a = []
    for x in v: insert(a, x, random.random() < 0.5)
    if random.random() < 0.3: random.shuffle(a)   # vjerojatno nemoguće
    return v, a
if mode == 'big':
    T = 10; print(T)
    for _ in range(T):
        n = 100000
        v, a = case(n, random.choice([10, 1000, 10**9]))
        print(n); print(*v); print(*a)
else:
    T = random.randint(1, 5); print(T)
    for _ in range(T):
        n = random.randint(1, 9)
        v, a = case(n, random.choice([2, 3, 5, 100]))
        print(n); print(*v); print(*a)
