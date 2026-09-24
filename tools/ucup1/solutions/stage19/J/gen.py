import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

if mode == 'big':
    n = 800
    tip = random.randint(0, 3)
    if tip == 0:
        s = 'a' * n
    elif tip == 1:
        s = ''.join(random.choice('ab') for _ in range(n))
    elif tip == 2:
        blok = ''.join(random.choice('abc') for _ in range(random.randint(1, 5)))
        s = (blok * (n // len(blok) + 1))[:n]
    else:
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n))
    print(s)
else:
    n = random.randint(1, 12)
    alfabet = random.choice(['a', 'ab', 'abc'])
    print(''.join(random.choice(alfabet) for _ in range(n)))
