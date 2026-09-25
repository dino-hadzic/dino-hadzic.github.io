import random, sys, string
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = 1000
    slova = random.sample(string.ascii_lowercase, 3)
    tip = random.choice(['ciklus', 'slucajno', 'petlje'])
else:
    n = random.randint(1, 12)
    slova = random.sample(string.ascii_lowercase, random.randint(1, 3))
    tip = 'slucajno'

# težine klasa (prvo, zadnje) da bi veliki testovi imali zanimljivu strukturu
w = {}
for a in slova:
    for b in slova:
        w[(a, b)] = 1
if tip == 'ciklus' and len(slova) == 3:
    a, b, c = slova
    w = {k: 0 for k in w}
    w[(a, b)] = w[(b, c)] = w[(c, a)] = 100
    w[(a, a)] = w[(b, b)] = w[(c, c)] = 1
    w[(b, a)] = 2
elif tip == 'petlje':
    for a in slova:
        w[(a, a)] = 10

klase = list(w.keys())
tez = [w[k] for k in klase]
rijeci = set()
while len(rijeci) < n:
    a, b = random.choices(klase, weights=tez)[0]
    L = random.randint(2, 6) if mode != 'big' else random.randint(2, 15)
    sredina = ''.join(random.choice(string.ascii_lowercase) for _ in range(L - 2))
    rijeci.add(a + sredina + b)
rijeci = list(rijeci); random.shuffle(rijeci)
print(n)
print("\n".join(rijeci))
