import sys
# Doslovni prijepis pseudokoda iz zadatka (valid/combine) i lijevo asocirano
# spajanje C_l, ..., C_{r-1} za svaki upit.

def valid(M, E, V, L, A, I):
    if min(L, A, I) < 0 or M <= max(L, A, I):
        return False
    if L == 0 and ((A + I) % M != 0 or A == I):
        return False
    expr = (A**3 - A*A*L + 3*A*A*I + E*A*L*L + L**3*V + 2*A*L*I + E*L*L*I + 3*A*I*I - L*I*I + I**3) % M
    # u tiskanom pseudokodu stoji "!= 0", ali primjer iz zadatka pokazuje da su
    # valjane upravo ćelije s vrijednošću 0 (točke na krivulji)
    return expr == 0

def combine(M, E, V, L0, A0, I0, L1, A1, I1):
    assert valid(M, E, V, L0, A0, I0) and valid(M, E, V, L1, A1, I1)
    if L1 == 0:
        return L0, A0, I0
    if L0 == 0:
        return L1, I1, A1
    B0 = (A0 + I0) * L1 % M; B1 = (I1 + A1) * L0 % M
    C0 = (A0 - I0) * L1 % M; C1 = (I1 - A1) * L0 % M
    if B0 == B1:
        if (C0 + C1) % M == 0:
            return 0, 3, M - 3
        Sum = (A0 + I0) % M; Dif = (A0 - I0) % M
        B = (3 * Sum * Sum + E * L0 * L0) % M
        C = 2 * Dif * L0 % M
        D = 2 * C * Sum * Dif % M
        Ee = (B * B - 2 * D) % M
        X = C * Ee % M
        Y = (B * (D - Ee) - 2 * C * C * Dif * Dif) % M
        return 2 * C**3 % M, (X + Y) % M, (X - Y) % M
    B = (B0 - B1) % M; C = (C0 - C1) % M; D = L0 * L1 % M
    Ee = (C * C * D - B * B * (B0 + B1)) % M
    X = B * Ee % M
    Y = (C * (B0 * B * B - Ee) - C0 * B**3) % M
    return 2 * B**3 * D % M, (X + Y) % M, (X - Y) % M

def main():
    data = sys.stdin.read().split(); p = 0
    M, E, V = int(data[0]), int(data[1]), int(data[2]); p = 3
    n = int(data[p]); p += 1
    cells = []
    for _ in range(n):
        cells.append((int(data[p]), int(data[p + 1]), int(data[p + 2]))); p += 3
    q = int(data[p]); p += 1
    out = []
    for _ in range(q):
        t = int(data[p]); p += 1
        if t == 1:
            i = int(data[p]); cells[i] = (int(data[p + 1]), int(data[p + 2]), int(data[p + 3])); p += 4
        else:
            l, r = int(data[p]), int(data[p + 1]); p += 2
            R = cells[l]
            for i in range(l + 1, r):
                R = combine(M, E, V, *R, *cells[i])
            L, A, I = R
            if L == 0:
                out.append(-1)
            else:
                out.append(A * I % M * pow(L * L % M, M - 2, M) % M)
    print('\n'.join(map(str, out)))

main()
