// UCup 1, Stage 11 (EC-Final 2022), L. Aqre
// Gornja granica: ako se ploča može rastaviti na disjunktne pravokutnike 1x4, svaki sadrži nulu.
// Bojanje (i+j) mod 4: svaki 1x4 pokriva po jednu ćeliju svake boje, pa je (za n, m >= 4) najveći broj
// jedinica nm - min_c k_c; dostiže ga periodični uzorak 4x4 (jedna nula u svakom retku i stupcu),
// uz pravi pomak. Za n <= 3 (ili m <= 3) okomitih 1x4 nema: tada je optimum 2m - floor(m/2) (n = 2),
// odnosno 3m - floor(m/4) - floor(m/2) (n = 3), a ako su obje dimenzije <= 3, cijela ploča su jedinice.
// Sve konstrukcije se prije ispisa provjere (pravila + povezanost BFS-om).
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> g;

// vrijedi li ploča: nema 4 uzastopne jednake u retku/stupcu, jedinice povezane
bool valid() {
    for (int i = 0; i < n; i++)
        for (int j = 0; j + 3 < m; j++)
            if (g[i][j] == g[i][j + 1] && g[i][j] == g[i][j + 2] && g[i][j] == g[i][j + 3]) return false;
    for (int j = 0; j < m; j++)
        for (int i = 0; i + 3 < n; i++)
            if (g[i][j] == g[i + 1][j] && g[i][j] == g[i + 2][j] && g[i][j] == g[i + 3][j]) return false;
    int total = 0, sx = -1, sy = -1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (g[i][j] == '1') { total++; sx = i; sy = j; }
    if (total == 0) return false;
    vector<vector<char>> vis(n, vector<char>(m, 0));
    queue<pair<int, int>> q; q.push({sx, sy}); vis[sx][sy] = 1;
    int seen = 1;
    const int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int a = x + dx[d], b = y + dy[d];
            if (a < 0 || b < 0 || a >= n || b >= m || g[a][b] != '1' || vis[a][b]) continue;
            vis[a][b] = 1; seen++; q.push({a, b});
        }
    }
    return seen == total;
}

int countOnes() {
    int c = 0;
    for (auto& row : g) c += count(row.begin(), row.end(), '1');
    return c;
}

// n <= 3, m >= 4: redci 0..n-2 imaju nule na j = 3 (mod 4), zadnji redak na j = 1 (mod 4)
void buildThin() {
    g.assign(n, string(m, '1'));
    for (int i = 0; i < n; i++) {
        int z = (i == n - 1) ? 1 : 3;
        for (int j = z; j < m; j += 4) g[i][j] = '0';
    }
}

void transposeGrid() {
    vector<string> t(m, string(n, '1'));
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) t[j][i] = g[i][j];
    g = t; swap(n, m);
}

// periodični uzorak 4x4; nula u retku a (mod 4) stoji u stupcu ZC[a] (mod 4)
const int ZC[4] = {2, 3, 1, 0};

void solve() {
    if (n <= 3 && m <= 3) { g.assign(n, string(m, '1')); }
    else if (n <= 3) buildThin();
    else if (m <= 3) { swap(n, m); buildThin(); transposeGrid(); }
    else {
        int kc[4] = {0, 0, 0, 0};
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) kc[(i + j) & 3]++;
        int target = n * m - *min_element(kc, kc + 4);
        bool done = false;
        for (int dx = 0; dx < 4 && !done; dx++)
            for (int dy = 0; dy < 4 && !done; dy++) {
                g.assign(n, string(m, '1'));
                int ones = n * m;
                for (int i = 0; i < n; i++)
                    for (int j = (ZC[(i + dx) & 3] - dy + 4) & 3; j < m; j += 4) { g[i][j] = '0'; ones--; }
                if (ones == target && valid()) done = true;
            }
        assert(done);
    }
    assert(valid());
    printf("%d\n", countOnes());
    for (auto& row : g) puts(row.c_str());
}

int main() {
    int T; scanf("%d", &T);
    while (T--) { scanf("%d %d", &n, &m); solve(); }
    return 0;
}
