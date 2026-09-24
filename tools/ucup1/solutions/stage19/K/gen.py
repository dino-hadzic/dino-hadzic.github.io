import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def brace_shape(n):
    # slučajan ispravan niz zagrada: prvi '{', zadnji '}'
    while True:
        s = ['{']; depth = 1
        for _ in range(n - 2):
            if depth == 0 or (depth < 60 and random.random() < 0.5):
                s.append('{'); depth += 1
            else:
                s.append('}'); depth -= 1
        if depth == 1:
            s.append('}'); return s

def depths(shape):
    d = 0; res = []
    for c in shape:
        if c == '{':
            res.append(d); d += 1
        else:
            d -= 1; res.append(d)
    return res

if mode == 'big':
    n = 100
    shape = brace_shape(n); ds = depths(shape)
    r = random.random()
    if r < 0.6:
        # konstruirano dosljedno uvlačenje s velikim k (do ~50000 razmaka po tabulatoru)
        k = random.choice([random.randint(1, 1000), random.randint(1000, 5000), random.randint(1, 49000)])
        i = random.randint(1, 999)
        lines = []
        for d in ds:
            total = d * i
            tmax = total // k
            t = random.randint(0, tmax) if random.random() < 0.9 else tmax
            s = total - t * k
            if s > 999 and tmax > 0:
                t = tmax; s = total - t * k
            if s > 999:
                s = 999   # nedosljedno, ali unutar ograničenja
            lines.append('t' * t + 's' * s)
    else:
        lines = []
        for d in ds:
            t = random.randint(0, 5); s = random.randint(0, 999 - t)
            lines.append('t' * t + 's' * s)
    print(n)
    for body, c in zip(lines, shape):
        print(body + c)
else:
    n = random.choice([2, 4, 4, 6, 6, 8, 10])   # broj redaka je nužno paran
    shape = brace_shape(n); ds = depths(shape)
    r = random.random()
    lines = []
    if r < 0.6:
        k = random.randint(1, 8); i = random.randint(1, 12)
        for d in ds:
            total = d * i
            tmax = total // k
            t = random.randint(0, tmax)
            s = total - t * k
            if random.random() < 0.1:   # ponekad pokvari jedan redak
                s += random.choice([-1, 1]); s = max(s, 0)
            lines.append('t' * t + 's' * s)
    else:
        for d in ds:
            t = random.randint(0, 3); s = random.randint(0, 10)
            lines.append('t' * t + 's' * s)
    print(n)
    for body, c in zip(lines, shape):
        print(body + c)
