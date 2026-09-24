# Sporo rješenje: izravno zbrajanje m(x) za x = 1..n.
import sys
def mode(x):
    s = str(x)
    cnt = [s.count(chr(48 + d)) for d in range(10)]
    best = 0
    for d in range(10):
        if cnt[d] >= cnt[best]:
            best = d
    return best
def main():
    data = sys.stdin.read().split()
    T = int(data[0])
    out = []
    for i in range(1, T + 1):
        n = int(data[i])
        out.append(str(sum(mode(x) for x in range(1, n + 1)) % (10**9 + 7)))
    print("\n".join(out))
main()
