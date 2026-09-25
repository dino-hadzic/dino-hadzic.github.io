import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def f(n):
    d = 0; i = 1
    while i * i <= n:
        if n % i == 0:
            d += 1 if i * i == n else 2
        i += 1
    return d

if mode == 'big':
    # veliki x: ili slučajan do 10^18, ili n^f(n) za n s malo djelitelja
    r = random.random()
    if r < 0.4:
        print(random.randint(1, 10**18))
    else:
        while True:
            n = random.randint(2, 10**9)
            v = n ** f(n)
            if v <= 10**18:
                print(v); break
else:
    r = random.random()
    if r < 0.4:
        print(random.randint(1, 3 * 10**6))
    elif r < 0.8:
        # točno n^f(n) za mali n (pozitivan slučaj)
        while True:
            n = random.randint(1, 60)
            v = n ** f(n)
            if v <= 3 * 10**6:
                print(v); break
    else:
        # točna potencija koja (možda) ne odgovara broju djelitelja
        n = random.randint(2, 40); e = random.randint(2, 6)
        v = n ** e
        print(v if v <= 3 * 10**6 else n * n)
