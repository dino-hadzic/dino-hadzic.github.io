// L - Many Products
// prod (x + A_i) = sum_k B_k x^k  (kao polinom u jednoj varijabli x, jer
// je zbroj po svim rastavima simetrican u x_1..x_N). Odgovor je
// sum_k B_k * S_k(M), gdje je S_k(M) = sum_{x1...xN=M} x1...xk multiplikativna
// funkcija; za p^e vrijedi
//   S_k(p^e) = sum_d p^d C(d+k-1, k-1) C(e-d+N-k-1, N-k-1).
// B_k racunamo umnoskom polinoma "podijeli pa vladaj" uz NTT.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1; b %= MOD; if (b < 0) b += MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

void ntt(vector<ll> &a, bool inv) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll w = power(3, (MOD - 1) / len);
        if (inv) w = power(w, MOD - 2);
        vector<ll> ws(len / 2);
        ws[0] = 1;
        for (int i = 1; i < len / 2; i++) ws[i] = ws[i - 1] * w % MOD;
        for (int i = 0; i < n; i += len)
            for (int j = 0; j < len / 2; j++) {
                ll u = a[i + j], v = a[i + j + len / 2] * ws[j] % MOD;
                a[i + j] = u + v < MOD ? u + v : u + v - MOD;
                a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + MOD;
            }
    }
    if (inv) {
        ll ni = power(n, MOD - 2);
        for (auto &x : a) x = x * ni % MOD;
    }
}

vector<ll> multiply(vector<ll> a, vector<ll> b) {
    int need = a.size() + b.size() - 1;
    if (min(a.size(), b.size()) <= 32) {  // mali slucajevi: naivno
        vector<ll> c(need, 0);
        for (size_t i = 0; i < a.size(); i++)
            for (size_t j = 0; j < b.size(); j++) c[i + j] = (c[i + j] + a[i] * b[j]) % MOD;
        return c;
    }
    int sz = 1;
    while (sz < need) sz <<= 1;
    a.resize(sz); b.resize(sz);
    ntt(a, false); ntt(b, false);
    for (int i = 0; i < sz; i++) a[i] = a[i] * b[i] % MOD;
    ntt(a, true);
    a.resize(need);
    return a;
}

vector<ll> A;
vector<ll> prodRange(int l, int r) {  // prod_{i in [l,r)} (x + A_i)
    if (r - l == 1) return {A[l] % MOD, 1};
    int m = (l + r) / 2;
    return multiply(prodRange(l, m), prodRange(m, r));
}

int main() {
    int n;
    ll M;
    scanf("%d %lld", &n, &M);
    A.resize(n);
    for (auto &x : A) scanf("%lld", &x);
    vector<ll> B = prodRange(0, n);  // B[k], k = 0..n

    // faktorizacija M (M <= 1e12: dijeljenje do 1e6)
    vector<pair<ll, int>> pf;
    for (ll p = 2; p * p <= M; p++)
        if (M % p == 0) {
            int e = 0;
            while (M % p == 0) { M /= p; e++; }
            pf.push_back({p, e});
        }
    if (M > 1) pf.push_back({M, 1});

    int maxE = 0;
    for (auto &pe : pf) maxE = max(maxE, pe.second);
    int F = n + maxE + 5;
    vector<ll> fact(F), inv(F);
    fact[0] = 1;
    for (int i = 1; i < F; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[F - 1] = power(fact[F - 1], MOD - 2);
    for (int i = F - 1; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    auto C = [&](int a, int b) -> ll {
        if (b < 0 || a < b) return 0;
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD;
    };

    ll ans = 0;
    for (int k = 0; k <= n; k++) {
        ll S = 1;  // S_k(M) = prod po prostim faktorima
        for (auto &pe : pf) {
            ll p = pe.first % MOD;
            int e = pe.second;
            ll s = 0, pd = 1;  // pd = p^d
            for (int d = 0; d <= e; d++) {
                // d = ukupan eksponent p na prvih k mjesta, e-d na preostalih N-k
                ll ways1 = (k == 0) ? (d == 0 ? 1 : 0) : C(d + k - 1, k - 1);
                ll ways2 = (k == n) ? (d == e ? 1 : 0) : C(e - d + n - k - 1, n - k - 1);
                s = (s + pd * ways1 % MOD * ways2) % MOD;
                pd = pd * p % MOD;
            }
            S = S * s % MOD;
        }
        ans = (ans + B[k] * S) % MOD;
    }
    printf("%lld\n", ans);
}
