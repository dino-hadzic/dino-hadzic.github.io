// UCup 1, Stage 18, D: Computational Geometry
// Dijametar konveksnog poligona = najveća udaljenost dvaju vrhova. Za sve lukove
// vrhova i..j računamo f(i,j) = max(f(i+1,j), f(i,j-1), |P_i P_j|^2) (intervalno DP),
// a za komplementarne lukove analogno g(i,j). Odgovor je min f(i,j)+g(i,j) po
// dijagonalama koje dijele poligon na dva dijela pozitivne površine.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n;
        if (scanf("%d", &n) != 1) return 0;
        vector<ll> x(n), y(n);
        for (int i = 0; i < n; i++) if (scanf("%lld %lld", &x[i], &y[i]) != 2) return 0;
        auto d2 = [&](int i, int j) {
            ll dx = x[i] - x[j], dy = y[i] - y[j];
            return (ull)(dx * dx) + (ull)(dy * dy);
        };
        auto cross = [&](int o, int a, int b) {  // (P_a - P_o) x (P_b - P_o)
            return (x[a] - x[o]) * (y[b] - y[o]) - (y[a] - y[o]) * (x[b] - x[o]);
        };
        // tab[i][j] (i<j): f(i,j) = dijametar^2 poligona s vrhovima i, i+1, ..., j
        // tab[j][i] (i<j): g(i,j) = dijametar^2 poligona s vrhovima j, j+1, ..., n-1, 0, ..., i
        vector<vector<ull>> tab(n, vector<ull>(n, 0));
        for (int len = 1; len < n; len++)
            for (int i = 0; i + len < n; i++) {
                int j = i + len;
                ull v = d2(i, j);
                if (len >= 2) v = max({v, tab[i + 1][j], tab[i][j - 1]});
                tab[i][j] = v;
            }
        for (int len = n - 1; len >= 1; len--)
            for (int i = 0; i + len < n; i++) {
                int j = i + len;
                ull v = d2(i, j);
                // izbacimo vrh i: ostaje {0..i-1} u {j..n-1}; za i = 0 to je luk j..n-1
                if (i > 0) v = max(v, tab[j][i - 1]);
                else if (j < n - 1) v = max(v, tab[j][n - 1]);
                // izbacimo vrh j: ostaje {0..i} u {j+1..n-1}; za j = n-1 to je luk 0..i
                if (j < n - 1) v = max(v, tab[j + 1][i]);
                else if (i > 0) v = max(v, tab[0][i]);
                tab[j][i] = v;
            }
        ull best = ULLONG_MAX;
        for (int i = 0; i < n; i++)
            for (int j = i + 2; j < n; j++) {
                if (n - (j - i) < 2) continue;              // drugi dio ima < 3 vrha
                if (cross(i, i + 1, j) == 0) continue;      // dio i..j je degeneriran
                if (cross(j, (j + 1) % n, i) == 0) continue;  // dio j..i je degeneriran
                best = min(best, tab[i][j] + tab[j][i]);
            }
        printf("%llu\n", best);
    }
    return 0;
}
