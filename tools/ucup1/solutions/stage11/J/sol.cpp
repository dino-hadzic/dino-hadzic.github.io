// UCup 1, Stage 11 (EC-Final 2022), J. Chase Game 2
// Pang hvata Shoua iz nekog početnog para točno onda kad postoji vrh v i vrh u != v
// takav da je N[v] podskup N[u] ("kut"). U stablu su kutovi upravo listovi.
// Zvijezda (uklj. n = 2): -1. Inače je odgovor max(ceil(s/2), mx), gdje je s broj
// listova, a mx najveći broj listova s istim susjedom.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        vector<int> deg(n + 1, 0), nb(n + 1, 0);   // nb[v] = neki susjed lista v
        vector<pair<int, int>> e(n - 1);
        for (auto &[u, v] : e) {
            scanf("%d %d", &u, &v);
            deg[u]++; deg[v]++;
        }
        for (auto [u, v] : e) { nb[u] = v; nb[v] = u; }  // za list je to jedini susjed

        vector<int> cnt(n + 1, 0);                  // broj listova po roditelju
        int s = 0, mx = 0;
        for (int v = 1; v <= n; v++)
            if (deg[v] == 1) { s++; mx = max(mx, ++cnt[nb[v]]); }

        // zvijezda: neki vrh je susjed svih ostalih (n - 1 listova s istim roditeljem, ili n = 2)
        if (n == 2 || mx == n - 1) { puts("-1"); continue; }
        printf("%d\n", max((s + 1) / 2, mx));
    }
    return 0;
}
