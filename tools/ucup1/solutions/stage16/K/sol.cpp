// UCup 1, Stage 16, zadatak K: Classical Summation Problem
// Prijatelji biraju donji medijan sortiranih gradova. Racunamo ocekivanje uz uniformno
// slucajne gradove i mnozimo s n^k.
//  - k neparan: medijan je simetrican oko sredine, E = (n+1)/2.
//  - k paran: E(a_{k/2}) = E(sredina dvaju medijana) - E(razmak)/2 = (n+1)/2 - E(d)/2,
//    a E(d) = sum_i P(rez izmedu i i i+1 lezi izmedu medijana)
//           = sum_{i=1}^{n-1} C(k,k/2) i^{k/2} (n-i)^{k/2} / n^k.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;

ll potencija(ll b, ll e) {
    ll r = 1; b %= MOD;
    while (e > 0) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD; e >>= 1;
    }
    return r;
}

int main() {
    ll n, k;
    if (scanf("%lld %lld", &n, &k) != 2) return 0;
    ll inv2 = potencija(2, MOD - 2);
    ll nk = potencija(n, k);
    ll ans = (n + 1) % MOD * inv2 % MOD * nk % MOD;  // (n+1)/2 * n^k
    if (k % 2 == 0) {
        // C(k, k/2) preko faktorijela
        vector<ll> f(k + 1);
        f[0] = 1;
        for (ll i = 1; i <= k; ++i) f[i] = f[i - 1] * i % MOD;
        ll binom = f[k] * potencija(f[k / 2], MOD - 2) % MOD * potencija(f[k / 2], MOD - 2) % MOD;
        ll suma = 0;  // sum_i i^{k/2} (n-i)^{k/2}
        for (ll i = 1; i < n; ++i) suma = (suma + potencija(i, k / 2) * potencija(n - i, k / 2)) % MOD;
        // oduzmi n^k * E(d)/2 = C(k,k/2)/2 * suma
        ans = (ans - binom * inv2 % MOD * suma % MOD + MOD) % MOD;
    }
    printf("%lld\n", ans);
    return 0;
}
