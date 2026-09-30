// UCup 1, Stage 19 (NAC 2023), K. Space Alignment – 2. rješenje (algebarski, bez isprobavanja k)
// Redak j s t_j tabulatora i s_j razmaka na dubini p_j > 0 zahtijeva t_j*k + s_j = p_j*i.
// Oduzimanjem dviju takvih jednadžbi (pomnoženih s p_2 odnosno p_1) nestaje nepoznanica i:
//     k * (p_2*t_1 - p_1*t_2) = p_1*s_2 - p_2*s_1.
// Ako neki par redaka ima zagradu != 0, k je jednoznačno određen (kvocijent mora biti cijeli
// i >= 1), pa ga samo provjerimo u O(n). Inače su svi retci proporcionalni referentnom:
// t_j/p_j = a/b za sve j, a onda i s_j/p_j = f/g mora biti isti skraćeni razlomak za sve j.
// Jedini preostali uvjet je da i = (a/b)*k + f/g bude pozitivan cijeli broj, tj. linearna
// kongruencija  a*g*k ≡ -f*b (mod b*g),  koju rješavamo proširenim Euklidovim algoritmom.
// Složenost O(n + log(b*g)) – nema petlje po k.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<ll> t, s, p;

// je li k dosljedan za cijelu datoteku (postoji zajednički i > 0)
bool dosljedno(ll k) {
    ll i = -1;
    for (int j = 0; j < n; ++j) {
        ll uvlaka = t[j] * k + s[j];
        if (p[j] == 0) { if (uvlaka != 0) return false; continue; }
        if (uvlaka % p[j] != 0) return false;
        ll kandidat = uvlaka / p[j];
        if (kandidat <= 0) return false;
        if (i == -1) i = kandidat;
        else if (i != kandidat) return false;
    }
    return true;
}

// prošireni Euklid: vraća gcd(a, b) i x, y takve da je a*x + b*y = gcd
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - (a / b) * y1;
    return g;
}

// najmanji k >= 1 takav da A*k ≡ B (mod M), ili -1 ako rješenje ne postoji
ll najmanjeRjesenje(ll A, ll B, ll M) {
    A %= M; if (A < 0) A += M;
    B %= M; if (B < 0) B += M;
    ll x, y;
    ll g = extgcd(A, M, x, y);           // A*x + M*y = g
    if (B % g != 0) return -1;
    ll M2 = M / g;                        // rješenja čine klasu ostataka modulo M2
    ll k = (ll)(((__int128)x * (B / g)) % M2);
    if (k < 0) k += M2;
    return k == 0 ? M2 : k;               // tražimo k >= 1
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    t.assign(n, 0); s.assign(n, 0); p.assign(n, 0);
    int dubina = 0;
    char buf[2005];
    for (int j = 0; j < n; ++j) {
        if (scanf("%s", buf) != 1) return 0;
        int len = strlen(buf);
        for (int q = 0; q + 1 < len; ++q) {
            if (buf[q] == 't') ++t[j]; else ++s[j];
        }
        if (buf[len - 1] == '{') { p[j] = dubina; ++dubina; }
        else { --dubina; p[j] = dubina; }   // zatvarajuća zagrada je na dubini bloka koji zatvara
    }

    // retci na dubini 0 ne smiju imati uvlaku
    for (int j = 0; j < n; ++j)
        if (p[j] == 0 && t[j] + s[j] > 0) { puts("-1"); return 0; }

    // referentni uvučeni redak
    int r = -1;
    for (int j = 0; j < n; ++j) if (p[j] > 0) { r = j; break; }
    if (r == -1) { puts("1"); return 0; }     // nema uvučenih redaka: svaki k odgovara

    // 1) postoji li par koji jednoznačno određuje k?
    for (int j = 0; j < n; ++j) {
        if (p[j] == 0) continue;
        ll nazivnik = p[j] * t[r] - p[r] * t[j];
        if (nazivnik == 0) continue;           // (t_j, p_j) proporcionalno (t_r, p_r)
        ll brojnik = p[r] * s[j] - p[j] * s[r];
        if (brojnik % nazivnik != 0) { puts("-1"); return 0; }
        ll k = brojnik / nazivnik;
        if (k < 1 || !dosljedno(k)) { puts("-1"); return 0; }
        printf("%lld\n", k);
        return 0;
    }

    // 2) svi su retci proporcionalni: t_j/p_j = a/b, pa mora biti i s_j/p_j = f/g za sve j
    ll g1 = __gcd(t[r], p[r]);
    ll a = t[r] / g1, b = p[r] / g1;           // a >= 0, b >= 1, gcd(a, b) = 1
    ll g2 = __gcd(s[r], p[r]);
    ll f = s[r] / g2, g = p[r] / g2;           // f >= 0, g >= 1, gcd(f, g) = 1
    for (int j = 0; j < n; ++j) {
        if (p[j] == 0) continue;
        if (s[j] * g != f * p[j]) { puts("-1"); return 0; }   // s_j/p_j != f/g
    }
    if (a == 0) {
        // nitko nema tabulatore: i = f/g mora biti pozitivan cijeli broj, k = 1 je najmanji
        puts((g == 1 && f > 0) ? "1" : "-1");
        return 0;
    }
    // i = (a*g*k + f*b) / (b*g) je cijeli broj  <=>  a*g*k ≡ -f*b (mod b*g); i > 0 automatski
    ll k = najmanjeRjesenje(a * g, -f * b, b * g);
    printf("%lld\n", k);
    return 0;
}
