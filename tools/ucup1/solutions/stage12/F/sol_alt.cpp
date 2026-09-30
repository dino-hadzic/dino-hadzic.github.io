// F - Forestry
// Komponenta C (povezan podskup) pojavljuje se u tocno 2^{N-2} * prod_{u in C} 2^{1-deg(u)}
// odabira bridova. Zato je odgovor 2^{N-2} * sum_C min(C) * prod_{u in C} w_u, w_u = 2^{1-deg u}.
// min(C) rastavimo po pragovima: min(C) = sum_t Delta_t [svi A u C >= t].
// Dodajemo vrhove u padajucem redoslijedu po A i odrzavamo
//   G = sum po povezanim podskupovima zivih vrhova od prod w
// dinamickim DP-om na stablu (HLD + segmentno stablo afinih preslikavanja):
//   D(u) = [u ziv] * w_u * prod_{djeca c} (1 + D(c)),  G = sum_u D(u).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1; b %= MOD; if (b < 0) b += MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

// Preslikavanje segmenta teskog puta: ulaz x = D(teskog djeteta dna),
// D(vrha segmenta) = a + b x, zbroj D po segmentu = s + t x.
struct Node {
    ll a, b, s, t;
};
Node combine(const Node &top, const Node &bot) {
    Node r;
    r.a = (top.a + top.b * bot.a) % MOD;
    r.b = top.b * bot.b % MOD;
    r.s = (top.s + top.t * bot.a + bot.s) % MOD;
    r.t = (top.t * bot.b + bot.t) % MOD;
    return r;
}

int n;
vector<Node> seg;
int SZ;
void segSet(int pos, Node v) {
    pos += SZ;
    seg[pos] = v;
    for (pos >>= 1; pos; pos >>= 1) seg[pos] = combine(seg[2 * pos], seg[2 * pos + 1]);
}
Node segQuery(int l, int r) {  // [l, r]
    Node L = {0, 1, 0, 0}, R = {0, 1, 0, 0};  // identitet
    for (l += SZ, r += SZ + 1; l < r; l >>= 1, r >>= 1) {
        if (l & 1) L = combine(L, seg[l++]);
        if (r & 1) R = combine(seg[--r], R);
    }
    return combine(L, R);
}

// umnozak (1 + D(lako dijete)) uz pracenje faktora jednakih nuli
struct Prod {
    ll val = 1;
    int zeros = 0;
    void mul(ll x) { if (x == 0) zeros++; else val = val * x % MOD; }
    void div(ll x) { if (x == 0) zeros--; else val = val * power(x, MOD - 2) % MOD; }
    ll get() const { return zeros ? 0 : val; }
};

int main() {
    scanf("%d", &n);
    vector<ll> A(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &A[i]);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    // HLD: BFS redoslijed, velicine, tesko dijete, pozicije
    vector<int> par(n + 1, 0), order, sz(n + 1, 1), heavy(n + 1, 0), head(n + 1), pos(n + 1);
    order.push_back(1);
    par[1] = 0;
    for (size_t i = 0; i < order.size(); i++)
        for (int u : g[order[i]])
            if (u != par[order[i]]) { par[u] = order[i]; order.push_back(u); }
    for (int i = n - 1; i > 0; i--) {
        int v = order[i];
        sz[par[v]] += sz[v];
        if (heavy[par[v]] == 0 || sz[v] > sz[heavy[par[v]]]) heavy[par[v]] = v;
    }
    // pozicije: teski put je neprekinut segment (vrh puta ima manju poziciju)
    int cur = 0;
    vector<int> bottom(n + 1);  // dno teskog puta (po glavi)
    {
        vector<int> st = {1};
        head[1] = 1;
        while (!st.empty()) {
            int h = st.back(); st.pop_back();
            for (int v = h; v; v = heavy[v]) {
                head[v] = h;
                pos[v] = cur++;
                bottom[h] = v;
                for (int u : g[v])
                    if (u != par[v] && u != heavy[v]) { head[u] = u; st.push_back(u); }
            }
        }
    }
    SZ = 1;
    while (SZ < n) SZ <<= 1;
    seg.assign(2 * SZ, {0, 1, 0, 0});
    // mrtvi vrhovi: D = 0 bez obzira na ulaz -> (a,b,s,t) = (0,0,0,0)
    Node dead = {0, 0, 0, 0};
    for (int v = 1; v <= n; v++) segSet(pos[v], dead);

    vector<ll> w(n + 1);
    ll inv2 = power(2, MOD - 2);
    for (int v = 1; v <= n; v++) w[v] = power(inv2, (int)g[v].size() - 1);  // 2^{1-deg}
    vector<Prod> light(n + 1);
    vector<char> alive(n + 1, 0);

    // D vrha v: vrijednost kompozicije segmenta [pos v, pos dna] uz x = 0
    auto topValue = [&](int h) { return segQuery(pos[h], pos[bottom[h]]); };

    ll G = 0;  // zbroj svih D
    vector<int> byA(n);
    iota(byA.begin(), byA.end(), 1);
    sort(byA.begin(), byA.end(), [&](int x, int y) { return A[x] > A[y]; });

    auto leafOf = [&](int u) -> Node {
        if (!alive[u]) return dead;
        ll c = w[u] * light[u].get() % MOD;
        return {c, c, c, c};
    };
    // azuriraj list u i propagiraj promjenu do korijena po teskim putevima
    auto update = [&](int u) {
        while (true) {
            int h = head[u];
            Node before = topValue(h);
            segSet(pos[u], leafOf(u));
            Node after = topValue(h);
            G = ((G - before.s + after.s) % MOD + MOD) % MOD;
            int p = par[h];
            if (p == 0) break;
            // laki brid (p, h): promijeni faktor (1 + D(h)) u umnosku p
            light[p].div((1 + before.a) % MOD);
            light[p].mul((1 + after.a) % MOD);
            u = p;
        }
    };

    ll ans = 0;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && A[byA[j]] == A[byA[i]]) {
            alive[byA[j]] = 1;
            update(byA[j]);
            j++;
        }
        ll nextVal = (j < n) ? A[byA[j]] : 0;
        ll delta = (A[byA[i]] - nextVal) % MOD;
        ans = (ans + delta * G) % MOD;
        i = j;
    }
    ans = ans * power(2, n - 2) % MOD;
    printf("%lld\n", ans);
}
