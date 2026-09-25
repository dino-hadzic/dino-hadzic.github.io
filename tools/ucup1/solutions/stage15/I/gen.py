import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def povezan(n, extra):
    # slucajno stablo + extra dodatnih bridova
    E = []
    perm = list(range(1, n + 1)); random.shuffle(perm)
    for i in range(1, n):
        E.append((perm[i], perm[random.randrange(i)]))
    for _ in range(extra if n > 1 else 0):
        while True:
            a, b = random.randint(1, n), random.randint(1, n)
            if a != b:
                E.append((a, b)); break
    random.shuffle(E)
    return E

if mode == 'big':
    n = 1000; m = 1000
    E = povezan(n, m - (n - 1))
    if seed % 3 == 0:
        ws = [random.randint(0, n) for _ in E]
    elif seed % 3 == 1:
        ws = [random.randint(0, 40) for _ in E]
    else:
        ws = list(range(len(E))); random.shuffle(ws)
else:
    n = random.randint(1, 6)
    m = random.randint(n - 1, min(8, n - 1 + 5))
    E = povezan(n, m - (n - 1))
    ws = [random.randint(0, random.choice([2, 4, n])) for _ in E]
print(n, len(E))
for (a, b), w in zip(E, ws):
    print(a, b, w)
