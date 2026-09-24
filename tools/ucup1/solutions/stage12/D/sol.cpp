// C/D - Parallel Processing
// Optimalan broj koraka: L = max(ceil(log2 N), ceil(2(N-1)/5)).
// N <= 8: klasicna shema "parovi -> prefiksi polovica -> spajanje" u <= 3 koraka.
// N >= 9: blokovska konstrukcija s L+1 blokova (blok 1 = {1}). Svaka operacija
// je oblika A[x] <- A[y] + A[x]:
//   * lancane op. bloka t:  A[x] <- A[x-1] + A[x]  (A[x] = [l_t, x]), gotove do koraka t-2;
//   * "P" op. bloka t u koraku t-1: A[r_t] <- A[r_{t-1}] + A[r_t] = [1, r_t];
//   * zavrsne op. bloka t (koraci >= t-1): A[x] <- A[r_{t-1}] + A[x] = [1, x].
// Ukupno 2N-2-L operacija <= 4L. Raspored: u svakom koraku P op., zatim lancane
// op. po najranijem roku (EDF), zatim zavrsne op. koje cekaju.
#include <bits/stdc++.h>
using namespace std;

struct Op { int c, a, b; };

int Lopt(int N) {
    int lg = 0;
    while ((1 << lg) < N) lg++;
    return max(lg, (2 * (N - 1) + 4) / 5);
}

int main() {
    int N;
    scanf("%d", &N);
    int L = Lopt(N);
    vector<vector<Op>> steps(L);
    if (N <= 8) {
        // shema za 8 elemenata; ispustamo operacije s indeksom > N
        vector<vector<Op>> full = {
            {{2, 1, 2}, {4, 3, 4}, {6, 5, 6}, {8, 7, 8}},
            {{3, 2, 3}, {4, 2, 4}, {7, 6, 7}, {8, 6, 8}},
            {{5, 4, 5}, {6, 4, 6}, {7, 4, 7}, {8, 4, 8}}};
        int s = 0;
        for (auto &st : full) {
            vector<Op> cur;
            for (auto &o : st) if (o.c <= N) cur.push_back(o);
            if (!cur.empty()) steps[s++] = cur;
        }
    } else {
        // velicine blokova 2..L+1: sto ravnomjernije, visak (+1) rasporeden
        // jednoliko od pocetka, uz ogranicenje m_t <= t-1 (visak guramo naprijed)
        vector<int> m(L + 2, 0), l(L + 2, 0), r(L + 2, 0);
        m[1] = 1;
        int tot = N - 1, cnt = L, base = tot / cnt, rem = tot % cnt;
        for (int t = 2; t <= L + 1; t++) m[t] = base;
        for (int i = 0; i < rem; i++) m[2 + (i * cnt) / rem]++;
        for (int t = 2; t <= L; t++)
            if (m[t] > t - 1) { m[t + 1] += m[t] - (t - 1); m[t] = t - 1; }
        l[1] = r[1] = 1;
        for (int t = 2; t <= L + 1; t++) { l[t] = r[t - 1] + 1; r[t] = r[t - 1] + m[t]; }
        vector<int> chainLeft(L + 2), chainPos(L + 2);
        for (int t = 2; t <= L + 1; t++) { chainLeft[t] = m[t] - 1; chainPos[t] = l[t]; }
        deque<pair<int, int>> fin;  // (blok, x) zavrsne operacije koje cekaju
        for (int j = 1; j <= L; j++) {
            vector<Op> &ops = steps[j - 1];
            int t = j + 1;
            ops.push_back({r[t], r[t - 1], r[t]});  // P_t = [1, r_t]
            for (int x = l[t]; x < r[t]; x++) fin.push_back({t, x});
            for (int tt = j + 2; tt <= L + 1 && ops.size() < 4; tt++) {
                if (chainLeft[tt] == 0) continue;
                int x = chainPos[tt] + 1;
                ops.push_back({x, x - 1, x});
                chainPos[tt] = x; chainLeft[tt]--;
            }
            while (ops.size() < 4 && !fin.empty()) {
                auto [tt, x] = fin.front(); fin.pop_front();
                ops.push_back({x, r[tt - 1], x});
            }
        }
    }
    printf("%d\n", L);
    for (auto &st : steps) {
        for (int i = 0; i < 4; i++) {
            if (i < (int)st.size()) printf("%d %d %d\n", st[i].c, st[i].a, st[i].b);
            else printf("2000 2000 2000\n");
        }
    }
}
