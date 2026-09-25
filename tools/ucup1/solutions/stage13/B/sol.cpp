// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), B. Random Interactive Convex Hull Bot
// Inkrementalno gradimo konveksnu ljusku: tocke dodajemo jednu po jednu i za svaku odredimo
// je li unutar trenutne ljuske. Lokalizaciju radimo binarnim pretrazivanjem po "lepezi"
// dijagonala iz jednog fiksnog vrha ljuske (pivota); podjelu biramo tezinski, prema broju
// ranijih tocaka koje su pale u pojedini trokut lepeze, jer su tocke slucajne pa je to dobra
// procjena povrsine. Ako je tocka izvan ljuske, od pronadenog vidljivog brida hodamo lijevo i
// desno dok su bridovi vidljivi te ih zamijenimo novom tockom.
#include <bits/stdc++.h>
using namespace std;

int n;
int brojUpita = 0;

// Upit: 1 ako je skretanje iz vektora (i -> j) u (i -> k) u smjeru suprotnom od kazaljke,
// tj. ako je tocka k lijevo od usmjerenog pravca i -> j; inace -1.
int upit(int i, int j, int k) {
    ++brojUpita;
    printf("? %d %d %d\n", i, j, k);
    fflush(stdout);
    int r;
    if (scanf("%d", &r) != 1) exit(0);
    return r;
}

// Je li tocka k lijevo od usmjerenog pravca i -> j?
bool lijevo(int i, int j, int k) { return upit(i, j, k) == 1; }

vector<int> ljuska;          // vrhovi ljuske u smjeru suprotnom od kazaljke, ljuska[0] je pivot
vector<long long> tezina;    // tezina[s] = broj tocaka koje su pale u "utor" s (vidi dolje)

// Utori za ljusku velicine m (pivot p = ljuska[0], zrake p -> ljuska[t], t = 1..m-1):
//   utor 0      : desno od zrake p -> ljuska[1]       (izvan ljuske, iza brida (0,1))
//   utor s      : izmedu zraka p -> ljuska[s] i p -> ljuska[s+1], 1 <= s <= m-2
//   utor m-1    : lijevo od zrake p -> ljuska[m-1]    (izvan ljuske, iza brida (m-1,0))
// Tocka q je u utoru s  <=>  L(s) istinito i L(s+1) lazno, gdje je L(t) = "q lijevo od p -> ljuska[t]",
// uz dogovor L(0) = istina, L(m) = laz. Za tocku koja nije "iza" pivota L je oblika istina...laz,
// a za tocku iza pivota pretraga zavrsi u utoru 0 ili m-1, sto je u oba slucaja vidljiv brid.

void postaviJednolikeTezine(int m, long long ukupno) {
    tezina.assign(m, max(1LL, ukupno / max(1, m)));
}

// Vraca utor u kojem se nalazi tocka q.
int pronadiUtor(int q) {
    int m = ljuska.size();
    int lo = 0, hi = m - 1;                 // utor je u [lo, hi]
    vector<long long> pref(m + 1, 0);
    for (int s = 0; s < m; ++s) pref[s + 1] = pref[s] + tezina[s] + 1;   // +1 da prazni utori ne budu nula
    while (lo < hi) {
        // Biramo t u (lo, hi] tako da su tezine utora [lo, t-1] i [t, hi] sto ujednacenije.
        long long cilj = (pref[lo] + pref[hi + 1]) / 2;
        int t = int(lower_bound(pref.begin() + lo + 1, pref.begin() + hi + 1, cilj) - pref.begin());
        if (t <= lo) t = lo + 1;
        if (t > hi) t = hi;
        // Ako je tezina bliza s druge strane, pomakni t (lokalna korekcija).
        if (t > lo + 1 && llabs(pref[t - 1] - cilj) < llabs(pref[t] - cilj)) --t;
        if (lijevo(ljuska[0], ljuska[t], q)) lo = t;     // L(t) istina => utor >= t
        else hi = t - 1;                                 // L(t) laz    => utor <= t-1
    }
    return lo;
}

// Ubaci tocku q ako je izvan ljuske; e je indeks vidljivog brida (ljuska[e] -> ljuska[(e+1)%m]).
void ubaci(int q, int e, long long ukupnoTocaka) {
    int m = ljuska.size();
    int lo = e, hi = (e + 1) % m;
    // Hodamo unatrag dok je brid (lo-1, lo) vidljiv, tj. q desno od njega.
    while (!lijevo(ljuska[(lo - 1 + m) % m], ljuska[lo], q)) lo = (lo - 1 + m) % m;
    // Hodamo unaprijed dok je brid (hi, hi+1) vidljiv.
    while (!lijevo(ljuska[hi], ljuska[(hi + 1) % m], q)) hi = (hi + 1) % m;

    // Uklonjeni su vrhovi lo+1, ..., hi-1 (ciklicki). Pivot (indeks 0) ostaje ako se raspon ne omata
    // preko nule; hi == 0 znaci da su uklonjeni samo indeksi lo+1..m-1.
    // Nova ljuska: ljuska[lo], q, ljuska[hi], ljuska[hi+1], ..., (ciklicki) do ljuska[lo].
    bool pivotOstaje = (lo < hi) || (hi == 0);
    vector<int> nova;
    vector<long long> novaTezina;
    if (pivotOstaje) {
        int hiEff = (hi == 0) ? m : hi;
        long long zbroj = 0;
        for (int s = lo; s < hiEff; ++s) zbroj += tezina[s];      // utori koji nestaju
        for (int s = 0; s <= lo; ++s) nova.push_back(ljuska[s]);
        for (int s = 0; s < lo; ++s) novaTezina.push_back(tezina[s]);
        nova.push_back(q);
        // Dva nova utora: izmedu zraka na ljuska[lo] i q, te izmedu zraka na q i ljuska[hi].
        // Ako je neki od njih "vanjski" utor (lo == 0 ili hi == 0), dobiva tezinu 0.
        long long prvi = zbroj / 2, drugi = zbroj - zbroj / 2;
        if (lo == 0) { prvi = 0; drugi = zbroj; }
        if (hiEff == m) { drugi = 0; prvi = zbroj; }
        if (lo == 0 && hiEff == m) prvi = drugi = 0;
        novaTezina.push_back(prvi);
        novaTezina.push_back(drugi);
        for (int s = hiEff; s < m; ++s) nova.push_back(ljuska[s]);
        for (int s = hiEff; s < m; ++s) novaTezina.push_back(tezina[s]);
        ljuska = nova;
        tezina = novaTezina;
    } else {
        // Pivot je uklonjen: novi pivot je ljuska[hi]; tezine resetiramo na jednolike.
        for (int s = hi; s != lo; s = (s + 1) % m) nova.push_back(ljuska[s]);
        nova.push_back(ljuska[lo]);
        nova.push_back(q);
        ljuska = nova;
        postaviJednolikeTezine(ljuska.size(), ukupnoTocaka);
    }
}

int main() {
    if (scanf("%d", &n) != 1) return 0;

    // Pocetni trokut od tocaka 1, 2, 3, orijentiran u smjeru suprotnom od kazaljke.
    if (lijevo(1, 2, 3)) ljuska = {1, 2, 3};
    else ljuska = {1, 3, 2};
    postaviJednolikeTezine(3, 3);

    for (int q = 4; q <= n; ++q) {
        int m = ljuska.size();
        int s = pronadiUtor(q);
        if (s == 0) {
            ubaci(q, 0, q);                      // vidljiv brid (0, 1)
        } else if (s == m - 1) {
            ubaci(q, m - 1, q);                  // vidljiv brid (m-1, 0)
        } else if (lijevo(ljuska[s], ljuska[s + 1], q)) {
            tezina[s] += 1;                      // unutar trokuta lepeze => unutar ljuske
        } else {
            ubaci(q, s, q);                      // vidljiv brid (s, s+1)
        }
    }

    printf("! %d", (int)ljuska.size());
    for (int v : ljuska) printf(" %d", v);
    printf("\n");
    fflush(stdout);
    fprintf(stderr, "upita: %d\n", brojUpita);
    return 0;
}
