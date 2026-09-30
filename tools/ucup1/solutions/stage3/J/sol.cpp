// UCup 1, Stage 3 (AMPPZ 2022), J. Job for a Hobbit
// Moguce je tocno kad sum_c ceil(cnt_c / k) <= n+2 (svaka boja treba toliko stupova).
// Konstrukcija u dvije faze:
//  1) "zbijeni" raspored: stupovi 0..n-1 puni, boje sortirane u redoslijedu citanja (stup po stup,
//     odozdo prema gore). Gradimo stup i dok su stupovi i, i+1 prazni, a desno je ostatak; trazeni
//     prsten "hodamo" ulijevo: par (rupa, stup s prstenom) pomicemo za jedan korak tako da sadrzaj
//     stupa lijevo od rupe prebacimo preko rupe udesno. Nakon svakog izgradenog stupa ostatak
//     zgusnemo udesno pa su opet dva stupa prazna.
//  2) Iz zbijenog rasporeda prstene obradujemo od zadnjeg prema prvom i svaki pomaknemo 0, 1 ili 2
//     stupa udesno na njegovo konacno mjesto (svaka boja zauzima ceil(cnt/k) stupova).
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<vector<int>> st;              // st[p] = prsteni na stupu p, odozdo prema gore
vector<pair<int, int>> potezi;

void pomak(int a, int b) {           // vrh stupa a -> vrh stupa b
    assert(abs(a - b) == 1 && !st[a].empty() && (int)st[b].size() < k);
    st[b].push_back(st[a].back()); st[a].pop_back();
    potezi.push_back({a, b});
}
void isprazni(int a, int b) { while (!st[a].empty()) pomak(a, b); }

int main() {
    int z;
    if (scanf("%d", &z) != 1) return 0;
    while (z--) {
        if (scanf("%d %d", &n, &k) != 2) return 0;
        st.assign(n + 2, {});
        map<int, int> cnt;
        for (int i = 1; i <= n; ++i) for (int j = 0; j < k; ++j) {
            int a; if (scanf("%d", &a) != 1) return 0;
            st[i].push_back(a); ++cnt[a];
        }
        long long stupova = 0;
        for (auto &pr : cnt) stupova += (pr.second + k - 1) / k;
        if (stupova > n + 2) { printf("NIE\n"); continue; }
        potezi.clear();
        if (k == 1) { printf("TAK\n0\n"); continue; }
        // ciljni zbijeni niz b (redoslijed citanja) i konacni stup svakog prstena u nizu
        vector<int> b, cilj;
        int stup = 0;
        for (auto &pr : cnt) {
            for (int t = 0; t < pr.second; ++t) { b.push_back(pr.first); cilj.push_back(stup + t / k); }
            stup += (pr.second + k - 1) / k;
        }
        // faza 1: sve pomakni udesno za jedan stup (stupovi 0 i 1 prazni, 2..n+1 puni)
        for (int p = n; p >= 1; --p) isprazni(p, p + 1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < k; ++j) {
                int v = b[i * k + j];
                // najljevlji stup desno od rupe koji sadrzi v; u njemu najvisi takav prsten
                int x = -1, y = -1;
                for (int p = i + 2; p <= n + 1 && x < 0; ++p)
                    for (int h = (int)st[p].size() - 1; h >= 0; --h)
                        if (st[p][h] == v) { x = p; y = h + 1; break; }
                assert(x >= 0);
                for (int p = i + 2; p < x; ++p) isprazni(p, p - 1);      // rupa dolazi na x-1
                int p = x;
                while (p > i + 2) {
                    // rupa je p-1 (prazan), v je na visini y stupa p
                    if (y == 1 && (int)st[p].size() == k) {
                        // poseban slucaj: v na dnu punog stupa; oslobodi jedno mjesto na p-2
                        int w = p - 2;
                        while ((int)st[w].size() == k) --w;             // stup i sigurno nije pun
                        for (int q = w + 1; q <= p - 2; ++q) pomak(q, q - 1);
                        pomak(p, p - 1); pomak(p - 1, p - 2);
                        isprazni(p, p - 1);                              // v na vrhu p-1 (visina k-1)
                        while (!st[p - 2].empty()) { pomak(p - 2, p - 1); pomak(p - 1, p); }
                        for (int q = p - 3; q >= w; --q) pomak(q, q + 1);
                        isprazni(p - 2, p - 1);                          // najvise jedan prsten
                        y = k - 1;
                    } else {
                        while ((int)st[p].size() >= y) pomak(p, p - 1);  // sve od v nagore -> p-1
                        y = st[p - 1].size();
                        while (!st[p - 2].empty()) {
                            pomak(p - 2, p - 1);
                            if ((int)st[p].size() < k) pomak(p - 1, p);
                        }
                    }
                    --p;
                }
                // p == i+2, rupa je i+1
                while ((int)st[p].size() >= y) pomak(p, p - 1);
                pomak(i + 1, i);
                isprazni(i + 1, i + 2);
            }
            // zgusni ostatak udesno: k slobodnih mjesta desnog dijela skupi se u stup i+2
            for (int p = n; p >= i + 2; --p)
                while (!st[p].empty() && (int)st[p + 1].size() < k) {
                    int x = p;
                    while (x < n + 1 && (int)st[x + 1].size() < k) { pomak(x, x + 1); ++x; }
                }
        }
        // faza 2: prsten na indeksu idx (stup idx/k) ide na stup cilj[idx] >= idx/k
        for (int idx = n * k - 1; idx >= 0; --idx) {
            int p = idx / k;
            assert(st[p].back() == b[idx]);
            for (int q = p; q < cilj[idx]; ++q) pomak(q, q + 1);
        }
        assert((int)potezi.size() <= 1000000);
        printf("TAK\n%d\n", (int)potezi.size());
        string out;
        for (auto &m : potezi) { out += to_string(m.first); out += ' '; out += to_string(m.second); out += '\n'; }
        fputs(out.c_str(), stdout);
    }
    return 0;
}
