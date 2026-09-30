import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    z = 5; print(z)
    for t in range(z):
        l = 10**6
        if t == 0: s = 'ania' * (l // 4)
        elif t == 1: s = ('ani' * (l // 3 + 1))[:l]
        elif t == 2: s = ''.join(random.choice('ani') for _ in range(l))
        else: s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(l))
        print(s)
else:
    z = random.randint(1, 5); print(z)
    for _ in range(z):
        l = random.randint(1, 8)
        print(''.join(random.choice('aniz' if random.random() < .8 else 'ani') for _ in range(l)))
