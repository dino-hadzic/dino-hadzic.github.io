import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def rnd(n):
    p = random.choice([0.1, 0.3, 0.5, 0.5, 0.7, 0.9, random.random()])
    return ''.join('1' if random.random() < p else '0' for _ in range(n))
if mode == 'big':
    if seed % 2 == 1:
        tests = [rnd(10**7)]
    else:
        tests = [rnd(10) for _ in range(10**6)]
else:
    tests = [rnd(random.randint(1, 12)) for _ in range(random.randint(1, 4))]
print(len(tests))
print('\n'.join(tests))
