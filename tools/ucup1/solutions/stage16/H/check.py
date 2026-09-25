#!/usr/bin/env python3
# Checker: k mora biti jednak ocekivanom (iz brute forcea), sparivanje savrseno,
# a broj prijateljskih parova tocno k.
import sys
inp = open(sys.argv[1]).read().split()
exp = open(sys.argv[2]).read().split() if sys.argv[2] != '-' else None
got = open(sys.argv[3]).read().split()
t = int(inp[0]); p = 1; q = 0; e = 0
for tc in range(t):
    n = int(inp[p]); p += 1
    pts = [(int(inp[p + 2 * i]), int(inp[p + 2 * i + 1])) for i in range(2 * n)]; p += 4 * n
    if q + 1 + 2 * n > len(got):
        print('premalo izlaza'); sys.exit(1)
    k = int(got[q]); q += 1
    if exp is not None:
        ke = int(exp[e]); e += 1 + 2 * n
        if k != ke:
            print(f'test {tc}: k={k}, ocekivano {ke}'); sys.exit(1)
    used = [False] * (2 * n + 1)
    fr = 0
    for i in range(n):
        a, b = int(got[q]), int(got[q + 1]); q += 2
        if not (1 <= a <= 2 * n and 1 <= b <= 2 * n) or a == b or used[a] or used[b]:
            print(f'test {tc}: nevaljan par {a} {b}'); sys.exit(1)
        used[a] = used[b] = True
        if pts[a - 1][0] == pts[b - 1][0] or pts[a - 1][1] == pts[b - 1][1]:
            fr += 1
    if fr != k:
        print(f'test {tc}: prijateljskih {fr}, ispisano k={k}'); sys.exit(1)
if q != len(got):
    print('visak izlaza'); sys.exit(1)
sys.exit(0)
