// UCup 1, Stage 19 (NAC 2023), F. Four Square
// Ukupna površina mora biti kvadrat S^2. Svako popločavanje pravokutnika s najviše 4
// pravokutnika je „giljotinsko” (prvi rez koji ništa ne presijeca postoji, jer bi
// najmanji protuprimjer – vjetrenjača – zahtijevao 5 pravokutnika). Zato rekurzivno
// dijelimo skup pravokutnika (bitmaska) na dva neprazna dijela i pokušavamo vertikalni ili
// horizontalni rez; dimenziju dijela određuje njegova površina.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int W[4], H[4];
ll povrsina[16];

// može li se pravokutnik sirina x visina točno popločati pravokutnicima iz maske?
bool moze(ll sirina, ll visina, int maska) {
    if (sirina <= 0 || visina <= 0) return false;
    if (povrsina[maska] != sirina * visina) return false;
    if (__builtin_popcount(maska) == 1) {
        int i = __builtin_ctz(maska);
        return (W[i] == sirina && H[i] == visina) || (W[i] == visina && H[i] == sirina);
    }
    // podskupovi maske (svaki par {sub, maska^sub} promatramo jednom)
    for (int sub = (maska - 1) & maska; sub > 0; sub = (sub - 1) & maska) {
        int ostatak = maska ^ sub;
        if (sub < ostatak) continue;
        ll a = povrsina[sub];
        // vertikalni rez: lijevi dio ima visinu 'visina' i širinu a / visina
        if (a % visina == 0) {
            ll w1 = a / visina;
            if (w1 < sirina && moze(w1, visina, sub) && moze(sirina - w1, visina, ostatak)) return true;
        }
        // horizontalni rez: gornji dio ima širinu 'sirina' i visinu a / sirina
        if (a % sirina == 0) {
            ll h1 = a / sirina;
            if (h1 < visina && moze(sirina, h1, sub) && moze(sirina, visina - h1, ostatak)) return true;
        }
    }
    return false;
}

int main() {
    for (int i = 0; i < 4; ++i) {
        if (scanf("%d %d", &W[i], &H[i]) != 2) return 0;
    }
    for (int m = 0; m < 16; ++m) {
        povrsina[m] = 0;
        for (int i = 0; i < 4; ++i) if (m >> i & 1) povrsina[m] += (ll)W[i] * H[i];
    }
    ll ukupno = povrsina[15];
    ll S = llround(sqrt((double)ukupno));
    while (S * S > ukupno) --S;
    while ((S + 1) * (S + 1) <= ukupno) ++S;
    if (S * S != ukupno) { puts("0"); return 0; }
    puts(moze(S, S, 15) ? "1" : "0");
    return 0;
}
