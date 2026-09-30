// UCup 1, Stage 9 (Qingdao 2018), L. Sub-cycle Graph
// Podciklički graf s m < n bridova = n-m disjunktnih puteva (i izolirani vrhovi = putevi duljine 0).
// Neka je k = n - m puteva od kojih j ima >= 2 vrha: broj načina = C(n, i) * i! / (2^j * j!) * C(i - j - 1, j - 1)
// gdje je i = n - (k - j) broj vrhova u "pravim" putevima (kompozicija i u j dijelova >= 2).
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;
const int MAXN = 100005;
long long fact[MAXN], inv[MAXN], pw2inv[MAXN];

long long power(long long b, long long e) {
    long long r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}
long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

int main() {
    fact[0] = 1;
    for (int i = 1; i < MAXN; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[MAXN - 1] = power(fact[MAXN - 1], MOD - 2);
    for (int i = MAXN - 1; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    long long inv2 = (MOD + 1) / 2;
    pw2inv[0] = 1;
    for (int i = 1; i < MAXN; i++) pw2inv[i] = pw2inv[i - 1] * inv2 % MOD;

    int T;
    scanf("%d", &T);
    while (T--) {
        int n; long long m;
        scanf("%d %lld", &n, &m);
        if (m > n) { puts("0"); continue; }
        if (m == n) { puts(to_string(fact[n - 1] * inv2 % MOD).c_str()); continue; }  // Hamiltonov ciklus
        int k = n - (int)m;                     // broj puteva
        long long ans = 0;
        for (int j = 0; j <= k; j++) {          // j puteva s >= 2 vrha
            int izol = k - j;                   // izolirani vrhovi
            int i = n - izol;                   // vrhovi u pravim putevima
            if (i < 2 * j) break;
            long long nacini;
            if (j == 0) nacini = (i == 0) ? 1 : 0;
            else nacini = C(i - j - 1, j - 1);  // kompozicije od i u j dijelova >= 2
            long long t = C(n, izol) * fact[i] % MOD * pw2inv[j] % MOD * inv[j] % MOD * nacini % MOD;
            ans = (ans + t) % MOD;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
