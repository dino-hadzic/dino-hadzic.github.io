import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exprlib import slucajno_stablo, evaluiraj, Los
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
n = 20 if mode == 'big' else random.randint(1, 20)
cmax = 9 if mode == 'big' else random.choice([1, 2, 3, 5, 7, 9])
while True:
    tree = slucajno_stablo(random.randint(0, cmax))
    xs = [round(random.uniform(-999.999999, 999.999999), 6) if random.random() < 0.5
          else round(random.uniform(-5, 5), 6) for _ in range(n)]
    try:
        ys = [evaluiraj(tree, x, 0.02) for x in xs]
    except Los:
        continue
    if all(abs(y) < 1000 for y in ys):
        break
print(n)
for x, y in zip(xs, ys):
    print('%.6f %.6f' % (x, y))
