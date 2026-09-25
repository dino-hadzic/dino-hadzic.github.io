import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
if mode == 'big':
    # s = 0: rjesenje samo provjerava sve skrivene lampice 1..n i ispisuje najveci broj upita
    n = [10**6, 10**6 - 1, 2**19, random.randint(1, 10**6)][(seed - 1) % 4]
    print(n, 0)
else:
    n = random.randint(1, random.choice([5, 40, 1000, 10**6]))
    print(n, random.randint(1, n))
