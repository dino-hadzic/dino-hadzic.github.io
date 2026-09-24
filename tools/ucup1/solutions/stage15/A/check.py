# Lokalni sudac za interaktivni zadatak. Ulaz: "n s".
#  s >= 1: izlaz je transkript (? x / odgovor / ... / ! s); provjeravamo valjanost upita,
#          da su ispisani odgovori upravo oni koje bi dao sudac, broj upita <= 40 i konačni odgovor.
#  s = 0 : izlaz je sažetak "sve n krivo 0 maksupita K" (sve skrivene lampice), K <= 40.
import sys
inp, exp, got = sys.argv[1:4]
n, s = map(int, open(inp).read().split())
tok = open(got).read().split()
if s == 0:
    if len(tok) != 6 or tok[0] != 'sve' or int(tok[1]) != n or tok[2] != 'krivo' or int(tok[3]) != 0 \
            or tok[4] != 'maksupita' or int(tok[5]) > 40:
        print('los sazetak:', ' '.join(tok)); sys.exit(1)
    sys.exit(0)
on = set(); L = R = 0; q = 0; i = 0
while i < len(tok):
    if tok[i] == '!':
        if i + 2 != len(tok) or int(tok[i + 1]) != s:
            print('krivi odgovor', tok[i:]); sys.exit(1)
        sys.exit(0)
    if tok[i] != '?':
        print('neocekivan token', tok[i]); sys.exit(1)
    x = int(tok[i + 1]); q += 1
    if not (1 <= x <= n) or q > 40:
        print('nevaljan upit ili previse upita', x, q); sys.exit(1)
    if x not in on:
        on.add(x)
        if x < s: L += 1
        elif x > s: R += 1
    if int(tok[i + 2]) != abs(L - R):
        print('krivi simulirani odgovor za upit', x); sys.exit(1)
    i += 3
print('nema odgovora'); sys.exit(1)
