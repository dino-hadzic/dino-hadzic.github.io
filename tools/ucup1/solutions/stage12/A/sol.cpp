// A - XOR Tree Path
// DP na stablu: dp[v][p] = najveci broj crnih vrhova u podstablu v ako je
// paritet broja odabranih listova u podstablu v jednak p.
// Obrada ide u obrnutom BFS redoslijedu (bez rekurzije, N do 1e5).
#include <bits/stdc++.h>
using namespace std;

const long long NEG = -1e18;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    // BFS redoslijed od korijena 1
    vector<int> order, par(n + 1, 0);
    order.reserve(n);
    order.push_back(1);
    par[1] = -1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int u : g[v])
            if (u != par[v]) { par[u] = v; order.push_back(u); }
    }
    // cur[v] = najbolje kombinacije djece obradjene do sada, po paritetu
    vector<array<long long, 2>> cur(n + 1, {0, NEG}), dp(n + 1);
    vector<char> hasChild(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        if (!hasChild[v]) {
            // list: ne biramo ga (paritet 0) ili biramo (paritet 1, boja se mijenja)
            dp[v][0] = a[v];
            dp[v][1] = 1 - a[v];
        } else {
            // boja vrha v = a[v] xor paritet odabranih listova u njegovom podstablu
            for (int p = 0; p < 2; p++)
                dp[v][p] = cur[v][p] > NEG ? cur[v][p] + (a[v] ^ p) : NEG;
        }
        int p = par[v];
        if (p > 0) {
            // spajanje s roditeljem: paritet se XOR-a (knapsack po paritetu)
            hasChild[p] = 1;
            array<long long, 2> nxt = {NEG, NEG};
            for (int x = 0; x < 2; x++)
                for (int y = 0; y < 2; y++)
                    if (cur[p][x] > NEG && dp[v][y] > NEG)
                        nxt[x ^ y] = max(nxt[x ^ y], cur[p][x] + dp[v][y]);
            cur[p] = nxt;
        }
    }
    printf("%lld\n", max(dp[1][0], dp[1][1]));
}
