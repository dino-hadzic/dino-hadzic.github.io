#!/usr/bin/env python3
"""Lokalni interaktor za zadatak B (Random Interactive Convex Hull Bot).

    python3 interactor.py <n> <broj_testova> [seed]

Za svaki test generira n slucajnih tocaka s cjelobrojnim koordinatama u [1, 10^9]
(bez tri kolinearne), pokrece ./sol (prevedeni sol.cpp), odgovara na upite
"? i j k" znakom vektorskog produkta i na kraju provjerava:
  * da je ispisana ljuska jednaka pravoj konveksnoj ljusci (kao ciklicki niz, CCW),
  * da je broj upita <= 30000, da su svi upiti valjani.
Ispisuje najveci i prosjecni broj upita.
"""
import os
import random
import subprocess
import sys


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull_ccw(pts):
    idx = sorted(range(len(pts)), key=lambda i: pts[i])
    lower = []
    for i in idx:
        while len(lower) >= 2 and cross(pts[lower[-2]], pts[lower[-1]], pts[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(idx):
        while len(upper) >= 2 and cross(pts[upper[-2]], pts[upper[-1]], pts[i]) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def gen_points(n, rng):
    pts = []
    while len(pts) < n:
        p = (rng.randint(1, 10**9), rng.randint(1, 10**9))
        if p in pts:
            continue
        pts.append(p)
    return pts


def run_one(binary, n, rng):
    pts = gen_points(n, rng)
    proc = subprocess.Popen([binary], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, text=True, bufsize=1)
    proc.stdin.write(f"{n}\n")
    proc.stdin.flush()
    queries = 0
    answer = None
    while True:
        line = proc.stdout.readline()
        if not line:
            raise RuntimeError("rjesenje je zavrsilo bez odgovora")
        tok = line.split()
        if tok[0] == '?':
            i, j, k = map(int, tok[1:4])
            if len({i, j, k}) != 3 or not all(1 <= v <= n for v in (i, j, k)):
                raise RuntimeError(f"nevaljan upit: {line.strip()}")
            queries += 1
            if queries > 30000:
                raise RuntimeError("previse upita")
            c = cross(pts[i - 1], pts[j - 1], pts[k - 1])
            if c == 0:
                raise RuntimeError("kolinearne tocke u testu (ponovi s drugim seedom)")
            proc.stdin.write("1\n" if c > 0 else "-1\n")
            proc.stdin.flush()
        elif tok[0] == '!':
            answer = list(map(int, tok[1:]))
            break
        else:
            raise RuntimeError(f"neocekivan redak: {line.strip()}")
    proc.stdin.close()
    proc.wait()

    k = answer[0]
    got = [v - 1 for v in answer[1:]]
    if len(got) != k:
        raise RuntimeError("k ne odgovara broju indeksa")
    hull = convex_hull_ccw(pts)
    if len(hull) != k or set(hull) != set(got):
        raise RuntimeError(f"kriva ljuska: ocekivano {sorted(hull)}, dobiveno {sorted(got)}")
    start = got.index(hull[0])
    rotated = got[start:] + got[:start]
    if rotated != hull:
        raise RuntimeError("krivi ciklicki redoslijed")
    return queries


def main():
    n = int(sys.argv[1])
    tests = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    here = os.path.dirname(os.path.abspath(__file__))
    binary = os.path.join(here, 'sol_interaktor_bin')
    subprocess.run(['g++', '-O2', '-std=c++17', '-Wall', '-Wno-unused-result', '-Wno-sign-compare',
                    os.path.join(here, 'sol.cpp'), '-o', binary], check=True)
    rng = random.Random(seed)
    worst, total = 0, 0
    try:
        for t in range(tests):
            q = run_one(binary, n, rng)
            worst = max(worst, q)
            total += q
        print(f"n={n}: {tests} testova OK, najvise upita {worst}, prosjek {total / tests:.1f}")
    finally:
        if os.path.exists(binary):
            os.remove(binary)


if __name__ == '__main__':
    main()
