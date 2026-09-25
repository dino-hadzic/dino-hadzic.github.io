// UCup 1, Stage 16, zadatak I: Classical Minimization Problem
// Neka je k najveci broj tocaka na jednom (horizontalnom ili vertikalnom) pravcu.
// Ako je k <= n, moguce je 0 prijateljskih parova; inace ih je barem k - n
// (k tocaka istog pravca, a samo 2n - k tocaka izvan njega), i toliko se postize.
// Gradimo neprijateljske parove jedan po jedan, uvijek "gaseci" pravce koji imaju
// tocno n tocaka (jer bi inace u sljedecem koraku, s n-1 parova, bio k > n).
// Pravce drzimo u uredenom skupu po broju tocaka, pa je svaki korak O(log n).
#include <bits/stdc++.h>
using namespace std;

// Skup pravaca jedne orijentacije; pravci poredani po trenutnom broju zivih tocaka.
struct Pravci {
    vector<vector<int>> tocke;   // tocke[l] = zive tocke na pravcu l
    vector<int> pos;             // pozicija tocke u svojoj listi (za brisanje u O(1))
    vector<int> cnt;             // trenutni broj zivih tocaka na pravcu
    set<pair<int, int>> poredak; // (cnt, pravac) za pravce s cnt > 0

    void init(int L, int P) {
        tocke.assign(L, {});
        cnt.assign(L, 0);
        pos.assign(P, 0);
    }
    void dodaj(int l, int p) { pos[p] = tocke[l].size(); tocke[l].push_back(p); }
    void zavrsi() {
        for (size_t l = 0; l < tocke.size(); ++l) {
            cnt[l] = tocke[l].size();
            poredak.insert({cnt[l], (int)l});
        }
    }
    // makni tocku p s pravca l
    void ukloni(int l, int p) {
        poredak.erase({cnt[l], l});
        vector<int>& lst = tocke[l];
        int q = lst.back();
        lst[pos[p]] = q; pos[q] = pos[p];
        lst.pop_back();
        if (--cnt[l] > 0) poredak.insert({cnt[l], l});
    }
    int najveci() const { return poredak.rbegin()->second; }
    int drugiNajveci() const { return next(poredak.rbegin())->second; }
    // bilo koja tocka pravca l razlicita od "osim" (pravac tada ima >= 2 tocke)
    int tocka(int l, int osim = -1) const {
        const vector<int>& lst = tocke[l];
        return lst.back() != osim ? lst.back() : lst[lst.size() - 2];
    }
};

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n;
        scanf("%d", &n);
        int P = 2 * n;
        vector<long long> xs(P), ys(P);
        for (int i = 0; i < P; ++i) scanf("%lld %lld", &xs[i], &ys[i]);

        vector<long long> sx(xs), sy(ys);
        sort(sx.begin(), sx.end()); sx.erase(unique(sx.begin(), sx.end()), sx.end());
        sort(sy.begin(), sy.end()); sy.erase(unique(sy.begin(), sy.end()), sy.end());
        vector<int> px(P), py(P);  // indeks vertikalnog / horizontalnog pravca tocke
        Pravci V, H;
        V.init(sx.size(), P);
        H.init(sy.size(), P);
        for (int i = 0; i < P; ++i) {
            px[i] = lower_bound(sx.begin(), sx.end(), xs[i]) - sx.begin();
            py[i] = lower_bound(sy.begin(), sy.end(), ys[i]) - sy.begin();
            V.dodaj(px[i], i);
            H.dodaj(py[i], i);
        }
        V.zavrsi(); H.zavrsi();

        vector<char> ziv(P, 1);
        auto obrisi = [&](int p) {
            ziv[p] = 0;
            V.ukloni(px[p], p);
            H.ukloni(py[p], p);
        };

        vector<pair<int, int>> parovi;
        int zivih = P;
        // 1) neprijateljski parovi dok je to moguce
        while (zivih > 0) {
            int h = H.najveci(), v = V.najveci();
            if (H.cnt[h] == zivih || V.cnt[v] == zivih) break;  // sve na jednom pravcu
            int a, b;
            if (H.cnt[h] == 1 && px[H.tocka(h)] == v) {
                // jedina tocka na H lezi na V: uparimo je s tockom drugog najveceg vertikalnog pravca
                a = H.tocka(h);
                b = V.tocka(V.drugiNajveci());
            } else if (V.cnt[v] == 1 && py[V.tocka(v)] == h) {
                a = V.tocka(v);
                b = H.tocka(H.drugiNajveci());
            } else {
                // h-tocka koja nije na V i v-tocka koja nije na H; ako je sjeciste
                // jedina tocka pravca, gornje grane su to vec rijesile
                a = H.tocka(h);
                if (px[a] == v) a = H.tocka(h, a);
                b = V.tocka(v);
                if (py[b] == h) b = V.tocka(v, b);
            }
            obrisi(a); obrisi(b);
            zivih -= 2;
            parovi.push_back({a, b});
        }
        // 2) preostale tocke su sve na jednom pravcu: uparimo ih proizvoljno
        int k = 0;
        vector<int> ostatak;
        for (int i = 0; i < P; ++i) if (ziv[i]) ostatak.push_back(i);
        for (size_t i = 0; i + 1 < ostatak.size(); i += 2) {
            parovi.push_back({ostatak[i], ostatak[i + 1]});
            ++k;
        }
        printf("%d\n", k);
        for (auto [a, b] : parovi) printf("%d %d\n", a + 1, b + 1);
    }
    return 0;
}
