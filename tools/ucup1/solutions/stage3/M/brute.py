# Brute force: probamo sve 2^k nizove T/N i simuliramo susrete unaprijed.
import sys
def main():
    d = sys.stdin.read().split(); p = 0
    z = int(d[p]); p += 1
    out = []
    for _ in range(z):
        n, k = int(d[p]), int(d[p+1]); p += 2
        ab = []
        for i in range(k):
            ab.append((int(d[p]), int(d[p+1]))); p += 2
        s = int(d[p]); p += 1
        en = [int(x) for x in d[p:p+s]]; p += s
        found = None
        for mask in range(1 << k):
            alive = [True] * (n + 1)
            for i, (a, b) in enumerate(ab):
                if (mask >> i) & 1 and alive[a] and alive[b]:
                    alive[b] = False
            if all(not alive[e] for e in en):
                found = ''.join('T' if (mask >> i) & 1 else 'N' for i in range(k))
                break
        if found is None: out.append("NIE")
        else: out.append("TAK"); out.append(found)
    print('\n'.join(out))
main()
