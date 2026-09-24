// UCup 1, Stage 20 (India), G. Perfect Strings
// String je savrsen <=> redukcija stogom (pop kad je znak jednak vrhu) zavrsi praznim stogom.
// Rastav po prvom povratku stoga na prazno daje funkcije izvodnice
//   G(x) = 1 + (c-1) x G(x)^2   (blokovi s fiksnim vanjskim slovom),  F(x) = 1 / (1 - c x G(x)).
// Sredjivanjem:  F(x) = ((2-c) + c*sqrt(1-4(c-1)x)) / (2(1-c^2 x)),  a iz toga
//   f(n) = c^{2n} - sum_{k=1..n} Cat(k-1) (c-1)^k c^{2n-2k+1}   (mod 1e9+7).
// Cat(k) racunamo iterativno: Cat(k) = Cat(k-1) * 2(2k-1) / (k+1), uz linearno predracunate inverze.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007LL;
const int MAXN = 10000002;

ll mpow(ll b, ll e) {
    ll r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

int main() {
    // inv[i] = i^{-1} mod p, linearno: inv[i] = -(p / i) * inv[p % i]
    vector<int> inv(MAXN);
    inv[1] = 1;
    for (int i = 2; i < MAXN; i++) inv[i] = (int)((MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD);

    int t;
    scanf("%d", &t);
    while (t--) {
        ll n, c;
        scanf("%lld %lld", &n, &c);
        ll cn = mpow(c, 2 * n);
        ll invc2 = mpow(mpow(c, 2), MOD - 2);
        ll term = (c - 1) % MOD * mpow(c, 2 * n - 1) % MOD;   // (c-1)^1 * c^{2n-1}
        ll cat = 1;                                            // Cat(0)
        ll sum = 0;
        for (ll k = 1; k <= n; k++) {
            sum = (sum + cat * term) % MOD;
            // priprema za k+1: Cat(k) = Cat(k-1) * 2(2k-1)/(k+1),  term *= (c-1)/c^2
            cat = cat * (2 * (2 * k - 1) % MOD) % MOD * inv[k + 1] % MOD;
            term = term * ((c - 1) % MOD) % MOD * invc2 % MOD;
        }
        printf("%lld\n", ((cn - sum) % MOD + MOD) % MOD);
    }
    return 0;
}
