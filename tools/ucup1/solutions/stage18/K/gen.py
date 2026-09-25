import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def case(lim, dlim):
    while True:
        xa = random.randint(-lim, lim); xb = random.randint(-lim, lim)
        if xa == xb: continue
        da = random.randint(1, dlim); db = random.randint(1, dlim)
        kind = random.random()
        if kind < 0.35:
            yc = 0                     # kolinearna središta
        else:
            yc = random.randint(-lim, lim)
        xc = random.randint(-lim, lim)
        if yc == 0 and xc in (xa, xb): continue
        dc = random.randint(-dlim, dlim)
        if dc == 0: continue
        if random.random() < 0.15:
            # gnijezdene kružnice s zajedničkom točkom dodira (degenerirane obitelji)
            t = random.choice([-1, 1])
            da, db = abs(xa - t * lim) or 1, abs(xb - t * lim) or 1
            if yc == 0:
                dc = abs(xc - t * lim) or 1
                if random.random() < 0.5: dc = -dc
        return (xa, da, xb, db, xc, yc, dc)
if mode == 'small':
    T = random.randint(1, 20); lim = random.choice([3, 5, 10]); dlim = random.choice([3, 5, 10])
else:
    T = 200000; lim = 100; dlim = 100
print(T)
out = []
for _ in range(T):
    xa, da, xb, db, xc, yc, dc = case(lim, dlim)
    out.append(f"{xa} 0 {da}\n{xb} 0 {db}\n{xc} {yc} {dc}")
print("\n".join(out))
