import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
T = ['Chang', 'Duan', 'Tong', '-']

def stablo(n, oblik):
    par = [0] * (n + 1)
    for i in range(2, n + 1):
        if oblik == 0: par[i] = random.randint(1, i - 1)
        elif oblik == 1: par[i] = random.randint(max(1, i - 3), i - 1)
        else: par[i] = 1 if i <= max(2, n // 20) else random.randint(1, i - 1)
    return par

def rjesivo(n, par, broj_parova, blizu=False):
    # konstruiraj instancu koja sigurno ima rjesenje: slucajni parovi s disjunktnim putovima
    dep = [0] * (n + 1)
    for i in range(2, n + 1): dep[i] = dep[par[i]] + 1
    tip = ['-'] * (n + 1); used = set()
    for _ in range(broj_parova):
        a = random.randint(2, n)
        b = random.randint(max(2, a - 40), min(n, a + 40)) if blizu else random.randint(2, n)
        if a == b or tip[a] != '-' or tip[b] != '-': continue
        x, y, e = a, b, set()
        while x != y:
            if dep[x] < dep[y]: x, y = y, x
            e.add(x); x = par[x]
        if e & used: continue
        used |= e
        if dep[a] == dep[b]: tip[a] = tip[b] = 'Tong'
        elif dep[a] > dep[b]: tip[a], tip[b] = 'Chang', 'Duan'
        else: tip[a], tip[b] = 'Duan', 'Chang'
    return tip

if mode == 'big':
    n = 100000
    par = stablo(n, seed % 3)
    tip = rjesivo(n, par, 200000, blizu=True) if seed % 2 else [random.choice(T) for _ in range(n + 1)]
else:
    n = random.randint(2, 9)
    par = stablo(n, random.randint(0, 2))
    if random.random() < 0.6:
        tip = rjesivo(n, par, random.randint(1, 6))
        if random.random() < 0.3:      # mala perturbacija: cesto postane nerjesivo na zanimljiv nacin
            v = random.randint(2, n); tip[v] = random.choice(T)
    else:
        tip = [random.choice(T if random.random() < 0.7 else T[:3]) for _ in range(n + 1)]
if all(tip[v] == '-' for v in range(2, n + 1)):
    tip[2] = 'Tong'
print(n)
for i in range(2, n + 1):
    print(i, par[i], tip[i])
