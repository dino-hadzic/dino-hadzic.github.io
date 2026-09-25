# Sporo rješenje: isprobaj sve parove (a, b).
import sys
def digits(x, b):
    d = []
    while x:
        d.append(x % b); x //= b
    return d
def main():
    data = sys.stdin.read().split()
    T = int(data[0]); p = 1
    out = []
    for _ in range(T):
        x, y, A, B = map(int, data[p:p + 4]); p += 4
        res = None
        for a in range(2, A + 1):
            da = digits(x, a)
            for b in range(2, B + 1):
                if da == digits(y, b):
                    res = (a, b); break
            if res: break
        if res:
            out.append("YES"); out.append(f"{res[0]} {res[1]}")
        else:
            out.append("NO")
    print("\n".join(out))
main()
