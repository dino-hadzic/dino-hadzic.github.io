# Checker: YES/NO mora odgovarati očekivanom; za YES provjeri da je par valjan.
import sys
def digits(x, b):
    d = []
    while x:
        d.append(x % b); x //= b
    return d
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
T = int(inp[0]); p = 1; g = 0; e = 0
for tc in range(T):
    x, y, A, B = map(int, inp[p:p + 4]); p += 4
    if g >= len(got):
        print("premalo redaka"); sys.exit(1)
    verdict = got[g]; g += 1
    if exp is not None:
        ev = exp[e]; e += 1
        if ev == 'YES': e += 2
        if ev != verdict:
            print(f"test {tc}: očekivano {ev}, dobiveno {verdict}"); sys.exit(1)
    if verdict == 'YES':
        a, b = int(got[g]), int(got[g + 1]); g += 2
        if not (2 <= a <= A and 2 <= b <= B and digits(x, a) == digits(y, b)):
            print(f"test {tc}: nevaljan par {a} {b}"); sys.exit(1)
    elif verdict != 'NO':
        print("neispravan izlaz"); sys.exit(1)
if g != len(got):
    print("previše izlaza"); sys.exit(1)
sys.exit(0)
