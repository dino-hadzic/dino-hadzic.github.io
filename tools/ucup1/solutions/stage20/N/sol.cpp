// UCup 1, Stage 20 (India), N. Red Black Grid
// Sve "neparne" celije (i+j neparno) su crne; parne celije nisu medjusobno susjedne,
// pa svaka crvena parna celija doprinosi tocno svoj stupanj (2, 3 ili 4).
// Treba podskup parnih celija sa zbrojem stupnjeva K. Ako je K > N(N-1) rijesimo
// za 2N(N-1) - K i uzmemo komplement (zbroj svih stupnjeva parnih celija je 2N(N-1)).
// Zatim biramo a celija stupnja 4, b stupnja 3, c stupnja 2 s 4a+3b+2c = K.
// N <= 3: gruba sila po svim 2^(N^2) bojanja.
#include <bits/stdc++.h>
using namespace std;

int n;

int prebroji(const vector<string>& g) {
    int k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (i + 1 < n && g[i][j] != g[i + 1][j]) k++;
            if (j + 1 < n && g[i][j] != g[i][j + 1]) k++;
        }
    return k;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        long long K;
        scanf("%d %lld", &n, &K);
        vector<string> g(n, string(n, 'B'));
        if (n <= 3) {
            bool nadjeno = false;
            for (int mask = 0; mask < (1 << (n * n)) && !nadjeno; mask++) {
                for (int c = 0; c < n * n; c++) g[c / n][c % n] = (mask >> c & 1) ? 'R' : 'B';
                if (prebroji(g) == K) nadjeno = true;
            }
            if (!nadjeno) { puts("Impossible"); continue; }
            puts("Possible");
            for (auto& r : g) puts(r.c_str());
            continue;
        }
        long long total = 2LL * n * (n - 1);
        bool komplement = false;
        if (K > total / 2) { K = total - K; komplement = true; }
        // parne celije po stupnju
        vector<pair<int, int>> st[5];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if ((i + j) % 2 == 0) {
                    int d = (i > 0) + (i < n - 1) + (j > 0) + (j < n - 1);
                    st[d].push_back({i, j});
                }
        long long c4 = st[4].size(), c3 = st[3].size(), c2 = st[2].size();
        long long A = -1, B = -1, C = -1;
        for (long long a = min(c4, K / 4); a >= 0 && A < 0; a--) {
            long long r = K - 4 * a;
            // trazimo b <= c3 s r - 3b paran, 0 <= (r-3b)/2 <= c2
            long long bmin = max(0LL, (r - 2 * c2 + 2) / 3);   // ceil((r-2c2)/3)
            if ((r - 3 * bmin) % 2 != 0) bmin++;
            if (bmin <= c3 && 3 * bmin <= r) { A = a; B = bmin; C = (r - 3 * bmin) / 2; }
        }
        if (A < 0) { puts("Impossible"); continue; }
        vector<vector<char>> crvena(n, vector<char>(n, 0));
        for (int i = 0; i < A; i++) crvena[st[4][i].first][st[4][i].second] = 1;
        for (int i = 0; i < B; i++) crvena[st[3][i].first][st[3][i].second] = 1;
        for (int i = 0; i < C; i++) crvena[st[2][i].first][st[2][i].second] = 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if ((i + j) % 2 == 0 && (crvena[i][j] ^ komplement)) g[i][j] = 'R';
        puts("Possible");
        for (auto& r : g) puts(r.c_str());
    }
    return 0;
}
