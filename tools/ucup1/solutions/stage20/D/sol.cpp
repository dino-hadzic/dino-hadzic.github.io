// UCup 1, Stage 20 (India), D. Central Subset
// Odgovor uvijek postoji. Uzmemo BFS razapinjuce stablo (udaljenosti u grafu su <= onima u stablu),
// s = ceil(sqrt N). Obradjujemo vrhove od najdubljih prema korijenu i pamtimo h[v] = udaljenost
// do najdaljeg jos nepokrivenog vrha u podstablu (-1 ako ga nema). Kad h[v] dosegne s, stavimo v
// u S: pokriva cijelo podstablo, a "trosi" barem s+1 vrhova (lanac do najdubljeg). Na kraju, ako
// je nesto ostalo nepokriveno, dodamo korijen. Ukupno |S| <= floor(N/(s+1)) + 1 <= s.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<vector<int>> adj(n + 1);
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int s = 0;
        while ((long long)s * s < n) s++;           // s = ceil(sqrt(n))
        vector<int> par(n + 1, 0), red;
        vector<char> vid(n + 1, 0);
        red.push_back(1); vid[1] = 1;
        for (size_t i = 0; i < red.size(); i++) {  // BFS razapinjuce stablo
            int v = red[i];
            for (int w : adj[v]) if (!vid[w]) { vid[w] = 1; par[w] = v; red.push_back(w); }
        }
        vector<int> h(n + 1, 0);                    // 0 = sam vrh je nepokriven
        vector<int> S;
        for (int i = n - 1; i >= 1; i--) {          // obrnuti BFS redoslijed = djeca prije roditelja
            int v = red[i];
            if (h[v] == s) { S.push_back(v); h[v] = -1; }
            if (h[v] >= 0) h[par[v]] = max(h[par[v]], h[v] + 1);
        }
        if (h[1] >= 0) S.push_back(1);
        printf("%d\n", (int)S.size());
        for (size_t i = 0; i < S.size(); i++) printf("%d%c", S[i], i + 1 == S.size() ? '\n' : ' ');
    }
    return 0;
}
