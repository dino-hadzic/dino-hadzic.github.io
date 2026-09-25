import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'small':
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        print(random.choice([random.randint(1, 30), random.randint(1, 1000), random.randint(1, 30000)]))
else:
    print(1)
    kind = random.randint(0, 2)
    if kind == 0:
        print('9' * 50)
    elif kind == 1:
        print(str(random.randint(1, 9)) + ''.join(random.choice('0123456789') for _ in range(49)))
    else:
        print('1' + '0' * 49)
