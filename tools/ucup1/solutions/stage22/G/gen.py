import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    n = 5000
    k = random.choice([1, 2, 7, 5000, random.randint(1, 5000)])
    p = random.choice([0.0, 0.2, 0.45])
else:
    n = random.randint(1, 9)
    k = random.randint(1, 14) if random.random() < 0.8 else random.randint(0, 3)
    p = random.choice([0.0, 0.2, 0.4, 0.6])
print(n, k)
rows = []
for i in range(n):
    row = ''.join('*' if random.random() < p else '.' for _ in range(n))
    rows.append(list(row))
rows[0][0] = '.'; rows[n - 1][n - 1] = '.'
sys.stdout.write('\n'.join(''.join(r) for r in rows) + '\n')
