// UCup 1, Stage 17, M - Expression 3
// Redoslijed brisanja = permutacija n-1 operatora. Broj a_i mijenja predznak
// točno kad se primijeni operator '-' na poziciji j < i u trenutku kad su svi
// operatori j+1..i-1 već primijenjeni, tj. kad je j "rekord s desna" među
// vremenima operatora 1..i-1. U slučajnoj permutaciji je j rekord s desna
// s vjerojatnošću 1/(i-j), a ti su događaji nezavisni, pa je
//   E[predznak a_i] = prod_{j<i} (i-j-1+s_j)/(i-j),   s_j = +1 za '+', -1 za '-'.
// Nazovimo V(i) = prod_{j<i} (i-j-1+s_j); faktor je i-j za '+', a i-j-2 za '-'.
// Odgovor = (n-1)! * sum_i a_i * V(i) / (i-1)!.
// V(i) računamo preko diskretnih logaritama: log V(i) = sum_k C[k] * L(i-k),
// gdje je L(d) = log_g d, C[k] = [op_k = '+'] + [op_{k-2} = '-']. To je jedna
// konvolucija (NTT). Logaritme svih brojeva do n dobijemo iz logaritama
// prostih brojeva (linearno sito) koje računamo Pohlig-Hellmanom, jer je
// p-1 = 2^23 * 7 * 17 gladak. Posebno: '-' na poziciji i-2 daje faktor 0,
// a '-' na poziciji i-1 faktor -1.
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const ll MOD = 998244353, G = 3;

ll pw(ll a, ll e) {
    ll r = 1;
    a %= MOD;
    if (a < 0) a += MOD;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

// diskretni logaritam po bazi G, Pohlig-Hellman za p-1 = 2^23 * 7 * 17
ll dlog_prime_power(ll a, ll q, int e) {
    // vraća x mod q^e takav da (G^((p-1)/q^e))^x = a^((p-1)/q^e)
    ll m = (MOD - 1) / pw(q, e) ;
    ll h = pw(a, m), gamma = pw(G, m);  // gamma ima red q^e
    ll x = 0, qk = 1;
    ll gamma_q = pw(gamma, pw(q, e - 1));  // red q
    for (int k = 0; k < e; k++) {
        // (h * gamma^{-x})^{q^{e-1-k}} = gamma_q^{d}, tražimo d < q
        ll cur = pw(h * pw(pw(gamma, x), MOD - 2) % MOD, pw(q, e - 1 - k));
        ll d = 0, t = 1;
        while (t != cur) { t = t * gamma_q % MOD; d++; }
        x += d * qk;
        qk *= q;
    }
    return x;
}

ll dlog(ll a) {
    // CRT za module 2^23, 7, 17
    ll mods[3] = {1LL << 23, 7, 17};
    ll rem[3] = {dlog_prime_power(a, 2, 23), dlog_prime_power(a, 7, 1), dlog_prime_power(a, 17, 1)};
    ll x = rem[0], M = mods[0];
    for (int i = 1; i < 3; i++) {
        // x ≡ rem[i] (mod mods[i]); M i mods[i] su relativno prosti
        ll t = ((rem[i] - x) % mods[i] + mods[i]) % mods[i];
        ll invM = 1;
        while (invM * (M % mods[i]) % mods[i] != 1) invM++;
        x += M * (t * invM % mods[i]);
        M *= mods[i];
    }
    return x % (MOD - 1);
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
        ll w = pw(G, (MOD - 1) / len);
        if (inv) w = pw(w, MOD - 2);
        vector<ll> ws(len / 2);
        ws[0] = 1;
        for (int j = 1; j < len / 2; j++) ws[j] = ws[j - 1] * w % MOD;
        for (int i = 0; i < n; i += len)
            for (int j = 0; j < len / 2; j++) {
                ll u = a[i + j], v = a[i + j + len / 2] * ws[j] % MOD;
                a[i + j] = u + v < MOD ? u + v : u + v - MOD;
                a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + MOD;
            }
    }
    if (inv) {
        ll ni = pw(n, MOD - 2);
        for (ll &x : a) x = x * ni % MOD;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    static char s[200005];
    if (n > 1) scanf("%s", s);

    // logaritmi brojeva 1..n: linearno sito + dlog prostih
    vector<ll> L(n + 1, 0);
    vector<int> lp(n + 1, 0), primes;
    for (int i = 2; i <= n; i++) {
        if (lp[i] == 0) {
            lp[i] = i;
            primes.push_back(i);
            L[i] = dlog(i);
        }
        for (int p : primes) {
            if (p > lp[i] || (ll)p * i > n) break;
            lp[p * i] = p;
            L[p * i] = (L[p] + L[i]) % (MOD - 1);
        }
    }

    // C[k] = [op_k = '+'] + [op_{k-2} = '-'],  k = 1..n
    vector<ll> C(n + 1, 0);
    for (int j = 1; j <= n - 1; j++) {
        if (s[j - 1] == '+') C[j] += 1;
        else if (j + 2 <= n) C[j + 2] += 1;
    }
    // konvolucija: E(i) = sum_{k<i} C[k] * L(i-k); L cijepamo na 3 dijela po 10 bitova
    int sz = 1;
    while (sz < 2 * (n + 1)) sz <<= 1;
    vector<ll> fc(sz, 0);
    for (int k = 0; k <= n; k++) fc[k] = C[k];
    ntt(fc, false);
    vector<ll> E(n + 1, 0);  // točan zbroj logaritama (do 2*n*2^30 < 2^60)
    for (int part = 0; part < 3; part++) {
        vector<ll> fl(sz, 0);
        for (int d = 1; d <= n; d++) fl[d] = (L[d] >> (10 * part)) & 1023;
        ntt(fl, false);
        for (int i = 0; i < sz; i++) fl[i] = fl[i] * fc[i] % MOD;
        ntt(fl, true);
        for (int i = 1; i <= n; i++) E[i] += fl[i] << (10 * part);
    }

    vector<ll> fact(n + 1, 1), inv(n + 1, 1);
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[n] = pw(fact[n], MOD - 2);
    for (int i = n; i >= 1; i--) inv[i - 1] = inv[i] * i % MOD;

    ll ans = 0;
    for (int i = 1; i <= n; i++) {
        ll V;
        if (i >= 3 && s[i - 3] == '-') V = 0;                // faktor i-(i-2)-2 = 0
        else {
            V = pw(G, E[i] % (MOD - 1));
            if (i >= 2 && s[i - 2] == '-') V = (MOD - V) % MOD;  // faktor -1
        }
        ans = (ans + a[i] % MOD * V % MOD * inv[i - 1]) % MOD;
    }
    ans = ans * fact[n - 1] % MOD;
    printf("%lld\n", ans);
    return 0;
}
