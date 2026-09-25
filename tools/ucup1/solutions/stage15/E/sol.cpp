// UCup 1, Stage 15 (ZJCPC 2023), E. Puzzle: Tapa
// Svaki trag ima 0 ili točno 1 neosjenčanu susjednu ćeliju. Ćelija između dva susjedna traga
// (jedna neparna koordinata) neosjenčana = ta dva traga „uparena”. Ćeliju s četiri dijagonalna
// traga nikad ne treba prazniti (zamijeni se s dvije ćelije-parovi). Rubni tragovi smiju imati
// prazninu samo uz rub (inače osjenčane nisu uzastopne). => savršeno sparivanje „manjkavih”
// tragova u bipartitnom mrežastom grafu (Kuhnov algoritam).
#include <bits/stdc++.h>
using namespace std;

int n, m, R, C;
vector<string> g;
vector<vector<int>> adj;
vector<int> matchL, matchR, vis;
int timer_ = 0;

bool dfs(int u) {
    for (int v : adj[u]) {
        if (vis[v] == timer_) continue;
        vis[v] = timer_;
        if (matchR[v] < 0 || dfs(matchR[v])) { matchL[u] = v; matchR[v] = u; return true; }
    }
    return false;
}

int main() {
    scanf("%d %d", &n, &m);
    R = 2 * n - 1; C = 2 * m - 1;
    g.resize(R);
    for (int i = 0; i < R; ++i) { static char buf[128]; scanf("%s", buf); g[i] = buf; }
    auto id = [&](int a, int b) { return a * m + b; };          // trag (2a, 2b)
    auto naRubu = [&](int a, int b) { return a == 0 || a == n - 1 || b == 0 || b == m - 1; };
    // manjkav[a][b] = trag ima vrijednost za 1 manju od broja susjednih ćelija
    vector<vector<char>> manjkav(n, vector<char>(m, 0));
    for (int a = 0; a < n; ++a)
        for (int b = 0; b < m; ++b) {
            int r = 2 * a, c = 2 * b, susjeda = 0;
            for (int dr = -1; dr <= 1; ++dr)
                for (int dc = -1; dc <= 1; ++dc)
                    if ((dr || dc) && r + dr >= 0 && r + dr < R && c + dc >= 0 && c + dc < C) ++susjeda;
            manjkav[a][b] = (g[r][c] - '0' == susjeda - 1);
        }
    // dopušteni parovi: ortogonalno susjedni manjkavi tragovi; ako je ijedan rubni, ćelija između
    // njih mora ležati na rubu (oba su tada na istom rubu)
    adj.assign(n * m, {});
    int dr4[4] = {1, -1, 0, 0}, dc4[4] = {0, 0, 1, -1};
    for (int a = 0; a < n; ++a)
        for (int b = 0; b < m; ++b) {
            if (!manjkav[a][b] || (a + b) % 2) continue;          // lijeva strana: parna (a+b)
            for (int d = 0; d < 4; ++d) {
                int a2 = a + dr4[d], b2 = b + dc4[d];
                if (a2 < 0 || a2 >= n || b2 < 0 || b2 >= m || !manjkav[a2][b2]) continue;
                int cr = 2 * a + dr4[d], cc = 2 * b + dc4[d];      // ćelija između
                bool celijaNaRubu = cr == 0 || cr == R - 1 || cc == 0 || cc == C - 1;
                if ((naRubu(a, b) || naRubu(a2, b2)) && !celijaNaRubu) continue;
                adj[id(a, b)].push_back(id(a2, b2));
            }
        }
    matchL.assign(n * m, -1); matchR.assign(n * m, -1); vis.assign(n * m, 0);
    int manjkavih = 0, sparenih = 0;
    for (int a = 0; a < n; ++a)
        for (int b = 0; b < m; ++b) manjkavih += manjkav[a][b];
    for (int a = 0; a < n; ++a)
        for (int b = 0; b < m; ++b)
            if (manjkav[a][b] && (a + b) % 2 == 0) { ++timer_; if (dfs(id(a, b))) ++sparenih; }
    if (2 * sparenih != manjkavih) { puts("NO"); return 0; }
    // sve ćelije bez traga osjenčane, osim ćelija između sparenih tragova
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (g[i][j] == '.') g[i][j] = '#';
    for (int u = 0; u < n * m; ++u)
        if (matchL[u] >= 0) {
            int a = u / m, b = u % m, a2 = matchL[u] / m, b2 = matchL[u] % m;
            g[a + a2][b + b2] = '.';    // (2a+2a2)/2, (2b+2b2)/2
        }
    puts("YES");
    for (int i = 0; i < R; ++i) puts(g[i].c_str());
    return 0;
}
