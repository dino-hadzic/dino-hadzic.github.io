import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def coord():
    return random.choice([0, 255, random.randint(0, 255), random.randint(0, 255), random.choice([1, 254, 127, 128])])
t = 10000 if mode == 'big' else random.randint(1, 200)
print(t)
for _ in range(t):
    print(coord(), coord(), coord())
