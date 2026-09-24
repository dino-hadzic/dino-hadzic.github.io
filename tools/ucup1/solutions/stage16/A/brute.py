#!/usr/bin/env python3
# Brute force: isprobaj sve repdigite a <= n i provjeri je li n - a repdigit.
import sys
data = sys.stdin.read().split()
t = int(data[0])
out = []
for i in range(1, t + 1):
    n = int(data[i])
    L = len(data[i])
    found = None
    for ln in range(1, L + 1):
        for d in range(1, 10):
            a = int(str(d) * ln)
            if a >= n:
                continue
            b = n - a
            s = str(b)
            if s == s[0] * len(s):
                found = (a, b)
                break
        if found:
            break
    out.append(f'{found[0]} {found[1]}')
print('\n'.join(out))
