// C. LaLa and Lamp
// Ćelija (i, j) leži na retku i, stupcu j i dijagonali i-j. Nad GF(2) tražimo
// r_i + c_j + d_{i-j} = s_{ij}. Fiksiramo r_{N-1}, r_{N-2} i c_0 (8 kombinacija);
// sve ostalo je tada jednoznačno određeno pa samo provjerimo cijelu mrežu.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<string> s(n);
    static char tmp[2100];
    for (int i = 0; i < n; i++) { scanf("%s", tmp); s[i] = tmp; }

    vector<int> r(n), c(n), d(n);
    for (int mask = 0; mask < 8; mask++) {
        r[n - 1] = mask & 1;
        r[n - 2] = (mask >> 1) & 1;
        c[0] = (mask >> 2) & 1;
        // a_j = c_j + d_{n-1-j} (iz zadnjeg retka), b_j = c_j + d_{n-2-j} (iz predzadnjeg)
        // => d_{n-1-j} + d_{n-2-j} = a_j + b_j, a d_{n-1} = a_0 + c_0.
        d[n - 1] = (s[n - 1][0] - '0') ^ r[n - 1] ^ c[0];
        for (int j = 0; j + 1 <= n - 1; j++) {
            int a = (s[n - 1][j] - '0') ^ r[n - 1];
            int b = (s[n - 2][j] - '0') ^ r[n - 2];
            d[n - 2 - j] = d[n - 1 - j] ^ a ^ b;
        }
        for (int j = 0; j < n; j++) c[j] = (s[n - 1][j] - '0') ^ r[n - 1] ^ d[n - 1 - j];
        for (int i = 0; i < n; i++) r[i] = (s[i][0] - '0') ^ c[0] ^ d[i];
        bool ok = true;
        for (int i = 0; i < n && ok; i++)
            for (int j = 0; j <= i; j++)
                if ((r[i] ^ c[j] ^ d[i - j]) != (s[i][j] - '0')) { ok = false; break; }
        if (ok) { puts("Yes"); return 0; }
    }
    puts("No");
    return 0;
}
