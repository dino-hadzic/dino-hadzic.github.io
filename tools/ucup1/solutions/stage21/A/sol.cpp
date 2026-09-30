// A. Colorful Segments – DP po blokovima iste boje + dva segmentna stabla, O(n log n)
// Sortiramo po desnom kraju. Odabrane segmente poredane po r dijelimo na maksimalne blokove
// iste boje. f(i) = broj odabira u kojima je segment i posljednji (po r) u odabiru.
// Prijelaz: j = posljednji odabrani segment suprotne boje (r_j < l_i, ili j = 0 virtualni);
// segmenti boje c_i s indeksom između j i i i l > r_j biraju se slobodno (svaki 2 mogućnosti).
// Stablo boje x čuva na poziciji j vrijednost f(j) * 2^(broj već obrađenih segmenata boje 1-x
// koji su iza j i ne sijeku j); obrada i: upit prefiksa [0,p_i] u stablu boje 1-c_i,
// zatim pomnoži taj prefiks s 2, pa upiši f(i) u stablo boje c_i.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;

struct SegTree {
    int n; vector<ll> s, lz;
    void init(int n_) { n = n_; s.assign(4 * n + 4, 0); lz.assign(4 * n + 4, 1); }
    void apply(int x, ll m) { s[x] = s[x] * m % MOD; lz[x] = lz[x] * m % MOD; }
    void push(int x) { if (lz[x] != 1) { apply(2 * x, lz[x]); apply(2 * x + 1, lz[x]); lz[x] = 1; } }
    void set(int x, int l, int r, int p, ll v) {
        if (l == r) { s[x] = v; return; }
        push(x); int m = (l + r) / 2;
        if (p <= m) set(2 * x, l, m, p, v); else set(2 * x + 1, m + 1, r, p, v);
        s[x] = (s[2 * x] + s[2 * x + 1]) % MOD;
    }
    void mul(int x, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) { apply(x, 2); return; }
        push(x); int m = (l + r) / 2;
        mul(2 * x, l, m, ql, qr); mul(2 * x + 1, m + 1, r, ql, qr);
        s[x] = (s[2 * x] + s[2 * x + 1]) % MOD;
    }
    ll sum(int x, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return s[x];
        push(x); int m = (l + r) / 2;
        return (sum(2 * x, l, m, ql, qr) + sum(2 * x + 1, m + 1, r, ql, qr)) % MOD;
    }
};

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        vector<array<int, 3>> seg(n);
        for (auto &s : seg) scanf("%d %d %d", &s[1], &s[0], &s[2]);   // (r, l, c) radi sortiranja po r
        sort(seg.begin(), seg.end());
        vector<int> rs(n);
        for (int i = 0; i < n; i++) rs[i] = seg[i][0];
        SegTree t[2];
        for (int c = 0; c < 2; c++) { t[c].init(n + 1); t[c].set(1, 0, n, 0, 1); }   // pozicija 0 = virtualni početak
        ll ans = 1;                                                    // prazan odabir
        for (int i = 1; i <= n; i++) {
            int l = seg[i - 1][1], c = seg[i - 1][2];
            int p = lower_bound(rs.begin(), rs.end(), l) - rs.begin(); // segmenti s r < l: pozicije 1..p
            ll f = t[1 - c].sum(1, 0, n, 0, p);
            t[1 - c].mul(1, 0, n, 0, p);                              // i je slobodan za sve te j
            t[c].set(1, 0, n, i, f);
            ans = (ans + f) % MOD;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
