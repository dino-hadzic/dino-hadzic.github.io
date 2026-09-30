import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def dopuni(a):
    # dodaj jedinice dok ne bude barem S/5 jedinica (a ostaje <= 2e5 elemenata)
    S = sum(a); o = a.count(1)
    while 5 * o < S:
        a.append(1); S += 1; o += 1
    return a

if mode == 'big':
    tip = seed % 4
    if tip == 0:            # sve dvojke, r ~ S/3 (najveca tablica)
        a = [2] * 66000 + [0] * 1000
    elif tip == 1:          # malo razlicitih vrijednosti s velikim brojnostima
        a = []
        for v in range(2, 12):
            a += [v] * 2460
    elif tip == 2:          # konstrukcija s prazninom: M dvojki i jedan M+1
        M = 40000
        a = [2] * M + [M + 1] + [0] * 3000
    else:                   # slucajne velike vrijednosti
        a = [0] * 2000
        while sum(a) < 75000:
            a.append(random.randint(2, random.choice([3, 10, 100, 3000])))
    a = dopuni(a)
    random.shuffle(a)
    assert len(a) <= 200000 and sum(a) <= 200000
else:
    a = []
    t = random.random()
    if t < 0.25:            # konstrukcija s velikom prazninom u skupu brojeva elemenata
        M = random.randint(10, 16)
        a = [2] * M + [M + 1] + [0] * random.randint(0, 2)
    elif t < 0.4:           # srednje velik test (brute je O(n^2 S))
        for _ in range(random.randint(10, 30)): a.append(random.randint(2, 12))
        for _ in range(random.randint(0, 5)): a.append(0)
    elif t < 0.6:           # vise elemenata malih vrijednosti
        for _ in range(random.randint(5, 14)): a.append(random.randint(2, 5))
        for _ in range(random.randint(0, 2)): a.append(0)
    else:
        for _ in range(random.randint(0, 3)): a.append(0)
        for _ in range(random.randint(0, 5)): a.append(random.randint(2, 9))
        for _ in range(random.randint(0, 3)): a.append(1)
    a = dopuni(a)
    if not a: a = [1]
    random.shuffle(a)
print(len(a), sum(a))
print(*a)
