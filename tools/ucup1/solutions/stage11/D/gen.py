import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def pvec(s):                      # definicija, O(n^3), za male n
    n = len(s); res = []
    for j in range(1, n + 1):
        best = min(range(j), key=lambda x: s[x:j]); res.append(best + 1)
    return res
def pvec_duval(s):                # Duval: unutar segmenta p_m = p_{m-P} + P (jednako) ili p_m = i (vece)
    n = len(s); p = [0] * n; i = 0
    while i < n:
        j = i; k = i + 1; P = 1; p[i] = i + 1
        while k < n and s[j] <= s[k]:
            if s[j] < s[k]: j = i; P = k - i + 1; p[k] = i + 1
            else: j += 1; p[k] = p[k - P] + P
            k += 1
        while i <= j: i += k - j
    return p
if mode == 'big':
    tests = []
    if seed % 2 == 0:
        n = 3 * 10**6
        kind = random.randint(0, 2)
        if kind == 0: tests.append(list(range(1, n + 1)))          # sami jednoslovni faktori
        elif kind == 1: tests.append([1] * n)                       # jedna Lyndonova rijec
        else: tests.append(pvec_duval([random.randint(1, 3) for _ in range(n)]))
    else:
        for _ in range(10**5):
            tests.append(pvec_duval([random.randint(1, 3) for _ in range(30)]))
else:
    tests = []
    for _ in range(random.randint(1, 4)):
        n = random.randint(1, 6)
        if random.random() < 0.6:
            s = [random.randint(1, random.randint(1, n)) for _ in range(n)]
            tests.append(pvec(s))
        else:
            tests.append([random.randint(1, i) for i in range(1, n + 1)])
print(len(tests))
for p in tests:
    print(len(p)); print(' '.join(map(str, p)))
