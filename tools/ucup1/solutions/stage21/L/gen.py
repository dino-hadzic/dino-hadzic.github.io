import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    T = 10; print(T)
    for _ in range(T):
        n = 100000
        pq = random.choice([0.3, 0.9, 1.0])
        s = ''.join('?' if random.random() < pq else random.choice('01') for _ in range(n))
        print(n, random.randint(0, n - 1)); print(s)
else:
    T = random.randint(1, 8); print(T)
    for _ in range(T):
        n = random.randint(1, 11)
        pq = random.choice([0.3, 0.6, 1.0])
        s = ''.join('?' if random.random() < pq else random.choice('01') for _ in range(n))
        print(n, random.randint(0, n - 1)); print(s)
