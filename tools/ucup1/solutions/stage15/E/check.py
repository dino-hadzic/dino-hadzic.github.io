import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tapalib import valjano
inp, exp, got = sys.argv[1:4]
data = open(inp).read().split()
n, m = int(data[0]), int(data[1]); grid = data[2:2 + 2 * n - 1]
tok = open(got).read().split()
ocek = open(exp).read().split()[0] if exp != '-' else None
if not tok: print('prazan izlaz'); sys.exit(1)
if ocek is not None and tok[0] != ocek:
    print('ocekivano', ocek, 'dobiveno', tok[0]); sys.exit(1)
if tok[0] == 'NO': sys.exit(0)
err = valjano(n, m, grid, tok[1:])
if err: print(err); sys.exit(1)
sys.exit(0)
