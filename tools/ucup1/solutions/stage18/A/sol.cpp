// UCup 1, Stage 18, A: Is it well known in Poland?
// Igra "termita" na stablu. Blokovi vrhova s neto vrijednošću d i parnošću (neparan blok
// predaje potez, paran ga zadržava). Uvijek promatramo neparan blok s najvećim d:
//  - ako je korijen, igrač na potezu ga uzima (načelo pohlepnog poteza);
//  - inače ga spajamo s roditeljskim blokom p: neparan p -> paran, d_p - d_v;
//    paran p -> neparan, d_p + d_v (načelo fuzije).
// Na kraju preostaju samo parni blokovi (d <= 0) koje mora uzeti igrač na potezu.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<int> dsu;
int find(int x) {
    while (dsu[x] != x) {
        dsu[x] = dsu[dsu[x]];
        x = dsu[x];
    }
    return x;
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) if (scanf("%lld", &a[i]) != 1) return 0;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        if (scanf("%d %d", &u, &v) != 2) return 0;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    // roditelji BFS-om iz korijena 1
    vector<int> par(n + 1, 0);
    {
        vector<int> q = {1};
        vector<char> seen(n + 1, 0);
        seen[1] = 1;
        for (size_t i = 0; i < q.size(); i++) {
            int v = q[i];
            for (int u : adj[v])
                if (!seen[u]) {
                    seen[u] = 1;
                    par[u] = v;
                    q.push_back(u);
                }
        }
    }
    dsu.resize(n + 1);
    iota(dsu.begin(), dsu.end(), 0);
    vector<ll> d(a);            // neto vrijednost bloka (indeks = predstavnik)
    vector<char> odd(n + 1, 1);  // parnost bloka
    vector<char> removed(n + 1, 0);
    vector<int> head(n + 1);     // vršni vrh bloka (njegov roditelj daje roditeljski blok)
    iota(head.begin(), head.end(), 0);
    priority_queue<pair<ll, int>> pq;
    for (int v = 1; v <= n; v++) pq.push({a[v], v});
    ll net = 0;  // (A - B) do sada
    int sign = 1;  // +1 ako je A na potezu
    while (!pq.empty()) {
        auto [dv, v] = pq.top();
        pq.pop();
        if (find(v) != v || removed[v] || !odd[v] || dv != d[v]) continue;  // zastarjeli zapis
        int pp = par[head[v]];
        if (pp != 0) {
            pp = find(pp);
            if (removed[pp]) pp = 0;
        }
        if (pp == 0) {
            net += sign * d[v];
            sign = -sign;
            removed[v] = 1;
        } else if (odd[pp]) {
            d[pp] -= d[v];
            odd[pp] = 0;
            dsu[v] = pp;
        } else {
            d[pp] += d[v];
            odd[pp] = 1;
            dsu[v] = pp;
            pq.push({d[pp], pp});
        }
    }
    ll rest = 0;
    for (int v = 1; v <= n; v++)
        if (find(v) == v && !removed[v]) rest += d[v];
    net += sign * rest;
    ll total = 0;
    for (int v = 1; v <= n; v++) total += a[v];
    printf("%lld\n", (total + net) / 2);
    return 0;
}
