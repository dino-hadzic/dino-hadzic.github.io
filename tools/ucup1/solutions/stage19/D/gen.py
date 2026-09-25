import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = 100000
    tip = random.choice(['lanac', 'suma', 'zvijezda', 'bez'])
    maxc = 10 ** 6
else:
    n = random.randint(1, 7)
    tip = random.choice(['suma', 'bez', 'lanac'])
    maxc = random.choice([3, 10, 100])

def vjer():
    dec = random.choice([1, 2, 6, 6]) if mode == 'small' else 6
    while True:
        x = random.randint(1, 10 ** dec - 1)
        s = ("%0*d" % (dec, x))
        return "0." + s

# ovisnosti: slučajna šuma po permutaciji (d = kasniji u perm ovisi o ranijem)
perm = list(range(1, n + 1)); random.shuffle(perm)
d = [0] * (n + 1)
for i in range(1, n):
    if tip == 'bez':
        break
    if tip == 'lanac':
        d[perm[i]] = perm[i - 1]
    elif tip == 'zvijezda':
        d[perm[i]] = perm[0]
    elif random.random() < 0.7:
        d[perm[i]] = perm[random.randint(0, i - 1)]
print(n)
for i in range(1, n + 1):
    c = random.randint(1, maxc)
    print(c, vjer(), d[i])
