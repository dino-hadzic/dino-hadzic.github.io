# Sporo, očito točno rješenje: DP po elementima skupa T = span(B) ∩ [1, X],
# stanje = kanonska baza (reducirani stupnjeviti oblik) do sada razapetog potprostora.
import sys
MOD = 998244353

def canon(vectors):
    # reducirani stupnjeviti oblik potprostora razapetog zadanim vektorima -> tuple
    rows = []
    for v in vectors:
        for r in rows:
            v = min(v, v ^ r)
        if v:
            rows.append(v)
    for i in range(len(rows)):
        p = rows[i].bit_length() - 1
        for j in range(len(rows)):
            if i != j and (rows[j] >> p) & 1:
                rows[j] ^= rows[i]
    return tuple(sorted(rows, reverse=True))

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    B = [int(s, 2) for s in data[2:2 + n]]
    X = int(data[2 + n], 2)
    V = canon(B)
    if len(V) != n:           # B nije linearno nezavisan -> nije minimalan
        print(0); return
    span = {0}
    for b in B:
        span |= {s ^ b for s in span}
    T = sorted(v for v in span if 1 <= v <= X)
    cnt = {(): 1}
    for e in T:
        new = dict(cnt)
        for key, c in cnt.items():
            k2 = canon(list(key) + [e])
            new[k2] = (new.get(k2, 0) + c) % MOD
        cnt = new
    print(cnt.get(V, 0) % MOD)

main()
