// G. Gem Island 2 – kombinatorika, O(n + d log log d)
// 1) Nakon d koraka svaki raspored (x_1..x_n), x_i >= 1, sum = n+d, jednako je vjerojatan
//    (Pólyina urna), ukupno C(n+d-1, n-1) rasporeda.
// 2) Zbroj r najvećih = sum_t min(r, #{i : x_i >= t}).
// 3) Uz A_j(t) = C(n,j) * C(n+d-1-j(t-1), n-1) (bar j zadanih kutija ima >= t) i binomnu
//    inverziju dobivamo  odgovor = ( sum_j c_j C(n,j) S_j ) / C(n+d-1, n-1),
//    c_j = [j=1] za j <= r,  c_j = (-1)^(j-r) C(j-2, r-1) za j > r,
//    S_j = sum_{m>=0, jm<=d} h(jm),  h(x) = C(n-1+d-x, n-1).
// 4) sume h po višekratnicima za sve j odjednom: Dirichletova sufiksna suma.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned int ui;
const ll MOD = 998244353;

ll pw(ll b, ll e) { ll r = 1; b %= MOD; while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; } return r; }

int main() {
    int n, d, r;
    scanf("%d %d %d", &n, &d, &r);
    int M = max(n, d) + 2;
    vector<ui> inv(M + 1);                       // inv[i] = i^{-1} mod p, linearno
    inv[1] = 1;
    for (int i = 2; i <= M; i++) inv[i] = (ui)((MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD);

    // h[x] = C(n-1+d-x, n-1), x = 0..d;  h[d] = 1,  h[x-1] = h[x] * (n-1+d-x+1) / (d-x+1)
    vector<ui> h(d + 1);
    h[d] = 1;
    for (int x = d; x >= 1; x--) h[x - 1] = (ui)((ll)h[x] * ((n + d - x) % MOD) % MOD * inv[d - x + 1] % MOD);
    ll total = h[0];                              // C(n+d-1, n-1)

    // H[x] = sum_{m>=1, mx<=d} h[mx]  (Dirichletova sufiksna suma po višekratnicima)
    vector<ui> H(h.begin(), h.end());              // H[0] se ne koristi
    {
        vector<char> comp(d + 1, 0);
        for (int p = 2; p <= d; p++) {
            if (comp[p]) continue;
            for (ll q = (ll)p * p; q <= d; q += p) comp[q] = 1;
            for (int x = d / p; x >= 1; x--) { ui v = H[x] + H[x * p]; if (v >= MOD) v -= MOD; H[x] = v; }
        }
    }

    ll ans = 0;
    ll binom = 1;                                  // C(n, j)
    ll cj2 = 0;                                    // C(j-2, r-1)
    for (int j = 1; j <= n; j++) {
        binom = binom * ((n - j + 1) % MOD) % MOD * inv[j] % MOD;   // C(n,j)
        ll c;
        if (j <= r) c = (j == 1) ? 1 : 0;
        else {
            if (j == r + 1) cj2 = 1;                                 // C(r-1, r-1)
            else cj2 = cj2 * ((j - 2) % MOD) % MOD * inv[j - 1 - r] % MOD;   // C(j-2,r-1) = C(j-3,r-1)*(j-2)/(j-1-r)
            c = ((j - r) % 2 == 0) ? cj2 : (MOD - cj2) % MOD;
        }
        if (c == 0) continue;
        ll S = h[0];
        if (j <= d) S = (S + H[j]) % MOD;
        ans = (ans + c * binom % MOD * S) % MOD;
    }
    ans = ans * pw(total, MOD - 2) % MOD;
    printf("%lld\n", ans);
    return 0;
}
