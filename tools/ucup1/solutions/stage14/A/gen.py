import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
# Zadatak je output-only (prazan ulaz). Radi testiranja konstrukcije na raznim
# velicinama, u malom nacinu ispisujemo N (djeljiv s 4) koji sol.cpp koristi umjesto 1000.
if mode == 'big':
    pass                      # prazan ulaz -> N = 1000, trazi se 120000 <= Q
else:
    print(4 * random.randint(2, 50))
