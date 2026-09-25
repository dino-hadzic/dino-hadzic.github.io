import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
n = 100000 if mode == 'big' else random.randint(3, 10)
a = random.randint(0, n)
print(n, a)
p = random.random()
print(' '.join('1' if random.random() < p else '0' for _ in range(n)))
