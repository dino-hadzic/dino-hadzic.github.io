// C. Stablo
// Dobar put koristi samo bridove (u, p(u)) s a_u = a_p, i svi su iste boje.
// Za vrh v: D[v] = najdulji dobar put od v prema dolje čiji bridovi imaju boju
// fc_v (boju brida prema roditelju): D[v] = max(0, max_{djeca u: fc_u=fc_v, a_u=a_v} w_u + D[u]).
// Dinamički DP nad HLD-om: u svakom vrhu lagana djeca grupirana po ključu
// (boja vrha, boja brida) u multisete; teški lanac čuva u segmentnom stablu
// (max,+) funkcije y -> w_v + D[v] = max(y + alpha, beta) i najbolji odgovor
// gamma / y + delta.  Promjena boje vrha: O(log^2 n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll NEG = -(ll)1e18;
static inline ll add(ll a, ll b) { return max(NEG, a + b); }

struct Node { ll al, be, ga, de; };   // alpha, beta, gamma, delta
static Node combine(const Node& U, const Node& Lo) {   // U bliže vrhu lanca, Lo ispod njega
    Node r;
    r.al = add(Lo.al, U.al);
    r.be = max(U.be, add(Lo.be, U.al));
    r.ga = max({Lo.ga, U.ga, add(Lo.be, U.de)});
    r.de = max(Lo.de, add(Lo.al, U.de));
    return r;
}

int n, q;
vector<int> a, fa, fc, heavy, top_, pos_, bottom_;
vector<ll> w, sz;
vector<vector<int>> ch;

// lagana djeca po vrhu: (boja djeteta, boja brida) -> multiset vrijednosti w_u + D[u]
vector<map<pair<int,int>, multiset<ll>>> groups;
// po vrhu: boja djeteta -> multiset "zbrojeva para" (top1 + top2) svih grupa te boje
vector<map<int, multiset<ll>>> pairsums;
vector<ll> storedVal; vector<int> storedKey;   // što je vrh lanca trenutno unio u roditelja

ll pairsum(const multiset<ll>& s) {
    auto it = s.rbegin(); ll t1 = *it; ++it;
    return t1 + (it != s.rend() ? *it : 0);
}
void groupRemove(int v, int col, int c, ll val) {
    auto& g = groups[v][{col, c}];
    pairsums[v][col].erase(pairsums[v][col].find(pairsum(g)));
    g.erase(g.find(val));
    if (!g.empty()) pairsums[v][col].insert(pairsum(g));
    else groups[v].erase({col, c});
}
void groupInsert(int v, int col, int c, ll val) {
    auto& g = groups[v][{col, c}];
    if (!g.empty()) pairsums[v][col].erase(pairsums[v][col].find(pairsum(g)));
    g.insert(val);
    pairsums[v][col].insert(pairsum(g));
}
ll top1(int v, int col, int c) {
    auto it = groups[v].find({col, c});
    return it == groups[v].end() ? 0 : max(0LL, *it->second.rbegin());
}
ll bestPair(int v, int col) {
    auto it = pairsums[v].find(col);
    return (it == pairsums[v].end() || it->second.empty()) ? 0 : max(0LL, *it->second.rbegin());
}

vector<Node> seg; int SZ;
Node leafOf(int v) {
    int h = heavy[v];
    bool pair_ = h && a[h] == a[v];               // teško dijete smije se spojiti s v
    bool up = pair_ && fc[h] == fc[v];            // ... i nastaviti prema roditelju (ista boja brida)
    ll L = top1(v, a[v], fc[v]);
    ll L2 = h ? top1(v, a[v], fc[h]) : 0;
    Node r; r.al = up ? w[v] : NEG; r.be = w[v] + L; r.ga = bestPair(v, a[v]); r.de = pair_ ? L2 : NEG;
    return r;
}
void segSet(int p, const Node& x) {
    p += SZ; seg[p] = x;
    for (p >>= 1; p; p >>= 1) seg[p] = combine(seg[2 * p], seg[2 * p + 1]);
}
Node segQuery(int l, int r) {          // [l, r], l = pozicija vrha lanca (bliže korijenu)
    Node L = {NEG, NEG, NEG, NEG}, R = {NEG, NEG, NEG, NEG};
    bool hasL = false, hasR = false;
    for (l += SZ, r += SZ + 1; l < r; l >>= 1, r >>= 1) {
        if (l & 1) { L = hasL ? combine(L, seg[l]) : seg[l]; hasL = true; ++l; }
        if (r & 1) { --r; R = hasR ? combine(seg[r], R) : seg[r]; hasR = true; }
    }
    if (!hasL) return R;
    if (!hasR) return L;
    return combine(L, R);
}
Node chainOf(int v) { int t = top_[v]; return segQuery(pos_[t], pos_[bottom_[t]]); }

multiset<ll> answers;                  // gamma svakog lanca
vector<ll> chainGamma;                 // po vrhu lanca

void refreshChain(int v) {             // ponovno izračunaj lanac koji sadrži v i propagiraj prema korijenu
    while (true) {
        int t = top_[v];
        Node res = chainOf(v);
        answers.erase(answers.find(chainGamma[t]));
        chainGamma[t] = res.ga; answers.insert(res.ga);
        int p = fa[t];
        if (!p) break;
        groupRemove(p, storedKey[t], fc[t], storedVal[t]);
        storedKey[t] = a[t]; storedVal[t] = res.be;
        groupInsert(p, a[t], fc[t], res.be);
        segSet(pos_[p], leafOf(p));
        v = p;
    }
}

int main() {
    scanf("%d %d", &n, &q);
    a.assign(n + 1, 0); fa.assign(n + 1, 0); fc.assign(n + 1, 0); w.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
    for (int i = 2; i <= n; ++i) scanf("%d", &fa[i]);
    for (int i = 2; i <= n; ++i) scanf("%d", &fc[i]);
    for (int i = 2; i <= n; ++i) scanf("%lld", &w[i]);
    ch.assign(n + 1, {});
    for (int i = 2; i <= n; ++i) ch[fa[i]].push_back(i);
    // HLD (fa_i < i pa ide obrnutim redoslijedom indeksa)
    sz.assign(n + 1, 1); heavy.assign(n + 1, 0);
    for (int v = n; v >= 2; --v) sz[fa[v]] += sz[v];
    for (int v = 1; v <= n; ++v) for (int u : ch[v]) if (!heavy[v] || sz[u] > sz[heavy[v]]) heavy[v] = u;
    top_.assign(n + 1, 0); pos_.assign(n + 1, 0); bottom_.assign(n + 1, 0);
    {
        int cur = 0;
        vector<int> st = {1};
        while (!st.empty()) {
            int t = st.back(); st.pop_back();
            for (int v = t; v; v = heavy[v]) {
                top_[v] = t; pos_[v] = cur++; bottom_[t] = v;
                for (int u : ch[v]) if (u != heavy[v]) st.push_back(u);
            }
        }
    }
    // početni DP (djeca imaju veće indekse)
    vector<ll> D(n + 1, 0);
    groups.assign(n + 1, {}); pairsums.assign(n + 1, {});
    storedVal.assign(n + 1, 0); storedKey.assign(n + 1, 0);
    for (int v = n; v >= 1; --v) {
        int h = heavy[v];
        ll best = top1(v, a[v], fc[v]);
        if (h && fc[h] == fc[v] && a[h] == a[v]) best = max(best, w[h] + D[h]);
        D[v] = best;
        if (v > 1 && heavy[fa[v]] != v) {
            storedKey[v] = a[v]; storedVal[v] = w[v] + D[v];
            groupInsert(fa[v], a[v], fc[v], storedVal[v]);
        }
    }
    SZ = 1; while (SZ < n) SZ <<= 1;
    seg.assign(2 * SZ, Node{NEG, NEG, NEG, NEG});
    for (int v = 1; v <= n; ++v) seg[SZ + pos_[v]] = leafOf(v);
    for (int p = SZ - 1; p >= 1; --p) seg[p] = combine(seg[2 * p], seg[2 * p + 1]);
    chainGamma.assign(n + 1, NEG);
    for (int v = 1; v <= n; ++v) if (top_[v] == v) { chainGamma[v] = chainOf(v).ga; answers.insert(chainGamma[v]); }

    string out;
    out += to_string(*answers.rbegin()); out += '\n';
    while (q--) {
        int x, c; scanf("%d %d", &x, &c);
        a[x] = c;
        segSet(pos_[x], leafOf(x));
        if (x > 1 && heavy[fa[x]] == x) segSet(pos_[fa[x]], leafOf(fa[x]));
        refreshChain(x);
        out += to_string(*answers.rbegin()); out += '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
