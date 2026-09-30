// UCup 1, Stage 9 (Qingdao 2018), B. Kawa Exam
// Sva pitanja iste komponente moraju imati isti odgovor, pa komponenta donosi najčešću vrijednost (mod).
// Uklanjanje brida mijenja odgovor samo ako je most: komponenta se raspadne na podstablo DFS stabla
// i njegov komplement. Modove podstabala i komplemenata računamo tehnikom DSU na stablu (sack),
// iterativno, nad Eulerovim obilaskom; brojač frekvencija freq[cnt] daje mod u O(1) po umetanju/brisanju.
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 100005;
// Multiskup s O(1) umetanjem/brisanjem i održavanjem moda: freq[c] = broj vrijednosti brojnosti c.
struct Multiskup {
    int cnt[MAXV];
    vector<int> freq;
    int mode = 0;
    void init(int n) { freq.assign(n + 2, 0); freq[0] = MAXV; mode = 0; }
    void dodaj(int val) {
        int c = cnt[val];
        freq[c]--; cnt[val] = c + 1; freq[c + 1]++;
        if (c + 1 > mode) mode = c + 1;
    }
    void makni(int val) {
        int c = cnt[val];
        freq[c]--; cnt[val] = c - 1; freq[c - 1]++;
        if (mode == c && freq[c] == 0) mode--;
    }
} S1, S2;   // S1 = trenutno podstablo, S2 = komponenta bez S1 (uvijek komplement)

void dodaj(int val) { S1.dodaj(val); S2.makni(val); }
void makni(int val) { S1.makni(val); S2.dodaj(val); }

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<int> a(n);
        for (auto &x : a) scanf("%d", &x);
        vector<int> eu(m), ev(m);
        vector<int> deg(n, 0);
        for (int i = 0; i < m; i++) {
            scanf("%d %d", &eu[i], &ev[i]);
            eu[i]--; ev[i]--;
            deg[eu[i]]++; deg[ev[i]]++;
        }
        // CSR lista susjedstva: (susjed, id brida)
        vector<int> start(n + 1, 0);
        for (int i = 0; i < n; i++) start[i + 1] = start[i] + deg[i];
        vector<int> to(2 * m), eid(2 * m), fill(start.begin(), start.end() - 1);
        for (int i = 0; i < m; i++) {
            to[fill[eu[i]]] = ev[i]; eid[fill[eu[i]]++] = i;
            to[fill[ev[i]]] = eu[i]; eid[fill[ev[i]]++] = i;
        }

        // Iterativni Tarjan: mostovi, DFS stablo, Eulerov poredak
        vector<int> tin(n, -1), low(n), tout(n), par(n, -1), parEdge(n, -1), order(n), it(n);
        vector<int> root(n), bridgeChild(m, -1);
        vector<vector<int>> ch(n);
        int timer = 0;
        for (int s = 0; s < n; s++) {
            if (tin[s] != -1) continue;
            vector<int> st = {s};
            tin[s] = low[s] = timer; order[timer++] = s; it[s] = start[s]; root[s] = s;
            while (!st.empty()) {
                int v = st.back();
                if (it[v] < start[v + 1]) {
                    int u = to[it[v]], id = eid[it[v]]; it[v]++;
                    if (id == parEdge[v]) continue;
                    if (tin[u] == -1) {
                        par[u] = v; parEdge[u] = id; root[u] = s; ch[v].push_back(u);
                        tin[u] = low[u] = timer; order[timer++] = u; it[u] = start[u];
                        st.push_back(u);
                    } else low[v] = min(low[v], tin[u]);
                } else {
                    tout[v] = timer - 1;
                    st.pop_back();
                    if (par[v] != -1) {
                        low[par[v]] = min(low[par[v]], low[v]);
                        if (low[v] > tin[par[v]]) bridgeChild[parEdge[v]] = v;   // most
                    }
                }
            }
        }
        // veličine podstabala i teško dijete
        vector<int> sz(n, 1), heavy(n, -1);
        for (int i = n - 1; i >= 0; i--) {
            int v = order[i];
            if (par[v] != -1) sz[par[v]] += sz[v];
            for (int c : ch[v]) if (heavy[v] == -1 || sz[c] > sz[heavy[v]]) heavy[v] = c;
        }
        auto dodajRaspon = [&](int v) { for (int p = tin[v]; p <= tout[v]; p++) dodaj(a[order[p]]); };
        auto makniRaspon = [&](int v) { for (int p = tin[v]; p <= tout[v]; p++) makni(a[order[p]]); };

        S1.init(n); S2.init(n);
        vector<int> modeSub(n), modeComp(n);
        struct Okvir { int v, faza, i; };

        // Sack (DSU na stablu): pri izlasku iz v vrijedi S1 = podstablo(v), S2 = komponenta \ podstablo(v)
        for (int s = 0; s < n; s++) {
            if (par[s] != -1) continue;
            for (int p = tin[s]; p <= tout[s]; p++) S2.dodaj(a[order[p]]);   // S2 = cijela komponenta
            vector<Okvir> st = {{s, 0, 0}};
            while (!st.empty()) {
                Okvir &f = st.back();
                int v = f.v;
                if (f.faza == 0) {
                    while (f.i < (int)ch[v].size() && ch[v][f.i] == heavy[v]) f.i++;
                    if (f.i < (int)ch[v].size()) { int c = ch[v][f.i++]; f.faza = 1; st.push_back({c, 0, 0}); }
                    else if (heavy[v] != -1) { f.faza = 3; st.push_back({heavy[v], 0, 0}); }
                    else f.faza = 3;
                } else if (f.faza == 1) {         // vratili se iz lakog djeteta: isprazni ga
                    makniRaspon(ch[v][f.i - 1]); f.faza = 0;
                } else {                          // teško dijete gotovo: dodaj v i laku djecu
                    dodaj(a[v]);
                    for (int c : ch[v]) if (c != heavy[v]) dodajRaspon(c);
                    modeSub[v] = S1.mode;
                    modeComp[v] = S2.mode;
                    st.pop_back();
                }
            }
            makniRaspon(s);                       // S1 = prazno, S2 = komponenta
            for (int p = tin[s]; p <= tout[s]; p++) S2.makni(a[order[p]]);   // očisti S2
        }
        long long base = 0;
        for (int s = 0; s < n; s++) if (par[s] == -1) base += modeSub[s];
        string out;
        for (int i = 0; i < m; i++) {
            long long ans = base;
            int v = bridgeChild[i];
            if (v != -1) ans += modeSub[v] + modeComp[v] - modeSub[root[v]];
            out += to_string(ans);
            out += (i + 1 < m ? ' ' : '\n');
        }
        fputs(out.c_str(), stdout);
    }
    return 0;
}
