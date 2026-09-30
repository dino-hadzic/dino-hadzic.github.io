import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)

def prost(p):
    # deterministicki Miller-Rabin za p < 3.3e9
    if p < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if p % q == 0: return p == q
    d, s = p - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7):
        x = pow(a, d, p)
        if x in (1, p - 1): continue
        for _ in range(s - 1):
            x = x * x % p
            if x == p - 1: break
        else:
            return False
    return True

PROSTI = [k * 65536 + 1 for k in range(1, 10**9 // 65536 + 1) if prost(k * 65536 + 1)]
if mode == 'big':
    N = 250
else:
    N = random.randint(2, 11)
print(N, random.choice(PROSTI))
