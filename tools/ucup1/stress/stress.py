#!/usr/bin/env python3
"""Lokalna provjera C++ rješenja (uzorci + stress test protiv brute forcea). Ništa se ne šalje na QOJ.

Struktura mape solutions/stageN/<slovo>/:
  sol.cpp        rješenje koje se prikazuje na stranici (obvezno)
  brute.cpp|py   sporo, očito točno rješenje za male ulaze (za stress test)
  gen.py         generator:  python3 gen.py <seed> [small|big]  -> ispisuje jedan test na stdout
  check.py       (neobvezno) checker za zadatke s više točnih odgovora:
                 python3 check.py <ulaz> <očekivani izlaz ili -> <dobiveni izlaz>; izlazni kod 0 = točno
  samples/K.in, samples/K.out   službeni primjeri

Pokretanje:  python3 stress.py stage19/A [-n 300] [--tl 2.0] [--big 3]
Ispisuje sažetak pogodan za polje 'verified' u content/stageN.py.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTIONS = os.path.join(HERE, '..', 'solutions')
CXX = ['g++', '-O2', '-std=c++17', '-Wall', '-Wno-unused-result', '-Wno-sign-compare']


def compile_cpp(src, out):
    r = subprocess.run(CXX + [src, '-o', out], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr)
        sys.exit(f'compile error: {src}')


def runner(path, build_dir):
    """Vrati naredbu za pokretanje programa (C++ se prevede, Python se pokreće izravno)."""
    if path.endswith('.cpp'):
        exe = os.path.join(build_dir, os.path.basename(path)[:-4])
        compile_cpp(path, exe)
        return [exe]
    return [sys.executable, path]


def run(cmd, inp, tl):
    t = time.time()
    try:
        r = subprocess.run(cmd, input=inp, capture_output=True, text=True, timeout=tl)
    except subprocess.TimeoutExpired:
        return None, 'TLE', tl
    dt = time.time() - t
    if r.returncode != 0:
        return None, f'RE (exit {r.returncode}): {r.stderr[-300:]}', dt
    return r.stdout, None, dt


def tokens_equal(a, b):
    return a.split() == b.split()


def check(checker, inp, expected, got, tmp):
    if checker is None:
        return tokens_equal(expected, got)
    fi, fe, fg = [os.path.join(tmp, n) for n in ('in.txt', 'exp.txt', 'got.txt')]
    open(fi, 'w').write(inp)
    open(fe, 'w').write(expected if expected is not None else '')
    open(fg, 'w').write(got)
    r = subprocess.run([sys.executable, checker, fi, fe if expected is not None else '-', fg], capture_output=True, text=True)
    if r.returncode != 0 and r.stdout.strip():
        print('   checker:', r.stdout.strip()[:200])
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('problem', help='npr. stage19/A')
    ap.add_argument('-n', type=int, default=300, help='broj slučajnih testova')
    ap.add_argument('--tl', type=float, default=2.0, help='vremensko ograničenje po testu (s)')
    ap.add_argument('--big', type=int, default=0, help='broj velikih testova (gen.py <seed> big) samo za mjerenje vremena')
    a = ap.parse_args()

    d = os.path.join(SOLUTIONS, a.problem)
    sol = os.path.join(d, 'sol.cpp')
    if not os.path.exists(sol):
        sys.exit(f'nema {sol}')
    brute = next((os.path.join(d, b) for b in ('brute.cpp', 'brute.py') if os.path.exists(os.path.join(d, b))), None)
    gen = os.path.join(d, 'gen.py') if os.path.exists(os.path.join(d, 'gen.py')) else None
    checker = os.path.join(d, 'check.py') if os.path.exists(os.path.join(d, 'check.py')) else None

    tmp = tempfile.mkdtemp(prefix='stress_')
    try:
        sol_cmd = runner(sol, tmp)
        brute_cmd = runner(brute, tmp) if brute else None
        summary = []

        # 1) službeni primjeri
        sdir = os.path.join(d, 'samples')
        ins = sorted(f for f in os.listdir(sdir) if f.endswith('.in')) if os.path.isdir(sdir) else []
        ok = 0
        for f in ins:
            inp = open(os.path.join(sdir, f)).read()
            exp_path = os.path.join(sdir, f[:-3] + '.out')
            exp = open(exp_path).read() if os.path.exists(exp_path) else None
            got, err, dt = run(sol_cmd, inp, a.tl)
            if err:
                print(f'uzorak {f}: {err}')
                continue
            if exp is None and checker is None:
                print(f'uzorak {f}: nema .out ni check.py – preskačem usporedbu')
                continue
            if check(checker, inp, exp, got, tmp):
                ok += 1
            else:
                print(f'uzorak {f}: KRIVO\n--- očekivano\n{(exp or "")[:400]}\n--- dobiveno\n{got[:400]}')
        if ins:
            print(f'uzorci: {ok}/{len(ins)}')
            summary.append(f'uzorci {ok}/{len(ins)}')
            if ok != len(ins):
                sys.exit(1)

        # 2) stress test protiv brute forcea
        if gen and brute_cmd:
            worst = 0.0
            for seed in range(1, a.n + 1):
                inp = subprocess.run([sys.executable, gen, str(seed), 'small'], capture_output=True, text=True, check=True).stdout
                exp, err_b, _ = run(brute_cmd, inp, max(a.tl * 5, 10))
                if err_b:
                    print(f'seed {seed}: brute {err_b}')
                    open(os.path.join(d, 'fail.in'), 'w').write(inp)
                    sys.exit(1)
                got, err, dt = run(sol_cmd, inp, a.tl)
                worst = max(worst, dt)
                if err or not check(checker, inp, exp, got, tmp):
                    print(f'seed {seed}: {err or "KRIVO"}\n--- ulaz\n{inp[:600]}\n--- očekivano\n{exp[:400]}\n--- dobiveno\n{(got or "")[:400]}')
                    open(os.path.join(d, 'fail.in'), 'w').write(inp)
                    sys.exit(1)
            print(f'stress: {a.n}/{a.n} slučajnih testova OK (najsporiji {worst:.2f} s)')
            summary.append(f'{a.n} slučajnih malih testova protiv brute forcea')
        elif gen and checker:
            # bez brute forcea: samo checker (npr. konstruktivni zadaci)
            for seed in range(1, a.n + 1):
                inp = subprocess.run([sys.executable, gen, str(seed), 'small'], capture_output=True, text=True, check=True).stdout
                got, err, dt = run(sol_cmd, inp, a.tl)
                if err or not check(checker, inp, None, got, tmp):
                    print(f'seed {seed}: {err or "checker odbio"}\n--- ulaz\n{inp[:600]}\n--- dobiveno\n{(got or "")[:400]}')
                    open(os.path.join(d, 'fail.in'), 'w').write(inp)
                    sys.exit(1)
            print(f'checker: {a.n}/{a.n} slučajnih testova OK')
            summary.append(f'{a.n} slučajnih testova provjereno checkerom')
        else:
            print('nema gen.py + brute/check.py – stress test preskočen')

        # 3) veliki testovi – samo vrijeme
        if gen and a.big:
            worst = 0.0
            for seed in range(1, a.big + 1):
                inp = subprocess.run([sys.executable, gen, str(seed), 'big'], capture_output=True, text=True, check=True).stdout
                got, err, dt = run(sol_cmd, inp, a.tl * 3)
                if err:
                    print(f'big seed {seed}: {err}')
                    sys.exit(1)
                worst = max(worst, dt)
            print(f'veliki testovi: {a.big}, najsporiji {worst:.2f} s')
            summary.append(f'{a.big} velikih testova (najviše {worst:.2f} s)')

        print('\nverified: ' + ', '.join(summary) + '.')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
