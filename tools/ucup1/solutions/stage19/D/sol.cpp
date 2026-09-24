// UCup 1, Stage 19 (NAC 2023), D. Fail Fast
// Očekivani trošak E(S) = sum_i c_i * P_{i-1} - C_n * P_n (Abelova sumacija), pa minimiziramo
// F(S) = sum_i c_i * P_{i-1} = očekivani zbroj troškova stvarno izvedenih testova.
// Bez ovisnosti: susjedna zamjena daje poredak po omjeru rho = c / (1 - p) (rastuće).
// S ovisnostima (šuma, roditelj prije djeteta): jedinica T s najmanjim rho među preostalima
// u nekom optimalnom rasporedu ide odmah nakon svoje roditeljske jedinice (blok između ima
// rho >= rho(T) jer je rho spoja "medijanta" pa leži između rho-ova dijelova). Zato:
//   - ako T nema roditelja ili je on izveden, T izvodimo odmah;
//   - inače T spajamo s roditeljem P u jedinicu (P pa T): c = c_P + p_P c_T, p = p_P p_T.
// Prioritetni red po rho s lijenim brisanjem, unija-pronađi za "u kojoj je jedinici test",
// povezane liste za redoslijed testova unutar jedinice. O(n log n).
#include <bits/stdc++.h>
using namespace std;

int n;
vector<double> c, p;
vector<int> d, dsu, glava, rep, sljedeci, verzija;
vector<char> izveden;

int nadji(int x) {
    while (dsu[x] != x) { dsu[x] = dsu[dsu[x]]; x = dsu[x]; }
    return x;
}

double omjer(int u) { return c[u] / (1.0 - p[u]); }

int main() {
    if (scanf("%d", &n) != 1) return 0;
    c.assign(n + 1, 0); p.assign(n + 1, 0); d.assign(n + 1, 0);
    dsu.resize(n + 1); glava.resize(n + 1); rep.resize(n + 1); sljedeci.assign(n + 1, 0);
    verzija.assign(n + 1, 0); izveden.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        if (scanf("%lf %lf %d", &c[i], &p[i], &d[i]) != 3) return 0;
        dsu[i] = i; glava[i] = rep[i] = i;
    }
    // (omjer, jedinica, verzija) – najmanji omjer na vrhu
    priority_queue<tuple<double, int, int>, vector<tuple<double, int, int>>, greater<>> red;
    for (int i = 1; i <= n; ++i) red.push({omjer(i), i, 0});

    vector<int> izlaz;
    izlaz.reserve(n);
    while (!red.empty()) {
        auto [r, u, ver] = red.top();
        red.pop();
        if (nadji(u) != u || verzija[u] != ver) continue;      // zastarjeli zapis
        int rod = d[u] ? nadji(d[u]) : 0;                        // roditeljska jedinica korijena
        if (rod == 0 || izveden[rod]) {
            // izvedi cijelu jedinicu redom
            izveden[u] = 1;
            for (int x = glava[u]; x; x = sljedeci[x]) izlaz.push_back(x);
        } else {
            // spoji u -> rod (rod pa u)
            c[rod] = c[rod] + p[rod] * c[u];
            p[rod] = p[rod] * p[u];
            sljedeci[rep[rod]] = glava[u];
            rep[rod] = rep[u];
            dsu[u] = rod;
            ++verzija[rod];
            red.push({omjer(rod), rod, verzija[rod]});
        }
    }
    string out;
    out.reserve(n * 7);
    for (int x : izlaz) { out += to_string(x); out += '\n'; }
    fputs(out.c_str(), stdout);
    return 0;
}
