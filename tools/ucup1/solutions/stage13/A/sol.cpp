// UCup 1, Stage 13, A: The Best Problem of 2021
// 1) Gaussova eliminacija nad Z_2 (bitsetovi): ako B nije nezavisan -> 0.
// 2) t = |span(B) ∩ [0,X]|; u koordinatama koeficijenata skup span(B) ∩ [0,X] je točno {0,1,...,t-1},
//    pa se zadatak svodi na: koliko podskupova od {1,...,Y}, Y = t-1, razapinje cijeli Z_2^n.
// 3) Möbiusova inverzija po potprostorima: odgovor = (1/2) * sum_k (-1)^{n-k} 2^{C(n-k,2)} A_k,
//    A_k = sum po potprostorima U dimenzije k od 2^{|U ∩ [0,Y]|}.
// 4) A_k računamo DP-om po bitovima odozdo prema gore preko reduciranih stupnjevitih baza
//    (stanje: broj pivota ispod, faza "ispod/iznad točke razilaženja D").
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const ll MOD = 998244353;

ll pw(ll b, ll e) { ll r = 1; b %= MOD; if (b < 0) b += MOD; while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; } return r; }

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    int W = (m + 63) / 64;
    vector<string> rows(n);
    static char buf[2100];
    for (int i = 0; i < n; i++) { if (scanf("%s", buf) != 1) return 0; rows[i] = buf; }
    if (scanf("%s", buf) != 1) return 0;
    string xs = buf;
    auto toBits = [&](const string& s) {
        vector<ull> v(W, 0);
        for (int i = 0; i < m; i++) if (s[m - 1 - i] == '1') v[i >> 6] |= 1ULL << (i & 63);
        return v;
    };
    // stupnjevita baza: row[p] = redak s najvišim bitom p
    vector<vector<ull>> row(m);
    vector<char> has(m, 0);
    for (int i = 0; i < n; i++) {
        vector<ull> v = toBits(rows[i]);
        for (int p = m - 1; p >= 0; p--) {
            if (!((v[p >> 6] >> (p & 63)) & 1)) continue;
            if (!has[p]) { has[p] = 1; row[p] = v; break; }
            for (int w = 0; w < W; w++) v[w] ^= row[p][w];
        }
        bool zero = true;
        for (int w = 0; w < W; w++) if (v[w]) zero = false;
        if (zero) { puts("0"); return 0; }   // B nije linearno nezavisan
    }
    // cntBelow[c] = broj pivota na pozicijama < c
    vector<int> cntBelow(m + 1, 0);
    for (int c = 0; c < m; c++) cntBelow[c + 1] = cntBelow[c] + has[c];
    // t = |span(B) ∩ [0,X]| kao binarni broj (n+2 bita)
    vector<int> t(n + 2, 0);
    auto addPow = [&](int j) { for (int k = j; ; k++) { if (t[k] == 0) { t[k] = 1; break; } t[k] = 0; } };
    vector<ull> now(W, 0);
    vector<ull> X = toBits(xs);
    bool ended = false;
    for (int c = m - 1; c >= 0; c--) {
        int xb = (X[c >> 6] >> (c & 63)) & 1;
        int nb = (now[c >> 6] >> (c & 63)) & 1;
        if (has[c]) {
            if (xb) addPow(cntBelow[c]);          // izbor koji daje bit 0: svih 2^{j} nastavaka je < X
            if (nb != xb) for (int w = 0; w < W; w++) now[w] ^= row[c][w];
        } else if (nb != xb) {
            if (nb == 0) addPow(cntBelow[c]);     // now < X na ovom bitu: svi nastavci su manji
            ended = true; break;
        }
    }
    if (!ended) addPow(0);                        // sam X pripada span(B)
    // Y = t - 1
    vector<int> Y(n + 2, 0);
    { int borrow = 1; for (int k = 0; k < n + 2; k++) { int v = t[k] - borrow; if (v < 0) { v += 2; borrow = 1; } else borrow = 0; Y[k] = v; } }
    if (!Y[n - 1]) { puts("0"); return 0; }      // nijedan element nema najviši bit -> ne razapinju
    // pomoćne tablice
    vector<ll> p2(2 * n + 5, 1);
    for (int i = 1; i < (int)p2.size(); i++) p2[i] = p2[i - 1] * 2 % MOD;
    vector<ll> big(n + 1);                       // big[j] = 2^{2^j} mod p (eksponent mod p-1)
    { ll e = 1; for (int j = 0; j <= n; j++) { big[j] = pw(2, e); e = e * 2 % (MOD - 1); } }
    const ll inv2 = (MOD + 1) / 2;
    // DP: f = ispod točke razilaženja D (D postoji iznad), g = iznad D ili D ne postoji
    vector<ll> f(n + 2, 0), g(n + 2, 0), nf(n + 2), ng(n + 2);
    f[0] = 1; g[0] = 2;
    for (int c = 0; c < n; c++) {
        fill(nf.begin(), nf.end(), 0); fill(ng.begin(), ng.end(), 0);
        for (int j = 0; j <= c; j++) {
            if (!f[j] && !g[j]) continue;
            ll fac = p2[c - j];                    // slobodni bitovi retka s pivotom c
            ll mul = Y[c] ? big[j] : 1;            // doprinos pivota c skupu U ∩ [0,Y]
            // c je pivot
            nf[j + 1] = (nf[j + 1] + f[j] * fac) % MOD;
            ng[j + 1] = (ng[j + 1] + g[j] * fac % MOD * mul) % MOD;
            if (c < n - 1) {                       // c nije pivot (najviši bit mora biti pivot)
                nf[j] = (nf[j] + f[j]) % MOD;                         // još ispod D
                ng[j] = (ng[j] + f[j] * inv2 % MOD * mul) % MOD;      // c je točno D
                ng[j] = (ng[j] + g[j] * inv2) % MOD;                  // iznad D: now_c = Y_c
            }
        }
        swap(f, nf); swap(g, ng);
    }
    vector<ll> A(n + 1, 0);
    for (int k = 0; k <= n; k++) A[k] = g[k];
    // potprostori bez pivota na najvišem bitu: svi elementi su <= Y
    {
        ll gb = 1;                                 // [n-1 choose k]_2
        for (int k = 0; k <= n - 1; k++) {
            A[k] = (A[k] + gb * big[k]) % MOD;
            // prijelaz na [n-1 choose k+1]
            ll num = (p2[n - 1 - k] - 1 + MOD) % MOD, den = (p2[k + 1] - 1 + MOD) % MOD;
            gb = gb * num % MOD * pw(den, MOD - 2) % MOD;
        }
    }
    ll ans = 0;
    for (int k = 0; k <= n; k++) {
        int d = n - k;
        ll mu = pw(2, (ll)d * (d - 1) / 2);     // |mu(U,V)| = 2^{C(n-k,2)}
        if (d & 1) mu = (MOD - mu) % MOD;
        ans = (ans + mu * A[k]) % MOD;
    }
    ans = ans * inv2 % MOD;
    printf("%lld\n", ans);
    return 0;
}
