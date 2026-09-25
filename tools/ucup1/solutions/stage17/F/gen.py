import random, sys
seed = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'small'
random.seed(seed)
def perm_close(n):
    # permutacija u kojoj su i, i+1 cesto blizu: lokalna mijesanja identitete
    p = list(range(1, n + 1))
    for _ in range(random.randint(0, n)):
        i = random.randint(0, n - 2)
        p[i], p[i + 1] = p[i + 1], p[i]
    return p
if mode == 'small':
    T = random.randint(1, 6)
    out = [str(T)]
    for _ in range(T):
        n = random.randint(2, 7)
        if random.random() < 0.5:
            p = perm_close(n)
        else:
            p = list(range(1, n + 1)); random.shuffle(p)
        out.append(str(n)); out.append(" ".join(map(str, p)))
else:
    out = ["1", "400000", " ".join(map(str, perm_close(400000)))]
print("\n".join(out))
