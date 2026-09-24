// G - Range NEQ
// Ukljucivanje-iskljucivanje po blokovima: f(x) = sum_k (-1)^k C(M,k) M!/(M-k)! x^k,
// odgovor = sum_s [x^s] f(x)^N * (NM - s)!.
// f^N racunamo NTT-om: transformiramo f u velicini >= NM+1, potenciramo po
// tockama (nema "omatanja" jer je deg f^N = NM < velicina) i vratimo.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

// iterativni NTT (korijen 3 za 998244353)
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

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int total = n * m;
    vector<ll> fact(total + 1), inv(total + 1);
    fact[0] = 1;
    for (int i = 1; i <= total; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[total] = power(fact[total], MOD - 2);
    for (int i = total; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    auto C = [&](int a, int b) { return fact[a] * inv[b] % MOD * inv[a - b] % MOD; };

    int sz = 1;
    while (sz < total + 1) sz <<= 1;
    vector<ll> f(sz, 0);
    for (int k = 0; k <= m; k++) {
        // biramo k pozicija u bloku i injektivno im dodjeljujemo vrijednosti bloka
        ll v = C(m, k) * fact[m] % MOD * inv[m - k] % MOD;
        f[k] = (k & 1) ? (MOD - v) % MOD : v;
    }
    ntt(f, false);
    for (auto &x : f) x = power(x, n);  // f^N po tockama
    ntt(f, true);
    ll ans = 0;
    for (int s = 0; s <= total; s++) ans = (ans + f[s] * fact[total - s]) % MOD;
    printf("%lld\n", ans);
}
