// UCup 1, Stage 18, G: Classic Problem
// Krajevi trojki su "posebni" vrhovi (<= 2m). Obični vrhovi između njih tvore segmente
// uzastopnih brojeva; bridovi težine 1 unutar segmenta sigurno su u nekom MST-u
// (Kruskal koji ih obrađuje prije ostalih bridova težine 1). Segmente sažmemo u po jedan
// čvor i na potpunom grafu od <= 4m+1 čvorova pokrenemo Borůvku: najjeftiniji brid
// čvora u drugu komponentu je ili trojka ili "udaljenosni" brid do najbližeg čvora
// druge komponente (lijevo/desno), koji nije povezan trojkom.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

static char buf[1 << 25];
int bufLen, bufPos;
inline int readChar() {
    if (bufPos == bufLen) {
        bufLen = fread(buf, 1, sizeof(buf), stdin);
        bufPos = 0;
        if (bufLen <= 0) return -1;
    }
    return buf[bufPos++];
}
inline ll readInt() {
    int c = readChar();
    while (c != -1 && (c < '0' || c > '9')) c = readChar();
    ll x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = readChar();
    }
    return x;
}

struct Edge {
    ll w;
    int u, v;  // u < v, indeksi čvorova sažetog grafa
    bool operator<(const Edge& o) const {
        if (w != o.w) return w < o.w;
        if (u != o.u) return u < o.u;
        return v < o.v;
    }
};

vector<int> dsu;
int find(int x) {
    while (dsu[x] != x) {
        dsu[x] = dsu[dsu[x]];
        x = dsu[x];
    }
    return x;
}

int main() {
    int T = readInt();
    while (T--) {
        ll n = readInt();
        int m = readInt();
        vector<ll> U(m), V(m), W(m);
        vector<ll> sp;
        for (int i = 0; i < m; i++) {
            U[i] = readInt();
            V[i] = readInt();
            W[i] = readInt();
            sp.push_back(U[i]);
            sp.push_back(V[i]);
        }
        sort(sp.begin(), sp.end());
        sp.erase(unique(sp.begin(), sp.end()), sp.end());
        // čvorovi sažetog grafa: posebni vrhovi i segmenti običnih vrhova, po položaju
        vector<ll> L, R;
        vector<char> special;
        vector<int> idOfSpecial(sp.size());
        ll ans = 0;
        ll prev = 0;  // posljednji obrađeni položaj
        for (size_t i = 0; i < sp.size(); i++) {
            if (sp[i] > prev + 1) {
                L.push_back(prev + 1);
                R.push_back(sp[i] - 1);
                special.push_back(0);
                ans += sp[i] - 1 - (prev + 1);  // bridovi težine 1 unutar segmenta
            }
            idOfSpecial[i] = L.size();
            L.push_back(sp[i]);
            R.push_back(sp[i]);
            special.push_back(1);
            prev = sp[i];
        }
        if (n > prev) {
            L.push_back(prev + 1);
            R.push_back(n);
            special.push_back(0);
            ans += n - (prev + 1);
        }
        int K = L.size();
        // liste trojki po čvoru
        vector<vector<pair<int, ll>>> adj(K);
        for (int i = 0; i < m; i++) {
            int a = idOfSpecial[lower_bound(sp.begin(), sp.end(), U[i]) - sp.begin()];
            int b = idOfSpecial[lower_bound(sp.begin(), sp.end(), V[i]) - sp.begin()];
            adj[a].push_back({b, W[i]});
            adj[b].push_back({a, W[i]});
        }
        dsu.assign(K, 0);
        iota(dsu.begin(), dsu.end(), 0);
        int comps = K;
        vector<int> comp(K), L1(K), L2(K), R1(K), R2(K), mark(K, -1);
        vector<Edge> best(K);
        auto distEdge = [&](int i, int y) {  // udaljenosni brid između čvorova i i y
            ll w = (L[i] > R[y]) ? L[i] - R[y] : L[y] - R[i];
            return Edge{w, min(i, y), max(i, y)};
        };
        while (comps > 1) {
            for (int i = 0; i < K; i++) comp[i] = find(i);
            // L1[t] = najbliži čvor lijevo od t; L2[t] = najbliži lijevo s komponentom != comp[L1[t]]
            int last1 = -1, last2 = -1;
            for (int t = 0; t < K; t++) {
                L1[t] = last1;
                L2[t] = last2;
                if (last1 == -1 || comp[t] != comp[last1]) last2 = last1;
                last1 = t;
            }
            last1 = last2 = -1;
            for (int t = K - 1; t >= 0; t--) {
                R1[t] = last1;
                R2[t] = last2;
                if (last1 == -1 || comp[t] != comp[last1]) last2 = last1;
                last1 = t;
            }
            auto nearLeft = [&](int t, int C) {
                if (L1[t] == -1) return -1;
                return comp[L1[t]] != C ? L1[t] : L2[t];
            };
            auto nearRight = [&](int t, int C) {
                if (R1[t] == -1) return -1;
                return comp[R1[t]] != C ? R1[t] : R2[t];
            };
            for (int i = 0; i < K; i++) best[i] = Edge{LLONG_MAX, -1, -1};
            auto offer = [&](int c, const Edge& e) {
                if (e < best[c]) best[c] = e;
            };
            for (int i = 0; i < K; i++) {
                int C = comp[i];
                if (special[i]) {
                    for (auto& p : adj[i]) {
                        mark[p.first] = i;
                        if (comp[p.first] != C) offer(C, Edge{p.second, min(i, p.first), max(i, p.first)});
                    }
                }
                // najbliži čvor lijevo iz druge komponente koji nije povezan trojkom s i
                int y = nearLeft(i, C);
                while (y != -1 && mark[y] == i) y = nearLeft(y, C);
                if (y != -1) offer(C, distEdge(i, y));
                y = nearRight(i, C);
                while (y != -1 && mark[y] == i) y = nearRight(y, C);
                if (y != -1) offer(C, distEdge(i, y));
            }
            for (int c = 0; c < K; c++) {
                if (best[c].u < 0) continue;
                int a = find(best[c].u), b = find(best[c].v);
                if (a == b) continue;
                dsu[a] = b;
                ans += best[c].w;
                comps--;
            }
        }
        printf("%lld\n", ans);
    }
    return 0;
}
