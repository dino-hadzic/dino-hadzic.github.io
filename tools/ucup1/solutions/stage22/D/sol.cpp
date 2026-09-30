// D. Alice i Bob
// Bob pobjeđuje točno kad je p_1 minimum prefiksa p_1..p_{p_1} (svi ostali
// elementi prefiksa su veći od p_1). Za p_1 = i biramo i-1 vrijednosti iz
// {i+1..n}, poredamo ih i poredamo ostatak:  C(n-i, i-1) (i-1)! (n-i)!
//   = (n-i)!^2 / (n-2i+1)!.   Zbroj po i s 2i-1 <= n, sve modulo 998244353.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;

ll mpow(ll b, ll e) {
    ll r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> fact(n + 1), inv(n + 1);      // faktorijeli i inverzni faktorijeli
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % MOD;
    inv[n] = (int)mpow(fact[n], MOD - 2);
    for (int i = n; i > 0; --i) inv[i - 1] = (ll)inv[i] * i % MOD;
    ll ans = 0;
    for (int i = 1; 2 * i - 1 <= n; ++i) {
        // (n-i)! * (n-i)! / (n-2i+1)!
        ll t = (ll)fact[n - i] * fact[n - i] % MOD * inv[n - 2 * i + 1] % MOD;
        ans = (ans + t) % MOD;
    }
    printf("%lld\n", ans);
    return 0;
}
