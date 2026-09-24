import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def stablo_s_malo_listova(n, listova, maxw):
    # put duljine ~n/listova plus (listova-2) putova zakvacenih na slucajne vrhove -> <= listova listova
    bridovi = []; nxt = 2
    def put(start, duljina):
        nonlocal nxt
        prev = start
        for _ in range(duljina):
            if nxt > n: break
            bridovi.append((prev, nxt, random.randint(1, maxw))); prev = nxt; nxt += 1
    put(1, n // max(1, listova - 1))
    for i in range(max(0, listova - 2)):
        if nxt > n: break
        preostalo = listova - 2 - i
        put(random.randint(1, nxt - 1), (n - nxt + 1) // preostalo if i + 1 < listova - 2 else n - nxt + 1)
    return bridovi
if mode == 'big':
    n = q = 200000; maxw = 10 ** 9
    bridovi = stablo_s_malo_listova(n, 50, maxw)
    s = ''.join(random.choice('01') for _ in range(n))
else:
    n = random.randint(1, 9); q = random.randint(1, 12); maxw = random.choice([3, 1000])
    if random.random() < 0.5:
        bridovi = [(random.randint(1, v - 1), v, random.randint(1, maxw)) for v in range(2, n + 1)]
    else:
        bridovi = stablo_s_malo_listova(n, random.randint(2, 4), maxw)
    s = ''.join(random.choice('01') for _ in range(n))
# slucajno preimenovanje vrhova
perm = list(range(1, n + 1)); random.shuffle(perm)
lab = [0] + perm
print(n, q)
print(''.join(s[lab[i] - 1] for i in range(1, n + 1)))
for u, v, w in bridovi: print(lab[u], lab[v], w)
for _ in range(q):
    if random.random() < 0.4: print(1, random.randint(1, n))
    else:
        l = random.randint(1, n); r = random.randint(l, n)
        if mode == 'big' and random.random() < 0.5: l = random.randint(1, n // 10); r = random.randint(n - n // 10, n)
        print(2, l, r)
