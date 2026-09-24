# Brute force: za k = 1..60000 doslovno zamijeni svaki tabulator s k razmaka i provjeri
# je li uvlačenje dosljedno (prvi uvučeni redak zadaje i, ostali se moraju slagati).
import sys
lines = sys.stdin.read().split()
n = int(lines[0]); rows = lines[1:1 + n]

depth = 0
info = []   # (dubina, tekst bez zagrade)
for r in rows:
    body, br = r[:-1], r[-1]
    if br == '{':
        info.append((depth, body)); depth += 1
    else:
        depth -= 1; info.append((depth, body))

def consistent(k):
    i = None
    for d, body in info:
        spaces = len(body.replace('t', ' ' * k))
        if d == 0:
            if spaces != 0:
                return False
            continue
        if spaces % d != 0 or spaces == 0:
            return False
        if i is None:
            i = spaces // d
        elif i != spaces // d:
            return False
    return True

for k in range(1, 60001):
    if consistent(k):
        print(k); break
else:
    print(-1)
