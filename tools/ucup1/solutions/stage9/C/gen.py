import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 10
    print(T)
    for _ in range(T):
        n = 1000000
        s = ''.join(random.choice('01') for _ in range(n))
        # malo razlika da odgovor ne bude trivijalno 0
        t = list(s)
        for _ in range(random.randint(0, 3)):
            i = random.randrange(n); t[i] = '1' if t[i] == '0' else '0'
        print(n); print(s); print(''.join(t))
else:
    T = random.randint(1, 5)
    print(T)
    for _ in range(T):
        n = random.randint(1, 8)
        s = ''.join(random.choice('01') for _ in range(n))
        t = list(s)
        # malo razlika (0-3 promijenjena mjesta ili nasumican t)
        if random.random() < 0.5:
            for _ in range(random.randint(0, 3)):
                i = random.randrange(n); t[i] = '1' if t[i] == '0' else '0'
        else:
            t = [random.choice('01') for _ in range(n)]
        print(n); print(s); print(''.join(t))
