import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def graf(n, m):
    # svaki vrh v>=2 dobije bar jedan ulazni brid iz manjeg vrha; ostatak slucajno bez duplikata
    bridovi = set()
    for v in range(2, n + 1): bridovi.add((random.randint(1, v - 1), v))
    svi = [(u, v) for v in range(2, n + 1) for u in range(1, v)]
    random.shuffle(svi)
    for e in svi:
        if len(bridovi) >= m: break
        bridovi.add(e)
    return sorted(bridovi)
if mode == 'big':
    if seed % 3 == 1: n, m = 26, 46           # najgori slucaj za DP
    elif seed % 3 == 2: n, m = 27, 45         # najvise stabala (2^19)
    else: n, m = 36, 36
    maxv = 10 ** 15
else:
    n = random.randint(2, 8)
    m = random.randint(n - 1, min(n * (n - 1) // 2, 72 - n))
    maxv = random.choice([5, 20, 10 ** 15])
bridovi = graf(n, m)
if mode == 'big' and seed % 3 == 2:
    # 19 vrhova s ulaznim stupnjem 2 -> 2^19 korijenskih stabala
    bridovi = set((random.randint(1, v - 1), v) for v in range(2, n + 1))
    for v in range(3, 22):
        while len([e for e in bridovi if e[1] == v]) < 2:
            bridovi.add((random.randint(1, v - 1), v))
    bridovi = sorted(bridovi)
print(n, len(bridovi))
for v in range(2, n + 1): print(random.randint(1, maxv), random.randint(1, maxv))
for u, v in bridovi: print(u, v)
