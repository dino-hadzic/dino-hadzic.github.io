// UCup 1, Stage 9 (Qingdao 2018), K. Airdrop
// Igrač ide prvo vertikalno do reda y0, zatim horizontalno. Dva igrača se mogu sresti samo ako imaju
// istu Manhattan udaljenost d do cilja i s iste su strane (lijevo/desno od x0). Za lijevu stranu klasa
// k = |y - y0| - x ne ovisi o x0, pa sweep po x slijeva: u stupcu x klasa k preživi točno ako je
// (živi iz klase) + (novi u stupcu) == 1. Simetrično zdesna. Kandidati za x0: x_i - 1, x_i, x_i + 1.
#include <bits/stdc++.h>
using namespace std;

const int OFF = 100005;      // pomak za negativne ključeve

int main() {
    int T;
    scanf("%d", &T);
    vector<char> zivL(3 * OFF, 0), zivR(3 * OFF, 0);
    vector<int> novi(3 * OFF, 0);
    while (T--) {
        int n, y0;
        scanf("%d %d", &n, &y0);
        vector<pair<int, int>> p(n);                    // (x, |y - y0|)
        for (auto &q : p) { int x, y; scanf("%d %d", &x, &y); q = {x, abs(y - y0)}; }
        sort(p.begin(), p.end());
        // stupci: [st[c], st[c+1]) u p
        vector<int> st;
        for (int i = 0; i < n; i++) if (i == 0 || p[i].first != p[i - 1].first) st.push_back(i);
        st.push_back(n);
        int C = st.size() - 1;
        vector<int> xs(C);
        for (int c = 0; c < C; c++) xs[c] = p[st[c]].first;

        // obradi stupac c za jednu stranu; kljuc(dy, x) ovisi o strani
        auto obradi = [&](int c, vector<char> &ziv, int &brojZivih, bool lijevo) {
            int x = xs[c];
            for (int i = st[c]; i < st[c + 1]; i++) {
                int k = (lijevo ? p[i].second - x : p[i].second + x) + OFF;
                novi[k]++;
            }
            for (int i = st[c]; i < st[c + 1]; i++) {
                int k = (lijevo ? p[i].second - x : p[i].second + x) + OFF;
                if (novi[k] == 0) continue;               // već obrađena klasa
                int ukupno = ziv[k] + novi[k];
                novi[k] = 0;
                if (ukupno == 1) { if (!ziv[k]) { ziv[k] = 1; brojZivih++; } }
                else if (ziv[k]) { ziv[k] = 0; brojZivih--; }
            }
        };
        // R[c] = broj preživjelih zdesna kad su obrađeni svi stupci > c  (c = -1..C-1), tj. za x0 < xs[c+1]
        vector<int> Rprefix(C + 1, 0);                    // Rprefix[c] = preživjeli iz stupaca c..C-1
        int zivihR = 0;
        for (int c = C - 1; c >= 0; c--) { obradi(c, zivR, zivihR, false); Rprefix[c] = zivihR; }
        for (int c = 0; c < C; c++) {                     // očisti
            for (int i = st[c]; i < st[c + 1]; i++) { int k = p[i].second + xs[c] + OFF; if (zivR[k]) { zivR[k] = 0; } }
        }
        // sweep slijeva po kandidatima x0
        vector<int> kand;
        for (int c = 0; c < C; c++) { kand.push_back(xs[c] - 1); kand.push_back(xs[c]); kand.push_back(xs[c] + 1); }
        sort(kand.begin(), kand.end());
        kand.erase(unique(kand.begin(), kand.end()), kand.end());
        int zivihL = 0, c = 0;                            // c = prvi stupac s xs >= x0 (još neobrađen)
        int pmin = INT_MAX, pmax = INT_MIN;
        for (int x0 : kand) {
            while (c < C && xs[c] < x0) { obradi(c, zivL, zivihL, true); c++; }
            int ans = zivihL;
            int cd = c;                                   // stupci strogo desno od x0 počinju od cd (ili cd+1 ako xs[c] == x0)
            if (cd < C && xs[cd] == x0) { ans += st[cd + 1] - st[cd]; cd++; }
            ans += (cd < C) ? Rprefix[cd] : 0;
            pmin = min(pmin, ans); pmax = max(pmax, ans);
        }
        for (int cc = 0; cc < C; cc++) {                  // očisti
            for (int i = st[cc]; i < st[cc + 1]; i++) { int k = p[i].second - xs[cc] + OFF; zivL[k] = 0; }
        }
        printf("%d %d\n", pmin, pmax);
    }
    return 0;
}
