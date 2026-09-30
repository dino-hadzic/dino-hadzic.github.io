// H. Funkcija
// f(x) ovisi samo o m = floor(n / x):  g(m) = 1 + sum_{k=2}^{min(m,A)} g(floor(m/k)),
// g(0) = 0, A = 20210926.  Sve potrebne vrijednosti m su oblika floor(n/d),
// ima ih O(sqrt n); svaku računamo blokovima jednakih kvocijenata (O(sqrt m)).
// Ukupno O(n^{3/4}).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;
const ll A = 20210926;

ll n, S;                 // S = floor(sqrt(n))
vector<ll> gsmall, gbig; // gsmall[m] za m <= S,  gbig[d] = g(floor(n/d)) za floor(n/d) > S
vector<char> dsmall, dbig;

ll g(ll m) {
    if (m == 0) return 0;
    bool small = (m <= S);
    ll idx = small ? m : n / m;          // za veliko m vrijedi m = floor(n / idx)
    if (small ? dsmall[idx] : dbig[idx]) return small ? gsmall[idx] : gbig[idx];
    ll lim = min(m, A);                  // k ide od 2 do lim
    ll res = 1;
    for (ll k = 2; k <= lim;) {
        ll q = m / k;                    // isti kvocijent za k..k2
        ll k2 = min(lim, m / q);
        res = (res + (k2 - k + 1) % MOD * g(q)) % MOD;
        k = k2 + 1;
    }
    if (small) { gsmall[idx] = res; dsmall[idx] = 1; }
    else       { gbig[idx] = res;   dbig[idx] = 1; }
    return res;
}

int main() {
    scanf("%lld", &n);
    S = (ll)sqrtl((long double)n);
    while (S * S > n) --S;
    while ((S + 1) * (S + 1) <= n) ++S;
    gsmall.assign(S + 2, 0); dsmall.assign(S + 2, 0);
    gbig.assign(n / (S + 1) + 2, 0); dbig.assign(n / (S + 1) + 2, 0);
    printf("%lld\n", g(n));
    return 0;
}
