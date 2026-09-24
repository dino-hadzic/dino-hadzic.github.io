// UCup 1, Stage 15 (ZJCPC 2023), L. Barkley
// Za svaki l čuvamo točke promjene prefiksnog gcd-a g(l, *) (najviše ~60).
// Rekurzija po najljevijem izbačenom elementu x: u bloku konstantnog g(l, x-1) isplati se
// izbaciti najdešnji x. Preostalih k-1 izbačaja rješavamo rekurzivno, prenoseći dosad
// nakupljeni gcd; k = 0 je upit na sparse tablici.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

// binarni gcd, brži od Euklida za 64-bitne brojeve
ull bgcd(ull a, ull b) {
    if (!a) return b;
    if (!b) return a;
    int s = __builtin_ctzll(a | b);
    a >>= __builtin_ctzll(a);
    while (b) {
        b >>= __builtin_ctzll(b);
        if (a > b) swap(a, b);
        b -= a;
    }
    return a << s;
}

int n, q;
vector<ull> a;
vector<vector<ull>> sp;   // sparse tablica gcd-a
vector<int> lg;
vector<vector<pair<int, ull>>> chg;  // chg[l] = (pozicija t, g(l, t)) na mjestima gdje g(l, *) pada

ull rangeGcd(int l, int r) {  // gcd a[l..r], 0 za prazan interval
    if (l > r) return 0;
    int k = lg[r - l + 1];
    return bgcd(sp[k][l], sp[k][r - (1 << k) + 1]);
}

// najveći gcd(cur, zadržani) nakon izbacivanja točno k elemenata iz [l, r]  (k <= r - l)
// cur = gcd svega što je već zadržano lijevo od l (mora se prenositi: gcd nije monoton u max-u!)
ull solve(int l, int r, int k, ull cur) {
    if (k == 0) return bgcd(cur, rangeGcd(l, r));
    int lastX = r - k + 1;                      // najdešnja dopuštena pozicija najljevijeg izbačaja
    ull best = solve(l + 1, r, k - 1, cur);     // x = l: prefiks prazan
    const auto &c = chg[l];
    for (size_t i = 0; i < c.size() && c[i].first <= r; ++i) {
        // blok x-1 ∈ [t_i, t_{i+1}-1] ima g(l, x-1) = v_i; kandidat x = min(t_{i+1}, lastX)
        int x = (i + 1 < c.size()) ? min(c[i + 1].first, lastX) : lastX;
        if (x < c[i].first + 1) continue;
        best = max(best, solve(x + 1, r, k - 1, bgcd(cur, c[i].second)));
    }
    return best;
}

int main() {
    scanf("%d %d", &n, &q);
    a.resize(n + 2);
    for (int i = 1; i <= n; ++i) scanf("%llu", &a[i]);
    lg.assign(n + 2, 0);
    for (int i = 2; i <= n + 1; ++i) lg[i] = lg[i / 2] + 1;
    int LOG = lg[n] + 1;
    sp.assign(LOG, vector<ull>(n + 2, 0));
    for (int i = 1; i <= n; ++i) sp[0][i] = a[i];
    for (int k = 1; k < LOG; ++k)
        for (int i = 1; i + (1 << k) - 1 <= n; ++i)
            sp[k][i] = bgcd(sp[k - 1][i], sp[k - 1][i + (1 << (k - 1))]);
    // točke promjene prefiksnog gcd-a, zdesna nalijevo: g(l, t) = gcd(a_l, g(l+1, t))
    chg.assign(n + 2, {});
    for (int l = n; l >= 1; --l) {
        auto &c = chg[l];
        c.push_back({l, a[l]});
        for (auto [t, v] : chg[l + 1]) {
            ull g = bgcd(a[l], v);
            if (g != c.back().second) c.push_back({t, g});
        }
    }
    while (q--) {
        int l, r, k;
        scanf("%d %d %d", &l, &r, &k);
        printf("%llu\n", solve(l, r, k, 0));
    }
    return 0;
}
