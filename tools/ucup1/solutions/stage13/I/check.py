# Checker: niz operacija mora sortirati permutaciju i biti jednako dug kao optimalni (iz brute forcea).
import sys
inp = open(sys.argv[1]).read().split()
exp = None if sys.argv[2] == '-' else open(sys.argv[2]).read().strip()
got = open(sys.argv[3]).read().strip()
n = int(inp[0]); p = list(map(int, inp[1:1 + n]))
if not got.endswith('.') or got.count('.') != 1 or any(ch not in 'PS' for ch in got[:-1]):
    print('los format'); sys.exit(1)
ops = got[:-1]
if len(ops) > n:
    print('predugo'); sys.exit(1)
a = p[:]
for k, o in enumerate(ops, 1):
    if o == 'P':
        a[:k] = sorted(a[:k])
    else:
        a[n - k:] = sorted(a[n - k:])
if a != list(range(1, n + 1)):
    print('nije sortirano'); sys.exit(1)
if exp is not None and len(ops) != len(exp) - 1:
    print(f'duljina {len(ops)} != optimalno {len(exp) - 1}'); sys.exit(1)
sys.exit(0)
