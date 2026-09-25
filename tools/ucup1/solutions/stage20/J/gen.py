import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
primes = [p for p in range(5, 400) if is_prime(p)]
if mode == 'small':
    T = random.randint(1, 5); print(T)
    for _ in range(T):
        p = random.choice(primes)
        t = random.choice([random.randint(1, p), random.randint(1, 10), p // 2, p, 2 * p])
        print(p, t)
else:
    big = [999999999989, 1000000000039, 999999999877, 1000003, 2003]
    if seed % 2 == 1:
        print(1); print(random.choice(big), 10**6)
    else:
        T = 500000; print(T)
        print("\n".join(f"{random.choice(big)} 2" for _ in range(T)))
