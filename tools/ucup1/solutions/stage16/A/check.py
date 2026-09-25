#!/usr/bin/env python3
# Checker: a i b moraju biti repdigiti i a + b = n.
import sys
inp = open(sys.argv[1]).read().split()
got = open(sys.argv[3]).read().split()
t = int(inp[0])
if len(got) != 2 * t:
    print('krivi broj tokena'); sys.exit(1)
def rep(s):
    return len(s) > 0 and s[0] != '0' and s == s[0] * len(s)
for i in range(t):
    n = inp[1 + i]
    a, b = got[2 * i], got[2 * i + 1]
    if not rep(a) or not rep(b):
        print('nije repdigit', a, b); sys.exit(1)
    if int(a) + int(b) != int(n):
        print('zbroj nije n'); sys.exit(1)
sys.exit(0)
