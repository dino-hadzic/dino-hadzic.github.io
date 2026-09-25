// UCup 1, Stage 18, I: Digit Mode
// Digit DP: fiksiramo prefiks broja (jednak prefiksu n, pa jedna manja znamenka),
// preostalih r pozicija je slobodno. Za svaki kandidat moda m i njegov ukupni broj
// pojavljivanja c brojimo popunjavanja slobodnih pozicija u kojima znamenke < m dolaze
// najviše c puta, a znamenke > m najviše c-1 puta: DP po znamenkama s eksponencijalnim
// generirajućim funkcijama (težina 1/k!), na kraju množimo s r!/(c-c'_m)!.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007LL;

ll fact[60], inv_fact[60];
ll power(ll b, ll e) {
    ll r = 1;
    b %= MOD;
    while (e) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return r;
}

// cnt[0..9] = znamenke već fiksiranog prefiksa; r = broj slobodnih pozicija.
// Vraća sumu moda po svim 10^r popunjavanjima.
ll sumFree(const int cnt[10], int r) {
    ll total = 0;
    static ll f[60];
    for (int m = 0; m <= 9; m++) {
        for (int c = max(cnt[m], 1); c <= cnt[m] + r; c++) {
            int rest = r - (c - cnt[m]);  // slobodne pozicije za ostale znamenke
            // DP: f[j] = suma po rasporedima ostalih znamenki na j pozicija od prod 1/k_e!
            for (int j = 0; j <= rest; j++) f[j] = 0;
            f[0] = 1;
            bool feasible = true;
            for (int e = 0; e <= 9 && feasible; e++) {
                if (e == m) continue;
                int cap = (e < m ? c : c - 1) - cnt[e];  // koliko još smijemo dodati znamenke e
                if (cap < 0) { feasible = false; break; }
                for (int j = rest; j >= 1; j--) {
                    ll s = f[j];
                    int lim = min(cap, j);
                    for (int k = 1; k <= lim; k++) s = (s + f[j - k] * inv_fact[k]) % MOD;
                    f[j] = s;
                }
            }
            if (!feasible) continue;
            ll ways = f[rest] * fact[r] % MOD * inv_fact[c - cnt[m]] % MOD;
            total = (total + ways * m) % MOD;
        }
    }
    return total;
}

int main() {
    fact[0] = 1;
    for (int i = 1; i < 60; i++) fact[i] = fact[i - 1] * i % MOD;
    for (int i = 0; i < 60; i++) inv_fact[i] = power(fact[i], MOD - 2);
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        static char s[64];
        if (scanf("%s", s) != 1) return 0;
        int L = strlen(s);
        ll ans = 0;
        int cnt[10];
        // brojevi s manje znamenki od n
        for (int len = 1; len < L; len++)
            for (int d = 1; d <= 9; d++) {
                memset(cnt, 0, sizeof(cnt));
                cnt[d] = 1;
                ans = (ans + sumFree(cnt, len - 1)) % MOD;
            }
        // brojevi iste duljine, manji od n: prefiks jednak, pa manja znamenka na poziciji p
        memset(cnt, 0, sizeof(cnt));
        for (int p = 0; p < L; p++) {
            int dn = s[p] - '0';
            for (int d = (p == 0 ? 1 : 0); d < dn; d++) {
                cnt[d]++;
                ans = (ans + sumFree(cnt, L - 1 - p)) % MOD;
                cnt[d]--;
            }
            cnt[dn]++;
        }
        // sam broj n
        int best = 0;
        for (int d = 0; d <= 9; d++)
            if (cnt[d] >= cnt[best]) best = d;
        ans = (ans + best) % MOD;
        printf("%lld\n", ans);
    }
    return 0;
}
