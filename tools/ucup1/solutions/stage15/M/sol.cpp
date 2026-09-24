// UCup 1, Stage 15 (ZJCPC 2023), M. Stage Clear
// Redoslijed borbi je valjan ako svaki čudak u trenutku borbe ima već poraženog prethodnika (ili 1).
// Dva pristupa, biramo jeftiniji:
//  1) DP po podskupovima preostalih čudovišta: f[S] = min_x max(f[S\x]-b_x,0)+a_x, O(n 2^{n-1});
//  2) svakom vrhu izaberemo jednog roditelja (2^{m-n+1} korijenskih stabala) i za stablo
//     pohlepno spajamo blok s najvišim prioritetom u blok njegova roditelja, O(n^2) po stablu.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m;
ll a[80], b[80];
vector<int> ulaz[80];     // ulazni susjedi (manji od vrha)

// blok = niz borbi: A = potreban HP na početku, D = ukupna promjena HP
struct Blok { ll A, D; };
Blok spoji(Blok p, Blok q) { return { max(p.A, q.A - p.D), p.D + q.D }; }
// x ima veći prioritet od y (x ide ranije u neograničenom optimalnom poretku)
bool prije(const Blok& x, const Blok& y) {
    if ((x.D >= 0) != (y.D >= 0)) return x.D >= 0;
    if (x.D >= 0) return x.A < y.A;
    return x.A + x.D > y.A + y.D;
}

int rod[80], dsu[80];
int nadji(int v) { return dsu[v] == v ? v : dsu[v] = nadji(dsu[v]); }
ll rijesiStablo() {
    static Blok blok[80]; static bool ziv[80];
    for (int v = 1; v <= n; ++v) { dsu[v] = v; blok[v] = { a[v], b[v] - a[v] }; ziv[v] = true; }
    blok[1] = { 0, 0 };
    for (int korak = 0; korak < n - 1; ++korak) {
        int naj = -1;
        for (int v = 2; v <= n; ++v)
            if (ziv[v] && (naj < 0 || prije(blok[v], blok[naj]))) naj = v;
        int h = nadji(rod[naj]);            // blok koji sadrži roditelja
        blok[h] = spoji(blok[h], blok[naj]);
        ziv[naj] = false; dsu[naj] = h;
    }
    return blok[1].A;
}

ll rijesiStablima() {
    ll najbolje = LLONG_MAX;
    vector<int> izbor(n + 1, 0);
    while (true) {
        for (int v = 2; v <= n; ++v) rod[v] = ulaz[v][izbor[v]];
        najbolje = min(najbolje, rijesiStablo());
        int v = 2;                          // sljedeća kombinacija roditelja (miješana baza)
        while (v <= n && ++izbor[v] == (int)ulaz[v].size()) izbor[v++] = 0;
        if (v > n) break;
    }
    return najbolje;
}

ll rijesiDP() {
    // bit v-1 predstavlja vrh v (v>=2); bit 0 (vrh 1) nikad nije u S
    int k = n - 1;
    vector<ll> f((size_t)1 << k, LLONG_MAX);
    vector<unsigned> maskaUlaza(n + 1, 0);
    for (int v = 2; v <= n; ++v) for (int u : ulaz[v]) maskaUlaza[v] |= 1u << (u - 1);
    f[0] = 0;
    unsigned puni = (1u << n) - 1;
    for (unsigned S = 1; S < (1u << k); ++S) {
        unsigned Sv = S << 1;               // maska po vrhovima
        ll naj = LLONG_MAX;
        for (unsigned t = Sv; t; t &= t - 1) {
            int v = __builtin_ctz(t) + 1;
            if ((maskaUlaza[v] & ~Sv & puni) == 0) continue;   // svi prethodnici još neporaženi
            ll prije_ = f[S ^ (1u << (v - 2))];
            naj = min(naj, max(prije_ - b[v], 0LL) + a[v]);
        }
        f[S] = naj;
    }
    return f[(1u << k) - 1];
}

int main() {
    scanf("%d %d", &n, &m);
    for (int v = 2; v <= n; ++v) scanf("%lld %lld", &a[v], &b[v]);
    for (int i = 0; i < m; ++i) { int u, v; scanf("%d %d", &u, &v); ulaz[v].push_back(u); }
    double stabala = 1;
    for (int v = 2; v <= n; ++v) stabala *= ulaz[v].size();
    double cijenaStabla = stabala * n * n, cijenaDP = ldexp((double)n, n - 1);
#ifdef FORSIRAJ_STABLA
    cijenaDP = 1e300;
#endif
#ifdef FORSIRAJ_DP
    cijenaStabla = 1e300;
#endif
    printf("%lld\n", cijenaStabla <= cijenaDP ? rijesiStablima() : rijesiDP());
    return 0;
}
