import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def rep(ln):
    return str(random.randint(1, 9)) * ln

if mode == 'big':
    # ukupno 1e5 znamenki: 25 testova s ~4000 znamenki
    t = 25
    print(t)
    for _ in range(t):
        la = random.choice([3999, 3998, 3999])
        lb = random.choice([1, 2, la - 1, la])
        print(int(rep(la)) + int(rep(lb)))
else:
    t = random.randint(1, 30)
    print(t)
    for _ in range(t):
        la = random.randint(1, 7)
        lb = random.randint(1, la)
        print(int(rep(la)) + int(rep(lb)))
