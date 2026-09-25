import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def test(n, maxx, L, R, mala_vrijednost=False):
    xs = sorted(random.sample(range(1, maxx + 1), n))
    if mala_vrijednost: a = [random.randint(1, min(n, 3)) for _ in range(n)]
    else: a = [random.randint(1, n) for _ in range(n)]
    return n, L, R, xs, a
tests = []
if mode == 'big':
    n = 10 ** 6
    if seed % 3 == 1: tests.append(test(n, n, 1, 2))                      # gust, mali prozor
    elif seed % 3 == 2: tests.append(test(n, 10 ** 9, 1, 10 ** 9, True))  # ogroman prozor, malo raznih vrijednosti
    else: tests.append(test(n, 3 * n, 2, 6))
else:
    T = random.randint(1, 3)
    for _ in range(T):
        n = random.randint(1, 8)
        L = random.randint(1, 4); R = L + random.randint(0, 4)
        tests.append(test(n, random.randint(n, 3 * n), L, R, random.random() < 0.4))
print(len(tests))
for n, L, R, xs, a in tests:
    print(n, L, R); print(*xs); print(*a)
