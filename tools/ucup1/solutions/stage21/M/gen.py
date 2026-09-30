import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def case(n, maxch, pkey):
    par = [0] * (n + 1); cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        while True:
            q = random.randint(max(0, i - random.choice([1, 3, 10, i])), i - 1)
            if cnt[q] < maxch: break
        par[i] = q; cnt[q] += 1
    keys = [v for v in range(1, n + 1) if cnt[v] == 0 or random.random() < pkey]
    return par, keys
if mode == 'big':
    T = 1; print(T)
    n = 200000
    par, keys = case(n, random.choice([2, 3, 26]), random.choice([0.0, 0.3]))
    print(n, len(keys)); print(*par[1:]); random.shuffle(keys); print(*keys)
else:
    T = random.randint(1, 5); print(T)
    for _ in range(T):
        n = random.randint(1, 8)
        par, keys = case(n, 3, random.choice([0.0, 0.3, 0.7]))
        print(n, len(keys)); print(*par[1:]); random.shuffle(keys); print(*keys)
