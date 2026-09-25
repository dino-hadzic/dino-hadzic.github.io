import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def prost(x):
    if x < 2: return False
    d = 2
    while d * d <= x:
        if x % d == 0: return False
        d += 1
    return True
def slucajni_prost(lo, hi):
    while True:
        x = random.randint(lo, hi)
        if prost(x): return x
def test(p):
    n = random.choice([1, p, random.randint(1, p), random.randint(max(1, p - 3), p)])
    S = random.sample(range(p), n)
    if 0 not in S and random.random() < 0.8:
        S[random.randrange(n)] = 0
    return n, p, S
tests = []
if mode == 'big':
    if seed % 2:
        tests.append(test(199999))                  # jedan veliki prost broj
    else:
        ukupno = 0
        while ukupno + 1000 <= 200000:
            p = slucajni_prost(2, 1000); ukupno += p; tests.append(test(p))
else:
    T = random.randint(1, 4)
    for _ in range(T): tests.append(test(slucajni_prost(2, 40)))
print(len(tests))
for n, p, S in tests:
    print(n, p); print(*S)
