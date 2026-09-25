import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
n = 2000 if mode == 'big' else random.randint(1, 9)
p = list(range(1, n + 1))
r = random.random()
if r < 0.7: random.shuffle(p)
elif r < 0.85: p.reverse()
# inace sortirana permutacija
print(n, ' '.join(map(str, p)))
