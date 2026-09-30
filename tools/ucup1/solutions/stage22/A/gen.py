import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 500000; q = 500000
    weights = random.choice([[1, 1, 1, 1, 1], [3, 3, 2, 1, 1], [1, 1, 1, 1, 4]])
else:
    n = random.randint(1, 6); q = random.randint(1, 40)
    weights = random.choice([[1, 1, 1, 1, 1], [3, 3, 2, 1, 1], [1, 2, 2, 1, 2]])
print(n, q)
for _ in range(q):
    op = random.choices([1, 2, 3, 4, 5], weights=weights)[0]
    if op == 5:
        l = random.randint(1, n); r = l
    else:
        l = random.randint(1, n); r = random.randint(l, n)
    print(op, l, r)
