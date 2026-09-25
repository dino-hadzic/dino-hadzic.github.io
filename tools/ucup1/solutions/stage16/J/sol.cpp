// UCup 1, Stage 16, zadatak J: Classical Scheduling Problem
// Teme sortiramo po b. Binarno trazimo x = broj tema u koje smo sigurni: ako naucimo
// skup s barem x sigurnih tema, sigurne su (barem) prve x naucene u poretku po b.
// Provjera za x: pretpostavimo da je x-ta naucena tema (po b) upravo tema i. Tada
// moramo nauciti tocno x-1 tema s indeksom < i (uzmemo najjeftinije) i jos
// max(0, b_i - x) tema s indeksom > i (opet najjeftinije), da ukupno bude k >= b_i.
// Najjeftinije prefiksne teme daje gomila fiksne velicine x-1, a najjeftinije
// sufiksne teme gomila velicine b_i - x koja se, iduci s desna na lijevo, samo smanjuje.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
ll t;
vector<ll> a;
vector<int> b, ord;  // ord = indeksi tema sortirani po b

// Vraca indeks (u sortiranom poretku) teme koja moze biti x-ta sigurna, ili -1.
int provjeri(int x) {
    if (x == 0) return n;  // trivijalno izvedivo
    // sufiks: suf[i] = zbroj max(0, b_i - x) najjeftinijih tema s pozicijama > i (ili -1 ako ih nema dovoljno)
    vector<ll> suf(n, -1);
    priority_queue<ll> gomila;  // max-gomila odabranih (najjeftinijih) sufiksnih tema
    ll zbroj = 0;
    for (int i = n - 1; i >= 0; --i) {
        int c = max(0, b[ord[i]] - x);
        while ((int)gomila.size() > c) { zbroj -= gomila.top(); gomila.pop(); }
        if ((int)gomila.size() == c) suf[i] = zbroj;
        gomila.push(a[ord[i]]); zbroj += a[ord[i]];
    }
    // prefiks: zbroj x-1 najjeftinijih tema s pozicijama < i
    priority_queue<ll> pref;
    ll zbrojP = 0;
    for (int i = 0; i < n; ++i) {
        if ((int)pref.size() == x - 1 && suf[i] >= 0 && zbrojP + a[ord[i]] + suf[i] <= t) return i;
        pref.push(a[ord[i]]); zbrojP += a[ord[i]];
        if ((int)pref.size() > x - 1) { zbrojP -= pref.top(); pref.pop(); }
    }
    return -1;
}

int main() {
    int q;
    if (scanf("%d", &q) != 1) return 0;
    while (q--) {
        scanf("%d %lld", &n, &t);
        a.assign(n, 0); b.assign(n, 0); ord.resize(n);
        for (int i = 0; i < n; ++i) scanf("%lld %d", &a[i], &b[i]);
        iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int i, int j) { return b[i] < b[j]; });

        int lo = 0, hi = n;  // najveci izvediv x
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (provjeri(mid) >= 0) lo = mid; else hi = mid - 1;
        }
        int x = lo;
        vector<int> odabir;
        if (x > 0) {
            int i = provjeri(x);
            // rekonstrukcija: x-1 najjeftinijih ispred i, tema i, b_i - x najjeftinijih iza i
            vector<int> lijevo(ord.begin(), ord.begin() + i), desno(ord.begin() + i + 1, ord.end());
            auto poCijeni = [&](int p, int r) { return a[p] < a[r]; };
            sort(lijevo.begin(), lijevo.end(), poCijeni);
            sort(desno.begin(), desno.end(), poCijeni);
            int c = max(0, b[ord[i]] - x);
            odabir.assign(lijevo.begin(), lijevo.begin() + (x - 1));
            odabir.push_back(ord[i]);
            odabir.insert(odabir.end(), desno.begin(), desno.begin() + c);
        }
        printf("%d\n%d\n", x, (int)odabir.size());
        for (size_t j = 0; j < odabir.size(); ++j)
            printf("%d%c", odabir[j] + 1, j + 1 == odabir.size() ? '\n' : ' ');
        if (odabir.empty()) printf("\n");
    }
    return 0;
}
