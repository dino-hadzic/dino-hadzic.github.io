// UCup 1, Stage 15 (ZJCPC 2023), K. Shuttle Tour
// Odgovor = 2 * težina Steinerova stabla otvorenih vrhova s indeksima u [l,r].
// Stablo ukorijenimo u 1 i rastavimo na k <= 50 lanaca (svaki završava listom). Segmentno stablo
// po indeksima u svakom čvoru pamti, za svaki lanac, najdublji otvoreni vrh (poziciju na lancu)
// te min/max ulaznog vremena DFS-a (za LCA). Težina unije putova do korijena = suma po lancima
// (najdublja potrebna točka - dubina roditelja vrha lanca), Steiner = unija - dubina LCA-a svih.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, q, k, LOG;
vector<vector<pair<int, int>>> adj;
vector<int> par, tin, niv, lanac, poz, vrhLanca, redoslijed;   // lanac[v], poz[v] = položaj na lancu; niv = razina
vector<ll> dub;                                           // težinska dubina
vector<vector<int>> vrhoviLanca, up;                      // vrhoviLanca[c][p] = vrh na poziciji p
int sz;
vector<int> mx, tmin, tmax;                               // mx[(čvor)*k + c]
const int INF = INT_MAX;

inline void postaviList(int i) {
    int nd = sz + i - 1;
    for (int c = 0; c < k; ++c) mx[(size_t)nd * k + c] = -1;
    tmin[nd] = INF; tmax[nd] = -1;
}
inline void spoji(int nd) {
    int a = 2 * nd, b = 2 * nd + 1;
    for (int c = 0; c < k; ++c) mx[(size_t)nd * k + c] = max(mx[(size_t)a * k + c], mx[(size_t)b * k + c]);
    tmin[nd] = min(tmin[a], tmin[b]); tmax[nd] = max(tmax[a], tmax[b]);
}
int lca(int a, int b) {
    if (niv[a] < niv[b]) swap(a, b);
    for (int j = LOG - 1; j >= 0; --j) if (niv[up[j][a]] >= niv[b]) a = up[j][a];
    if (a == b) return a;
    for (int j = LOG - 1; j >= 0; --j) if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
    return par[a];
}

int main() {
    scanf("%d %d", &n, &q);
    static char s[200005]; scanf("%s", s + 1);
    adj.assign(n + 1, {});
    for (int i = 0; i < n - 1; ++i) { int u, v, w; scanf("%d %d %d", &u, &v, &w); adj[u].push_back({v, w}); adj[v].push_back({u, w}); }
    // iterativni DFS iz korijena 1: roditelji, dubine, ulazna vremena, preorder
    par.assign(n + 1, 0); dub.assign(n + 1, 0); tin.assign(n + 1, 0); niv.assign(n + 1, 0);
    vector<int> preorder; preorder.reserve(n);
    { vector<int> st = {1}; par[1] = 1; int t = 0;
      while (!st.empty()) { int v = st.back(); st.pop_back(); tin[v] = t++; preorder.push_back(v);
          for (auto [w, c] : adj[v]) if (w != par[v]) { par[w] = v; dub[w] = dub[v] + c; niv[w] = niv[v] + 1; st.push_back(w); } } }
    // rastav na lance: svaki još nedodijeljeni vrh (u preorderu) otvara lanac koji ide do lista
    lanac.assign(n + 1, -1); poz.assign(n + 1, 0);
    for (int v : preorder) {
        if (lanac[v] >= 0) continue;
        int c = vrhoviLanca.size(); vrhoviLanca.push_back({}); vrhLanca.push_back(v);
        int x = v;
        while (true) {
            lanac[x] = c; poz[x] = vrhoviLanca[c].size(); vrhoviLanca[c].push_back(x);
            int dalje = -1;
            for (auto [w, cw] : adj[x]) if (w != par[x] && lanac[w] < 0) { dalje = w; break; }
            if (dalje < 0) break;
            x = dalje;
        }
    }
    k = vrhoviLanca.size();
    redoslijed.resize(k); iota(redoslijed.begin(), redoslijed.end(), 0);   // dublji vrhovi lanaca prvi
    sort(redoslijed.begin(), redoslijed.end(), [&](int a, int b) { return dub[vrhLanca[a]] > dub[vrhLanca[b]]; });
    LOG = 1; while ((1 << LOG) <= n) ++LOG;
    up.assign(LOG, vector<int>(n + 1));
    for (int v = 1; v <= n; ++v) up[0][v] = par[v];
    for (int j = 1; j < LOG; ++j) for (int v = 1; v <= n; ++v) up[j][v] = up[j - 1][up[j - 1][v]];
    // segmentno stablo
    sz = 1; while (sz < n) sz <<= 1;
    mx.assign((size_t)2 * sz * k, -1); tmin.assign(2 * sz, INF); tmax.assign(2 * sz, -1);
    vector<char> otvoren(n + 1);
    for (int i = 1; i <= n; ++i) {
        otvoren[i] = s[i] == '1';
        if (otvoren[i]) { int nd = sz + i - 1; mx[(size_t)nd * k + lanac[i]] = poz[i]; tmin[nd] = tmax[nd] = tin[i]; }
    }
    for (int nd = sz - 1; nd >= 1; --nd) spoji(nd);
    vector<ll> potrebno(k);
    vector<int> akum(k);
    while (q--) {
        int tip; scanf("%d", &tip);
        if (tip == 1) {
            int x; scanf("%d", &x);
            otvoren[x] ^= 1;
            postaviList(x);
            if (otvoren[x]) { int nd = sz + x - 1; mx[(size_t)nd * k + lanac[x]] = poz[x]; tmin[nd] = tmax[nd] = tin[x]; }
            for (int nd = (sz + x - 1) / 2; nd >= 1; nd /= 2) spoji(nd);
        } else {
            int l, r; scanf("%d %d", &l, &r);
            fill(akum.begin(), akum.end(), -1);
            int mn = INF, mxt = -1;
            for (int lo = l + sz - 1, hi = r + sz; lo < hi; lo >>= 1, hi >>= 1) {
                if (lo & 1) { for (int c = 0; c < k; ++c) akum[c] = max(akum[c], mx[(size_t)lo * k + c]); mn = min(mn, tmin[lo]); mxt = max(mxt, tmax[lo]); ++lo; }
                if (hi & 1) { --hi; for (int c = 0; c < k; ++c) akum[c] = max(akum[c], mx[(size_t)hi * k + c]); mn = min(mn, tmin[hi]); mxt = max(mxt, tmax[hi]); }
            }
            if (mxt < 0) { puts("-1"); continue; }
            // unija putova do korijena
            for (int c = 0; c < k; ++c) potrebno[c] = akum[c] >= 0 ? dub[vrhoviLanca[c][akum[c]]] : -1;
            ll unija = 0;
            for (int c : redoslijed) {
                if (potrebno[c] < 0) continue;
                int top = vrhLanca[c];
                if (top == 1) { unija += potrebno[c]; continue; }
                int p = par[top];
                unija += potrebno[c] - dub[p];
                potrebno[lanac[p]] = max(potrebno[lanac[p]], dub[p]);
            }
            int a = preorder[mn], b = preorder[mxt];     // vrhovi s min i max ulaznim vremenom
            ll odgovor = unija - dub[lca(a, b)];
            printf("%lld\n", 2 * odgovor);
        }
    }
    return 0;
}
