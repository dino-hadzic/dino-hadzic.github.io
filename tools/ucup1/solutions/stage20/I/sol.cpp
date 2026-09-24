// UCup 1, Stage 20 (India), I. Disk Tree
// Rjesenje uvijek postoji. Sweep po x: disk "ulazi" na X = max(0, x_i - r_i) i "izlazi" na x_i + r_i.
// Aktivni diskovi sijeku pravac x = X u disjunktnim tetivama koje su poredane kao y-koordinate sredista,
// pa aktivni skup S drzimo u std::set-u sortiranom po y. Na svakom X najprije ubacimo SVE nove diskove,
// zatim za svaki maksimalni niz uzastopnih (u poretku S) novih diskova povucemo vertikalne segmente
// (X, y_u)-(X, y_v) izmedu susjeda unutar niza te jedan segment do starog susjeda (ispod ako postoji,
// inace iznad). Segment izmedu susjednih tetiva dira tocno ta dva diska, a segmenti na istom X se
// najvise dodiruju u krajnjim tockama. Na kraju su komponente = intervali unije x-projekcija; susjedne
// komponente spojimo segmentom od najdesnije tocke lijeve komponente do najljevije tocke desne, koji
// prolazi kroz "rupu" bez diskova. Ukupno n - 1 segmenata, sve koordinate u [0, 1e9].
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> x(n), y(n), r(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld %lld", &x[i], &y[i], &r[i]);
    // dogadaji: (X, tip, id); tip 0 = ulaz, 1 = izlaz; na istom X ulazi prije izlaza
    vector<array<ll, 3>> ev;
    for (int i = 0; i < n; i++) {
        ev.push_back({max(0LL, x[i] - r[i]), 0, i});
        ev.push_back({x[i] + r[i], 1, i});
    }
    sort(ev.begin(), ev.end());
    set<pair<ll, int>> S;                       // (y sredista, id)
    vector<array<ll, 4>> out;
    vector<int> kompStart;                      // najljeviji disk svake komponente (po redu)
    vector<int> kompKraj;                       // disk s najvecim x + r u komponenti
    vector<char> jeNov(n, 0);
    size_t p = 0;
    while (p < ev.size()) {
        ll X = ev[p][0];
        vector<int> novi;
        while (p < ev.size() && ev[p][0] == X && ev[p][1] == 0) novi.push_back(ev[p++][2]);
        if (!novi.empty()) {
            bool bioPrazan = S.empty();
            if (bioPrazan) { kompStart.push_back(novi[0]); kompKraj.push_back(novi[0]); }
            for (int i : novi) S.insert({y[i], i});
            sort(novi.begin(), novi.end(), [&](int a, int b) { return y[a] < y[b]; });
            for (int i : novi) jeNov[i] = 1;
            // obradi nizove uzastopnih novih diskova u poretku S
            for (size_t k = 0; k < novi.size();) {
                auto it = S.find({y[novi[k]], novi[k]});
                // dno niza: prethodnik u S nije nov (ili ne postoji)
                size_t k2 = k;
                auto jt = it;
                while (true) {
                    auto nx = next(jt);
                    if (nx == S.end() || !jeNov[nx->second]) break;
                    out.push_back({X, jt->first, X, nx->first});   // segment unutar niza
                    jt = nx; k2++;
                }
                if (!bioPrazan) {
                    if (it != S.begin()) { auto pr = prev(it); out.push_back({X, pr->first, X, it->first}); }
                    else { auto nx = next(jt); out.push_back({X, jt->first, X, nx->first}); }
                }
                k = k2 + 1;
            }
            for (int i : novi) jeNov[i] = 0;
        }
        while (p < ev.size() && ev[p][0] == X) {   // izlazi
            int i = ev[p++][2];
            S.erase({y[i], i});
            if (x[i] + r[i] > x[kompKraj.back()] + r[kompKraj.back()]) kompKraj.back() = i;
        }
    }
    for (size_t c = 1; c < kompStart.size(); c++) {
        int j = kompKraj[c - 1], k = kompStart[c];
        out.push_back({x[j] + r[j], y[j], x[k] - r[k], y[k]});
    }
    puts("YES");
    string s;
    char buf[100];
    for (auto& e : out) { sprintf(buf, "%lld %lld %lld %lld\n", e[0], e[1], e[2], e[3]); s += buf; }
    fputs(s.c_str(), stdout);
    return 0;
}
