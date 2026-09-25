# Provjera izlaza: gramatika, slozenost <= 9, duljina <= 1000, nazivnici >= 0.01, tolerancija 1e-3.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exprlib import parsiraj, evaluiraj, slozenost, Los
inp, exp, got = sys.argv[1:4]
lines = open(inp).read().split('\n')
n = int(lines[0])
pts = [tuple(map(float, lines[i + 1].split())) for i in range(n)]
s = open(got).read().strip()
try:
    if len(s) > 1000: raise Los('predugacko')
    if any(ch not in 'xsincos()+-*/' for ch in s): raise Los('nedopusten znak')
    tree = parsiraj(s)
    if slozenost(tree) > 9: raise Los('slozenost > 9')
    for x, y in pts:
        v = evaluiraj(tree, x, 0.01)
        if abs(v - y) > 1e-3 * max(1.0, abs(y)):
            raise Los('ne odgovara u x=%r: f=%r y=%r' % (x, v, y))
except Los as e:
    print('odbijeno:', e, '|', s[:100]); sys.exit(1)
sys.exit(0)
