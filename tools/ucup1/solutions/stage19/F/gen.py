import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def split_rect(w, h, cnt):
    # slučajno giljotinsko popločavanje pravokutnika w x h s cnt pravokutnika
    if cnt == 1:
        return [(w, h)]
    if w * h < cnt:
        return None
    for _ in range(50):
        left = random.randint(1, cnt - 1)
        if random.random() < 0.5 and w >= 2:
            x = random.randint(1, w - 1)
            a = split_rect(x, h, left); b = split_rect(w - x, h, cnt - left)
        elif h >= 2:
            y = random.randint(1, h - 1)
            a = split_rect(w, y, left); b = split_rect(w, h - y, cnt - left)
        else:
            continue
        if a is not None and b is not None:
            return a + b
    return None

def valid_case(S):
    while True:
        r = split_rect(S, S, 4)
        if r is not None:
            return r

MAX = 1000 if mode == 'big' else 6
r = random.random()
if r < 0.45:
    S = random.randint(2, MAX)
    rects = valid_case(S)
elif r < 0.6:
    # valjano, ali s jednim pokvarenim pravokutnikom (zadrži površinu ako je moguće)
    S = random.randint(2, MAX)
    rects = valid_case(S)
    i = random.randrange(4)
    w, h = rects[i]
    a = w * h
    divs = [d for d in range(1, min(a, MAX) + 1) if a % d == 0 and a // d <= MAX and d != w and d != h]
    if divs:
        d = random.choice(divs); rects[i] = (d, a // d)
else:
    rects = [(random.randint(1, MAX), random.randint(1, MAX)) for _ in range(4)]

rects = [(h, w) if random.random() < 0.5 else (w, h) for (w, h) in rects]
random.shuffle(rects)
for w, h in rects:
    print(w, h)
