// UCup 1, Stage 3 (AMPPZ 2022), E. Euclidean Algorithm
// Algoritam je tocan za (x,y) <=> x = d(1+pk), y = d(1+(p+1)k), d,k>=1, p>=0.
// Broj parova = sum_d D(floor(n/d) - 1), D(m) = sum_{i<=m} floor(m/i) (djeliteljska sumatorna funkcija).
// Male vrijednosti D racunamo segmentiranim sitom broja djelitelja (memorija 8 MB!),
// velike formulom u O(sqrt m). Ukupno ~O(n^{2/3}).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

static ull D_formula(ll m) {          // sum_{i=1..m} floor(m/i) u O(sqrt m)
    if (m <= 0) return 0;
    ll s = (ll)sqrtl((long double)m);
    while (s * s > m) --s;
    while ((s + 1) * (s + 1) <= m) ++s;
    ull r = 0;
    for (ll i = 1; i <= s; ++i) r += m / i;
    return 2 * r - (ull)s * s;
}

int main() {
    int z;
    if (scanf("%d", &z) != 1) return 0;
    const int SEG = 1 << 18;                           // segment sita: 2^18 * 2 B = 0.5 MB
    static unsigned short tau[1 << 18];
    while (z--) {
        ll n;
        scanf("%lld", &n);
        // prag T ~ n^{2/3}: D(m) za m <= T iz sita, inace formulom
        ll T = (ll)cbrtl((long double)n);
        T = T * T;
        if (T > n) T = n;
        if (T < 1) T = 1;
        ull odg = 0;
        // segmentirano sito: tau[i] = broj djelitelja i; prolazimo m rastuce
        ll segL = 1;                                    // trenutni segment [segL, segL+SEG)
        ll sitoPos = 1;                                 // sljedeci i ciji tau jos nije dodan u prefiks
        ull prefiks = 0;                                // sum_{i < sitoPos} tau(i)
        auto sijaj = [&](ll L) {
            ll R = min(L + SEG, T + 1);                 // [L, R)
            memset(tau, 0, sizeof(unsigned short) * (size_t)(R - L));
            for (ll i = 1; i * i < R; ++i) {
                ll start = max(i * i, ((L + i - 1) / i) * i);
                for (ll m = start; m < R; m += i) tau[m - L] += (m == i * i) ? 1 : 2;
            }
        };
        sijaj(segL);
        auto D_sito = [&](ll m) {                       // m <= T, pozivi s nepadajucim m
            while (sitoPos <= m) {
                if (sitoPos >= segL + SEG) { segL += SEG; sijaj(segL); }
                prefiks += tau[sitoPos - segL];
                ++sitoPos;
            }
            return prefiks;
        };
        // blokovi jednakih vrijednosti v = floor(n/d), od velikih d (mali v) prema malima
        for (ll d = n; d >= 1;) {
            ll v = n / d;
            ll dlo = n / (v + 1) + 1;                   // najmanji d s istim v
            ll m = v - 1;
            ull Dm = (m <= T) ? D_sito(m) : D_formula(m);
            odg += (ull)(d - dlo + 1) * Dm;
            d = dlo - 1;
        }
        printf("%llu\n", odg);
    }
    return 0;
}
