// L. Difficult Constructive Problem – DP po sufiksima + pohlepno slijeva, O(n)
// Fiksiramo posljednji znak (ako je '?', probamo oba). f[i][j] / g[i][j] = najmanji /
// najveći broj prijelaza u sufiksu i..n uz s_i = j. Uz fiksne krajeve sufiksa dostižni su
// točno svi brojevi između f i g s istim paritetom (paritet = s_i xor s_n), pa slijeva
// pohlepno stavljamo '0' kad god preostali k ostaje dostižan.
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

// vraća najmanji niz za zadani s (bez '?' na kraju) ili "" ako ne postoji
string solve(const string &s, int k) {
    int n = s.size();
    vector<array<int, 2>> f(n + 1), g(n + 1);
    auto ok = [&](int i, int j) { return s[i] == '?' || s[i] - '0' == j; };
    for (int j = 0; j < 2; j++) { f[n - 1][j] = ok(n - 1, j) ? 0 : INF; g[n - 1][j] = ok(n - 1, j) ? 0 : -INF; }
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j < 2; j++) {
            f[i][j] = INF; g[i][j] = -INF;
            if (!ok(i, j)) continue;
            for (int t = 0; t < 2; t++) {
                if (f[i + 1][t] < INF) f[i][j] = min(f[i][j], f[i + 1][t] + (j != t));
                if (g[i + 1][t] > -INF) g[i][j] = max(g[i][j], g[i + 1][t] + (j != t));
            }
        }
    string res(n, '0');
    int prev = -1;
    for (int i = 0; i < n; i++) {
        bool placed = false;
        for (int j = 0; j < 2 && !placed; j++) {
            if (!ok(i, j) || f[i][j] >= INF) continue;
            int cost = (prev != -1 && prev != j);
            int rem = k - cost;
            if (rem >= f[i][j] && rem <= g[i][j] && (rem - f[i][j]) % 2 == 0) {
                res[i] = '0' + j; k = rem; prev = j; placed = true;
            }
        }
        if (!placed) return "";
    }
    return res;
}

int main() {
    int T; scanf("%d", &T);
    static char buf[100005];
    while (T--) {
        int n, k; scanf("%d %d %s", &n, &k, buf);
        string s(buf), best = "";
        if (s[n - 1] != '?') best = solve(s, k);
        else
            for (char c : {'0', '1'}) {
                s[n - 1] = c;
                string r = solve(s, k);
                if (!r.empty() && (best.empty() || r < best)) best = r;
            }
        puts(best.empty() ? "Impossible" : best.c_str());
    }
    return 0;
}
