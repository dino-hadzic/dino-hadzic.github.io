// UCup 1, Stage 16, zadatak E: Classical FFT Problem
// Kao u zadatku D: r = k (stranica najveceg kvadrata), a broj rasporeda je
//   W(a, t) + W(b, t') - k!,
// gdje je W(a, t) broj nacina da se u svaki od k redaka sirina a_1 >= ... >= a_k
// stavi top tako da svaki od prvih t stupaca dobije topa. Ukljucivanjem-iskljucivanjem
//   W(a, t) = sum_{p=0}^{t} (-1)^p C(t, p) f(p),   f(x) = prod_i (a_i - x).
// Koeficijente f racunamo podijeli-pa-vladaj mnozenjem (NTT), a f(0..t)
// multipoint evaluacijom (stablo podprodukata + polinomski ostatak): O(n log^2 n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> Poly;

const ll MOD = 998244353, G = 3;

static ll pw(ll b, ll e) {
    ll r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

// ---------- NTT ----------
static void ntt(vector<ll>& a, bool inv) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll w = pw(G, (MOD - 1) / len);
        if (inv) w = pw(w, MOD - 2);
        static vector<ll> ws;
        ws.assign(len / 2, 1);
        for (int i = 1; i < len / 2; ++i) ws[i] = ws[i - 1] * w % MOD;
        for (int i = 0; i < n; i += len)
            for (int j = 0; j < len / 2; ++j) {
                ll u = a[i + j], v = a[i + j + len / 2] * ws[j] % MOD;
                a[i + j] = u + v < MOD ? u + v : u + v - MOD;
                a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + MOD;
            }
    }
    if (inv) {
        ll ni = pw(n, MOD - 2);
        for (ll& x : a) x = x * ni % MOD;
    }
}

static Poly mul(Poly a, Poly b) {
    if (a.empty() || b.empty()) return {};
    int need = a.size() + b.size() - 1;
    if (min(a.size(), b.size()) <= 32) {  // mali slucajevi: naivno
        Poly c(need, 0);
        for (size_t i = 0; i < a.size(); ++i)
            for (size_t j = 0; j < b.size(); ++j)
                c[i + j] = (c[i + j] + a[i] * b[j]) % MOD;
        return c;
    }
    int n = 1;
    while (n < need) n <<= 1;
    a.resize(n); b.resize(n);
    ntt(a, false); ntt(b, false);
    for (int i = 0; i < n; ++i) a[i] = a[i] * b[i] % MOD;
    ntt(a, true);
    a.resize(need);
    return a;
}

// inverz reda polinoma modulo x^n (Newtonova iteracija)
static Poly inverse(const Poly& a, int n) {
    Poly r = {pw(a[0], MOD - 2)};
    for (int len = 1; len < n; len <<= 1) {
        Poly t(a.begin(), a.begin() + min<int>(a.size(), 2 * len));
        Poly rt = mul(r, t);            // r * a
        rt.resize(2 * len);
        for (ll& x : rt) x = (MOD - x) % MOD;
        rt[0] = (rt[0] + 2) % MOD;      // 2 - r*a
        r = mul(r, rt);
        r.resize(2 * len);
    }
    r.resize(n);
    return r;
}

// ostatak f mod g (deg g >= 1, vodeci koeficijent g != 0)
static Poly rem(const Poly& f, const Poly& g) {
    int n = f.size(), m = g.size();
    if (n < m) return f;
    Poly rf(f.rbegin(), f.rend()), rg(g.rbegin(), g.rend());
    int qd = n - m + 1;
    rf.resize(qd);
    Poly q = mul(rf, inverse(rg, qd));
    q.resize(qd);
    reverse(q.begin(), q.end());  // kvocijent
    Poly qg = mul(q, g);
    Poly r(m - 1);
    for (int i = 0; i < m - 1; ++i) r[i] = (f[i] - qg[i] + MOD) % MOD;
    while (!r.empty() && r.back() == 0) r.pop_back();
    if (r.empty()) r.push_back(0);
    return r;
}

// ---------- multipoint evaluacija ----------
struct Multipoint {
    vector<Poly> tree;   // tree[v] = prod (x - p) po tockama u cvoru v
    vector<ll> pts, vals;
    void build(int v, int l, int r) {
        if (l == r) { tree[v] = {(MOD - pts[l]) % MOD, 1}; return; }
        int m = (l + r) / 2;
        build(2 * v, l, m); build(2 * v + 1, m + 1, r);
        tree[v] = mul(tree[2 * v], tree[2 * v + 1]);
    }
    void eval(int v, int l, int r, const Poly& f) {
        Poly g = ((int)f.size() >= (int)tree[v].size()) ? rem(f, tree[v]) : f;
        if (l == r) { vals[l] = g.empty() ? 0 : g[0]; return; }
        int m = (l + r) / 2;
        eval(2 * v, l, m, g); eval(2 * v + 1, m + 1, r, g);
    }
    vector<ll> run(const Poly& f, const vector<ll>& points) {
        pts = points; int n = pts.size();
        tree.assign(4 * n, {}); vals.assign(n, 0);
        build(1, 0, n - 1);
        eval(1, 0, n - 1, f);
        return vals;
    }
};

// f(x) = prod_i (a_i - x), koeficijenti podijeli-pa-vladaj mnozenjem
static Poly produkt(const vector<int>& a, int l, int r) {
    if (l == r) return {a[l] % MOD, MOD - 1};
    int m = (l + r) / 2;
    return mul(produkt(a, l, m), produkt(a, m + 1, r));
}

static vector<ll> fakt, ifakt;
static ll C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fakt[n] * ifakt[k] % MOD * ifakt[n - k] % MOD;
}

// W(a, t) = sum_{p=0}^t (-1)^p C(t, p) prod_i (a_i - p), a ima k clanova
static ll W(const vector<int>& a, int k, int t) {
    vector<int> rows(a.begin(), a.begin() + k);
    Poly f = produkt(rows, 0, k - 1);
    vector<ll> pts(t + 1);
    for (int p = 0; p <= t; ++p) pts[p] = p;
    vector<ll> v = Multipoint().run(f, pts);
    ll res = 0;
    for (int p = 0; p <= t; ++p) {
        ll term = C(t, p) * v[p] % MOD;
        res = (p & 1) ? (res - term + MOD) % MOD : (res + term) % MOD;
    }
    return res;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<int> a(n);
    for (int& v : a) scanf("%d", &v);
    reverse(a.begin(), a.end());  // a_0 >= a_1 >= ... >= a_{n-1}

    fakt.assign(n + 2, 1); ifakt.assign(n + 2, 1);
    for (int i = 1; i <= n + 1; ++i) fakt[i] = fakt[i - 1] * i % MOD;
    ifakt[n + 1] = pw(fakt[n + 1], MOD - 2);
    for (int i = n + 1; i > 0; --i) ifakt[i - 1] = ifakt[i] * i % MOD;

    int k = 0;
    while (k < n && a[k] >= k + 1) ++k;
    int t = (k < n) ? a[k] : 0;

    vector<int> b(n);  // transponirani dijagram
    for (int j = 0, c = n; j < n; ++j) {
        while (c > 0 && a[c - 1] < j + 1) --c;
        b[j] = c;
    }
    int t2 = (k < n) ? b[k] : 0;

    ll w = (W(a, k, t) + W(b, k, t2) - fakt[k] + MOD) % MOD;
    printf("%d %lld\n", k, w);
    return 0;
}
