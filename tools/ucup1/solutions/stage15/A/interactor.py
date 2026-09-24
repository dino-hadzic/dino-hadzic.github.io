# Pravi interaktivni sudac (cijevi): python3 interactor.py <binarka> [n] [s]
# Bez argumenata n, s: iscrpno sve (n, s) za n <= 60 te nekoliko slucajnih velikih n.
import random, subprocess, sys

def run(exe, n, s):
    p = subprocess.Popen([exe], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
    p.stdin.write(f'{n}\n'); p.stdin.flush()
    on = set(); L = R = 0; q = 0
    while True:
        line = p.stdout.readline()
        if not line:
            raise RuntimeError(f'nema izlaza (n={n}, s={s})')
        t, x = line.split(); x = int(x)
        if t == '!':
            p.wait()
            if x != s: raise RuntimeError(f'krivi odgovor n={n} s={s}: {x}')
            return q
        assert t == '?' and 1 <= x <= n, line
        q += 1
        if q > 40: raise RuntimeError(f'previse upita n={n} s={s}')
        if x not in on:
            on.add(x)
            if x < s: L += 1
            elif x > s: R += 1
        p.stdin.write(f'{abs(L - R)}\n'); p.stdin.flush()

exe = sys.argv[1]
if len(sys.argv) >= 4:
    print('upita:', run(exe, int(sys.argv[2]), int(sys.argv[3])))
else:
    mx = 0
    for n in range(1, 61):
        for s in range(1, n + 1):
            mx = max(mx, run(exe, n, s))
    print('iscrpno n<=60: OK, najvise upita', mx)
    random.seed(1)
    for _ in range(30):
        n = random.randint(1, 10**6); s = random.randint(1, n)
        mx = max(mx, run(exe, n, s))
    print('30 slucajnih velikih: OK, najvise upita ukupno', mx)
