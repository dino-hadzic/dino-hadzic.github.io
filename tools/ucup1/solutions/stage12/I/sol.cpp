// I - Peaceful Results
// Nerijesena runda je RRR/PPP/SSS (a_1,a_2,a_3), "ciklicka" (R,P,S),(P,S,R),(S,R,P)
// (b_1,b_2,b_3) ili "anticiklicka" (R,S,P),(P,R,S),(S,P,R) (c_1,c_2,c_3).
// Iz razlika D1 = A - B i D2 = A - C jednoznacno slijede b_2-b_1, b_3-b_1,
// c_2-c_1, c_3-c_1 (nazivnik 3); slobodni su s = b_1 i t = c_1, a
// a_j = alpha_j - s - t. Odgovor je N! * sum_u H(u) * (F*G)(u), konvolucija NTT-om.
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

int main() {
    ll N, AR, AP, AS, BR, BP, BS, CR, CP, CS;
    scanf("%lld", &N);
    scanf("%lld %lld %lld", &AR, &AP, &AS);
    scanf("%lld %lld %lld", &BR, &BP, &BS);
    scanf("%lld %lld %lld", &CR, &CP, &CS);
    ll D1R = AR - BR, D1P = AP - BP, D2R = AR - CR, D2P = AP - CP;
    // brojnici razlika (moraju biti djeljivi s 3)
    ll nb2 = 2 * D1P + D1R - D2P - 2 * D2R;
    ll nb3 = D1P - D1R - 2 * D2P - D2R;
    ll nc2 = -(D1P + 2 * D1R - 2 * D2P - D2R);
    ll nc3 = -(2 * D1P + D1R - D2P + D2R);
    auto div3 = [](ll x) { return ((x % 3) + 3) % 3 == 0; };
    if (!div3(nb2) || !div3(nb3) || !div3(nc2) || !div3(nc3)) { puts("0"); return 0; }
    ll beta2 = nb2 / 3, beta3 = nb3 / 3, gamma2 = nc2 / 3, gamma3 = nc3 / 3;
    // a = (alpha1 - u, alpha2 - u, alpha3 - u), u = s + t
    ll alpha1 = AR, alpha2 = AP - beta2 - gamma2, alpha3 = AS - beta3 - gamma3;
    ll umax = min({alpha1, alpha2, alpha3});
    if (umax < 0) { puts("0"); return 0; }
    ll smin = max({0LL, -beta2, -beta3}), tmin = max({0LL, -gamma2, -gamma3});
    if (smin + tmin > umax) { puts("0"); return 0; }

    int F = N + 1;
    vector<ll> fact(F), inv(F);
    fact[0] = 1;
    for (int i = 1; i < F; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[F - 1] = power(fact[F - 1], MOD - 2);
    for (int i = F - 1; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    // Fs[s] = 1/(s!(s+beta2)!(s+beta3)!), Gt[t] analogno, Hu[u] = 1/prod (alpha_j-u)!
    int L = umax + 1;
    int sz = 1;
    while (sz < 2 * L) sz <<= 1;
    vector<ll> Fs(sz, 0), Gt(sz, 0);
    // s <= umax - tmin (i t <= umax - smin) jamci da su svi indeksi <= N
    for (ll s = smin; s <= umax - tmin; s++)
        Fs[s] = inv[s] * inv[s + beta2] % MOD * inv[s + beta3] % MOD;
    for (ll t = tmin; t <= umax - smin; t++)
        Gt[t] = inv[t] * inv[t + gamma2] % MOD * inv[t + gamma3] % MOD;
    ntt(Fs, false); ntt(Gt, false);
    for (int i = 0; i < sz; i++) Fs[i] = Fs[i] * Gt[i] % MOD;
    ntt(Fs, true);
    ll ans = 0;
    for (ll u = 0; u <= umax; u++) {
        ll H = inv[alpha1 - u] * inv[alpha2 - u] % MOD * inv[alpha3 - u] % MOD;
        ans = (ans + Fs[u] * H) % MOD;
    }
    ans = ans * fact[N] % MOD;
    printf("%lld\n", ans);
}
