// F. LaLa and Monster Hunting (Part 2)
// Uzorak: trokut {a,b,c} + rep c-d-e-f (jednostavan put duljine 3 iz c).
// Za svaki trokut i svaki izbor vrha c zbrajamo broj puteva c-d-e-f koji
// izbjegavaju a i b: P(c) - (putevi kroz a) - (putevi kroz b) + (putevi kroz oba).
// Sve potrebne veličine su lokalne: stupnjevi, broj trokuta po bridu tri(uv),
// broj 4-ciklusa po bridu c4(uv) i Q(v) = sum_{e~v} (deg(e)-1).
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll MOD = 998244353;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<int> eu(m), ev(m), deg(n, 0);
    for (int i = 0; i < m; i++) { scanf("%d %d", &eu[i], &ev[i]); deg[eu[i]]++; deg[ev[i]]++; }

    // poredak po stupnju: rank[v]; brid usmjeravamo od manjeg prema većem ranku
    vector<int> ord(n), rnk(n);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) { return deg[a] != deg[b] ? deg[a] < deg[b] : a < b; });
    for (int i = 0; i < n; i++) rnk[ord[i]] = i;

    vector<vector<pair<int, int>>> adj(n), out(n);   // (susjed, id brida)
    for (int i = 0; i < m; i++) {
        adj[eu[i]].push_back({ev[i], i}); adj[ev[i]].push_back({eu[i], i});
        if (rnk[eu[i]] < rnk[ev[i]]) out[eu[i]].push_back({ev[i], i}); else out[ev[i]].push_back({eu[i], i});
    }

    // Q(v) = sum_{e ~ v} (deg(e) - 1)
    vector<ll> Q(n, 0);
    for (int v = 0; v < n; v++) for (auto [e, id] : adj[v]) Q[v] += deg[e] - 1;

    // tri(id): broj trokuta koji sadrže brid id; usput popis trokuta (bridovi)
    vector<ll> tri(m, 0);
    vector<array<int, 3>> triangles;   // (id ab, id bc, id ca) s vrhovima u, v, w
    vector<array<int, 3>> triV;
    vector<int> mark(n, -1);
    for (int u = 0; u < n; u++) {
        for (auto [v, id] : out[u]) mark[v] = id;
        for (auto [v, idUV] : out[u])
            for (auto [w, idVW] : out[v])
                if (mark[w] >= 0) {
                    int idUW = mark[w];
                    tri[idUV]++; tri[idVW]++; tri[idUW]++;
                    triangles.push_back({idUV, idVW, idUW});
                    triV.push_back({u, v, w});
                }
        for (auto [v, id] : out[u]) mark[v] = -1;
    }

    // c4(id): broj 4-ciklusa koji sadrže brid id.
    // Za svaki vrh u i sve puteve u-v-w s rank(v), rank(w) < rank(u): cnt[w] = broj
    // takvih puteva; svaki par puteva do istog w je 4-ciklus s maksimumom u,
    // pa bridovi uv i vw dobivaju cnt[w]-1 ciklusa iz tog puta.
    vector<ll> c4(m, 0), cnt(n, 0);
    vector<int> touched;
    for (int u = 0; u < n; u++) {
        for (auto [v, idUV] : adj[u]) {
            if (rnk[v] >= rnk[u]) continue;
            for (auto [w, idVW] : adj[v]) {
                if (rnk[w] >= rnk[u]) continue;
                if (cnt[w] == 0) touched.push_back(w);
                cnt[w]++;
            }
        }
        for (auto [v, idUV] : adj[u]) {
            if (rnk[v] >= rnk[u]) continue;
            for (auto [w, idVW] : adj[v]) {
                if (rnk[w] >= rnk[u]) continue;
                c4[idUV] += cnt[w] - 1;
                c4[idVW] += cnt[w] - 1;
            }
        }
        for (int w : touched) cnt[w] = 0;
        touched.clear();
    }

    // P(c) = broj jednostavnih puteva c-d-e-f
    //      = sum_{d ~ c} ( Q(d) - (deg(c) - 1) - tri(cd) )
    vector<ll> P(n, 0);
    for (int c = 0; c < n; c++)
        for (auto [d, id] : adj[c]) P[c] += Q[d] - (deg[c] - 1) - tri[id];

    // putevi c-d-e-f koji prolaze kroz a (a ~ c): d = a, e = a ili f = a
    auto through = [&](int c, int a, int idCA) -> ll {
        ll dA = Q[a] - (deg[c] - 1) - tri[idCA];   // c-a-e-f
        ll eA = tri[idCA] * (deg[a] - 2);           // c-d-a-f, d zajednički susjed
        ll fA = c4[idCA];                           // c-d-e-a: 4-ciklus kroz brid ca
        return dA + eA + fA;
    };

    ll ans = 0;
    for (size_t t = 0; t < triangles.size(); t++) {
        int vs[3] = {triV[t][0], triV[t][1], triV[t][2]};
        // bridovi: e01 = (v0,v1), e12 = (v1,v2), e02 = (v0,v2)
        int e01 = triangles[t][0], e12 = triangles[t][1], e02 = triangles[t][2];
        for (int k = 0; k < 3; k++) {
            int c = vs[k], a = vs[(k + 1) % 3], b = vs[(k + 2) % 3];
            auto eid = [&](int x, int y) {
                if ((x == vs[0] && y == vs[1]) || (x == vs[1] && y == vs[0])) return e01;
                if ((x == vs[1] && y == vs[2]) || (x == vs[2] && y == vs[1])) return e12;
                return e02;
            };
            int idCA = eid(c, a), idCB = eid(c, b), idAB = eid(a, b);
            ll both = (deg[a] - 2) + (deg[b] - 2)          // c-a-b-f, c-b-a-f
                    + 2 * (tri[idAB] - 1)                   // c-a-e-b, c-b-e-a
                    + (tri[idCA] - 1) + (tri[idCB] - 1);    // c-d-a-b, c-d-b-a
            ll cur = P[c] - through(c, a, idCA) - through(c, b, idCB) + both;
            ans = (ans + cur) % MOD;
        }
    }
    printf("%lld\n", (ans % MOD + MOD) % MOD);
    return 0;
}
