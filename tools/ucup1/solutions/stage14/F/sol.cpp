// F. LaLa and Monster Hunting (Part 2) – službeni pristup
// Čudovište: trokut {a,b,c} + rep c-d-e-f. Redom računamo:
//   1. tri(u)      – broj trokuta kroz vrh u
//   2. tri(e)      – broj trokuta kroz brid e
//   3. Dm(u->v)    – "romb": dva trokuta sa zajedničkim bridom (dijagonalom) v-w,
//                    u je vrh izvan dijagonale susjedan s v   (4 vrha, 5 bridova)
//   4. Hs(u->v)    – "kuća": 4-ciklus u-v-z-w + vrh t susjedan s v i z  (5 vrhova, 6 bridova)
//   5. L1(u), L2(u), L3(u) – broj (trokut, rep duljine 1/2/3) čiji rep završava u u.
// Odgovor je sum_u L3(u).  Složenost O(n + m sqrt m).
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll MOD = 998244353;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<int> eu(m), ev(m), deg(n, 0);
    for (int i = 0; i < m; i++) { scanf("%d %d", &eu[i], &ev[i]); deg[eu[i]]++; deg[ev[i]]++; }

    // usmjereni brid id "iz vrha from": indeks 2*id + (from == ev[id])
    auto dir = [&](int id, int from) { return 2 * id + (from == ev[id] ? 1 : 0); };

    // poredak po stupnju; brid usmjeravamo od manjeg prema većem ranku -> izlazni stupanj O(sqrt m)
    vector<int> ord(n), rnk(n);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) { return deg[a] != deg[b] ? deg[a] < deg[b] : a < b; });
    for (int i = 0; i < n; i++) rnk[ord[i]] = i;

    vector<vector<pair<int, int>>> adj(n), out(n);   // (susjed, id brida)
    for (int i = 0; i < m; i++) {
        adj[eu[i]].push_back({ev[i], i}); adj[ev[i]].push_back({eu[i], i});
        if (rnk[eu[i]] < rnk[ev[i]]) out[eu[i]].push_back({ev[i], i}); else out[ev[i]].push_back({eu[i], i});
    }

    // 1.+2. trokuti po vrhu i po bridu (svaki trokut nađen točno jednom: u < v < w po ranku)
    vector<ll> triV(n, 0), triE(m, 0);
    vector<int> mark(n, -1);
    for (int u = 0; u < n; u++) {
        for (auto [v, id] : out[u]) mark[v] = id;
        for (auto [v, idUV] : out[u])
            for (auto [w, idVW] : out[v])
                if (mark[w] >= 0) {
                    int idUW = mark[w];
                    triV[u]++; triV[v]++; triV[w]++;
                    triE[idUV]++; triE[idVW]++; triE[idUW]++;
                }
        for (auto [v, id] : out[u]) mark[v] = -1;
    }

    // 3. rombovi po usmjerenom bridu: Dm(x->y) = sum po trokutima {x,y,z} od (tri(yz) - 1).
    //    Usput badC(u) = broj (trokut T kroz u, trokut {u,d,e} disjunktan s T osim u), uređeno po (d,e).
    vector<ll> Dm(2 * m, 0), badC(n, 0);
    for (int u = 0; u < n; u++) {
        for (auto [v, id] : out[u]) mark[v] = id;
        for (auto [v, idUV] : out[u])
            for (auto [w, idVW] : out[v])
                if (mark[w] >= 0) {
                    int idUW = mark[w];
                    Dm[dir(idUV, u)] += triE[idVW] - 1;  Dm[dir(idUW, u)] += triE[idVW] - 1;
                    Dm[dir(idUV, v)] += triE[idUW] - 1;  Dm[dir(idVW, v)] += triE[idUW] - 1;
                    Dm[dir(idUW, w)] += triE[idUV] - 1;  Dm[dir(idVW, w)] += triE[idUV] - 1;
                    badC[u] += 2 * (triV[u] - triE[idUV] - triE[idUW] + 1);
                    badC[v] += 2 * (triV[v] - triE[idUV] - triE[idVW] + 1);
                    badC[w] += 2 * (triV[w] - triE[idUW] - triE[idVW] + 1);
                }
        for (auto [v, id] : out[u]) mark[v] = -1;
    }

    // 4. kuće. Prvo W(x->y) = sum po 4-ciklusima x-y-z-w od tri(yz)  (težinski 4-ciklusi po
    //    usmjerenom bridu), zatim Hs(x->y) = W(x->y) - Dm(x->y) - Dm(y->x) (izbacivanje
    //    slučajeva u kojima se peti vrh podudara s x odnosno s w).
    //    4-cikluse nabrajamo iz vrha najvećeg ranka h: putevi h-y-z s rank(y), rank(z) < rank(h),
    //    grupirani po z; svaki par puteva do istog z je jedan 4-ciklus.
    vector<ll> W(2 * m, 0);
    {
        vector<vector<array<int, 3>>> paths(n);   // paths[z] = (y, id hy, id yz)
        vector<int> touched;
        for (int h = 0; h < n; h++) {
            for (auto [y, idHY] : adj[h]) {
                if (rnk[y] >= rnk[h]) continue;
                for (auto [z, idYZ] : adj[y]) {
                    if (rnk[z] >= rnk[h]) continue;
                    if (paths[z].empty()) touched.push_back(z);
                    paths[z].push_back({y, idHY, idYZ});
                }
            }
            for (int z : touched) {
                auto &P = paths[z];
                ll cnt = P.size();
                if (cnt >= 2) {
                    ll Sh = 0, Sz = 0;
                    for (auto &p : P) { Sh += triE[p[1]]; Sz += triE[p[2]]; }
                    for (auto &p : P) {
                        int y = p[0], idHY = p[1], idYZ = p[2];
                        W[dir(idHY, h)] += (cnt - 1) * triE[idYZ];   // h->y, sljedeći z
                        W[dir(idHY, y)] += Sh - triE[idHY];          // y->h, sljedeći y'
                        W[dir(idYZ, y)] += Sz - triE[idYZ];          // y->z, sljedeći y'
                        W[dir(idYZ, z)] += (cnt - 1) * triE[idHY];   // z->y, sljedeći h
                    }
                }
                P.clear();
            }
            touched.clear();
        }
    }
    vector<ll> Hs(2 * m);
    for (int id = 0; id < m; id++) {
        ll both = Dm[2 * id] + Dm[2 * id + 1];
        Hs[2 * id] = W[2 * id] - both;
        Hs[2 * id + 1] = W[2 * id + 1] - both;
    }

    // 5. repovi duljine 1, 2, 3 koji završavaju u u
    vector<ll> L1(n, 0), L2(n, 0), L3(n, 0);
    for (int u = 0; u < n; u++)
        for (auto [c, id] : adj[u]) L1[u] += triV[c] - triE[id];
    for (int u = 0; u < n; u++) {
        ll s = 0, dmIn = 0;
        for (auto [d, id] : adj[u]) { s += L1[d]; dmIn += Dm[dir(id, d)]; }
        L2[u] = s - triV[u] * (deg[u] - 2) - dmIn;
    }
    ll ans = 0;
    for (int u = 0; u < n; u++) {
        ll s = 0, dmOut = 0, hsIn = 0;
        for (auto [e, id] : adj[u]) { s += L2[e]; dmOut += Dm[dir(id, u)]; hsIn += Hs[dir(id, e)]; }
        ll badD = (ll)(deg[u] - 1) * L1[u] - dmOut;   // u = d: put c-u-e-u nije jednostavan
        L3[u] = s - badC[u] - badD - hsIn;             // badC: u = c; hsIn: u in trokutu \ {c}
        ans = (ans + L3[u]) % MOD;
    }
    printf("%lld\n", (ans % MOD + MOD) % MOD);
    return 0;
}
