// UCup 1, Stage 15 (ZJCPC 2023), D. Master of Both III
// g[R] = najmanja cijena multiskupa pomaka čiji je skup podzbrojeva (mod n) točno R;
// f(S) = min g[R] po R koji sadrže -S; SOS-DP po nadskupovima.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> w(n);
    for (auto &x : w) scanf("%lld", &x);
    int full = (1 << n) - 1;
    const ll INF = LLONG_MAX / 4;
    vector<ll> g(1 << n, INF);
    g[1] = 0;  // prazan multiskup pomaka generira samo ostatak 0 (bit 0)
    for (int mask = 1; mask <= full; ++mask) {
        if (g[mask] == INF) continue;
        for (int y = 0; y < n; ++y) {
            // ciklički pomak bitmaske za y: R + y (mod n)
            int rot = ((mask << y) | (mask >> (n - y))) & full;
            int nm = mask | rot;               // nm >= mask, pa je već obrađeno sve što treba
            if (g[mask] + w[y] < g[nm]) g[nm] = g[mask] + w[y];
        }
    }
    // h[S] = g[-S]: skup S može se poništiti pomacima koji generiraju -S
    vector<ll> h(1 << n, INF);
    for (int mask = 1; mask <= full; ++mask) {
        if (g[mask] == INF) continue;
        int neg = 0;
        for (int v = 0; v < n; ++v)
            if (mask >> v & 1) neg |= 1 << ((n - v) % n);
        h[neg] = min(h[neg], g[mask]);
    }
    // minimum po nadskupovima (SOS-DP)
    for (int b = 0; b < n; ++b)
        for (int mask = 0; mask <= full; ++mask)
            if (!(mask >> b & 1)) h[mask] = min(h[mask], h[mask | 1 << b]);
    ll ans = 0;
    for (int mask = 1; mask <= full; ++mask)
        ans = (ans + (h[mask] % MOD) * (mask % MOD)) % MOD;
    printf("%lld\n", ans);
    return 0;
}
